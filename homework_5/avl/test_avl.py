from avl import AVL


def test_left_left_case_balancing():
    avl = AVL()
    values = [30, 20, 10]

    for val in values:
        avl.insert(val)

    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30
    assert avl.is_balanced()


def test_right_right_case_balancing():
    avl = AVL()
    values = [10, 20, 30]

    for val in values:
        avl.insert(val)

    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30
    assert avl.is_balanced()


def test_left_right_case_balancing():
    avl = AVL()
    values = [30, 10, 20]

    for val in values:
        avl.insert(val)

    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30
    assert avl.is_balanced()


def test_right_left_case_balancing():
    avl = AVL()
    values = [10, 30, 20]

    for val in values:
        avl.insert(val)

    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30


def test_complex_insert_sequence_balanced():
    avl = AVL()
    values = [41, 20, 65, 11, 29, 50, 91, 32, 72, 99]

    for val in values:
        avl.insert(val)
    assert avl.is_balanced()


def test_delete_leaf_node():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    assert avl.is_balanced()

    avl.delete(5)

    assert avl.search(5) is None
    assert avl.root.value == 10
    assert avl.root.left is None
    assert avl.root.right.value == 15
    assert avl.is_balanced()


def test_delete_node_with_one_child():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(12)
    assert avl.is_balanced()

    avl.delete(15)

    assert avl.search(15) is None
    assert avl.root.right.value == 12
    assert avl.is_balanced() is True


def test_delete_node_with_two_children():
    avl = AVL()
    avl.insert(50)
    avl.insert(30)
    avl.insert(70)
    avl.insert(20)
    avl.insert(40)
    avl.insert(60)
    avl.insert(80)
    assert avl.is_balanced()

    avl.delete(50)

    assert avl.search(50) is None
    assert avl.is_balanced() is True


def test_delete_root_node():
    avl = AVL()
    avl.insert(10)
    assert avl.is_balanced()

    avl.delete(10)

    assert avl.root is None
    assert avl.is_balanced() is True
