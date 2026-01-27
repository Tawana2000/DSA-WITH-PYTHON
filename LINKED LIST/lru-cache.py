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
