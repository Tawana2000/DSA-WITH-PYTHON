#Write a program to insert a new node at the end of an already existing ciruclar linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def create_circular_linked_list(self):

        node1 = Node(28)
        node2 = Node(14)
        node3 = Node(50)
        node4 = Node(7)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = self.head

    def insert_node_at_the_end(self, data):
        new_node = Node(data)

        #If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node

            return
    
        current = self.head

        while current.next != self.head:
            current = current.next

        #Insert at the end
        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.head
        
        while True:
            print(current.data, end = " -> ")
            current = current.next
            if current == self.head:
                break

        print("(back to head)")


linked_list = CircularLinkedList()
linked_list.create_circular_linked_list()

print("Before Insertion: ")
linked_list.display()

linked_list.insert_node_at_the_end(19)

print("After insertion: ")
linked_list.display()
