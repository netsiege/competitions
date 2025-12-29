from core.test_structs import AttackResult
from pypsrp.client import Client
import paramiko 

def test_cmd_execution_over_ssh(target_ip: str, username: str, password: str, command: str, expected_output: str = "", port: int = 22) -> AttackResult:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, port=port, username=username, password=password)
        _, stdout, _ = client.exec_command(command)
        output = stdout.read().decode()
        client.close()  
        if expected_output != "":
            if expected_output in output:
                return AttackResult(success=True, message="Command executed successfully")
            else:
                return AttackResult(success=False, message="Command executed but output did not match expected output")
        return AttackResult(success=True, message="Command executed successfully")
    except Exception as e:
        return AttackResult(success=False, message=str(e))
    
def test_cmd_execution_over_psrp(
    target_ip: str, 
    username: str, 
    password: str, 
    command: str, 
    expected_output: str = "", 
    port: int = 5985  # Default WinRM HTTP port
) -> AttackResult:
    try:
        # Initialize the PSRP client
        # ssl=False for port 5985; set ssl=True and port 5986 for HTTPS
        client = Client(target_ip, username=username, password=password, ssl=False, auth="ntlm")

        # Execute the command
        # execute_ps is used for PowerShell; execute_cmd for batch/shell commands
        stdout, stderr, had_errors = client.execute_ps(command)

        if had_errors:
            return AttackResult(success=False, message=f"PSRP Error: {stderr}")

        output = stdout.strip()
        # print(output)

        if expected_output:
            if expected_output in output:
                return AttackResult(success=True, message="Command executed successfully")
            else:
                return AttackResult(
                    success=False, 
                    message=f"Output mismatch. Received: {output[:50]}..."
                )

        return AttackResult(success=True, message="Command executed successfully")

    except Exception as e:
        return AttackResult(success=False, message=f"Connection failed: {str(e)}")