
"""
Write a function `merge_dicts(d1, d2)` that:
- Takes two dictionaries
- Returns a new dictionary containing all key/value pairs
- If a key exists in both, use the value from d2
"""

def merge_dicts(d1: dict, d2: dict) -> dict:
    d3 = {}
    for k, v in d1.items():
        d3[k] = v
    for k, v in d2.items():
        d3[k] = v
    return d3

# ALTERNATIVELY you can do this:

"""
def merge_dicts(d1: dict, d2: dict) -> dict:
    d3 = d1.copy()
    d3.update(d2)
    return d3
"""

