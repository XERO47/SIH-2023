import os

def read_file(file_path):
    """Read a file and return its contents."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.isfile(file_path)

def dir_exists(dir_path):
    """Check if a directory exists."""
    return os.path.isdir(dir_path)

# These functions are quite basic and don't handle any errors.
# In a real-world application, you would want to add error checking and handling, 
# for example to deal with cases where the file doesn't exist, the path is not a file, you don't have permission to read or write the file, etc.