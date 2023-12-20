import requests
from base64 import b64decode
def get_github_file_content(owner, repo_name, file_path):
    base_url = f'https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}'

    try:
        headers = {'Authorization': f'token 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'}
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        file_info = response.json()

        if 'content' in file_info:
            # Decode base64-encoded content
            content = b64decode(file_info['content']).decode('utf-8')
            return content
        else:
            print(f"File {file_path} not found or is not a regular file.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching file content: {e}")
import requests

import requests

def get_all_files_in_repo(owner, repo, path=''):
    headers = {
        'Authorization': f'Bearer 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',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Get the contents of the specified path in the repository
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    contents = response.json()

    # Initialize a list to store all file names
    file_names = []

    # Process each content item
    for content in contents:
        # Check if the content is a file
        if content['type'] == 'file':
            file_names.append(content['name'])
        # If the content is a directory, recursively get files in the subdirectory
        elif content['type'] == 'dir':
            subfolder_files = get_all_files_in_repo(owner, repo, path=content['path'])
            file_names.extend(subfolder_files)

    return file_names