import unittest
from libraries.smb_login_tests import test_smb_login

class TestHelios(unittest.TestCase):
    helios_target_ip = "10.100.7.41"

    # initial access via SMB, weak password for helios user
    def test_0_helios_smb_login(self): # check if SMB login is successful
        result = test_smb_login(target_ip=self.helios_target_ip, username="helios", password="password")
        self.assertTrue(result.success, msg=result.message)

if __name__ == "__main__":
    unittest.main()