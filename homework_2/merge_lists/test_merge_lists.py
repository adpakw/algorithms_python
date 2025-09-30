from linked_list import LinkedList
from merge_lists import (
    merge_two_sorted_lists_with_dummy,
    merge_two_sorted_lists_without_dummy,
)


def test_both_lists_empty():
    """Оба списка пустые"""
    list1 = LinkedList()
    list2 = LinkedList()

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)
    result2 = merge_two_sorted_lists_without_dummy(list1, list2)

    assert result1.to_list() == []
    assert result2.to_list() == []
    assert result1.head is None
    assert result2.head is None


def test_first_list_empty():
    """Первый список пустой"""
    list1 = LinkedList()
    list2 = LinkedList()
    list2.from_list([1, 3, 5])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)
    result2 = merge_two_sorted_lists_without_dummy(list1, list2)

    assert result1.to_list() == [1, 3, 5]
    assert result2.to_list() == [1, 3, 5]


def test_second_list_empty():
    """Второй список пустой"""
    list1 = LinkedList()
    list1.from_list([2, 4, 6])
    list2 = LinkedList()

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)
    result2 = merge_two_sorted_lists_without_dummy(list1, list2)

    assert result1.to_list() == [2, 4, 6]
    assert result2.to_list() == [2, 4, 6]


def test_equal_length_lists():
    """Списки одинаковой длины"""
    list1 = LinkedList()
    list1.from_list([1, 2, 4])
    list2 = LinkedList()
    list2.from_list([1, 3, 4])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)
    result2 = merge_two_sorted_lists_without_dummy(list1, list2)

    expected = [1, 1, 2, 3, 4, 4]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_different_length_lists():
    """Списки разной длины"""
    list1 = LinkedList()
    list1.from_list([1, 5, 9])
    list2 = LinkedList()
    list2.from_list([2, 3, 6, 7, 8])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    # Создаем новые списки для второго метода, т.к. исходные изменяются
    list3 = LinkedList()
    list3.from_list([1, 5, 9])
    list4 = LinkedList()
    list4.from_list([2, 3, 6, 7, 8])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [1, 2, 3, 5, 6, 7, 8, 9]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_all_elements_from_first_list():
    """Все элементы первого списка меньше"""
    list1 = LinkedList()
    list1.from_list([1, 2, 3])
    list2 = LinkedList()
    list2.from_list([4, 5, 6])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    list3 = LinkedList()
    list3.from_list([1, 2, 3])
    list4 = LinkedList()
    list4.from_list([4, 5, 6])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [1, 2, 3, 4, 5, 6]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_all_elements_from_second_list():
    """Все элементы второго списка меньше"""
    list1 = LinkedList()
    list1.from_list([7, 8, 9])
    list2 = LinkedList()
    list2.from_list([4, 5, 6])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    list3 = LinkedList()
    list3.from_list([7, 8, 9])
    list4 = LinkedList()
    list4.from_list([4, 5, 6])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [4, 5, 6, 7, 8, 9]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_single_element_lists():
    """Списки из одного элемента"""
    list1 = LinkedList()
    list1.from_list([2])
    list2 = LinkedList()
    list2.from_list([1])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    list3 = LinkedList()
    list3.from_list([2])
    list4 = LinkedList()
    list4.from_list([1])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [1, 2]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_duplicate_values():
    """Списки с повторяющимися значениями"""
    list1 = LinkedList()
    list1.from_list([1, 1, 3, 5])
    list2 = LinkedList()
    list2.from_list([1, 2, 2, 6])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    list3 = LinkedList()
    list3.from_list([1, 1, 3, 5])
    list4 = LinkedList()
    list4.from_list([1, 2, 2, 6])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [1, 1, 1, 2, 2, 3, 5, 6]
    assert result1.to_list() == expected
    assert result2.to_list() == expected


def test_negative_numbers():
    """Списки с отрицательными числами"""
    list1 = LinkedList()
    list1.from_list([-5, -3, 0])
    list2 = LinkedList()
    list2.from_list([-4, -2, 1])

    result1 = merge_two_sorted_lists_with_dummy(list1, list2)

    list3 = LinkedList()
    list3.from_list([-5, -3, 0])
    list4 = LinkedList()
    list4.from_list([-4, -2, 1])
    result2 = merge_two_sorted_lists_without_dummy(list3, list4)

    expected = [-5, -4, -3, -2, 0, 1]
    assert result1.to_list() == expected
    assert result2.to_list() == expected
