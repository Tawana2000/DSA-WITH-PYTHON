# Write a program to find the sum of all nodes in a linked list

class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def creat_linked_list(self):

        node1 = Node(14)
        node2 = Node(25)
        node3 = Node(30)
        node4 = Node(6)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
