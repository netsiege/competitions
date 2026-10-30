# Forge (10.100.7.44) Concurrent Incident Report

**Total incidents targeting Forge**: 2

## Vulnerability Summary
- cron: 6 incidents
- git: 10 incidents

## All Incidents
### Incident 1
- Time window: 2026-01-26T20:01:00
- Target: forge (10.100.7.44)
- Number of entries: 2
- Entries:
  - 2026-01-26T20:01:58 | logs/10.100.7.32/shell_history.csv#L618
    Command: `ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44`
  - 2026-01-26T20:01:04 | logs/10.100.7.24/shell_history.csv#L224
    Command: `gobuster dir -u https://http://10.100.7.44/ -w wordlist.txt`
- Matched vulnerability documentation:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

### Incident 2
- Time window: 2026-01-26T20:02:00
- Target: forge (10.100.7.44)
- Number of entries: 2
- Entries:
  - 2026-01-26T20:02:06 | logs/10.100.7.32/shell_history.csv#L621
    Command: `ssh forge@10.100.7.44`
  - 2026-01-26T20:02:37 | logs/10.100.7.24/shell_history.csv#L227
    Command: `gobuster dir -u https://http://10.100.7.44/ -w wordlist.txt`
- Matched vulnerability documentation:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

