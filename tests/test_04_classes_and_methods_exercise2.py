def run(module):
    p = module.Point(3, 4)
    assert p.distance_to_origin() == 5.0, "Point did not correctly calculate distance to the origin"
