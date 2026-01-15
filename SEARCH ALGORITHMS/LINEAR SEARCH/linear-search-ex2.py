# Write a function to return all indexes where the target appears
"""
Input:
lst = [4, 2, 7, 2, 9, 2]
target = 2

Output:
[1, 3, 5]
"""

def all_indexes(lst, target):

    indexes = []

    for index, element in enumerate(lst):
        if element == target:
            indexes.append(index)
    return indexes

print(all_indexes([4, 2, 7, 2, 9, 2], 2))
