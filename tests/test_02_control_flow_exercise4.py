def run(module):
    assert module.sum_list([1, 2, 3]) == 6, "sum_list did not return the correct total for a list of positives"
    assert module.sum_list([]) == 0, "sum_list did not handle the empty list correctly"
    assert module.sum_list([5, -2, 7]) == 10, "sum_list did not return the correct total for a list with both positive and negative numbers"
