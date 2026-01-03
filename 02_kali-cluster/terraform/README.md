# Kali Cluster Terraform Configuration

This Terraform configuration deploys 12 Kali Linux VMs across 3 groups on Proxmox node `cuci-pve-02`.

## Structure

**Three groups of 4 machines each:**

### Group 1 (IPs: 10.100.7.11-14)
- Username: `kali`
- Password: `6pMAUz1N`
- VM IDs: 1041-1044
- MACs: BC:24:11:3A:BE:01 - BE:04

### Group 2 (IPs: 10.100.7.21-24)
- Username: `kali`
- Password: `dFMVxYA4`
- VM IDs: 1045-1048
- MACs: BC:24:11:3A:BE:05 - BE:08

### Group 3 (IPs: 10.100.7.31-34)
- Username: `kali`
- Password: `PhF7ffPZ`
- VM IDs: 1049-1052
- MACs: BC:24:11:3A:BE:09 - BE:0C

## Common Configuration

All VMs share the same specs:
- **CPU Cores**: 2
- **Memory**: 2048 MB (2 GB)
- **Disk**: 33 GB (QCOW2 on pve-pool-730xd)
- **Template**: VM 1041 (kali-netsiege-b)
- **Network**: vmbr3, Gateway: 10.100.0.1
- **Cloud-init**: Enabled with static IP configuration

## Setup

1. Set Proxmox API credentials:
   ```bash
   export TF_VAR_token_id="your-token-id"
   export TF_VAR_token_secret="your-token-secret"
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Review the plan:
   ```bash
   terraform plan
   ```

4. Apply the configuration:
   ```bash
   terraform apply
   ```

## MAC Address Consistency

MAC addresses are sequential (BE:01 through BE:0C) to ensure consistent network identity across reclones. If you need to redeploy, the MACs will remain the same, preventing network conflicts.

## Accessing the VMs

After deployment, SSH into any VM:
```bash
ssh kali@10.100.7.11  # Group 1 machine 1
ssh kali@10.100.7.21  # Group 2 machine 1
ssh kali@10.100.7.31  # Group 3 machine 1
```

Use the appropriate password for each group.

## Notes

- Clones use linked clones (`full_clone = false`) for faster deployment
- Cloud-init is configured to inject network and user credentials
- Each VM is tagged with its group (`kali-group_1`, `kali-group_2`, `kali-group_3`)
- VMs will be provisioned on `cuci-pve-02` as specified in the template
