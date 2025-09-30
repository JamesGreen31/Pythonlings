
"""
The goal of this module is to practice handling input and output in Python.

Python provides a simple way to get input from the user using the `input()` function.

In this exercise, you will write a program that keeps track of a running total of
numbers entered by the user. The program should:

1. Ask the user to enter a number.
2. Add the number to the running total.
3. Continue asking until the user types "q".
4. When the user types "q", display the final total.

Important:
- The user may enter floating-point numbers (e.g., 3.5).
- If the user enters something that is not a number or "q", show an error message
  and prompt them again.
"""

def running_total():
    # TODO Implement this
    total = 0.0
    while True:
        user_input = input("Enter a number (or 'q' to quit):").strip()

        # TODO: Implement quit functionality
        if(user_input.lower() == 'q'):
            break

        try:
            user_input = float(user_input)
            total += user_input
            # TODO: Implement functionality to convert user input to float and track it with total
            print(f"Current total: {total}")
        except ValueError:
            print("Invalid input, please enter a number or 'q'.")

    print(f"Final total: {total}")

    return total
