import os
import joblib
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RansomwareDetector(FileSystemEventHandler):
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
    
    def on_modified(self, event):
        if not event.is_directory:
            file_activity = self.extract_file_features(event.src_path)
            if self.detect_ransomware(file_activity):
                print("Ransomware detected!")
                self.generate_report(file_activity)
    
    def extract_file_features(self, file_path):
        # Placeholder for feature extraction logic
        return []

    def detect_ransomware(self, file_activity):
        return self.model.predict([file_activity]) == 1

    def generate_report(self, file_activity):
        with open('data/reports/report.txt', 'a') as report_file:
            report_file.write(f"Ransomware detected: {file_activity}\n")

def monitor_file_system(path, model_path):
    event_handler = RansomwareDetector(model_path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    monitor_file_system('/path/to/monitor', 'models/trained_model.pkl')
