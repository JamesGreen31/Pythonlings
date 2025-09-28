
"""
Write a function `sum_list(numbers)` that:
- Takes a list of integers
- Uses a for loop to return the sum
"""

def sum_list(numbers: list[int]) -> int:
    total = 0
    for i in numbers:
        total += i
    return total
