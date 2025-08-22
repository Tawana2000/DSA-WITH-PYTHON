# Write a program to insert a node in a linked list.

lass Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def create_linked_list(self):

        node1 = Node(14)
        node2 = Node(8)
        node3 = Node(11)
        node4 = Node(6)

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


    def insert_node_at_position(self, data, position):
        new_node = Node(data)
        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        

ll = Linkedlist()
ll.create_linked_list()
position = int(input("Enter the position where you want to insert the node: "))
data = int(input("Enter the new node data: "))
