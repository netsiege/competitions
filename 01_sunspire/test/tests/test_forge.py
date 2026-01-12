import unittest
from libraries.http_tests import check_http_payload_200
from libraries.cmd_tests import test_cmd_execution_over_ssh
from custom.forge import forge_git_initial_access_via_git

class TestForge(unittest.TestCase):
    forge_target_ip = "10.100.7.44"

    def test_0_forge_git_repo_available(self):  # git repo available
        result = check_http_payload_200(
            target_ip=self.forge_target_ip,
            url_path="/git/",
        )

        self.assertTrue(result.success, msg=result.message)

    def test_0_forge_git_initial_access(self):  # git initial access
        result = forge_git_initial_access_via_git(
            target_ip=self.forge_target_ip,
        )

        self.assertTrue(result.success, msg=result.message)

    def test_1_forge_api_status(self):  # api status
        result = check_http_payload_200(
            target_ip=self.forge_target_ip,
            url_path="/api/status",
            port=4000,
        )

        self.assertTrue(result.success, msg=result.message)

        import json
        if json.loads(result.data).get("operational") is not True:
            self.fail("API status 'operational' is not true")


    def test_1_sensitive_endpoint(self):  # sensitive endpoint
        result = check_http_payload_200(
            target_ip=self.forge_target_ip,
            url_path="/api/info?token=ab5f4cad309",
            port=4000,
            headers={"User-Agent": "STARFALLER"}
        )
        self.assertTrue(result.success, msg=result.message)
        self.assertIn("7ZjXxjQB", result.data or "", msg="Sensitive data not found")
    
    def test_1_sensitive_endpoint_from_starfall(self):
        result = test_cmd_execution_over_ssh(
            target_ip="10.100.7.43",
            username="starfall",
            password="starfall",
            command=f"curl -s -H 'User-Agent: STARFALLER' http://{self.forge_target_ip}:4000/api/info?token=ab5f4cad309",
            expected_output="7ZjXxjQB"
        )
        self.assertTrue(result.success, msg=result.message)

    # test if CRON job is running by checking syslog for the last 10 minutes
    # we should see CRON[some_number]: (root) CMD (/usr/local/bin/forge-build.sh)
    def test_2_forge_cron_job_is_running(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.forge_target_ip,
            username="root",
            password="7ZjXxjQB",
            command="grep 'CRON' /var/log/syslog | tail -n 20",
            expected_output="/usr/local/bin/forge-build.sh"
        )
        self.assertTrue(result.success, msg=result.message)
    
    def test_2_manufacturing_repository_exists(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.forge_target_ip,
            username="root",
            password="7ZjXxjQB",
            command="stat /home/forge/manufacturing"
        )
        self.assertTrue(result.success, msg=result.message)
    
    def test_2_manufacturing_repository_validation_sh_is_writable(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.forge_target_ip,
            username="forge",
            password="h1ewFWZG",
            command="if [ -w /home/forge/manufacturing-scripts/validate.sh ]; then echo 'valid'; fi",
            expected_output="valid"
        )
        self.assertTrue(result.success, msg=result.message)
    
    def test_2_manufacturing_repository_precommit_hooks_is_writable(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.forge_target_ip,
            username="forge",
            password="h1ewFWZG",
            command="if [ -w /home/forge/manufacturing-scripts/.git/hooks/pre-commit.sample ]; then echo 'valid'; fi",
            expected_output="valid"
        )
        self.assertTrue(result.success, msg=result.message)

    def test_3_lateral_movement_to_pyre_password_reuse(self):
        result = test_cmd_execution_over_ssh(
            target_ip="10.100.7.45",
            username="pyre",
            password="h1ewFWZG",
            command="whoami",
            expected_output="pyre"
        )
        self.assertTrue(result.success, msg=result.message)