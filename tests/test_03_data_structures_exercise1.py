def run(module):
    assert module.first_element([1, 2, 3]) == 1, "first_element did not return the first item from a non-empty list"
    assert module.first_element([]) is None, "first_element did not handle the empty list correctly"
