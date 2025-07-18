"""
Selection sort works by repeatedly selecting the smallest (or largest) unsorted element and placing it towards the beginning of the list
"""

def selection_sort(lst):

    for i in range(len(lst)):
        min_max = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_max]:   #sorting in ascending order
                min_max = j

        lst[i], lst[min_max] = lst[min_max], lst[i]

    return lst

lst = list(map(int, input("Enter the list elements separated by space: ").split()))            #if taking integer input lst = list(map(int, input().split()))
print(selection_sort(lst))