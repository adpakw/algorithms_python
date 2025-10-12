from bst import BST
from validate_bst import is_valid_bst, is_valid_bst_in_order


# is_valid_bst
def test_is_valid_bst_big_negative():
    """В BST поочередно меняю все элементы кроме минимальной ноды на большое отрицательное число"""
    values = [5, 3, 7, 2, 4, 6, 8]
    value_for_reset = -1000  # большое отрицательное число

    for reset_val in values:
        # init
        bst = BST()
        for value in values:
            bst.insert(value)

        # reset
        if reset_val == min(values):
            continue

        node = bst.search(reset_val)
        node.value = value_for_reset

        assert (
            is_valid_bst(bst.root) == False
        )  # т.к. заменяем ноду на  большое отрицательное число


def test_is_valid_bst_big_positive():
    """В BST поочередно меняю все элементы кроме минимальной ноды на большое положительное число"""
    values = [5, 3, 7, 2, 4, 6, 8]
    value_for_reset = 1000  # большое положительное число

    for reset_val in values:
        # init
        bst = BST()
        for value in values:
            bst.insert(value)

        # reset
        if reset_val == max(values):
            continue

        node = bst.search(reset_val)
        node.value = value_for_reset

        assert (
            is_valid_bst(bst.root) == False
        )  # т.к. заменяем ноду на  большое положительное число


def test_is_valid_bst_medium_value():
    """В BST поочередно меняю все элементы кроме совпадающих на другие"""
    values = [5, 3, 7, 2, 4, 6, 8]

    for value_for_reset in values:
        for reset_val in values:
            bst = BST()
            for value in values:
                bst.insert(value)

            if value_for_reset == reset_val:
                continue

            node = bst.search(reset_val)
            node.value = value_for_reset

            assert (
                is_valid_bst(bst.root) == False
            )  # т.к. заменяем ноду на другое значене


##################################################################################################################
# is_valid_bst_in_order
def test_is_valid_bst_in_order_big_negative():
    """В BST поочередно меняю все элементы кроме минимальной ноды на большое отрицательное число"""
    values = [5, 3, 7, 2, 4, 6, 8]
    value_for_reset = -1000  # большое отрицательное число

    for reset_val in values:
        # init
        bst = BST()
        for value in values:
            bst.insert(value)

        # reset
        if reset_val == min(values):
            continue

        node = bst.search(reset_val)
        node.value = value_for_reset

        assert (
            is_valid_bst_in_order(bst.root) == False
        )  # т.к. заменяем ноду на  большое отрицательное число


def test_is_valid_bst_in_order_big_positive():
    """В BST поочередно меняю все элементы кроме минимальной ноды на большое положительное число"""
    values = [5, 3, 7, 2, 4, 6, 8]
    value_for_reset = 1000  # большое положительное число

    for reset_val in values:
        # init
        bst = BST()
        for value in values:
            bst.insert(value)

        # reset
        if reset_val == max(values):
            continue

        node = bst.search(reset_val)
        node.value = value_for_reset

        assert (
            is_valid_bst_in_order(bst.root) == False
        )  # т.к. заменяем ноду на  большое положительное число


def test_is_valid_bst_in_order_medium_value():
    """В BST поочередно меняю все элементы кроме совпадающих на другие"""
    values = [5, 3, 7, 2, 4, 6, 8]

    for value_for_reset in values:
        for reset_val in values:
            bst = BST()
            for value in values:
                bst.insert(value)

            if value_for_reset == reset_val:
                continue

            node = bst.search(reset_val)
            node.value = value_for_reset
            
            assert (
                is_valid_bst_in_order(bst.root) == False
            )  # т.к. заменяем ноду на другое значене
