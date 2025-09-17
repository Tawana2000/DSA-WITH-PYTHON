Write a program to concatenate two linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
    print("None")
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
            
    def concatenate(self, second_list):
        if self.head is None:
            self.head = second_list.head
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = second_list.head


list1 = LinkedList()
list1.append(10)
list1.append(12)
list1.append(14)

list2 = LinkedList()
list2.append(20)
list2.append(22)
list2.append(24)
