<!DOCTYPE html>
<html>
<head>
    <title>Solaris - File Storage</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a1a2e; color: #eee; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        h1 { color: #f39c12; }
        .upload-form { background: #16213e; padding: 20px; border-radius: 8px; margin-top: 20px; }
        input[type="file"] { margin: 10px 0; }
        input[type="submit"] { background: #f39c12; border: none; padding: 10px 20px; cursor: pointer; border-radius: 4px; }
        .message { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .success { background: #27ae60; }
        .error { background: #c0392b; }
    </style>
</head>
<body>
    <div class="container">
        <h1>☀️ Solaris File Storage</h1>
        <p>Welcome to the Solaris file storage system. Upload your files securely.</p>
        
        <div class="upload-form">
            <h3>Upload File</h3>
            <form action="upload.php" method="post" enctype="multipart/form-data">
                <input type="file" name="fileToUpload" id="fileToUpload">
                <br>
                <input type="submit" value="Upload File" name="submit">
            </form>
        </div>
        
        <p style="margin-top: 20px; font-size: 12px; color: #666;">
            Solaris Server v1.0 - Reliable storage since 2019
        </p>
    </div>
</body>
</html>