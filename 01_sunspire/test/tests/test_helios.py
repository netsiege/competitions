import unittest
from libraries.smb_login_tests import test_smb_login
from libraries.cmd_tests import test_cmd_execution_over_psrp
from libraries.http_tests import check_http_payload_200

class TestHelios(unittest.TestCase):
    helios_target_ip = "10.100.7.41"

    # initial access via SMB, weak password for helios user
    def test_0_helios_smb_login(self): # check if SMB login is successful
        result = test_smb_login(
            target_ip=self.helios_target_ip, 
            username="helios", 
            password="password"
        )
        self.assertTrue(result.success, msg=result.message)

    # test to see if ADMIN_BACKUP_KEY=BTw5hYqi environment variable is set
    def test_1_helios_admin_backup_key_env_var(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.helios_target_ip,
            username="Administrator",
            password="BTw5hYqi",
            # check if it is available to all users 
            command="[Environment]::GetEnvironmentVariables('Machine')['ADMIN_BACKUP_KEY']",
            expected_output="BTw5hYqi"
        )

        self.assertTrue(result.success, msg=result.message)

    # test to see if C:\Users\helios\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine contains administrator's password
    def test_2_helios_psreadline_contains_admin_password(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.helios_target_ip,
            username="Administrator",
            password="BTw5hYqi",
            command="Get-Content -Path 'C:\\Users\\helios\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt' | Select-String -Pattern 'BTw5hYqi'",
            expected_output="BTw5hYqi"
        )

        self.assertTrue(result.success, msg=result.message)
    
    # test to see if /credentials.txt on helios web server contains helios user's password
    def test_3_helios_http_credentials_txt(self):
        result = check_http_payload_200(
            target_ip=self.helios_target_ip,
            url_path="/credentials.txt",
        )
        # print(result.data)
        if result.success:
            if "password" in result.data:
                result.success = True
                result.message = "Found helios user's password in /credentials.txt"
            else:
                result.success = False
                result.message = "Did not find helios user's password in /credentials.txt"

        self.assertTrue(result.success, msg=result.message)

    # test if IIS server is running on helios
    def test_3_helios_iis_server_running(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.helios_target_ip,
            username="Administrator",
            password="BTw5hYqi",
            command="Get-Service -Name W3SVC | Select-Object -ExpandProperty Status",
            expected_output="Running"
        )

        self.assertTrue(result.success, msg=result.message)
    
    # test if directory browsing is enabled on helios web server
    def test_3_helios_http_directory_browsing(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.helios_target_ip,
            username="Administrator",
            password="BTw5hYqi",
            command="Import-Module WebAdministration; Get-WebConfigurationProperty -Filter /system.webServer/directoryBrowse -Name enabled -PSPath 'IIS:\\' | Select-Object -ExpandProperty Value",
            expected_output="True"
        )

        self.assertTrue(result.success, msg=result.message)

if __name__ == "__main__":
    unittest.main()