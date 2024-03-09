# Help you to read the JSON files and provide the JSON data

import json

def get_payload_auth():
    # read from auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data

