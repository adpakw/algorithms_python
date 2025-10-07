from hash_table import HashTable


def test_insert_and_get():
    table = HashTable()
    table.insert("key1", "value1")
    table.insert("key2", 42)
    table.insert(123, [1, 2, 3])

    assert table.get("key1") == "value1"
    assert table.get("key2") == 42
    assert table.get(123) == [1, 2, 3]
    assert table.size == 3


def test_insert_update():
    table = HashTable()
    table.insert("key1", "value1")
    table.insert("key1", "updated_value")

    assert table.get("key1") == "updated_value"
    assert table.size == 1


def test_get_nonexistent():
    table = HashTable()
    assert table.get("nonexistent") is None
    assert table.get("another", "default") == "default"


def test_delete_existing():
    table = HashTable()
    table.insert("key1", "value1")
    table.insert("key2", "value2")

    assert table.delete("key1") is True
    assert table.get("key1") is None
    assert table.size == 1
    assert table.get("key2") == "value2"


def test_delete_nonexistent():
    table = HashTable()
    assert table.delete("nonexistent") is False
    assert table.size == 0


def test_resize_on_insert():
    table = HashTable(initial_capacity=4, max_load_factor=0.75)

    # Вставляем 3 элемента (load factor = 0.75)
    table.insert("a", 1)
    table.insert("b", 2)
    table.insert("c", 3)

    original_capacity = table.capacity

    # Следующая вставка должна вызвать ресайз
    table.insert("d", 4)

    assert table.capacity > original_capacity
    assert table.size == 4
    assert table.get("a") == 1
    assert table.get("b") == 2
    assert table.get("c") == 3
    assert table.get("d") == 4


def test_resize_on_delete():
    table = HashTable(initial_capacity=16, min_load_factor=0.3)

    for i in range(32):
        table.insert(f"key{i}", i)

    original_capacity = table.capacity

    # Удаляем элементы чтобы load factor упал ниже min_load_factor
    for i in range(20):
        table.delete(f"key{i}")

    assert table.capacity < original_capacity
    assert table.size == 12
    assert table.capacity == 36


def test_load_factor_calculation():
    table = HashTable(initial_capacity=10)

    table.insert("a", 1)
    assert table.size / table.capacity == 0.1

    table.insert("b", 2)
    assert table.size / table.capacity == 0.2


def test_same_hash_keys():
    """Честно украл у гпт"""

    class SameHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 777

        def __eq__(self, other):
            return isinstance(other, SameHash) and self.value == other.value

    table = HashTable()

    key1 = SameHash(1)
    key2 = SameHash(2)
    key3 = SameHash(3)

    table.insert(key1, "value1")
    table.insert(key2, "value2")
    table.insert(key3, "value3")

    assert table.get(key1) == "value1"
    assert table.get(key2) == "value2"
    assert table.get(key3) == "value3"
    assert table.size == 3
