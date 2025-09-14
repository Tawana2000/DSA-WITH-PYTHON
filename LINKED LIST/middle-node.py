# Write a program to find the middle node

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
        
    #Insert a node at a specific position
    def insert_node_at_position(self, data, position):
        new_node = Node(data)
        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        
    #Traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
        
    #Return the smalles number 
    def find_middle_element(self):

        if not self.head:
            return None
        
        fast = self.head
        slow = self.head

        #Traverse the linked list
        while fast is not None and fast.next is not None:
            #Move fast two steps ahead
            fast = fast.next.next

            #Move slow one step ahead
            slow = slow.next

        return slow.data

ll = Linkedlist()

data_list = list(map(int, input("Enter the list Elements: ").split()))

for node in data_list:
    ll.insert_node(node)

middle = ll.find_middle_element()
print(middle)
