terraform {
    required_providers {
        proxmox = {
            source  = "telmate/proxmox"
            version = "3.0.2-rc06"
        }
    }
}

provider "proxmox" {
  pm_api_url          = var.api_url
  pm_api_token_id     = var.token_id
  pm_api_token_secret = var.token_secret
  pm_tls_insecure     = true
}

# Define password groups
locals {
  password_groups = {
    group_1 = "6pMAUz1N"
    group_2 = "dFMVxYA4"
    group_3 = "PhF7ffPZ"
  }
}

resource "proxmox_vm_qemu" "kali_vms" {
    for_each = var.kali_vms

    name        = each.key
    target_node = var.proxmox_host
    clone       = var.kali_template_name

    force_create        = true
    clone_wait          = 40
    additional_wait     = 15
    bios                = "seabios"
    memory              = each.value.memory
    scsihw              = "virtio-scsi-single"
    full_clone          = false
    vmid                = each.value.vmid

    cpu {
        cores   = each.value.cores
        sockets = 1
    }

    # Primary disk and cloud-init drive
    disks {
        scsi {
            scsi0 {
                disk {
                    size     = each.value.disk_size
                    storage  = "pve-pool-730xd"
                    format   = "qcow2"
                }
            }
        }
        
        # Cloud-init drive on IDE2
        ide {
            ide2 {
                cloudinit {
                    storage = "pve-pool-730xd"
                }
            }
        }
    }

    network {
        id      = 0
        model   = "virtio"
        bridge  = var.nic_name
        macaddr = each.value.macaddr
    }

    # Cloud-init configuration
    os_type    = "cloud-init"
    agent      = 1
    ciuser     = "kali"
    cipassword = local.password_groups[each.value.group]
    boot       = "order=ide2;scsi0;net0"
    ipconfig0  = "ip=${each.value.ip_address},gw=10.100.0.1"
    nameserver = "10.100.0.1"
    tags       = "kali-${each.value.group}"
}
