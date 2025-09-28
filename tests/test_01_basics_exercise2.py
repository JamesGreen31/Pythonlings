def run(module):
    assert module.subtract(5,2) == 3, f"Subtract did not function properly for two positive numbers"
    assert module.subtract(-1, 1) == -2, f"Subtract did not function properly for a negative and positive number"
    assert module.subtract(1, -1) == 2, f"Subtract did not function properly for a positive and negative number"
    assert module.subtract(-18, -5) == -13, f"Subtract did not function properly for two negatie numbers"
