from typing import Optional

from bst import BST
from treenode import TreeNode
from balanced_binary_tree import is_balanced_btree

def build_tree(values):
    bst = BST()
    for value in values:
        bst.insert(value)
    return bst

def test_empty_tree():
    bst = build_tree([])
    assert is_balanced_btree(bst) == True

def test_single_node():
    bst = build_tree([5])
    assert is_balanced_btree(bst) == True

def test_balanced_two_nodes():
    bst = build_tree([5, 3])
    assert is_balanced_btree(bst) == True

def test_balanced_three_nodes():
    bst = build_tree([5, 3, 7])
    assert is_balanced_btree(bst) == True

def test_balanced_perfect_tree():
    bst = build_tree([5, 3, 7, 2, 4, 6, 8])
    assert is_balanced_btree(bst) == True

def test_balanced_with_difference_one():
    bst = build_tree([5, 3, 7, 2])
    assert is_balanced_btree(bst) == True

def test_balanced_complex_tree():
    bst = build_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
    assert is_balanced_btree(bst) == True

def test_unbalanced_right_heavy():
    bst = build_tree([1, 2, 3, 4])
    assert is_balanced_btree(bst) == False

def test_unbalanced_left_heavy():
    bst = build_tree([4, 3, 2, 1])
    assert is_balanced_btree(bst) == False

def test_unbalanced_borderline():
    bst = build_tree([5, 3, 7, 2, 4, 1]) # delta h = 2
    assert is_balanced_btree(bst) == False

def test_unbalanced_sequential():
    bst = build_tree([1, 2, 3, 4, 5, 6])
    assert is_balanced_btree(bst) == False

def test_unbalanced_complex():
    bst = build_tree([10, 5, 15, 3, 20, 1, 25, 30])
    assert is_balanced_btree(bst) == False

def test_duplicate_values():
    bst = build_tree([5, 3, 7, 5, 3, 7])
    assert is_balanced_btree(bst) == True

