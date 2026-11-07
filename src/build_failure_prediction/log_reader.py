
import os

def read_log_file(file_path):
    """
    Read the build log file.
    """
    if not os.path.exists(file_path):
        print("Log file not found!")
        return ""

    with open(file_path, "r", encoding="utf-8") as file:
        log_content = file.read()

    return log_content
