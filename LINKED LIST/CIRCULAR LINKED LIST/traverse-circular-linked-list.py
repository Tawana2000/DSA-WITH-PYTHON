#Write a complete code for traversing a circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    #Add an is_empty() method
    def is_empty(self):
        return self.head is None
    
    def traverse_list(self):

        if self.is_empty():
            print("Empty Linked LIst")
            return
        

        current = self.head
        while current.next is not self.head:
            print(f"{current.data} ->", end=" ")
            current = current.next
        
        #print the last node's as well
        print(f"{current.data} -> {self.head.data}")

linked_list = CircularLinkedList()
linked_list.traverse_list()
