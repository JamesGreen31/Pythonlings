def run(module):
    assert module.fizzbuzz(3) == "Fizz", "fizzbuzz did not return 'Fizz' for a multiple of 3"
    assert module.fizzbuzz(5) == "Buzz", "fizzbuzz did not return 'Buzz' for a multiple of 5"
    assert module.fizzbuzz(15) == "FizzBuzz", "fizzbuzz did not return 'FizzBuzz' for a multiple of both 3 and 5"
    assert module.fizzbuzz(7) == "7", "fizzbuzz did not return the number itself when not a multiple of 3 or 5"
