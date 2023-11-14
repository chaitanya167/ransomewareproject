import os
import subprocess

def check_file_permissions(file_path):
    permissions = oct(os.stat(file_path).st_mode & 0o777)
    print(f"File: {file_path}, Permissions: {permissions}")

def run_security_scanner(folder_path):
    print("Checking file permissions...")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            check_file_permissions(file_path)

    print("Running security scanner...")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                result = subprocess.run(["binwalk", file_path], check=True, capture_output=True, text=True)
                if "encrypted" in result.stdout.lower() or "compressed" in result.stdout.lower():
                    print(f"File: {file_path} is encrypted or compressed.")
                else:
                    print(f"File: {file_path} is not encrypted.")
            except subprocess.CalledProcessError:
                print(f"Error processing file: {file_path}")

if __name__ == "__main__":
    target_folder = "/home/sec-lab/Dummy"  # Replace with your target folder path
    run_security_scanner(target_folder)

