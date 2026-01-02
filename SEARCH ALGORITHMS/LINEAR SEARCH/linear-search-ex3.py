# Write a linear search algorithm that return all indexes where the target appears
"""
Input:
lst = [4, 2, 7, 2, 9, 2]
target = 2

Output:
3
"""

def count_occurences(lst, target):

    count = 0

    for element in lst:
        if element == target:
            count += 1

    return count

print(count_occurences([4, 2, 7, 2, 9, 2], 2))
