
"""
Write a function `even_or_odd(n)` that:
- Returns "even" if n is divisible by 2
- Returns "odd" otherwise
"""

def even_or_odd(n: int) -> str:
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
    return None
