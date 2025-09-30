import builtins
import io
import sys

def run(learner_mod):
    # Make sure the function exists
    assert hasattr(learner_mod, "running_total"), "Function `running_total` not defined"

    # Backup originals
    orig_input = builtins.input
    orig_stdout = sys.stdout

    try:
        # Fake input sequence: numbers then "q"
        inputs = iter(["5", "3.2", "q"])
        builtins.input = lambda _: next(inputs)

        # Capture output
        sys.stdout = io.StringIO()

        total = learner_mod.running_total()
        output = sys.stdout.getvalue()

        # Check the outputs
        assert "Current total: 5.0" in output, "Did not print running total after first input"
        assert "Current total: 8.2" in output, "Did not print running total after second input"
        assert "Final total: 8.2" in output, "Did not print final total correctly"
        assert total == 8.2, "Function should return final total"

    finally:
        # Restore
        builtins.input = orig_input
        sys.stdout = orig_stdout
