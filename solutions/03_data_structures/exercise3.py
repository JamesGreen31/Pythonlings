
"""
Write a function `word_count(words)` that:
- Takes a list of words
- Returns a dictionary mapping each word to how many times it appears
Example: ["dog", "cat", "dog"] -> {"dog": 2, "cat": 1}
"""

def word_count(words: list[str]) -> dict[str, int]:
    lib = {}
    for word in words:
        if word in lib:
            lib[word] += 1
        else:
            lib[word] = 1
    return lib
