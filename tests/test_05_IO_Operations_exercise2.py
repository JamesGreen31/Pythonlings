import builtins
import io
import sys

def run(learner_mod):
    assert hasattr(learner_mod, "calculator"), "Function `calculator` not defined"

    orig_input = builtins.input
    orig_stdout = sys.stdout

    try:
        # Simulated input sequence: +5 → *2 → -3 → /2 → q
        inputs = iter(["+ 5", "* 2", "- 3", "/ 2", "q"])
        builtins.input = lambda _: next(inputs)

        # Capture all printed output
        sys.stdout = io.StringIO()
        total = learner_mod.calculator()
        output = sys.stdout.getvalue()

        # Check step-by-step output
        assert "Current total: 5.0" in output, "Addition failed (expected 5.0)"
        assert "Current total: 10.0" in output, "Multiplication failed (expected 10.0)"
        assert "Current total: 7.0" in output, "Subtraction failed (expected 7.0)"
        assert "Current total: 3.5" in output, "Division failed (expected 3.5)"

        # Check final output
        assert "Final total: 3.5" in output, "Final total not printed correctly"
        assert total == 3.5, f"Expected return value 3.5, got {total}"

    finally:
        builtins.input = orig_input
        sys.stdout = orig_stdout
