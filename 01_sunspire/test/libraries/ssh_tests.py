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

def test_ssh_key_login(target_ip: str, username: str, private_key_str: str, port: int = 22) -> AttackResult:
    try:
        private_key = paramiko.Ed25519Key.from_private_key_file(private_key_str)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, port=port, username=username, pkey=private_key)
        client.close()
        return AttackResult(success=True, message="SSH key-based login successful")
    except Exception as e:
        return AttackResult(success=False, message=str(e))