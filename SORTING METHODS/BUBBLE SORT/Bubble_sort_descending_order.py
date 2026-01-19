# Write a program to sort the list items in descending order using bubble sort

def bubble_sort(lst):

    for i in range(len(lst)):
        for j in range(len(lst) - 1):

            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

result = list(map(int, input().split()))   #Takes integer input and converts it into list
print(bubble_sort(result))
