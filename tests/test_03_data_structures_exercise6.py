def run(module):
    result = module.student_grades([("Alice", 90), ("Bob", 80), ("Alice", 70)])
    assert result == {"Alice": 80.0, "Bob": 80.0}

    result = module.student_grades([])
    assert result == {}
