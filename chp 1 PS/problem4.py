import os

# Specify the directory you want to list
directory_path = '/Web deveolpment'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
