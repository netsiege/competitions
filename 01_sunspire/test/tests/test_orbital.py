import unittest
from libraries.smb_share_tests import test_smb_share_exists, test_smb_file_access, test_smb_file_contents
from libraries.smb_login_tests import test_smb_login

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

    