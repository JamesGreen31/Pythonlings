# REMOVE THIS TO MOVE ON

"""
The goal of this exercise is to practice working with user input and
performing basic arithmetic operations.

You will write a program that maintains a running total. The program should:

1. Start with a total of 0.
2. Prompt the user to enter an operation symbol (+, -, *, /) followed by a number.
   Example inputs: "+ 5", "- 2", "* 3", "/ 4"
3. Update the running total using the operation.
4. Display the running total after each entry.
5. Continue prompting until the user enters "q" to quit.
6. When the user quits, print the final total.

Important:
- The input must be two parts: operator and number, separated by space.
- Division should handle floats (e.g., `/ 2`).
- If the user enters something invalid (wrong operator, bad number, wrong format),
  show an error message and keep prompting.
"""

def calculator():
    # TODO: Implement
    return None
    total = 0.0
    while True:
        user_input = input("Enter operation and number (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            break

        try:
            parts = # TODO: Implement using the split function

            op, num_as_str = parts[0], parts[1]
            number = float(num_as_str)

            match op:
                case '+':
                    total += number
                case '-':
                    # TODO: Implement
                case '*':
                    # TODO: Implement
                # TODO: Implement '/' functionality
                case '_':
                    total = total # Normally we would throw exception, but this time we just won't do anything

            print(f"Current total: {total}")

        except Exception:
            print("Invalid input. Use format: <op> <number> (e.g., + 5)")

    print(f"Final total: {total}")
    return total
