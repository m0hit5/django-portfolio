import os

def print_directory_contents(dir_path):
    for root, dirs, files in os.walk(dir_path):
        print(f"📁 Directory: {root}")
        for file in files:
            print(f"    📄 File: {os.path.join(root, file)}")
        for directory in dirs:
            print(f"    📁 Subdirectory: {os.path.join(root, directory)}")

# Specify the directory you want to scan
directory_to_scan = 'C:/Users/MOHIT/Desktop/p_project'
print_directory_contents(directory_to_scan)
