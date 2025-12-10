terraform {
    required_providers {
        proxmox = {                   //< allows us to refer to path as "proxmox"
            source  = "telmate/proxmox" //< Grabs the proxmox provider support ("bgp/proxmox" is another provider) 
            version = "3.0.2-rc04"       //< Enforce usage of pre-release to avoid fatal error present in 2.X versions. pre-rc7 versions are breaking.
        }
    }
}

provider "proxmox" {
  pm_api_url          = var.api_url                      //< PROXMOX API URL
  pm_api_token_id     = var.token_id     //< PROXMOX TOKEN ID (Secrets)
  pm_api_token_secret = var.token_secret //< PROXMOX API Token (Secrets)
  pm_tls_insecure     = true                               //< Enable TLS verification
}


resource "proxmox_vm_qemu" "vms" {
    for_each = var.vms

    name        = each.key
    target_node = var.proxmox_host
    clone       = each.value.os_type == "linux" ? var.ubuntu_template_name : var.windows_template_name

    os_type     = "cloud-init"

    bios        = "seabios"
    memory      = each.value.memory
    scsihw      = "virtio-scsi-single"
    full_clone  = false

    cpu {
        cores   = each.value.cores
        sockets = 1
    }

    disk {
        size     = each.value.disk_size
        storage  = "pve-pool-730xd"
        iothread = true
        slot     = "scsi0"
    }

    network {
        id     = 0
        model  = "virtio"
        bridge = var.nic_name
    }

    ciuser     = "ops"
    cipassword = "9ksP311p"
    boot       = "order=scsi0,net0"
    ipconfig0  = "ip=${each.value.ip_address},gw=10.100.0.1"
}