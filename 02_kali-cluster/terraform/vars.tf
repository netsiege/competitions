variable "token_secret" {}
variable "token_id" {}

variable "proxmox_host" {
    default = "cuci-pve-02"
}

variable "kali_template_name" {
    description = "Name of the Kali template to clone from (VM 1041: kali-netsiege-b)"
    default     = "kali-netsiege-b"
}

variable "api_url" {
    default = "https://pve1.cyberuci.com/api2/json"
}

variable "nic_name" {
    default = "vmbr3"
}

variable "kali_vms" {
    description = "Map of Kali VMs to create with their configurations (12 machines in 3 groups)"
    type = map(object({
        group      = string  # "group_1", "group_2", or "group_3"
        ip_address = string  # IP address with CIDR (e.g., "10.100.7.11/18")
        macaddr    = string  # MAC address
        cores      = number
        memory     = number  # in MB
        disk_size  = string  # with unit (e.g., "33G")
        vmid       = number
    }))
    default = {
        # Group 1: IPs 10.100.7.11-14, password 6pMAUz1N
        kali-group1-01 = {
            group      = "group_1"
            ip_address = "10.100.7.11/18"
            macaddr    = "BC:24:11:3A:BF:01"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1053
        }
        kali-group1-02 = {
            group      = "group_1"
            ip_address = "10.100.7.12/18"
            macaddr    = "BC:24:11:3A:BF:02"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1042
        }
        kali-group1-03 = {
            group      = "group_1"
            ip_address = "10.100.7.13/18"
            macaddr    = "BC:24:11:3A:BF:03"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1043
        }
        kali-group1-04 = {
            group      = "group_1"
            ip_address = "10.100.7.14/18"
            macaddr    = "BC:24:11:3A:BF:04"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1044
        }

        # Group 2: IPs 10.100.7.21-24, password dFMVxYA4
        kali-group2-01 = {
            group      = "group_2"
            ip_address = "10.100.7.21/18"
            macaddr    = "BC:24:11:3A:BF:05"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1045
        }
        kali-group2-02 = {
            group      = "group_2"
            ip_address = "10.100.7.22/18"
            macaddr    = "BC:24:11:3A:BF:06"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1046
        }
        kali-group2-03 = {
            group      = "group_2"
            ip_address = "10.100.7.23/18"
            macaddr    = "BC:24:11:3A:BF:07"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1047
        }
        kali-group2-04 = {
            group      = "group_2"
            ip_address = "10.100.7.24/18"
            macaddr    = "BC:24:11:3A:BF:08"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1048
        }

        # Group 3: IPs 10.100.7.31-34, password PhF7ffPZ
        kali-group3-01 = {
            group      = "group_3"
            ip_address = "10.100.7.31/18"
            macaddr    = "BC:24:11:3A:BF:09"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1049
        }
        kali-group3-02 = {
            group      = "group_3"
            ip_address = "10.100.7.32/18"
            macaddr    = "BC:24:11:3A:BF:0A"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1050
        }
        kali-group3-03 = {
            group      = "group_3"
            ip_address = "10.100.7.33/18"
            macaddr    = "BC:24:11:3A:BF:0B"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1051
        }
        kali-group3-04 = {
            group      = "group_3"
            ip_address = "10.100.7.34/18"
            macaddr    = "BC:24:11:3A:BF:0C"
            cores      = 2
            memory     = 2048
            disk_size  = "33G"
            vmid       = 1052
        }
    }
}
