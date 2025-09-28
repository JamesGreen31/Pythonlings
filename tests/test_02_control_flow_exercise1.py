def run(module):
    assert module.even_or_odd(2) == "even", "even_or_odd did not return 'even' for an even number"
    assert module.even_or_odd(7) == "odd", "even_or_odd did not return 'odd' for an odd number"
    assert module.even_or_odd(0) == "even", "even_or_odd did not treat zero correctly as even"
