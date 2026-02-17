# Write a program to delete the first node from a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def create_linked_list(self):

        node1 = Node(12)
        node2 = Node(9)
        node3 = Node(20)
        node4 = Node(3)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    def delete_first_node(self):
        if self.head:
            self.head = self.head.next

ll = Linkedlist()
ll.create_linked_list()
print("Original List")
ll.display()
ll.delete_first_node()
print("After deleting the first node")
ll.display()
