import json

class PipParser:
    def parse(data):
        lines = data.splitlines()
        dependencies = [line.strip() for line in lines if line.strip()]
        result = {
            'dependencies': dependencies,
        }
        # Convert the dictionary to a JSON string and return it
        return json.dumps(result)