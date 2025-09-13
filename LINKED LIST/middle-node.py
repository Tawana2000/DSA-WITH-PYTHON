# Write a program to find the middle node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(45)
        self.head = node1

        node2 = Node(23)
        node1.next = node2

        node3 = Node(50)
        node2.next = node3
