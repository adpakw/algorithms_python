from typing import Optional

from bst import BST
from treenode import TreeNode


def calc_height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0

    return max(calc_height(node.left), calc_height(node.right)) + 1


def is_balanced_btree(bst: BST) -> bool:
    if bst.root is None:
        return True

    h_left = calc_height(bst.root.left)
    h_right = calc_height(bst.root.right)

    if abs(h_left - h_right) > 1:
        return False

    # рекурсивно проверяем левое и правое дерево
    return is_balanced_btree(BST(bst.root.left)) and is_balanced_btree(
        BST(bst.root.right)
    )
