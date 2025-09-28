def run(module):
    assert module.first_element([1, 2, 3]) == 1
    assert module.first_element([]) is None
