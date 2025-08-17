#Create a linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    
    def create_linked_list(self):

        node1 = Node(56)
        self.head = node1

        node2 = Node(8)
        node1.next = node2

        node3 = Node(17)
        node2.next = node3

LinkedList = LinkedList()
LinkedList.create_linked_list()
