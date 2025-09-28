import io
from contextlib import redirect_stdout

def run(module):
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.play_guessing_game(10, [5, 15, 10])
    output = buf.getvalue().strip().splitlines()
    assert output == ["Too low!", "Too high!", "Correct!"]

    buf = io.StringIO()
    with redirect_stdout(buf):
        module.play_guessing_game(7, [1, 2, 3])
    output = buf.getvalue().strip().splitlines()
    assert output == ["Too low!", "Too low!", "Too low!", "Game over! The number was 7"]
