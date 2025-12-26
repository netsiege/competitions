from smb.SMBConnection import SMBConnection
from typing import *
from core.test_structs import AttackResult

def test_smb_share_exists(target_ip: str, share_name: str, username: str = "", password: str = "", remote_hostname: str = "remote_machine", anon: bool = True) -> AttackResult:
    """
    Test access to a file share on a target SMB server.
    """
    try:
        if anon:
            username = ""
            password = ""

        conn = SMBConnection(username, password, "netsiege-client", remote_hostname)
        connected = conn.connect(target_ip, 139)

        if not connected:
            return AttackResult(success=False, message="Could not connect to the SMB server.")

        # print('listing shares')
        shares = conn.listShares()
        share_names = [share.name for share in shares]

        if share_name and share_name not in share_names:
            return AttackResult(success=False, message=f"Share '{share_name}' not found on the server.")

        target_share = share_name if share_name else share_names[0]
        files = conn.listPath(target_share, '/')

        return AttackResult(success=True, message=f"Accessed share '{target_share}' successfully.", data=[f.filename for f in files])

    except Exception as e:
        return AttackResult(success=False, message=f"{type(e).__name__}: {e}")

def test_smb_file_access(target_ip: str, share_name: str, file: str, path: str = "/", username: str = "", password: str = "", remote_hostname: str = "remote_machine", anon: bool = True) -> AttackResult:
    """
    Test access to a specific file on a target SMB server.
    """
    try:
        if anon:
            username = ""
            password = ""

        conn = SMBConnection(username, password, "local_machine", remote_hostname)
        connected = conn.connect(target_ip, 139)

        if not connected:
            return AttackResult(success=False, message="Could not connect to the SMB server.")

        shares = conn.listShares()
        share_names = [share.name for share in shares]

        if share_name and share_name not in share_names:
            return AttackResult(success=False, message=f"Share '{share_name}' not found on the server.")

        target_share = share_name if share_name else share_names[0]
        files = conn.listPath(target_share, path=path)
        file_names = [f.filename for f in files]

        if file not in file_names:
            return AttackResult(success=False, message=f"File '{file}' not found in share '{target_share}'.")

        return AttackResult(success=True, message=f"Accessed file '{file}' successfully.")

    except Exception as e:
        return AttackResult(success=False, message=str(e))
    
def test_smb_file_contents(target_ip: str, share_name: str, file: str, expected_content: str, path: str = "/", username: str = "", password: str = "", remote_hostname: str = "remote_machine", anon: bool = True) -> AttackResult:
    """
    Test contents of a specific file on a target SMB server.
    """
    try:
        if anon:
            username = ""
            password = ""

        conn = SMBConnection(username, password, "local_machine", remote_hostname)
        connected = conn.connect(target_ip, 139)

        if not connected:
            return AttackResult(success=False, message="Could not connect to the SMB server.")

        shares = conn.listShares()
        share_names = [share.name for share in shares]

        if share_name and share_name not in share_names:
            return AttackResult(success=False, message=f"Share '{share_name}' not found on the server.")

        target_share = share_name if share_name else share_names[0]
        from utils.file_share_utils import download_smb_file
        file_content = download_smb_file(conn, target_share, f"{path}{file}").decode()

        if expected_content in file_content:
            return AttackResult(success=True, message=f"File '{file}' contains expected content.", data=file_content)
        else:
            return AttackResult(success=False, message=f"File '{file}' does not contain expected content.")

    except Exception as e:
        return AttackResult(success=False, message=str(e))