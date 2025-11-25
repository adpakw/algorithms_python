import heapq
from typing import List, Optional, Union


class MinHeap:
    def __init__(self, arr: Optional[List[Union[int, float]]] = None):
        self.heap: List[Union[int, float]] = []

        if arr is not None:
            self._build_heap(arr)

    def _build_heap(self, arr: List[Union[int, float]]) -> None:
        if not arr:
            return

        self.heap = arr.copy()
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def push(self, val: Union[int, float]) -> None:
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> Union[int, float]:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty!")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, index: int) -> None:
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )

            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        if len(self.heap) <= 1:
            return

        left_idx = 2 * index + 1
        right_idx = 2 * index + 2
        smallest_idx = index

        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[smallest_idx]:
            smallest_idx = left_idx

        if (
            right_idx < len(self.heap)
            and self.heap[right_idx] < self.heap[smallest_idx]
        ):
            smallest_idx = right_idx

        if smallest_idx != index:
            self.heap[smallest_idx], self.heap[index] = (
                self.heap[index],
                self.heap[smallest_idx],
            )
            self._sift_down(smallest_idx)

    def __len__(self) -> int:
        return len(self.heap)

    def draw_heap(self) -> None:
        """
        Красиво отрисовывает массив как бинарное дерево (heap)
        """
        if not self.heap:
            print("(empty heap)")
            return

        def get_lines(start: int = 0, level: int = 0) -> tuple:
            """Рекурсивно строит линии для отрисовки дерева"""
            if start >= len(self.heap):
                return [], 0, 0, 0

            # Текущий узел
            node_str = str(self.heap[start])
            width = len(node_str)

            # Левый и правый потомки
            left_idx = 2 * start + 1
            right_idx = 2 * start + 2

            # Лист (нет потомков)
            if left_idx >= len(self.heap) and right_idx >= len(self.heap):
                line = node_str
                return [line], width, 1, width // 2

            # Только левый потомок
            if right_idx >= len(self.heap):
                lines, n, p, x = get_lines(left_idx, level + 1)
                s = node_str
                u = len(s)
                first_line = (x + 1) * " " + (n - x - 1) * "_" + s
                second_line = x * " " + "/" + (n - x - 1 + u) * " "
                shifted_lines = [line + u * " " for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    n + u // 2,
                )

            # Только правый потомок
            if left_idx >= len(self.heap):
                lines, n, p, x = get_lines(right_idx, level + 1)
                s = node_str
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Есть оба потомка
            left_lines, left_n, left_p, left_x = get_lines(left_idx, level + 1)
            right_lines, right_n, right_p, right_x = get_lines(right_idx, level + 1)

            s = node_str
            u = len(s)

            # Первая линия: соединяет текущий узел с потомками
            first_line = (
                (left_x + 1) * " "
                + (left_n - left_x - 1) * "_"
                + s
                + right_x * "_"
                + (right_n - right_x) * " "
            )

            # Вторая линия: соединительные линии к потомкам
            second_line = (
                left_x * " "
                + "/"
                + (left_n - left_x - 1 + u + right_x) * " "
                + "\\"
                + (right_n - right_x - 1) * " "
            )

            # Выравнивание высот поддеревьев
            if left_p < right_p:
                left_lines += [left_n * " "] * (right_p - left_p)
            elif right_p < left_p:
                right_lines += [right_n * " "] * (left_p - right_p)

            # Объединяем линии левого и правого поддеревьев
            zipped_lines = zip(left_lines, right_lines)
            lines = [first_line, second_line] + [
                a + u * " " + b for a, b in zipped_lines
            ]

            return (
                lines,
                left_n + right_n + u,
                max(left_p, right_p) + 2,
                left_n + u // 2,
            )

        lines, *_ = get_lines()
        for line in lines:
            print(line)


def find_kth_largest_custom_heap(
    nums: List[Union[int, float]], k: int
) -> Union[int, float]:
    heap = MinHeap()

    for num in nums:
        if len(heap) < k:
            heap.push(num)
        else:
            if num > heap.heap[0]:
                heap.pop()
                heap.push(num)

    return heap.heap[0]


def find_kth_largest_heapq(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

    return heap[0]
