
"""
Write a function `countdown(n)` that:
- Prints numbers from n down to 1, one per line
- Then prints "Blast off!"
Use a while loop.
"""

def countdown(n: int) -> None:
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
