# Write a program to take the list elements as use input and sort the list in ascending order using bubble sort

def bubble_sort(lst):

    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

list_elements = list(map(int, input().split()))  # Take the inputs and convert them to a list

sorted_list = bubble_sort(list_elements)
print(f"sorted_list: {sorted_list}")
