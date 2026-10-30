#!/usr/bin/env python3
"""
Generate a cleaned Markdown report from reports/filtered_incidents.json
Produces: reports/redone_report.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
IN_FILE = REPORTS / 'filtered_incidents.json'
OUT_MD = REPORTS / 'redone_report.md'

def summarize(incidents):
    # top incidents by number of entries
    by_size = sorted(incidents, key=lambda i: len(i.get('entries',[])), reverse=True)
    top10 = by_size[:10]
    return top10

def fmt_entry(e):
    ts = e.get('timestamp') or 'no-ts'
    return f"- {ts} | {e['log_file']}#L{e['line']} | `{e['command']}`"

def main():
    data = json.loads(IN_FILE.read_text())
    incs = data.get('incidents', [])
    top10 = summarize(incs)
    with OUT_MD.open('w') as fh:
        fh.write('# Redone Concurrent Incident Report\n\n')
        fh.write('**Scope**: incidents filtered to those mapped to documented vulnerabilities and involving agents from different subnet groups.\n\n')
        fh.write('## Executive Summary\n')
        fh.write(f'- Total filtered incidents: {len(incs)}\n')
        fh.write(f'- Top incidents shown: {len(top10)}\n\n')

        fh.write('## Top 10 Incidents (by number of entries)\n')
        for idx,inc in enumerate(top10, start=1):
            fh.write(f'### {idx}. {inc.get("target_box") or inc.get("target_ip")} — {len(inc.get("entries",[]))} events\n')
            fh.write(f'- Time window: {inc.get("time_window")}\n')
            fh.write(f'- Target IP: {inc.get("target_ip")}\n')
            fh.write('- Entries:\n')
            for e in inc.get('entries',[]):
                fh.write(fmt_entry(e) + '\n')
            if inc.get('matched_vuln_notes'):
                fh.write('- Matched vulnerability documentation:\n')
                for n in inc['matched_vuln_notes']:
                    fh.write(f"  - {n['file']}: {', '.join(n['matches'])}\n")
            fh.write('\n')

        fh.write('## Full Incident Index\n')
        for i,inc in enumerate(incs, start=1):
            fh.write(f'- Incident {i}: {inc.get("time_window")} | Target: {inc.get("target_box") or inc.get("target_ip")} | Events: {len(inc.get("entries",[]))}\n')

    print(f'Wrote {OUT_MD}')

if __name__ == '__main__':
    main()
