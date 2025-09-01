# Write a program to reverse the elements of linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    
    def __init__(self):
        self.head = None

    def create_linked_list(self):

        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(4)
        node4 = Node(5)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        
    def display(self):

        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
