import io
from contextlib import redirect_stdout

def run(module):
    # check upper
    assert module.upper("dog") == "DOG"
    assert module.upper("Cat") == "CAT"

    # check lower
    assert module.lower("DOG") == "dog"
    assert module.lower("cAt") == "cat"

    # check printing
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.show("dog")
    output = buf.getvalue().strip()
    assert output == "dog!"
