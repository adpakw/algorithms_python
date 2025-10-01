from linked_list import LinkedList, ListNode


def merge_two_sorted_lists_without_dummy(
    list1: LinkedList, list2: LinkedList
) -> LinkedList:
    l1 = list1.head
    l2 = list2.head

    result = LinkedList()

    # Обработка пустых списков
    if l1 is None and l2 is None:
        return result
    elif l1 is None and l2 is not None:
        result = list2.copy()
        return result
    elif l1 is not None and l2 is None:
        result = list1.copy()
        return result

    if l1.value <= l2.value:
        result.head = ListNode(l1.value)
        l1 = l1.next
    else:
        result.head = ListNode(l2.value)
        l2 = l2.next

    current = result.head

    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            current.next = ListNode(l1.value)
            l1 = l1.next
        else:
            current.next = ListNode(l2.value)
            l2 = l2.next
        current = current.next

    if l1 is not None:
        remaining = l1
    else:
        remaining = l2

    while remaining:
        current.next = ListNode(remaining.value)
        current = current.next
        remaining = remaining.next

    return result


def merge_two_sorted_lists_with_dummy(
    list1: LinkedList, list2: LinkedList
) -> LinkedList:
    l1 = list1.head
    l2 = list2.head

    result = LinkedList()

    dummy = ListNode(None)
    current = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = ListNode(l1.value)
            l1 = l1.next
        else:
            current.next = ListNode(l2.value)
            l2 = l2.next
        current = current.next

    if l1 is not None:
        remaining = l1
    else:
        remaining = l2
    while remaining:
        current.next = ListNode(remaining.value)
        current = current.next
        remaining = remaining.next

    result.head = dummy.next
    return result
