#!/usr/bin/env python3
"""
Filter incidents to include only those that map to documented vulnerabilities
and involve agents from different subnet groups (e.g., .1x, .2x, .3x).

Reads: reports/incidents.json
Writes: reports/filtered_incidents.json and reports/filtered_incidents.md
"""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
IN = REPORTS / 'incidents.json'
OUT_JSON = REPORTS / 'filtered_incidents.json'
OUT_MD = REPORTS / 'filtered_incidents.md'

IP_RE = re.compile(r"10\.100\.[0-9]{1,3}\.[0-9]{1,3}")

def extract_attacker_ip(log_file_path):
    # log_file like 'logs/10.100.7.11/shell_history.csv'
    m = IP_RE.search(log_file_path)
    return m.group(0) if m else None

def subnet_group(ip):
    # group by last-octet tens: 11->1, 21->2, 31->3
    if not ip:
        return None
    last = int(ip.split('.')[-1])
    return last // 10

def main():
    data = json.loads(IN.read_text())
    incs = data.get('incidents', [])
    filtered = []
    for inc in incs:
        # require that matched_vuln_notes is non-empty
        if not inc.get('matched_vuln_notes'):
            continue
        groups = set()
        for e in inc.get('entries', []):
            ip = extract_attacker_ip(e.get('log_file',''))
            g = subnet_group(ip)
            if g is not None:
                groups.add(g)
        if len(groups) >= 2:
            filtered.append(inc)
    OUT_JSON.write_text(json.dumps({'generated': data.get('generated'), 'filtered_count': len(filtered), 'incidents': filtered}, indent=2))
    with OUT_MD.open('w') as fh:
        fh.write('# Filtered Concurrent Incidents (different teams + documented vuln)\n\n')
        for i,inc in enumerate(filtered, start=1):
            fh.write(f'## Incident {i} - {inc.get("time_window")}\n')
            fh.write(f'- Target IP: {inc.get("target_ip")}\n')
            fh.write(f'- Target Box: {inc.get("target_box")}\n')
            fh.write('- Entries:\n')
            for e in inc['entries']:
                fh.write(f"  - {e.get('timestamp') or 'no-ts'} | {e['log_file']}#L{e['line']} | {e['command']}\n")
            fh.write('- Matched Vulnerability Notes:\n')
            for n in inc.get('matched_vuln_notes',[]):
                fh.write(f"  - {n['file']}: {', '.join(n['matches'])}\n")
            fh.write('\n')
    print(f'Wrote {OUT_JSON} and {OUT_MD} with {len(filtered)} incidents')

if __name__ == '__main__':
    main()
