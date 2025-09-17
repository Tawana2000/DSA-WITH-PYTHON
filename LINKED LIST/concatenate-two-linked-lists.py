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
            
    def concatenate(self, second_list):
        if self.head is None:
            self.head = second_list.head
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = second_list.head
