from typing import Any, List, Optional

from treenode import TreeNode


class BST:
    def __init__(self, root: Optional[TreeNode] = None):
        """Инициализация BST пустым или с корнем"""
        self.root = root

    def insert(self, value: Any) -> None:
        """Вставка значения в дерево"""
        if self.root is None:
            self.root = TreeNode(value)  # создания корня
        else:
            self._insert_recur(self.root, value)  # поиск в дереве места для вставки

    def _insert_recur(self, node: TreeNode, value: Any) -> None:
        """Рекурсивная вставка

        Args:
            node (TreeNode): нода, в которой находимся при поиске места для вставки
            value (Any): значение, которое хотим вставить
        """
        if value == node.value:
            return  # игнорируем, если уже есть такой же элемент
        elif value < node.value:
            if node.left is None:  # нашли место для вставки
                node.left = TreeNode(value)
            else:
                self._insert_recur(node.left, value)
        else:
            if node.right is None:  # нашли место для вставки
                node.right = TreeNode(value)
            else:
                self._insert_recur(node.right, value)

    def search(self, value: Any) -> Optional[TreeNode]:
        """Поиск значения в дереве"""
        return self._search_recur(self.root, value)

    def _search_recur(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        """рекурсивный поиск ноды с заданными значением

        Args:
            node (Optional[TreeNode]): нода, в которой находимся при поиске
            value (Any): значение, которое хотим найти

        Returns:
            Optional[TreeNode]: нода со заданным значением
        """
        if node is None:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            return self._search_recur(node.left, value)
        else:
            return self._search_recur(node.right, value)

    # Все обходы
    def pre_order(self) -> List[Any]:
        """Pre-order обход (NLR)"""
        result: List[Any] = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        if node is not None:
            result.append(node.value)  # N
            self._pre_order_recursive(node.left, result)  # L
            self._pre_order_recursive(node.right, result)  # R

    def post_order(self) -> List[Any]:
        """Post-order обход (LRN)"""
        result: List[Any] = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(
        self, node: Optional[TreeNode], result: List[Any]
    ) -> None:
        if node is not None:
            self._post_order_recursive(node.left, result)  # L
            self._post_order_recursive(node.right, result)  # R
            result.append(node.value)  # N

    def in_order(self) -> List[Any]:
        """In-order обход (LNR)"""
        result: List[Any] = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        if node is not None:
            self._in_order_recursive(node.left, result)  # L
            result.append(node.value)  # N
            self._in_order_recursive(node.right, result)  # R

    def reverse_pre_order(self) -> List[Any]:
        """Reverse pre-order (NRL)"""
        result: List[Any] = []
        self._reverse_pre_order_recursive(self.root, result)
        return result

    def _reverse_pre_order_recursive(
        self, node: Optional[TreeNode], result: List[Any]
    ) -> None:
        if node is not None:
            result.append(node.value)  # N
            self._reverse_pre_order_recursive(node.right, result)  # R
            self._reverse_pre_order_recursive(node.left, result)  # L

    def reverse_post_order(self) -> List[Any]:
        """Reverse post-order (RLN)"""
        result: List[Any] = []
        self._reverse_post_order_recursive(self.root, result)
        return result

    def _reverse_post_order_recursive(
        self, node: Optional[TreeNode], result: List[Any]
    ) -> None:
        if node is not None:
            self._reverse_post_order_recursive(node.right, result)  # R
            self._reverse_post_order_recursive(node.left, result)  # L
            result.append(node.value)  # N

    def reverse_in_order(self) -> List[Any]:
        """Reverse in-order (RNL)"""
        result: List[Any] = []
        self._reverse_in_order_recursive(self.root, result)
        return result

    def _reverse_in_order_recursive(
        self, node: Optional[TreeNode], result: List[Any]
    ) -> None:
        if node is not None:
            self._reverse_in_order_recursive(node.right, result)  # R
            result.append(node.value)  # N
            self._reverse_in_order_recursive(node.left, result)  # L

    def display(self):
        """Отрисовка дерева"""
        if self.root is None:
            print("Empty BST")
        else:
            self.root.display()
