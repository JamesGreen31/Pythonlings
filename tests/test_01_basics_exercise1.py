def run(module):
    assert module.add(2, 3) == 5, f"Add did not add two positive numbers correctly"
    assert module.add(-1, 1) == 0, f"Add did not add a negative and positive correctly"
    assert module.add(-18, -5) == -23, f"Add did not add two negative numbers properly"
