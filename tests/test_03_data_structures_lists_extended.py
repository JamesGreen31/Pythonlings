def run(learner_mod):
    # 1. Modify list
    result = learner_mod.modify_list(["apple"])
    assert result == ["apple", "banana", "orange"], f"modify_list failed: {result}"

    # 2. Remove + pop
    animals, popped = learner_mod.remove_items(["dog", "cat", "mouse"])
    assert animals == ["mouse"], f"remove_items animals failed: {animals}"
    assert popped == "dog", f"remove_items popped failed: {popped}"

    # 3. Length + membership
    length, has_apple = learner_mod.list_info(["apple", "pear"])
    assert length == 2, f"list_info length failed: {length}"
    assert has_apple is True, f"list_info membership failed: {has_apple}"

    # 4. Iteration
    total, sentence = learner_mod.process_list([1, 2, 3], ["Python", "is", "fun"])
    assert total == 6, f"process_list total failed: {total}"
    assert sentence == "Python is fun", f"process_list sentence failed: {sentence}"

    # 5. Sorting + reversing
    sorted_list, reversed_list = learner_mod.sort_and_reverse([3, 1, 2])
    assert sorted_list == [1, 2, 3], f"sort_and_reverse sorted failed: {sorted_list}"
    assert reversed_list == [3, 2, 1], f"sort_and_reverse reversed failed: {reversed_list}"

    # 6. Copying
    orig, copied = learner_mod.copy_list([1, 2])
    assert orig == [1, 2], f"copy_list original changed: {orig}"
    assert copied == [1, 2, "extra"], f"copy_list copy failed: {copied}"
