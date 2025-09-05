# Write a program to reverse a linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  #Helper method to append a node at the end
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
  def insert_node_at_beginning(self, data):
