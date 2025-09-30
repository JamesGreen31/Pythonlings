
"""
The goal of this exercise is to practice working with strings in Python.

Strings are pieces of text, like "hello" or "Python!". You can:
- **Concatenate (join) them together** using the + operator.
- **Format them** using f-strings, which allow you to insert values inside text.

Examples:
    name = "Alice"
    age = 30

    # Concatenation
    message = "Hello, " + name + "!"

    # f-string formatting
    formatted = f"{name} is {age} years old."

In this exercise, you will:
1. Concatenate two strings to form a full sentence.
2. Use an f-string to create a sentence with a number in it.
3. Return both sentences from the function below.

Expected results:
- If `first = "Python"` and `second = "Rocks"`, then concatenation gives:
    "Python Rocks!"
- If `count = 3`, then formatting gives:
    "We have 3 apples."
"""

def string_work(first="Python", second="Rocks", count=3):
    # TODO: Concatenate first and second with a space and an exclamation mark
    concatenated = first + " " + second + "!"

    # TODO: Use an f-string to create: "We have X apples."
    formatted = f"We have {count} apples."

    return concatenated, formatted
