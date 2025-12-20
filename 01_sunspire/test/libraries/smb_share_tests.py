from smb.SMBConnection import SMBConnection
from typing import *
from core.test_structs import AttackResult

def test_smb_share_exists(target_ip: str, share_name: str, username: str = "", password: str = "", anon: bool = True) -> AttackResult:
    """
    Test access to a file share on a target SMB server.
    """
    try:
        if anon:
            username = ""
            password = ""

        conn = SMBConnection(username, password, "local_machine", "remote_machine")
        connected = conn.connect(target_ip, 139)

        if not connected:
            return AttackResult(success=False, message="Could not connect to the SMB server.")

        shares = conn.listShares()
        share_names = [share.name for share in shares]

        if share_name and share_name not in share_names:
            return AttackResult(success=False, message=f"Share '{share_name}' not found on the server.")

        target_share = share_name if share_name else share_names[0]
        files = conn.listPath(target_share, '/')

        return AttackResult(success=True, message=f"Accessed share '{target_share}' successfully.", data=[f.filename for f in files])

    except Exception as e:
        return AttackResult(success=False, message=str(e))

def test_smb_file_access(target_ip: str, share_name: str, file: str, path: str, username: str = "", password: str = "", anon: bool = True) -> AttackResult:
    """
    Test access to a specific file on a target SMB server.
    """
    try:
        if anon:
            username = ""
            password = ""

        conn = SMBConnection(username, password, "local_machine", "remote_machine")
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