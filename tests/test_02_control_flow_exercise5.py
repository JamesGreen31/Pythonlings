import io
from contextlib import redirect_stdout

def run(module):
    # case: correct guess sequence
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.play_guessing_game(10, [5, 15, 10])
    output = buf.getvalue().strip().splitlines()
    assert output == ["Too low!", "Too high!", "Correct!"], \
        "play_guessing_game did not give the correct sequence of hints leading to a correct guess"

    # case: never guessed correctly
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.play_guessing_game(7, [1, 2, 3])
    output = buf.getvalue().strip().splitlines()
    assert output == ["Too low!", "Too low!", "Too low!", "Game over! The number was 7"], \
        "play_guessing_game did not handle repeated wrong guesses and the game-over case correctly"
