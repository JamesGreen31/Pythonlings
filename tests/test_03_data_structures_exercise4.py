def run(module):
    assert module.unique_numbers([1, 2, 2, 3]) == {1, 2, 3}, \
        "unique_numbers did not remove duplicates correctly"
    assert module.unique_numbers([]) == set(), \
        "unique_numbers did not handle the empty list correctly"
