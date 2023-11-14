import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RansomwareDetector(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path

    def on_any_event(self, event):
        if event.is_directory:
            return
        if self.detect_ransomware(event.src_path):
            print(f"Ransomware detected: {event.src_path}")

    def detect_ransomware(self, file_path):
        # Implement your ransomware detection logic here
        # Example: Check for all files regardless of extension
        return True  # Update this logic based on your detection criteria

def start_monitoring(path_to_monitor):
    event_handler = RansomwareDetector(path_to_monitor)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_monitor, recursive=True)
    
    print(f"Monitoring started for potential ransomware activity in {path_to_monitor}")

    try:
        observer.start()
        observer.join()  # Run indefinitely
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    path_to_monitor = "/home/sec-lab/Dummy"
    start_monitoring(path_to_monitor)

