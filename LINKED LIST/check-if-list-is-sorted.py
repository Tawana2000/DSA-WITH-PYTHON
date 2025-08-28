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


ll = Linkedlist()
ll.create_linked_list()
print(f"The linked list is {'sorted' if ll.is_sorted() else 'not sorted'}")


"""
This program checks if the linked list sorted in ascending order, I traversed the list and checked if next node is smaller than current node, that's how we know that the list is not sorted.
But if each node is smaller than the next node right until the end of the linked list, then it' sorted.
"""
