import json

def read_json_file(file_path):
    """
    Read a JSON file and return the data as a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        The data from the JSON file as a Python object.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    """
    Write a Python object to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data: The Python object to write.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def parse_json_string(json_string):
    """
    Parse a JSON string and return the data as a Python object.

    Args:
        json_string (str): The JSON string.

    Returns:
        The data from the JSON string as a Python object.
    """
    return json.loads(json_string)

def to_json_string(data):
    """
    Convert a Python object to a JSON string.

    Args:
        data: The Python object to convert.

    Returns:
        The Python object as a JSON string.
    """
    return json.dumps(data, indent=4)