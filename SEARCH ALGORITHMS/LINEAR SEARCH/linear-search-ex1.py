# Write a function that returns the first index of a target value in a list
"""
Input:
lst = [4, 2, 7, 2, 9, 2]
target = 2

Output:
1
"""

def target_index(lst, target):

    for index, element in enumerate(lst):
        if element == target:
            return index
    return None

lst = [4, 2, 7, 2, 9, 2]
target = 2

print(target_index(lst, target))
