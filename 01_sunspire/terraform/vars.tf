# these are handled by terraform.tfvars
variable "token_secret" {}
variable "token_id" {}

variable "proxmox_host" {
    default = "cuci-pve-02"
}

variable "ubuntu_template_name" {
    default = "ubuntu-24-04-server-template-new"
}

variable "windows_template_name" {
    default = "windows-server-2022-template"
}

variable "api_url" {
    default = "https://pve1.cyberuci.com/api2/json"
}

variable "nic_name" {
    default = "vmbr3"
}

variable "vms" {
    description = "Map of VMs to create with their configurations"
    type = map(object({
        os_type       = string  # "linux" or "windows"
        ip_address    = string  # IP address with CIDR (e.g., "10.100.7.50/24")
        macaddr       = string  # MAC address (e.g., "BC:24:11:3A:BE:FF")
        cores         = number
        memory        = number  # in MB
        disk_size     = string  # with unit (e.g., "10G")
        vmid          = number
    }))
    default = {
        solaris = {
            os_type    = "linux"
            ip_address = "10.100.7.40/18"
            macaddr    = "BC:24:11:3A:BE:00"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1014
        }
        helios = {
            os_type    = "windows"
            ip_address = "10.100.7.41/18"
            macaddr    = "BC:24:11:3A:BE:01"
            cores      = 4
            memory     = 4096
            disk_size  = "40G"
            vmid       = 1015
        }
        orbital = {
            os_type    = "windows"
            ip_address = "10.100.7.42/18"
            macaddr    = "BC:24:11:3A:BE:02"
            cores      = 4
            memory     = 4096
            disk_size  = "40G"
            vmid       = 1016
        }
        starfall = {
            os_type    = "linux"
            ip_address = "10.100.7.43/18"
            macaddr    = "BC:24:11:3A:BE:03"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1017
        }
        forge = {
            os_type    = "linux"
            ip_address = "10.100.7.44/18"
            macaddr    = "BC:24:11:3A:BE:04"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1018
        }
        pyre = {
            os_type    = "linux"
            ip_address = "10.100.7.45/18"
            macaddr    = "BC:24:11:3A:BE:05"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1019
        }
        ember = {
            os_type    = "windows"
            ip_address = "10.100.7.46/18"
            macaddr    = "BC:24:11:3A:BE:06"
            cores      = 4
            memory     = 4096
            disk_size  = "40G"
            vmid       = 1020
        }
        crucible = {
            os_type    = "linux"
            ip_address = "10.100.7.47/18"
            macaddr    = "BC:24:11:3A:BE:07"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1021
        }
        inspire = {
            os_type    = "linux"
            ip_address = "10.100.7.48/18"
            macaddr    = "BC:24:11:3A:BE:08"
            cores      = 2
            memory     = 2048
            disk_size  = "20G"
            vmid       = 1022
        }
    }
}