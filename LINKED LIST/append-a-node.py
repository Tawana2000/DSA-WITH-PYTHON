# Write a program to add a node at the end of an exisiting linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    
    def __init__(self):
        self.head = None
        
    def create_linked_list(self):

        node1 = Node(16)
        node2 = Node(8)
        node3 = Node(23)
        node4 = Node(30)
        node5 = Node(4)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
