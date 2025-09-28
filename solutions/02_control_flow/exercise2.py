
"""
Write a function `fizzbuzz(n)` that:
- Returns "Fizz" if n is divisible by 3
- Returns "Buzz" if n is divisible by 5
- Returns "FizzBuzz" if divisible by both
- Otherwise, return the number as a string
"""

def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
