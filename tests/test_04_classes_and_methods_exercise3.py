def run(module):
    c = module.Counter()
    c.increment()
    c.increment()
    assert c.count == 2
    c.reset()
    assert c.count == 0
