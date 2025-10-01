class ListNode:
    """Нода связного списка"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Стэк на основе связанного списка"""

    def __init__(self):
        self.top = None

    def push(self, value):
        """Добавление элемента на вершину стека"""
        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Удаление и возврат элемента с вершины стека"""
        if self.top is None:
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def __str__(self):
        """Отрисовка стека"""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.value))
            current = current.next

        if self.top is None:
            result = "empty stack"
        else:
            result = "top\n |\n v\n" + "[" + " -> ".join(elements) + "]"
        return result
