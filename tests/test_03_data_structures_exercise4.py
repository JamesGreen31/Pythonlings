def run(module):
    assert module.unique_numbers([1, 2, 2, 3]) == {1, 2, 3}
    assert module.unique_numbers([]) == set()
