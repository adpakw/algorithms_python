from stack import Stack


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
