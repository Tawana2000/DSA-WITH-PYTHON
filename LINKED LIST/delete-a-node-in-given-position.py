# Write a program to delete a node in a given position in an existing linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def create_linked_list(self):

        node1 = Node(14)
        node2 = Node(60)
        node3 = Node(23)
        node4 = Node(30)
        node5 = Node(8)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next

        print(None)
        
    def get_lenght(self):

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
        
    def delete_node(self, position):
        if position <= 0 or position > self.get_lenght():
            print("Invalid Position")
            return 
        
        #If list is empty
        if not self.head:
            return 
        
        # Condition to delete node at the first position
        if position == 1:
            self.head = self.head.next
            return 
        
        current = self.head

        for i in range(1, position - 1):
            # To handle if position is greater than number of nodes
            if not current.next:
                return 
            current = current.next

        if current.next:
            current.next = current.next.next
