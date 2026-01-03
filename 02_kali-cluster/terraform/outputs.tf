output "kali_vms" {
    description = "Details of created Kali VMs"
    value = {
        for name, vm in proxmox_vm_qemu.kali_vms : name => {
            vmid       = vm.vmid
            ip_address = vm.ipconfig0
            mac_address = vm.network[0].macaddr
            group      = var.kali_vms[name].group
        }
    }
}

output "group_1_vms" {
    description = "Group 1 Kali VMs (10.100.7.11-14)"
    value = {
        for name, vm in proxmox_vm_qemu.kali_vms : name => {
            vmid       = vm.vmid
            ip_address = vm.ipconfig0
        } if var.kali_vms[name].group == "group_1"
    }
}

output "group_2_vms" {
    description = "Group 2 Kali VMs (10.100.7.21-24)"
    value = {
        for name, vm in proxmox_vm_qemu.kali_vms : name => {
            vmid       = vm.vmid
            ip_address = vm.ipconfig0
        } if var.kali_vms[name].group == "group_2"
    }
}

output "group_3_vms" {
    description = "Group 3 Kali VMs (10.100.7.31-34)"
    value = {
        for name, vm in proxmox_vm_qemu.kali_vms : name => {
            vmid       = vm.vmid
            ip_address = vm.ipconfig0
        } if var.kali_vms[name].group == "group_3"
    }
}
