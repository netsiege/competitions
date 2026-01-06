import unittest 
from libraries.smb_share_tests import test_smb_share_exists, test_smb_file_contents
from libraries.cmd_tests import test_cmd_execution_over_psrp
from libraries.http_tests import check_http_payload_200

class TestEmber(unittest.TestCase):
    ember_target_ip = "10.100.7.46"

    def test_0_ember_public_share_access(self): # check if share is accessible
        result = test_smb_share_exists(target_ip=self.ember_target_ip, share_name="Scripts", remote_hostname="EMBER", anon=True)
        # print(result)
        self.assertTrue(result.success, msg=result.message)

    def test_0_ember_scripts_maintenance_script_access(self): 
        result = test_smb_file_contents(target_ip=self.ember_target_ip, share_name="Scripts", expected_content="Running scheduled maintenance...", file="maintenance.ps1", remote_hostname="EMBER", anon=True)

        self.assertTrue(result.success, msg=result.message)

    def test_0_ember_scripts_readme_file_access(self): # check contents of readme.txt
        result = test_smb_file_contents(
            target_ip=self.ember_target_ip,
            share_name="Scripts",
            expected_content="runs every 5 minutes",
            file="readme.txt",
            remote_hostname="EMBER",
            anon=True
        )
        self.assertTrue(result.success, msg=result.message)

    def test_0_maintenance_script_writable(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.ember_target_ip,
            username="ember",
            password="J4f9juEr",
            command="(Get-Acl 'C:\\Scripts\\maintenance.ps1').Access | Where-Object { $_.IdentityReference -eq 'Everyone' } | Select-Object -ExpandProperty FileSystemRights",
            expected_output="FullControl"
        )
        self.assertTrue(result.success, msg=result.message)

    def test_0_ember_scheduled_task_exists(self): # check to see if scheduled task EmberMaintenance exists
        result = test_cmd_execution_over_psrp(
            target_ip=self.ember_target_ip,
            username="Administrator",
            password="RM1dT8zj",
            command="Get-ScheduledTask -TaskName 'SystemMaintenance'",
            expected_output="SystemMaintenance"
        )
        self.assertTrue(result.success, msg=result.message)

    def test_0_ember_scheduled_task_recent_run(self): # check if scheduled task has been run within the last 6 minutes
        result = test_cmd_execution_over_psrp(
            target_ip=self.ember_target_ip,
            username="Administrator",
            password="RM1dT8zj",
            command="$task = Get-ScheduledTask -TaskName 'SystemMaintenance'; $lastRun = (Get-ScheduledTaskInfo -TaskName 'SystemMaintenance').LastRunTime; if ((Get-Date) - $lastRun -lt (New-TimeSpan -Minutes 6)) { Write-Output 'Recent' } else { Write-Output 'Old' }",
            expected_output="Recent"
        )
        self.assertTrue(result.success, msg=result.message)

    def test_1_ember_phpinfo_leaks_secret(self):
        result = check_http_payload_200(
            target_ip=self.ember_target_ip,
            url_path="/info.php",
        )
        self.assertTrue(result.success, msg=result.message)
        self.assertIn("J4f9juEr", result.data, msg="Secret password not found in phpinfo output")
