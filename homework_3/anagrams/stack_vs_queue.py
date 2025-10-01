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


class Queue:
    """Очередь на основе связанного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """Добавление элемента в конец очереди"""
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """Удаление и возврат элемента из начала очереди"""
        if self.head is None and self.tail is None:
            raise IndexError("Queue is empty")

        value = self.head.value
        self.head = self.head.next

        # Проверка на то, что очередь пустая
        if self.head is None:
            self.tail = None

        return value

    def __str__(self):
        """Отрисовка стека"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        if self.head is None and self.tail is None:
            result = "empty queue"
        elif self.head is self.tail:
            result = "head\n |\n v\n" + "[" + " -> ".join(elements) + "] <- tail"
        else:
            result = "head\n |\n v\n" + "[" + " -> ".join(elements) + "] <- tail"
        return result
