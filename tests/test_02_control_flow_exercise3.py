import io
from contextlib import redirect_stdout

def run(module):
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.countdown(3)
    output = buf.getvalue().strip().splitlines()
    assert output == ["3", "2", "1", "Blast off!"]
