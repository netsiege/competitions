from smb.SMBConnection import SMBConnection
from typing import *

def download_smb_file(conn: SMBConnection, share_name: str, file_path: str) -> bytes:
    """
    Download a file from an SMB share.

    :param conn: An established SMBConnection object.
    :param share_name: The name of the share to download the file from.
    :param file_path: The path to the file within the share.
    :return: The content of the downloaded file as bytes.
    """
    from io import BytesIO

    file_obj = BytesIO()
    conn.retrieveFile(share_name, file_path, file_obj)
    file_obj.seek(0)
    return file_obj.read()