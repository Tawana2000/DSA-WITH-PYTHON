# Create a Circular Linked List
# To convert a regular linked list to a cirular linked list, we will make the last node point to the head node

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    #create circular linked list
    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(75)
        node1.next = node2

        node3 = Node(30)
        node2.next = node3

        #make the last node point back to the head node, making it circular
        node3.next = self.head

linked_list = CircularLinkedList()
linked_list.create_linked_list()
