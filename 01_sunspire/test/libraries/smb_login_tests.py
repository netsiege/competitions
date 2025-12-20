from smbclient import register_session, listdir
from smbprotocol.exceptions import SMBAuthenticationError
from core.test_structs import AttackResult

def test_smb_login(target_ip: str, username: str, password: str, share: str = "IPC$") -> AttackResult:
    try:
        register_session(target_ip, username=username, password=password)
        # Attempt to list the root directory of the share to verify access
        listdir(f"\\\\{target_ip}\\{share}")
        
        return AttackResult(success=True, message="SMB login successful")
    except SMBAuthenticationError as e:
        return AttackResult(success=False, message="Authentication failed: " + str(e))
    except Exception as e:
        return AttackResult(success=False, message=str(e))