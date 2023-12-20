import requests

# Replace these values with your actual information
org_id = "a8e0ba19-4ce8-4305-a3fb-d965f21a0044"
package_name = "grpc"
package_version = "1.24.3"
api_key = "5d603aca-5e69-4e0c-a520-2c5c321a6a51"  # Replace with your actual API key or Bearer token

# Snyk API endpoint URL
url = f"https://api.snyk.io/v1/org/{org_id}/test/npm:{package_name}@{package_version}"

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {api_key}"  # or "Api-Key: your_api_key" if using an API key
}

try:
    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        # Parse and work with the response data (in JSON format)
        data = response.json()
        print("Response data:", data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
