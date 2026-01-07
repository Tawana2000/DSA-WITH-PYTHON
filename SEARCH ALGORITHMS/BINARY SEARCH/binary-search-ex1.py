# You are building a scheduling system
"""
You are given a sorted list of delivery times (in hours, 24-hour format)
delivery_slots = [8, 9, 10, 12, 14, 16, 18]
A customer requests a delivery after a given time.
Write a function that returns the index of the earliest delivery slot that is strictly greater than the requested time.

Requirements:
- Use Binary Search
- Return -1 if no valid slot exists
- The list is already sorted

Rules:
- NO linear Scan 
- NO built-in .index()
"""
