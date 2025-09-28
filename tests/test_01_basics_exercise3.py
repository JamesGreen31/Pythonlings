def run(module):
    assert module.multiply(5, 6) == 30, "multiply did not work correctly for two positives"
    assert module.multiply(2, 3) == 6, "multiply did not work correctly for two positives"

    assert module.divide(6, 2) == 3.0, "divide did not work correctly for exact division"
    assert module.divide(10, 2) == 5.0, "divide did not work correctly for exact division"

    assert module.i_divide(6, 3) == 2, "i_divide did not work correctly for whole numbers"
    assert module.i_divide(3, 2) == 1, "i_divide did not work correctly for integer truncation"

    assert module.mod(5, 2) == 1, "mod did not work correctly for remainder case"
    assert module.mod(5, 5) == 0, "mod did not work correctly for zero remainder case"
    