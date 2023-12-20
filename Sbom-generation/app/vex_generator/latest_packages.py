import requests

def get_latest_maven_version(group_id, artifact_id):
    url = f'https://search.maven.org/solrsearch/select?q=g:"{group_id}" AND a:"{artifact_id}"&core=gav&rows=1&wt=json'
    response = requests.get(url)
    data = response.json()
    
    if "response" in data and "docs" in data["response"]:
        latest_version = data["response"]["docs"][0]["v"]
        return latest_version
    else:
        return None

def get_latest_npm_version(package_name):
    url = f'https://registry.npmjs.org/{package_name}'
    response = requests.get(url)
    data = response.json()

    if "dist-tags" in data and "latest" in data["dist-tags"]:
        latest_version = data["dist-tags"]["latest"]
        return latest_version
    else:
        return None

def get_latest_pypi_version(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    response = requests.get(url)
    data = response.json()

    if "info" in data and "version" in data["info"]:
        latest_version = data["info"]["version"]
        return latest_version
    else:
        return None

def get_latest_rubygems_version(package_name):
    url = f'https://rubygems.org/api/v1/versions/{package_name}/latest.json'
    response = requests.get(url)
    data = response.json()

    if "version" in data:
        latest_version = data["version"]
        return latest_version
    else:
        return None
