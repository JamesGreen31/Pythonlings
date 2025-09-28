
"""
Write a function `unique_numbers(nums)` that:
- Takes a list of integers
- Returns a set containing only the unique numbers
"""

def unique_numbers(nums: list[int]) -> set[int]:
    s = set()
    for num in nums:
        if num not in s:
            s.add(num)
    return s
