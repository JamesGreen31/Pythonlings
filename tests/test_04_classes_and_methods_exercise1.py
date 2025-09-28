def run(module):
    p = module.Point(2, 3)
    assert p.x == 2, "Point did not correctly assign the x coordinate"
    assert p.y == 3, "Point did not correctly assign the y coordinate"
