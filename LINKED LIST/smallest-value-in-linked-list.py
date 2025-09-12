#Write a program to find the smallest value in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(45)
        self.head = node1

        node2 = Node(23)
        node1.next = node2

        node3 = Node(50)
        node2.next = node3
        
     
    #Append a node at the end
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    #Insert a node at the beginning 
    def insert_node_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    #Universal insert method
    def insert_node(self, data, position = None):

        if position is None or position >= self.get_length():
            self.append_node(data)

        elif position == 0:
            self.insert_node_at_the_beginning(data)
        else:
            self.insert_node_at_position(data, position)
            
    #Get the lenght of linked list
    def get_length(self):
        current = self.head
        lenght = 0
        while current:
            lenght += 1
            current = current.next
        return lenght
        
    #Traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
        
    #Return the smalles number 
    def find_smalles(self):

        if not self.head:
            return None
        current = self.head
        smallest = current.data
        while current is not None:
            if current.data < smallest:
                smallest = current.data
            current = current.next
        return smallest


ll = Linkedlist()
ll.create_linked_list()
ll.display()
