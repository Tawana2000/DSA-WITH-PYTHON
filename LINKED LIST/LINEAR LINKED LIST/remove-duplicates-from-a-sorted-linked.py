# Write a program to remove duplicates from a sorted linked list.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def create_linked_list(self):

        node1 = Node(8)
        node2 = Node(12)
        node3 = Node(12)
        node4 = Node(12)
        node5 = Node(15)
        node6 = Node(18)
        node7 = Node(18)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next

        print(None)
        
    def remove_duplicates(self):
        #If list is empty
        if not self.head:
            return 
        
        current = self.head

        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

ll = Linkedlist()
ll.create_linked_list()
print("Original List:")
ll.display()
print("After removing duplicates: ")
ll.remove_duplicates()
ll.display()
