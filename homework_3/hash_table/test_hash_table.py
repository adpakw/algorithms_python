from homework_3.hash_table.hash_table import validate_stack_sequences


def test_validate_stack_sequences():
    assert validate_stack_sequences([1, 2, 3, 4, 5], [1, 3, 5, 4, 2])
    assert not validate_stack_sequences([1, 2, 3], [3, 1, 2])
    assert validate_stack_sequences([1, 2, 3], [1, 2, 3])
    assert validate_stack_sequences([1, 2, 3], [3, 2, 1])
    assert validate_stack_sequences([], [])
    assert validate_stack_sequences([1], [1])
    assert validate_stack_sequences([0, 1, 2, 3, 4], [2, 1, 4, 3, 0])
    assert not validate_stack_sequences([0, 1, 2, 3, 4], [2, 4, 1, 3, 0])
    assert not validate_stack_sequences([1, 2, 3], [3, 2])
    assert not validate_stack_sequences([1], [3, 2, 1])
