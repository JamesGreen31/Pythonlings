def run(learner_mod):
    assert hasattr(learner_mod, "string_work"), "Function `string_work` not defined"

    concatenated, formatted = learner_mod.string_work("Python", "Rocks", 3)

    # Test concatenation
    assert concatenated == "Python Rocks!", f"Expected 'Python Rocks!' but got {concatenated}"

    # Test f-string formatting
    assert formatted == "We have 3 apples.", f"Expected 'We have 3 apples.' but got {formatted}"
