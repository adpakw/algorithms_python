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


def validate_stack_sequences(pushed, popped):
    if len(pushed) != len(popped):
        return False

    stack = Stack()
    pop_index = 0

    for value in pushed:
        stack.push(value)

        # Пока на вершине стека есть элемент, который нужно извлечь - извлекаем
        while (
            stack.top is not None
            and pop_index < len(popped)
            and stack.top.value == popped[pop_index]
        ):
            stack.pop()
            pop_index += 1

    # Если смогли извлечь все элементы - последовательность валидна
    return pop_index == len(popped)
