# Write a program to find the nth smallest element after merging and sorting two sorted lists
# Assumption: The input lists will always be in ascending order, --inside the function merge two lists in ascending order, then find the nth element from the list and return it.

def smallest_number(list1, list2, n):

    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1

        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result[n - 1]

list1 = list(map(int, input("First list's elements: ").split()))
list2 = list(map(int, input("Second list's elements: ").split()))
n = int(input('nth smallest number: '))

print(smallest_number(list1, list2, n))