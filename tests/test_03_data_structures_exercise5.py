def run(module):
    assert module.merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    assert module.merge_dicts({}, {"x": 10}) == {"x": 10}
