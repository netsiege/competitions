#!/usr/bin/env python3
"""
Generate a detailed report for all Orbital (10.100.7.42) incidents.
Produces: reports/orbital_report.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
IN_FILE = REPORTS / 'filtered_incidents.json'
OUT_MD = REPORTS / 'orbital_report.md'

def main():
    data = json.loads(IN_FILE.read_text())
    incs = data.get('incidents', [])
    
    # filter to orbital (10.100.7.42)
    orbital_incs = [i for i in incs if i.get('target_ip') == '10.100.7.42']
    
    with OUT_MD.open('w') as fh:
        fh.write('# Orbital (10.100.7.42) Concurrent Incident Report\n\n')
        fh.write(f'**Total incidents targeting Orbital**: {len(orbital_incs)}\n\n')
        
        fh.write('## Vulnerability Summary\n')
        all_vulns = set()
        for inc in orbital_incs:
            for n in inc.get('matched_vuln_notes',[]):
+                for m in n.get('matches',[]):
+                    all_vulns.add(m)
+        for v in sorted(all_vulns):
+            count = sum(1 for i in orbital_incs for n in i.get('matched_vuln_notes',[]) for m in n.get('matches',[]) if m == v)
+            fh.write(f'- {v}: {count} incidents\n')
+        
+        fh.write('\n## All Incidents\n')
+        for idx,inc in enumerate(orbital_incs, start=1):
+            fh.write(f'### Incident {idx}\n')
+            fh.write(f'- Time window: {inc.get("time_window")}\n')
+            fh.write(f'- Target: {inc.get("target_box")} ({inc.get("target_ip")})\n')
+            fh.write(f'- Number of entries: {len(inc.get("entries",[]))}\n')
+            fh.write('- Entries:\n')
+            for e in inc.get('entries',[]):
+                ts = e.get('timestamp') or 'no-ts'
+                fh.write(f"  - {ts} | {e['log_file']}#L{e['line']}\n")
+                fh.write(f"    Command: `{e['command']}`\n")
+            if inc.get('matched_vuln_notes'):
+                fh.write('- Matched vulnerability documentation:\n')
+                for n in inc['matched_vuln_notes']:
+                    fh.write(f"  - {n['file']}: {', '.join(n['matches'])}\n")
+            fh.write('\n')
+
+    print(f'Wrote {OUT_MD} with {len(orbital_incs)} incidents')
+
+if __name__ == '__main__':
+    main()
