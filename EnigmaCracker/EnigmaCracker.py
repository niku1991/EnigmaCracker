import subprocess
import sys
import time
import os

def install_packages():
    packages = [
        "requests",
        "python-dotenv",
        # "bip-utils"  # Commented out because it causes installation issues
    ]
    for package in packages:
        for attempt in range(3):  # Retry up to 3 times
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                break  # Break if installation is successful
            except subprocess.CalledProcessError as e:
                print(f"Attempt {attempt + 1} failed to install {package}: {e}")
                time.sleep(5)  # Wait for 5 seconds before retrying
        else:
            print(f"Failed to install {package} after 3 attempts")
    
    # Install packages from requirements.txt
    requirements_file = "requirements.txt"
    if os.path.isfile(requirements_file):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages from {requirements_file}: {e}")
    else:
        print(f"{requirements_file} not found. Skipping installation from {requirements_file}.")

if __name__ == "__main__":
    install_packages()