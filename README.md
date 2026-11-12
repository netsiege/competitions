# Netsiege Competitions

Scenarios, provisioning code, vulnerable applications, curriculum, and research data from past **Netsiege** competitions.

Netsiege is a long-form, club-led **King-of-the-Hill (KotH)** cybersecurity competition. It is built so that a student cyber club with no instructor of record and no dedicated budget can give its newer members hands-on training. This repository holds the *competition content*: the networks teams break into, the code that builds them, and the material used to teach alongside them. The scoring toolchain lives in separate repositories (see [Related repositories](#related-repositories)).


> [!WARNING]
> **Everything in this repository is intentionally vulnerable.** The applications, deploy scripts, credentials, SSH keys, and `.env` files are deliberate parts of the attack surface. Deploy them **only** on isolated lab networks you control. 



## Repository structure

```
.
├── 00_olympus/                 # Olympus: early prototype scenario (partial)
│   ├── apollo/                 #   Flask inventory API ("phobos-api") + systemd unit
│   └── hermes/                 #   Static status page
│
├── 01_sunspire/                # Sunspire: scenario from the SIGCSE TS 2027 pilot
│   ├── apps/                   #   Vulnerable applications, one per host role
│   ├── boxes/<host>/           #   Per-host deploy scripts + documentation.md
│   │   ├── deploy/             #     deploy.sh / deploy.ps1 (+ helpers)
│   │   └── documentation.md    #     Intended attack paths, users, services, lateral movement
│   ├── credentials/            #   SSH keypairs that are part of the scenario (intentionally public)
│   ├── terraform/              #   Proxmox VM provisioning for the 9 scored hosts
│   ├── ansible/                #   Deploy, Tally agent install, scoring user, log collection, cleanup
│   ├── test/                   #   Python validation suite that checks each host's attack paths
│   ├── phase2.yml              #   Scorekeeper config: control + uptime checks for all Sunspire hosts
│   ├── phase1.yml              #   Scorekeeper config from the earlier Olympus scenario
│   ├── deploy-all.py           #   Alternative to Ansible: push sunspire.tar.gz and run deploy scripts
│   ├── sunspire.tar.gz         #   Pre-built bundle of apps/ boxes/ credentials/ for deployment
│   ├── curriculum/             #   Rulebook, scenario documentation, roadmap, lecture slides
│   ├── logs/<ip>/              #   Raw shell-history telemetry from the 12 participant workstations
│   ├── aggregated_data/        #   Cleaned and aggregated telemetry datasets (CSV)
│   ├── tools/                  #   Analysis scripts (incident detection, time-series, plots)
│   ├── aggregate_shell_history.py
│   └── reports/                #   Generated analysis reports, figures, and intermediate JSON
│
├── 02_kali-cluster/            # Terraform for 12 participant Kali workstations (3 teams × 4)
├── 02_kali-cluster.zip         # Archived copy of the above
├── LICENSE                     # GPL-3.0
└── README.md
```

---

## Scenarios

### Sunspire (`01_sunspire/`)

Sunspire is the scenario from the pilot reported in the paper. It is set in the municipal computing network of a fictional futuristic city, and each machine stands in for one civic system. It has **9 scored machines** (Ubuntu and Windows Server) introduced over **three phases**:

| Phase | Host | OS | Role |
|---|---|---|---|
| 1 | **Helios** | Windows Server 2022 | Network administration server (IIS, RDP) |
| 1 | **Orbital** | Windows Server 2022 | File processing and scheduling (SMB, MSSQL) |
| 1 | **Solaris** | Ubuntu | Legacy file-sharing server (SSH, SMB, HTTP) |
| 1 | **Starfall** | Ubuntu 24.04 | Gateway / critical services API |
| 2 | **Forge** | Ubuntu 24.04 | Manufacturing: git server and materials API |
| 2 | **Pyre** | Ubuntu | Thermal management and safety monitoring |
| 2 | **Ember** | Windows Server | Forgotten legacy web server (IIS + PHP) |
| 3 | **Inspire** | Ubuntu 24.04 | Solar weather and energy forecasting |
| 3 | **Crucible** | Ubuntu | — |

Each host's intended initial-access, privilege-escalation, and lateral-movement paths are documented in `01_sunspire/boxes/<host>/documentation.md`. 

The pilot ran for seven weeks (January–February 2026) with 12 novice-leaning participants from a student cyber club, split into three teams of four.


### Olympus (`00_olympus/`)

An earlier, smaller scenario built on Greek-mythology hosts (Hera, Hermes, Hestia, Apollo, Hades). Only part of it is preserved here. The scoring configuration for it is `01_sunspire/phase1.yml`.


### Kali cluster (`02_kali-cluster/`)

Terraform that provisions the participant workstations: 12 Kali Linux VMs in three groups of four (`10.100.7.11–14`, `.21–24`, `.31–34`). Giving everyone the same workstation removes per-participant setup and provides a uniform platform for telemetry collection. See [`02_kali-cluster/terraform/README.md`](02_kali-cluster/terraform/README.md).


---


## Using this repository

### 1. Teach with the curriculum only

`01_sunspire/curriculum/` contains:

- **`Competition Rulebook and Instructions.pdf`**: rules, scoring, and access instructions for participants
- **`Sunspire - Documentation.pdf`**: the scenario write-up
- **`Sunspire Educational Roadmap.csv`**: session-by-session schedule mapping lectures to competition phases
- **`presentations/`**: lecture slides for each session, plus a blank template

| Phase | Sessions |
|---|---|
| 1 | Intro to Netsiege · OS fundamentals (Linux/Windows CLI, SSH, RDP) · Network enumeration (nmap, enum4linux, password reuse) · File shares (SMB, FTP) |
| 2 | CVEs (using and adapting PoCs) · Basic privilege escalation (SUID, writable files, scheduled jobs, leaked creds) · Web exploitation I (command injection, LFI, file upload) · Defense (log review, credential rotation, hardening) |
| 3 | Review and compete · Web exploitation II (SQLi, log poisoning, SSTI) · Wrap-up and exploit-path release |

The slides were written for peer mentors, so they assume club members with some competition experience are presenting them.


### 2. Run Sunspire as-is

**What you need:**
- A hypervisor. The Terraform targets **Proxmox** through the `telmate/proxmox` provider; for anything else, adapt `terraform/main.tf`.
- Ubuntu and Windows Server VM templates
- 9 VMs for the scored hosts, plus one workstation per participant (optional, see `02_kali-cluster/`)
- One host for [Scorekeeper](https://github.com/netsiege/scorekeeper) and [Perspective](https://github.com/netsiege/perspective)
- An isolated network segment

**Steps:**

```bash
cd 01_sunspire

# 1. Provision VMs
cd terraform
cp terraform.tfvars.example terraform.tfvars   # fill in your Proxmox API credentials
terraform init && terraform apply
cd ..

# 2. Build the deployment bundle (or use the provided sunspire.tar.gz)
tar -czvf sunspire.tar.gz apps/ boxes/ credentials/

# 3. Deploy the scenario, Tally agents, and scoring user
cd ansible
pip install ansible pypsrp
ansible-galaxy collection install -r requirements.yml
ansible-playbook -i inventory.ini deploy.yml
cd ..

# 4. Validate that every intended attack path works
cd test
python main.py        # select the host test classes to run in main.py

# 5. Point Scorekeeper at phase2.yml and start the competition
```

You will need to change the IP addresses, template names, and network bridge in `terraform/vars.tf` and `ansible/inventory.ini` to match your environment. [`01_sunspire/ansible/README.md`](01_sunspire/ansible/README.md) covers all the playbooks, including partition resizing, log fetching, and cleanup.

**Phasing.** All hosts can be provisioned up front. Release each phase's hosts to participants at its phase boundary, either by enabling their network access or by adding them to the Scorekeeper config.

---

## Related repositories

The Netsiege scoring toolchain:

| Repository | Description |
|---|---|
| [`netsiege/scorekeeper`](https://github.com/netsiege/scorekeeper) | Central scoring engine. Runs the randomized round loop, executes checks, rotates team tokens, and stores state in MongoDB. |
| [`netsiege/tally`](https://github.com/netsiege/tally) | Minimal per-host agent that reports control-check results to Scorekeeper. (A prebuilt binary ships in `01_sunspire/ansible/files/`.) |
| [`netsiege/perspective`](https://github.com/netsiege/perspective) | Participant- and spectator-facing credential portal and live scoreboard, broken down by privilege tier. |
| [`netsiege/automation`](https://github.com/netsiege/automation) | Operational tooling for organizers. |



---

## License

Released under the [GNU General Public License v3.0](LICENSE).

Contributions are welcome, including new scenarios, fixes to existing hosts, and curriculum improvements. Please open an issue or a pull request. If you run Netsiege at your club, we would like to hear how it went.

