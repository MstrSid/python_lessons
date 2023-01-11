# Create dict with values different types
# Convert dict in json
# Output result json in terminal
# Output type result json in terminal
import json
import requests

some_dict = {
    'id': 15,
    'number': 2.5,
    'some_data': {
        's1': 'String',
        'a2': [1, 2, 3]
    }
}

json_from_dict = json.dumps(some_dict, indent=2)
print(json_from_dict)
print(type(json_from_dict))
