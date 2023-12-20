import xml.etree.ElementTree as ET
import json

class MavenParser:
    def parse(data):
        tree = ET.fromstring(data)
        root = tree

        # XML namespaces
        namespaces = {'mvn': 'http://maven.apache.org/POM/4.0.0'}

        # Extract relevant information
        group_id = root.find('mvn:groupId', namespaces).text
        artifact_id = root.find('mvn:artifactId', namespaces).text
        version = root.find('mvn:version', namespaces).text

        # Extract dependencies
        dependencies = []
        for dependency in root.findall('.//mvn:dependency', namespaces):
            dep_group_id = dependency.find('mvn:groupId', namespaces).text
            dep_artifact_id = dependency.find('mvn:artifactId', namespaces).text
            dep_version = dependency.find('mvn:version', namespaces).text
            dependencies.append({
                'groupId': dep_group_id,
                'artifactId': dep_artifact_id,
                'version': dep_version,
            })

        # Create a dictionary
        result = {
            'groupId': group_id,
            'artifactId': artifact_id,
            'version': version,
            'dependencies': dependencies,
        }

        # Convert the dictionary to JSON
        return json.dumps(result)