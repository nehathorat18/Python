import subprocess

# Simple function to check disk usage
def check_disk():
    subprocess.run(["df", "-h"])

check_disk()
