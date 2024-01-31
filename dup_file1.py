from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib
from pathlib import Path

# Select the folder to clean
Tk().withdraw()
file_path = askdirectory(title="Select a folder")

# Walk through each subdirectory of the folder and list out all the files
for root, dirs, files in os.walk(file_path):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        # Open the file in binary mode and read its contents
        with open(file_path, 'rb') as f:
            file_contents = f.read()
        # Generate the md5 hash of the file contents
        md5_hash = hashlib.md5(file_contents).hexdigest()
        # Check if the hash already exists in the dictionary
        if md5_hash in hash_dict:
            # If the hash exists, delete the file
            os.remove(file_path)
        else:
            # If the hash does not exist, add it to the dictionary
            hash_dict[md5_hash] = file_path
