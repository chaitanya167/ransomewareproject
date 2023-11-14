import os
import subprocess

class RansomwareDetector:
    def __init__(self, path):
        self.path = path

    def detect_ransomware(self, file_path):
        # List of executable file extensions
        executable_extensions = ['.exe', '.bat', '.sh', '.dll', '.com', '.cmd']
        
        _, file_extension = os.path.splitext(file_path)
        return file_extension.lower() in executable_extensions

    def mitigate_ransomware(self, file_path):
        # Terminate the process associated with the suspicious file
        try:
            process_name = os.path.basename(file_path)
            subprocess.run(['pkill', '-f', process_name])
            print(f"Mitigated ransomware: {file_path}. Process terminated.")
        except Exception as e:
            print(f"Error mitigating ransomware: {e}")

    def monitor(self):
        # Monitor the specified path for file modifications
        # In a real-world scenario, this would run indefinitely
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                if self.detect_ransomware(file_path):
                    self.mitigate_ransomware(file_path)

if __name__ == "__main__":
    # Replace "/home/user/documents" with the path you want to monitor
    path_to_monitor = "/home/sec-lab/Downloads"
    
    # Create an instance of the RansomwareDetector and start monitoring
    ransomware_detector = RansomwareDetector(path_to_monitor)
    ransomware_detector.monitor()
