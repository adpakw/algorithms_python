import pytest
from stack_vs_queue import ListNode, Queue, Stack


class TestListNode:
    """Тесты для класса ListNode"""

    def test_list_node_creation(self):
        """Тест создания узла списка"""
        node = ListNode(1)
        assert node.value == 1
        assert node.next is None

    def test_list_node_linking(self):
        """Тест связи между узлами"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2

        assert node1.next == node2
        assert node1.next.value == 2


class TestStack:
    """Тесты для класса Stack"""

    def test_stack_initialization(self):
        """Тест инициализации пустого стека"""
        stack = Stack()
        assert stack.top is None

    def test_push_single_element(self):
        """Тест добавления одного элемента в стек"""
        stack = Stack()
        stack.push(1)

        assert stack.top is not None
        assert stack.top.value == 1
        assert stack.top.next is None

    def test_push_multiple_elements(self):
        """Тест добавления нескольких элементов в стек"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.top.value == 3
        assert stack.top.next.value == 2
        assert stack.top.next.next.value == 1
        assert stack.top.next.next.next is None

    def test_pop_from_stack(self):
        """Тест извлечения элемента из стека"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        value = stack.pop()
        assert value == 3
        assert stack.top.value == 2

        value = stack.pop()
        assert value == 2
        assert stack.top.value == 1

        value = stack.pop()
        assert value == 1
        assert stack.top is None

    def test_pop_from_empty_stack(self):
        """Тест извлечения из пустого стека"""
        stack = Stack()

        with pytest.raises(IndexError) as exc_info:
            stack.pop()

            assert "Stack is empty" in str(exc_info.value)

    def test_stack_after_pop_all_elements(self):
        """Тест состояния стека после извлечения всех элементов"""
        stack = Stack()
        stack.push(1)
        stack.push(2)

        stack.pop()
        stack.pop()

        assert stack.top is None

        # Проверяем, что можно снова добавлять элементы
        stack.push(3)
        assert stack.top.value == 3


class TestQueue:
    """Тесты для класса Queue"""

    def test_queue_initialization(self):
        """Тест инициализации пустой очереди"""
        queue = Queue()
        assert queue.head is None
        assert queue.tail is None

    def test_enqueue_single_element(self):
        """Тест добавления одного элемента в очередь"""
        queue = Queue()
        queue.enqueue(1)

        assert queue.head is not None
        assert queue.tail is not None
        assert queue.head.value == 1
        assert queue.tail.value == 1
        assert queue.head == queue.tail

    def test_enqueue_multiple_elements(self):
        """Тест добавления нескольких элементов в очередь"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.head.value == 1
        assert queue.head.next.value == 2
        assert queue.tail.value == 3
        assert queue.tail.next is None

    def test_dequeue_from_queue(self):
        """Тест извлечения элемента из очереди"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        value = queue.dequeue()
        assert value == 1
        assert queue.head.value == 2
        assert queue.tail.value == 3

        value = queue.dequeue()
        assert value == 2
        assert queue.head.value == 3
        assert queue.tail.value == 3

        value = queue.dequeue()
        assert value == 3
        assert queue.head is None
        assert queue.tail is None

    def test_dequeue_from_empty_queue(self):
        """Тест извлечения из пустой очереди"""
        queue = Queue()

        with pytest.raises(IndexError) as exc_info:
            queue.dequeue()

        assert "Queue is empty" in str(exc_info.value)

    def test_queue_after_dequeue_all_elements(self):
        """Тест состояния очереди после извлечения всех элементов"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        queue.dequeue()
        queue.dequeue()

        assert queue.head is None
        assert queue.tail is None

        # Проверяем, что можно снова добавлять элементы
        queue.enqueue(3)
        assert queue.head.value == 3
        assert queue.tail.value == 3
