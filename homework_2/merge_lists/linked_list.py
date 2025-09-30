class ListNode:
    """Нода связного списка"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Односвязный список"""
    
    def __init__(self):
        self.head = None
    
    def append(self, value):
        """Добавление элемента в конец списка"""
        new_node = ListNode(value)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def from_list(self, values):
        """Создание связного списка из обычного списка"""
        self.head = None
        for value in values:
            self.append(value)
    
    def to_list(self):
        """Преобразование связного списка в обычный список"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def copy(self):
        """Создание глубокой копии связного списка"""
        new_list = LinkedList()
        
        if self.head is None:
            return new_list
        
        new_list.head = ListNode(self.head.value)
        current_original = self.head.next
        current_copy = new_list.head
        
        while current_original:
            current_copy.next = ListNode(current_original.value)
            current_original = current_original.next
            current_copy = current_copy.next
        
        return new_list
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        
        if not elements:
            return "empty LinkedList"
        
        return "[" + " -> ".join(elements) + "]"