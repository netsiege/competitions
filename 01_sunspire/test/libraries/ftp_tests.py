from ftplib import FTP
from core.test_structs import AttackResult

def check_ftp_anonymous_login(target_ip: str, port: int = 21) -> AttackResult:
    """
    Check if the target FTP server allows anonymous login.
    """
    try:
        ftp = FTP()
        ftp.connect(target_ip, port, timeout=5)
        msg = ftp.login() # Anonymous by default
        ftp.quit()
        return AttackResult(success=True, message=f"Anonymous FTP Login Successful: {msg}")
    except Exception as e:
        return AttackResult(success=False, message=str(e))
