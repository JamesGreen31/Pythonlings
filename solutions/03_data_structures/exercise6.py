"""
HARD EXERCISE: STUDENT GRADES

Write a function `student_grades(records)` that:
- Takes a list of (student, grade) tuples
- Returns a dictionary mapping each student to their average grade

Example:
[("Alice", 90), ("Bob", 80), ("Alice", 70)]
-> {"Alice": 80.0, "Bob": 80.0}
"""

def student_grades(records: list[tuple[str, int]]) -> dict[str, float]:

    # We need to track 3 things: the students name, the grades, and the amount of times they appear.

    # Step 1: Create and populate a list that collects student data into 1 dictionary which contains the student, their total grade, and how many times they appear.
    scores = {}
    for name, grade in records:
        if name not in scores:
            scores[name] = [0,0]
        scores[name][0] += grade
        scores[name][1] += 1

    # Step 2: Create the result dictionary that collects the requested information.
    avg_grades = {}
    for name, (total, count) in scores.items():
        avg_grades[name] = total / count
    return avg_grades
