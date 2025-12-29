import unittest
from libraries.smb_share_tests import test_smb_share_exists, test_smb_file_access, test_smb_file_contents
from libraries.smb_login_tests import test_smb_login
from libraries.cmd_tests import test_cmd_execution_over_psrp

class TestOrbital(unittest.TestCase):
    orbital_target_ip = "10.100.7.42"

    def test_0_orbital_public_share_access(self): # check if share is accessible
        result = test_smb_share_exists(target_ip=self.orbital_target_ip, share_name="public", remote_hostname="ORBITAL", anon=True)
        # print(result)
        self.assertTrue(result.success, msg=result.message)

    def test_0_orbital_hashes_file_access(self): # check if hashes.txt is accessible
        result = test_smb_file_access(target_ip=self.orbital_target_ip, share_name="public", file="hashes.txt", remote_hostname="ORBITAL", anon=True)
        # print(result)
        self.assertTrue(result.success, msg=result.message)
    
    def test_0_orbital_hashes_file_contents(self): # check contents of hashes.txt
        result = test_smb_file_contents(target_ip=self.orbital_target_ip, share_name="public", expected_content="b0439fae31f8cbba6294af86234d5a28", file="hashes.txt", remote_hostname="ORBITAL", anon=True)
        # print(result)
        self.assertTrue(result.success, msg=result.message)
    
    def test_0_orbital_smb_login(self): # check if SMB login is successful with recovered password from hashes.txt
        result = test_smb_login(target_ip=self.orbital_target_ip, username="orbital", password="securepassword")
        # print(result)
        self.assertTrue(result.success, msg=result.message)

    # check to see if scheduled task SolarTelemetry exists
    def test_1_orbital_scheduled_task_exists(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.orbital_target_ip,
            username="Administrator",
            password="5EVB7Zmp",
            command="Get-ScheduledTask -TaskName 'SolarTelemetry'",
            expected_output="SolarTelemetry"
        )
        self.assertTrue(result.success, msg=result.message)

    # check if scheduled task has been run within the last 3 minutes
    def test_1_orbital_scheduled_task_recent_run(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.orbital_target_ip,
            username="Administrator",
            password="5EVB7Zmp",
            command="$task = Get-ScheduledTask -TaskName 'SolarTelemetry'; $lastRun = (Get-ScheduledTaskInfo -TaskName 'SolarTelemetry').LastRunTime; if ((Get-Date) - $lastRun -lt (New-TimeSpan -Minutes 3)) { Write-Output 'Recent' } else { Write-Output 'Old' }",
            expected_output="Recent"
        )
        self.assertTrue(result.success, msg=result.message)

    # check if C:\Sunspire\telemetry.ps1 file exists
    def test_1_orbital_telemetry_file_exists(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.orbital_target_ip,
            username="Administrator",
            password="5EVB7Zmp",
            command="Test-Path 'C:\\Sunspire\\telemetry.ps1'",
            expected_output="True"
        )
        self.assertTrue(result.success, msg=result.message)

    # check to see if everyone has full control over the C:\Sunspire\telemetry.ps1 file
    def test_1_orbital_telemetry_file_permissions(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.orbital_target_ip,
            username="Administrator",
            password="5EVB7Zmp",
            command="(Get-Acl 'C:\\Sunspire\\telemetry.ps1').Access | Where-Object { $_.IdentityReference -eq 'Everyone' } | Select-Object -ExpandProperty FileSystemRights",
            expected_output="FullControl"
        )
        self.assertTrue(result.success, msg=result.message)

    # see if user orbital has SeShutdownPrivilege
    def test_2_orbital_orbital_shutdown_privilege(self):
        result = test_cmd_execution_over_psrp(
            target_ip=self.orbital_target_ip,
            username="orbital",
            password="securepassword",
            command="whoami /priv | findstr SeShutdownPrivilege",
            expected_output="SeShutdownPrivilege"
        )
        self.assertTrue(result.success, msg=result.message)