import io
from contextlib import redirect_stdout

def run(module):
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.countdown(3)
    output = buf.getvalue().strip().splitlines()

    assert output[0].isdigit(), "countdown did not start with a number"
    assert output[-1] == "Blast off!", "countdown did not end with 'Blast off!'"
    assert output == ["3", "2", "1", "Blast off!"], "countdown sequence did not match the expected pattern"
