import requests
from core.test_structs import AttackResult
from typing import Dict, Union, BinaryIO
import os

def check_http_payload_200(
    target_ip: str, 
    url_path: str = "/", 
    params: dict = {}, 
    port: int = 80, 
    verb: str = "GET", 
    form_data: dict = {}, 
    files: Dict[str, Union[str, bytes, BinaryIO]] = {},
    headers: dict = {}
) -> AttackResult:
    """
    Check if a specific payload can be sent to an HTTP endpoint.
    
    Args:
        target_ip: Target IP address
        url_path: URL path (default: "/")
        params: URL query parameters
        port: Target port (default: 80)
        verb: HTTP method - "GET" or "POST" (default: "GET")
        form_data: Form data to send in POST body
        files: Files to upload. Can be:
            - Dict[str, str]: filename -> file path (will auto-open and read)
            - Dict[str, bytes]: filename -> file content bytes
            - Dict[str, BinaryIO]: filename -> file object
            
            If a string value starts with '@', it will be treated as a file path
            
    Returns:
        AttackResult with success status and response data
    """
    try:
        url = f"http://{target_ip}:{port}{url_path}"
        
        # Process files parameter to handle file paths
        processed_files = {}
        files_to_close = []
        
        for field_name, file_data in files.items():
            if isinstance(file_data, str):
                # If string starts with @, treat as file path
                file_path = file_data[1:] if file_data.startswith('@') else file_data
                
                if os.path.exists(file_path):
                    # Open file and track it for cleanup
                    f = open(file_path, 'rb')
                    files_to_close.append(f)
                    # Use basename as filename in multipart
                    processed_files[field_name] = (os.path.basename(file_path), f)
                else:
                    return AttackResult(success=False, message=f"File not found: {file_path}")
            elif isinstance(file_data, bytes):
                # Direct bytes - use field name as filename
                processed_files[field_name] = (field_name, file_data)
            else:
                # Assume file-like object
                processed_files[field_name] = file_data
        
        try:
            if verb == "POST":
                response = requests.post(
                    url, 
                    data={**params, **form_data}, 
                    files=processed_files if processed_files else None,
                    timeout=5,
                    headers=headers
                )
            elif verb == "GET":
                response = requests.get(url, params={**params, **form_data}, timeout=5, headers=headers)
            else:
                return AttackResult(success=False, message=f"Unsupported HTTP verb: {verb}")

            if response.status_code == 200:
                # print(response.status_code)
                return AttackResult(
                    success=True, 
                    message=f"Payload sent successfully to {url}. Status: {response.status_code}", 
                    data=response.text
                )
            else:
                return AttackResult(
                    success=False, 
                    message=f"Request failed with status: {response.status_code}"
                )
        finally:
            # Clean up opened files
            for f in files_to_close:
                f.close()

    except Exception as e:
        return AttackResult(success=False, message=str(e))
