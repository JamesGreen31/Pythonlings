def run(module):
    assert module.word_count(["dog", "cat", "dog"]) == {"dog": 2, "cat": 1}
    assert module.word_count([]) == {}
