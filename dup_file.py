import os
import hashlib

def calculate_checksum(file_path, block_size=8192):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

def delete_duplicate_files(directory):
    file_checksums = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)

            if checksum in file_checksums:
                # Duplicate found. Decide which one to delete based on your criteria.
                # For example, delete the one with the lower quality (lower checksum).
                existing_file = file_checksums[checksum]
                delete_file(file_path)
                print(f"Keeping: {existing_file}")
            else:
                # No duplicate, add to the dictionary
                file_checksums[checksum] = file_path

# Example usage: Provide the directory path where you want to delete duplicate files
directory_to_scan = 'C:\\Users\\Newton\\Desktop\\ds'
delete_duplicate_files(directory_to_scan)
