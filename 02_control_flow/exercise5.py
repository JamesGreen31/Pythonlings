# REMOVE THIS TO MOVE ON

"""
HARDER GUESSING GAME

The goal of this exercise is to combine multiple control flow concepts.

Write a function `play_guessing_game(secret, guesses)` that:

- INPUTS:
    secret: int       -- the number to guess
    guesses: list[int] -- a list of guesses the "player" makes

- BEHAVIOR:
    * The player starts with 3 attempts max.
    * Loop through the guesses one by one.
    * For each guess:
        - If the guess is lower than secret, print "Too low!"
        - If the guess is higher than secret, print "Too high!"
        - If the guess is correct, print "Correct!" and stop the game early.
    * If the player runs out of attempts without guessing correctly,
      print "Game over! The number was X" where X is the secret.

HINT: 
- Use a while loop (or for loop with a counter).
- Use if/elif/else to check the guess.
"""

def play_guessing_game(secret: int, guesses: list[int]) -> None:
    # TODO Implement this
    pass