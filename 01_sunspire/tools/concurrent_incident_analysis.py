#!/usr/bin/env python3
"""
Scan workspace `terraform/vars.tf`, `boxes/` and `logs/*/shell_history.csv` to
identify concurrent exploit attempts against documented vulnerabilities.

Outputs:
- reports/incidents.json
- reports/incidents.md

This is a forensic/detection helper (no exploit code).
"""
import csv
import json
import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
VARS = ROOT / 'terraform' / 'vars.tf'
BOXES = ROOT / 'boxes'
LOGS = ROOT / 'logs'
REPORTS = ROOT / 'reports'
REPORTS.mkdir(exist_ok=True)

IP_RE = re.compile(r"\b10\.100\.[0-9]{1,3}\.[0-9]{1,3}\b")

def parse_vars_tf(path):
    text = path.read_text()
    # crude parse for vms block entries: <name> = { ... ip_address = "10.100.x.y/.." ... }
    vm_re = re.compile(r"(\w+)\s*=\s*{([^}]+)}", re.M)
    ip_re = re.compile(r'ip_address\s*=\s*"([0-9.]+)\/[0-9]+"')
    os_re = re.compile(r'os_type\s*=\s*"(linux|windows)"')
    mapping = {}
    for m in vm_re.finditer(text):
        name = m.group(1)
        body = m.group(2)
        ipm = ip_re.search(body)
        osm = os_re.search(body)
        if ipm:
            mapping[ipm.group(1)] = {'box': name, 'os': osm.group(1) if osm else None}
    return mapping

def scan_boxes_for_vulns(boxes_dir):
    keywords = ['SMB', 'backup.zip', 'sql', 'sql injection', 'phpinfo', 'maintenance.ps1', 'git', 'SUID', 'base64', 'pickle', 'anonymous', 'cron']
    vulns = {}
    for box in boxes_dir.iterdir():
        if not box.is_dir():
            continue
        notes = []
        for f in box.rglob('*'):
            if f.is_file() and f.suffix in ('.md', '.sh', '.ps1', '.conf'):
                txt = f.read_text(errors='ignore')
                found = [k for k in keywords if re.search(k, txt, re.I)]
                if found:
                    notes.append({'file': str(f.relative_to(ROOT)), 'matches': list(set(found))})
        if notes:
            vulns[box.name] = notes
    return vulns

def parse_shell_histories(logs_dir):
    # Expect path logs/<ip>/shell_history.csv
    entries = []
    for sub in logs_dir.iterdir():
        if not sub.is_dir():
            continue
        csvf = sub / 'shell_history.csv'
        if not csvf.exists():
            continue
        with csvf.open() as fh:
            reader = csv.reader(fh)
            for i,row in enumerate(reader, start=1):
                if not row: continue
                # naive handling: find timestamp-like cell and command cell
                # common formats: timestamp,command,user
                if len(row) >= 2:
                    # try to parse first cell as timestamp
                    ts = None
                    try:
                        ts = datetime.fromisoformat(row[0])
                    except Exception:
                        # try common formats
                        for col in row:
                            if re.search(r"\d{4}-\d{2}-\d{2}", col):
                                try:
                                    ts = datetime.fromisoformat(col)
                                    break
                                except Exception:
                                    pass
                    cmd = row[-1].strip()
                    entries.append({'log_file': str(csvf.relative_to(ROOT)), 'line': i, 'timestamp': ts.isoformat() if ts else None, 'command': cmd})
                else:
                    entries.append({'log_file': str(csvf.relative_to(ROOT)), 'line': i, 'timestamp': None, 'command': row[0].strip()})
    return entries

def correlate(entries, ip_map, vulns):
    # find commands referencing IPs and map to boxes; group by minute windows
    incidents = []
    # augment entries with found ips and boxes
    for e in entries:
        e['ips'] = IP_RE.findall(e['command'])
        e['boxes'] = [ip_map.get(ip, {}).get('box') for ip in e['ips']]
    # build time-indexed dict (minute) -> list
    time_buckets = defaultdict(list)
    for e in entries:
        ts = e.get('timestamp')
        if ts:
            try:
                dt = datetime.fromisoformat(ts)
                key = dt.replace(second=0, microsecond=0).isoformat()
            except Exception:
                key = 'unknown'
        else:
            key = 'unknown'
        time_buckets[key].append(e)
    # find buckets with 2+ entries targeting same box or same ip
    for key, items in time_buckets.items():
        if len(items) < 2:
            continue
        # group by target ip/box
        by_target = defaultdict(list)
        for it in items:
            if it['ips']:
                for ip in it['ips']:
                    by_target[ip].append(it)
            else:
                by_target['unknown'].append(it)
        for target, hits in by_target.items():
            if len(hits) < 2:
                continue
            # craft incident
            involved = []
            for h in hits:
                involved.append({'log_file': h['log_file'], 'line': h['line'], 'command': h['command'], 'timestamp': h['timestamp']})
            incident = {
                'time_window': key,
                'target_ip': target if target!='unknown' else None,
                'target_box': ip_map.get(target, {}).get('box') if target and target in ip_map else None,
                'entries': involved,
                'matched_vuln_notes': vulns.get(ip_map.get(target, {}).get('box'), []) if target and target in ip_map else []
            }
            incidents.append(incident)
    return incidents

def save_reports(incidents):
    j = REPORTS / 'incidents.json'
    with j.open('w') as fh:
        json.dump({'generated': datetime.utcnow().isoformat(), 'incidents': incidents}, fh, indent=2)
    md = REPORTS / 'incidents.md'
    with md.open('w') as fh:
        fh.write('# Concurrent Exploit Incidents\n\n')
        for i,inc in enumerate(incidents, start=1):
            fh.write(f'## Incident {i} - {inc.get("time_window")}\n')
            fh.write(f'- Target IP: {inc.get("target_ip")}\n')
            fh.write(f'- Target Box: {inc.get("target_box")}\n')
            fh.write('- Entries:\n')
            for e in inc['entries']:
                fh.write(f"  - {e.get('timestamp') or 'no-ts'} | {e['log_file']}#L{e['line']} | {e['command']}\n")
            if inc.get('matched_vuln_notes'):
                fh.write('- Matched Vulnerability Notes:\n')
                for n in inc['matched_vuln_notes']:
                    fh.write(f"  - {n['file']}: {', '.join(n['matches'])}\n")
            fh.write('\n')

def main():
    print('Parsing vars.tf...')
    ip_map = parse_vars_tf(VARS)
    print(f'Found {len(ip_map)} IP mappings')
    print('Scanning boxes for vuln keywords...')
    vulns = scan_boxes_for_vulns(BOXES)
    print(f'Found vulnerabilities notes for {len(vulns)} boxes')
    print('Parsing shell histories...')
    entries = parse_shell_histories(LOGS)
    print(f'Parsed {len(entries)} history entries')
    print('Correlating concurrent incidents...')
    incidents = correlate(entries, ip_map, vulns)
    print(f'Found {len(incidents)} concurrent incidents')
    save_reports(incidents)
    print('Reports written to reports/')

if __name__ == '__main__':
    main()
