<?php
$target_dir = "uploads/";

if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

if(isset($_POST["submit"])) {
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    
    // VULNERABLE: No file type validation!
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "<html><head><style>body{font-family:Arial;background:#1a1a2e;color:#eee;padding:20px;}</style></head><body>";
        echo "<h2>File uploaded successfully!</h2>";
        echo "<p>File available at: <a href='" . $target_file . "' style='color:#f39c12;'>" . $target_file . "</a></p>";
        echo "<p><a href='index.php' style='color:#f39c12;'>← Back to upload</a></p>";
        echo "</body></html>";
    } else {
        echo "<html><head><style>body{font-family:Arial;background:#1a1a2e;color:#eee;padding:20px;}</style></head><body>";
        echo "<h2 style='color:#c0392b;'>Error uploading file.</h2>";
        echo "<p><a href='index.php' style='color:#f39c12;'>← Back to upload</a></p>";
        echo "</body></html>";
    }
} else {
    header("Location: index.php");
}
?>