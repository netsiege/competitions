import unittest
from libraries.smb_login_tests import test_smb_login
from libraries.cmd_tests import test_cmd_execution_over_psrp

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


if __name__ == "__main__":
    unittest.main()