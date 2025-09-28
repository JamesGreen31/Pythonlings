def run(module):
    assert module.sum_list([1, 2, 3]) == 6
    assert module.sum_list([]) == 0
    assert module.sum_list([5, -2, 7]) == 10
