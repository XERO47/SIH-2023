import json
import json

def npm_parser(data):
    # Load the JSON data from the string
    try:
        package_data = json.loads(data)
    except Exception as e:
        print(f"Failed to load JSON data. Error: {e}")
        return None

    # Retrieve the package information
    name = package_data.get('name')
    version = package_data.get('version')
    dependencies = package_data.get('dependencies', {})
    project_name = package_data.get('name')
    dependency_versions = [{"name":package,"version":version} for package, version in dependencies.items()]

    # Create a dictionary with the data to return
    result = {
        'name': name,
        'version': version,
        'dependencies': dependency_versions,
        'project_name': project_name,
    }

    # Convert the dictionary to a JSON string and return it
    return json.dumps(result)