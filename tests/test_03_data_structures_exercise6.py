def run(module):
    result = module.student_grades([("Alice", 90), ("Bob", 80), ("Alice", 70)])
    assert result == {"Alice": 80.0, "Bob": 80.0}, \
        "student_grades did not correctly average grades for students with multiple entries"

    result = module.student_grades([])
    assert result == {}, \
        "student_grades did not handle the empty input correctly"
