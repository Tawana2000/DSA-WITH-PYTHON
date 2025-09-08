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

  #Universal insertion method
  def insert_node(self, data, position = None):
      #If no position is given , or position exceeds the lenght of the list, insert at the end
      if position is None or position >= self.get_lenght():
          self.append_node(data)
      elif position == 0:
          self.insert_node_at_beginning(data)
      else:
          self.insert_node_at_position(data, position)

    #Helper method to get the lenght of the linked list
    def get_lenght(self):
        current = self.head
        lenght = 0
        while current:
            lenght += 1
            current = current.next
        return lenght
