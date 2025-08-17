# Write a program to create a linked list and print it

class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):

        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())

        node1 = Node(data1)
        self.head = node1

        node2 = Node(data2)
        node1.next = node2

        node3 = Node(data3)
        node2.next = node3

        node4 = Node(data4)
        node3.next = node
        
    def traverse_linked_list(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

linked_list = LinkedList()
linked_list.create_linked_list()
linked_list.traverse_linked_list()
