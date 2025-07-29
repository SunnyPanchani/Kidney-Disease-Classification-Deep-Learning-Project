import os
import shutil

project_root = '.'  # Change to your project folder path if needed

for root, dirs, files in os.walk(project_root):
    # Delete any .pyc files
    for file in files:
        if file.endswith('.pyc'):
            pyc_path = os.path.join(root, file)
            print(f"Deleting: {pyc_path}")
            os.remove(pyc_path)
    # Delete __pycache__ folders
    for dir_name in dirs:
        if dir_name == '__pycache__':
            cache_dir = os.path.join(root, dir_name)
            print(f"Deleting directory: {cache_dir}")
            shutil.rmtree(cache_dir)
