def run(module):
    assert module.word_count(["dog", "cat", "dog"]) == {"dog": 2, "cat": 1}, \
        "word_count did not count repeated words correctly"
    assert module.word_count([]) == {}, \
        "word_count did not handle the empty list correctly"
