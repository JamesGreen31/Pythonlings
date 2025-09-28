def run(module):
    assert module.reverse_string("dog") == "god", "reverse_string did not reverse a normal string correctly"
    assert module.reverse_string("racecar") == "racecar", "reverse_string did not handle a palindrome correctly"
