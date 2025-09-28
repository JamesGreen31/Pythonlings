def run(module):
    assert module.merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}, \
        "merge_dicts did not handle overlapping keys correctly"
    assert module.merge_dicts({}, {"x": 10}) == {"x": 10}, \
        "merge_dicts did not handle merging with an empty dictionary correctly"
