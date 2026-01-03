# Write a linear shearch algorithm that finds the first number greater than the target
"""
Input:
lst = [3, 7, 1, 9, 4]
target = 5

Output:
1
"""

def first_greater(lst, target):

    for index, element in enumerate(lst):
        if element > target:
            return index
    
    return None

print(first_greater([3, 7, 1, 9, 4], 5))
