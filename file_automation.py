import os
import datetime

directory_path = input("Enter the directory path: ")

threshold_days = 180

current_time = datetime.datetime.now()

threshold_date = current_time - datetime.timedelta(days=threshold_days)

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        
        if file_mtime < threshold_date:
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {str(e)}")


