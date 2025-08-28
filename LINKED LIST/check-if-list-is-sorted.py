# Write a program to check if the given linked list is sorted

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def create_linked_list(self):

        node1 = Node(int(input()))
        node2 = Node(int(input()))
        node3 = Node(int(input()))
        node4 = Node(int(input()))


        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        def is_sorted(self):

        if not self.head:
            return True
        current = self.head

        while current.next:
            if current.data > current.next.data:
                return False
            
            current = current.next

        return True 
