class HashTable:
    """Реализация хеш-таблицы с линейным пробированием, игнорирующая удаленные ячейки при вставке."""

    def __init__(
        self,
        initial_capacity: int = 16,
        min_load_factor: float = 0.3,
        max_load_factor: float = 0.8,
        coef_resize: float = 1.5,
    ):
        self.min_capacity = initial_capacity

        self.capacity = initial_capacity
        self.size = 0

        self.min_load_factor = min_load_factor
        self.max_load_factor = max_load_factor
        self.coef_resize = coef_resize

        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self._deleted = [False] * self.capacity

    def _probe(self, key, mode: str = "search"):
        """
        Линейное пробирование, вставка осуществляется только на свободные места,
        игнорируются удаленные места.
        """
        if mode not in ["search", "insert"]:
            raise ValueError("Mode must be 'search' or 'insert'")

        index = hash(key) % self.capacity
        needs_resize = False

        for i in range(self.capacity):
            current_index = (index + i) % self.capacity  # цикличесикй сдвиг

            # Если нашли пустую ячейку
            # для вставки еще есть проверка на то, что не вывалимся ли мы за load factor
            # если мы ищем (mode=search), то отдаем None
            if self.keys[current_index] is None:
                if mode == "insert":
                    # Проверяем load factor
                    if (self.size + 1) / self.capacity > self.max_load_factor:
                        needs_resize = True
                    return (current_index, needs_resize)
                elif mode == "search":
                    return (None, False)

            # при поиске проверяем существующие ключи, игнорируем удаленные
            if mode == "search":
                if not self._deleted[current_index] and self.keys[current_index] == key:
                    return (current_index, False)

            # при вставке для обновления игнорируем удаленные ячейки и проверяем только существующие ключи
            elif mode == "insert":
                if not self._deleted[current_index] and self.keys[current_index] == key:
                    return (
                        current_index,
                        False,
                    )  # Нашли существующий ключ для обновления

        # Если прошли всю таблицу и не нашли подходящего места
        if mode == "insert":
            return (None, True)  # Нет места - нужен ресайз
        else:
            return (None, False)

    def _resize(self, new_capacity: int):
        """Изменение размера таблицы."""
        old_keys = self.keys
        old_values = self.values
        old_deleted = self._deleted

        self.capacity = new_capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self._deleted = [False] * self.capacity
        self.size = 0

        # Перехэширование только неудаленных элементов
        for i in range(len(old_keys)):
            if old_keys[i] is not None and not old_deleted[i]:
                self.insert(old_keys[i], old_values[i])

    def insert(self, key, value) -> None:
        """Вставка или обновление элемента."""
        search_result, needs_resize = self._probe(key, mode="search")

        # (обновление) если ключ существует, то обновляем значение
        if search_result is not None:
            index = search_result
            self.values[index] = value
            return

        # (вставка) ищем место для вставки (только пустые ячейки, не удаленные)
        index, needs_resize = self._probe(key, mode="insert")

        if needs_resize:
            self._resize(int(self.capacity * self.coef_resize))
            self.insert(key, value)
            return

        # Таблица полностью заполнена
        if index is None:
            self._resize(int(self.capacity * self.coef_resize))
            self.insert(key, value)
            return

        # Вставляем новый элемент в пустую ячейку
        self.keys[index] = key
        self.values[index] = value
        self._deleted[index] = False
        self.size += 1

    def get(self, key, default=None):
        index, _ = self._probe(key, mode="search")
        if index is not None:
            return self.values[index]
        return default

    def delete(self, key) -> bool:
        index, _ = self._probe(key, mode="search")
        if index is not None:
            self._deleted[index] = True
            self.size -= 1

            # Уменьшаем размер если таблица слишком пустая
            if (
                self.size / self.capacity < self.min_load_factor
                and self.capacity > self.min_capacity
            ):
                self._resize(
                    int(max(self.min_capacity, self.capacity // self.coef_resize))
                )

            return True
        return False

    def __str__(self) -> str:
        items = []
        for i in range(self.capacity):
            if self.keys[i] is not None and not self._deleted[i]:
                key_str = (
                    f"'{self.keys[i]}'"
                    if isinstance(self.keys[i], str)
                    else str(self.keys[i])
                )
                value_str = (
                    f"'{self.values[i]}'"
                    if isinstance(self.values[i], str)
                    else str(self.values[i])
                )
                items.append(f"{key_str}: {value_str}")
        return "{" + ", ".join(items) + "}"
