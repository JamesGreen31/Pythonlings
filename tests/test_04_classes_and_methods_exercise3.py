def run(module):
    c = module.Counter()
    c.increment()
    c.increment()
    assert c.count == 2, "Counter did not increment correctly"
    c.reset()
    assert c.count == 0, "Counter did not reset correctly"
