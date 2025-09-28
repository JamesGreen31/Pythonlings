
"""
Write a function `first_element(lst)` that:
- Takes a list
- Returns the first element if the list is not empty
- Returns None if the list is empty
"""

def first_element(lst: list) -> any:
    if len(lst) > 0:
        return lst[0]
    return None
