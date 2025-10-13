from typing import Optional

from bst import BST
from treenode import TreeNode


def is_valid_bst(
    node: Optional[TreeNode],
    min_val_subtree: Optional[float] = float("-inf"),
    max_val_subtree: Optional[float] = float("inf"),
) -> bool:
    if node is None:
        return True

    # ch_loc: проверка ноды с ограничениями с верхних уровней (наследуемые ограничения)
    if not (min_val_subtree < node.value < max_val_subtree):
        return False

    # ch_in: проверка ноды с ограничениями с нижним уровнем (локальные ограничения)
    left_node_value = node.left.value if node.left is not None else min_val_subtree
    right_node_value = node.right.value if node.right is not None else max_val_subtree

    if not (left_node_value < node.value < right_node_value):
        return False

    # рекурсия
    left_res = is_valid_bst(
        node.left, min_val_subtree=min_val_subtree, max_val_subtree=node.value
    )
    right_res = is_valid_bst(
        node.right, min_val_subtree=node.value, max_val_subtree=max_val_subtree
    )

    return left_res and right_res


def is_valid_bst_in_order(node: TreeNode) -> bool:
    bst = BST(root=node)
    in_order_elements = bst.in_order()

    # преобразование к set нужно чтобы избежать случаев
    # с дублированием элементов(уже противоречит условиям BST)
    return in_order_elements == sorted(list(set(in_order_elements)))
