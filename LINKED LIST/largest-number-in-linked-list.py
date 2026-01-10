# Write a program to find the largest number in an existing linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def create_linked_list(self):

        node1 = Node(5)
        node2 = Node(3)
        node3 = Node(18)
        node4 = Node(23)
        node5 = Node(7)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        
    def find_largest(self):
        
        #If list is empty
        if not self.head:
            return None
        
        current = self.head
        largest = current.data

        while current:
            if current.data > largest:
                largest = current.data
            current = current.next

        return largest

ll = Linkedlist()
ll.create_linked_list()
print(f"The largest number in the linked list is: {ll.find_largest()}")

"""
In this program I assumed the first node is the largest, then traversed through each node and compared each node's value as I went through
"""
