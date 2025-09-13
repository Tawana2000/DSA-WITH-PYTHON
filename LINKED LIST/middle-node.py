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
