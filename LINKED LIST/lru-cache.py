#Desing and implement a Least Recently Used (LRU) Cache
"""
The cache should support the following operations in O(1) time:
get(key) -> returns the value if the key exists, otherwise -1
put(key, value) -> inserts or updates the value

Rules:
- When the cache exceeds its capacity, remove the least recently used item
- Every access (get/put) makes the item most recently used
- Use:
-> Doubly Linked List -> track usage order 
-> Hash Map -> fast access
"""

"""
Approach:
Doubly Linked List:
-> Head: Most Recently Used (MRU)
-> Tail: Least Recently Used (LRU)
Hash Map:
-> Key: linked list node
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):

        node.prev.next = node.next
        node.next = node.prev  

    def _add_to_front(self, node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:

            lru = self.tail
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)    
    print(lru.get(2))
