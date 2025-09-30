# REMOVE THIS TO MOVE ON

"""
The goal of this exercise is to practice converting a Python dictionary into JSON.

JSON (JavaScript Object Notation) is a common data format for saving and sharing data.

Python provides the `json` module with the function `json.dumps()` to convert
a Python object (like a dict) into a JSON string.

Example:
    import json
    data = {"name": "Alice", "age": 30}
    json_str = json.dumps(data)
    print(json_str)  # {"name": "Alice", "age": 30}

In this exercise:
1. A dictionary is already created for you.
2. Convert it to a JSON string.
3. Return the JSON string.
"""

import json

def dict_to_json() -> str:
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}
    # TODO: Convert `data` into a JSON string using json.dumps
    json_str = None
    return json_str
