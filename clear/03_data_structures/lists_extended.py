# REMOVE THIS TO MOVE ON

"""
The goal of this exercise is to practice working with Python lists.

Lists can:
- Hold multiple values
- Be modified (mutable)
- Support useful operations like append, insert, remove, iteration, sorting, and copying.

In this exercise you will complete a series of functions that use lists.
Each function focuses on a different skill.
"""

# 1. Append and Insert
def modify_list(fruits: list[str]) -> list[str]:
    """
    Add "orange" to the end of the list and insert "banana" at index 1.
    Example:
        modify_list(["apple"]) -> ["apple", "banana", "orange"]
    """
    # TODO: Append "orange"
    # TODO: Insert "banana" at index 1
    return fruits


# 2. Remove and Pop
def remove_items(animals: list[str]) -> tuple[list[str], str | None]:
    """
    Remove "cat" from the list, then pop the first element and return both
    the modified list and the popped item.
    Example:
        remove_items(["dog", "cat", "mouse"]) -> (["mouse"], "dog")
    """
    popped: str | None = None
    # TODO: Remove "cat"
    # TODO: Pop index 0 into popped
    return animals, popped


# 3. Length and Membership
def list_info(fruits: list[str]) -> tuple[int, bool]:
    """
    Return a tuple with:
    - the length of the list
    - True/False depending on whether "apple" is in the list
    Example:
        list_info(["apple", "pear"]) -> (2, True)
    """
    length: int | None = None
    has_apple: bool | None = None
    return length, has_apple


# 4. Iteration (sum + concatenation)
def process_list(numbers: list[int], words: list[str]) -> tuple[int, str]:
    """
    Return:
    - the sum of all numbers in the list
    - a string made by joining all the words with spaces
    Example:
        process_list([1, 2, 3], ["Python", "is", "fun"]) -> (6, "Python is fun")
    """
    total: int | None = None
    sentence: str | None = None
    return total, sentence


# 5. Sorting
def sort_and_reverse(values: list[int]) -> tuple[list[int], list[int]]:
    """
    Sort the list in ascending order, then return both:
    - the sorted list
    - the sorted list reversed
    Example:
        sort_and_reverse([3, 1, 2]) -> ([1, 2, 3], [3, 2, 1])
    """
    sorted_list: list[int] | None = None
    reversed_list: list[int] | None = None
    return sorted_list, reversed_list


# 6. Copying Lists
def copy_list(values: list[int]) -> tuple[list[int], list[int] | None]:
    """
    Copy the list, append "extra" to the copy, and return both the original
    and the copy.
    Example:
        copy_list([1, 2]) -> ([1, 2], [1, 2, "extra"])
    """
    new_values: list[int] | None = None
    # TODO: Copy and append "extra"
    return values, new_values
