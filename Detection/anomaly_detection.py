import time
import os

def monitor_folder_size(folder_path):
    while True:
        folder_size = get_folder_size(folder_path)
        if folder_size > 1000000:  # Adjust the threshold as needed
            print(f"Alert: Unusual folder size detected - {folder_size} bytes")
            # Implement alert mechanism here (e.g., send_alert_function())
        time.sleep(30)  # Adjust the frequency of checks as needed

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

if __name__ == "__main__":
    target_folder = "/home/sec-lab/Downloads"
    monitor_folder_size(target_folder)

