from core.test_structs import AttackResult
import paramiko

def test_ssh_login(target_ip: str, username: str, password: str, port: int = 22) -> AttackResult:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, port=port, username=username, password=password)
        client.close()
        return AttackResult(success=True, message="SSH login successful")
    except Exception as e:
        return AttackResult(success=False, message=str(e))        

def test_command_over_ssh(target_ip: str, username: str, password: str, command: str, expected_output: str = "", port: int = 22) -> AttackResult:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
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
