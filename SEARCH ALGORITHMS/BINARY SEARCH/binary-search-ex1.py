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


def delivery_times(slots, target):

    left = 0 
    right = len(slots) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if target < slots[mid]:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer

delivery_slots = [8, 9, 10, 12, 14, 16, 18]

print(delivery_times(delivery_slots, 10))
print(delivery_times(delivery_slots, 15))
print(delivery_times(delivery_slots, 18))
