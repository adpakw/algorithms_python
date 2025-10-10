from bst import BST
from treenode import TreeNode


class TestTreeNode:
    def test_tree_node_creation(self):
        node = TreeNode(5)
        assert node.value == 5
        assert node.left is None
        assert node.right is None

    def test_tree_node_with_children(self):
        left_child = TreeNode(3)
        right_child = TreeNode(7)
        node = TreeNode(5, left_child, right_child)

        assert node.value == 5
        assert node.left == left_child
        assert node.right == right_child
        assert node.left.value == 3
        assert node.right.value == 7


class TestBST:
    def test_insert_into_empty_tree(self):
        bst = BST()
        bst.insert(5)
        assert bst.root is not None
        assert bst.root.value == 5
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_smaller_value(self):
        bst = BST()
        bst.insert(5)
        bst.insert(3)

        assert bst.root.value == 5
        assert bst.root.left is not None
        assert bst.root.left.value == 3
        assert bst.root.right is None

    def test_insert_larger_value(self):
        bst = BST()
        bst.insert(5)
        bst.insert(7)

        assert bst.root.value == 5
        assert bst.root.right is not None
        assert bst.root.right.value == 7
        assert bst.root.left is None

    def test_insert_duplicate(self):
        bst = BST()
        bst.insert(5)
        bst.insert(5)  # дубликат

        assert bst.root.value == 5
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_multiple_values(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        assert bst.root.value == 5
        assert bst.root.left.value == 3
        assert bst.root.right.value == 7
        assert bst.root.left.left.value == 2
        assert bst.root.left.right.value == 4
        assert bst.root.right.left.value == 6
        assert bst.root.right.right.value == 8

    def test_search_existing_value(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        for value in values:
            assert bst.search(value).value == value

    def test_search_non_existing_value(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        assert bst.search(1) is None
        assert bst.search(9) is None
        assert bst.search(10) is None

    def test_search_in_empty_tree(self):
        bst = BST()
        assert bst.search(5) is None

    def test_pre_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [5, 3, 2, 4, 7, 6, 8]
        assert bst.pre_order() == expected

    def test_post_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [2, 4, 3, 6, 8, 7, 5]
        assert bst.post_order() == expected

    def test_in_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [2, 3, 4, 5, 6, 7, 8]  # отсортированный список
        assert bst.in_order() == expected

    def test_reverse_pre_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [5, 7, 8, 6, 3, 4, 2]
        assert bst.reverse_pre_order() == expected

    def test_reverse_post_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [8, 6, 7, 4, 2, 3, 5]
        assert bst.reverse_post_order() == expected

    def test_reverse_in_order_traversal(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        expected = [8, 7, 6, 5, 4, 3, 2]  # обратный отсортированный список
        assert bst.reverse_in_order() == expected

    def test_traversals_empty_tree(self):
        bst = BST()
        assert bst.pre_order() == []
        assert bst.post_order() == []
        assert bst.in_order() == []
        assert bst.reverse_pre_order() == []
        assert bst.reverse_post_order() == []
        assert bst.reverse_in_order() == []

    def test_traversals_single_node(self):
        """Тест обходов дерева с одним узлом"""
        bst = BST()
        bst.insert(5)

        assert bst.pre_order() == [5]
        assert bst.post_order() == [5]
        assert bst.in_order() == [5]
        assert bst.reverse_pre_order() == [5]
        assert bst.reverse_post_order() == [5]
        assert bst.reverse_in_order() == [5]

    def test_string_values(self):
        bst = BST()
        words = ["banana", "apple", "cherry", "date"]

        for word in words:
            bst.insert(word)

        assert bst.in_order() == ["apple", "banana", "cherry", "date"]
        assert bst.search("apple").value == "apple"
        assert bst.search("grape") is None

    def test_float_values(self):
        bst = BST()
        numbers = [3.14, 2.71, 1.41, 1.61]

        for num in numbers:
            bst.insert(num)

        assert bst.in_order() == [1.41, 1.61, 2.71, 3.14]
        assert bst.search(2.71).value == 2.71
        assert bst.search(3.0) is None
