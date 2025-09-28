import io
from contextlib import redirect_stdout

def run(module):
    # check upper
    assert module.upper("dog") == "DOG", "upper did not convert lowercase correctly"
    assert module.upper("Cat") == "CAT", "upper did not convert mixed case correctly"

    # check lower
    assert module.lower("DOG") == "dog", "lower did not convert uppercase correctly"
    assert module.lower("cAt") == "cat", "lower did not convert mixed case correctly"

    # check printing
    buf = io.StringIO()
    with redirect_stdout(buf):
        module.show("dog")
    output = buf.getvalue().strip()
    assert output == "dog!", "show did not print the expected string format"
