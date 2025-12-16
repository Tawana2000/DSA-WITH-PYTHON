# Write a program to count the number of nodes in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 

    def create_linked_list(self):

        node1 = Node(4)
        self.head = node1

        node2 = Node(12)
        node1.next = node2

        node3 = Node(2)
        node2.next = node3
        
    def count_elements(self):
        current = self.head
        
        count = 0

        while current:
            count += 1
            current = current.next

        return count

ll = Linkedlist()
ll.create_linked_list()
print("Number of nodes: ", ll.count_elements())
