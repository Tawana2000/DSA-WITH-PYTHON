# Write a program to insert a node at the beginning of an existing linked list

class Node:
    def __init__(self, data):
         self.data = data
         self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node

    def create_linked_list(self):

        node1 = Node(14)
        node2 = Node(43)
        node3 = Node(8)

        self.head = node1
        node1.next = node2
        node2.next = node3

    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
