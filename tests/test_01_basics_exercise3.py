def run(module):
    assert module.multiply(5,6) == 30
    assert module.multiply(2,3) == 6
    assert module.divide(6,2) == 3.0
    assert module.divide(10,2) == 5.0
    assert module.i_divide(6,3) == 2
    assert module.i_divide(3,2) == 1
    assert module.mod(5,2) == 1
    assert module.mod(5,5) == 0