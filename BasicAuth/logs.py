import os
import json
from datetime import datetime

def initialize_logs_file(file_path):
    """Ensure the logs file exists and is initialized properly."""
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

def write_logs(file_path, logs):
    """Write logs to the specified file in append mode."""
    try:
        with open(file_path, 'w') as f:
            json.dump(logs, f, indent=2)
    except IOError as e:
        print(f"Error writing to log file {file_path}: {e}")

def read_logs(file_path):
    """Read logs from the specified file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading from log file {file_path}: {e}")
        return []

class Logs:
    def __init__(self, log_file='logs.json'):
        """Initialize the Logs manager."""
        self.log_file = log_file
        initialize_logs_file(self.log_file)

    def log(self, event, username, status):
        """Log an event with a timestamp, username, and status."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event,
            "username": username,
            "status": status
        }
        logs = read_logs(self.log_file)
        logs.append(log_entry)
        write_logs(self.log_file, logs)
        return log_entry


