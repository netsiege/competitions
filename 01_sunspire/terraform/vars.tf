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
        cores         = number
        memory        = number  # in MB
        disk_size     = string  # with unit (e.g., "10G")
        vmid          = number
    }))
    default = {
        solaris = {
            os_type    = "linux"
            ip_address = "10.100.7.50/18"
            cores      = 2
            memory     = 2048
            disk_size  = "10G"
            vmid       = 1014
        }
        helios = {
            os_type    = "windows"
            ip_address = "10.100.7.51/18"
            cores      = 4
            memory     = 4096
            disk_size  = "40G"
            vmid       = 1015
        }
        orbital = {
            os_type    = "windows"
            ip_address = "10.100.7.52/18"
            cores      = 4
            memory     = 4096
            disk_size  = "40G"
            vmid       = 1016
        }
        starfall = {
            os_type    = "linux"
            ip_address = "10.100.7.53/18"
            cores      = 2
            memory     = 2048
            disk_size  = "10G"
            vmid       = 1017
        }
    }
}