# Write a quick sort program to sort the elements of the list in ascending order

def quick_sort(lst):

    lst_lenght = len(lst)

    if lst_lenght <= 1:
        return lst
    
    else:
        pivot = lst.pop()

    left_elements = []
    right_elements = []

    for elements in lst:
        if elements < pivot:
            left_elements.append(elements)

        else:
            right_elements.append(elements)

    return quick_sort(left_elements) + [pivot] + quick_sort(right_elements)

data_list = list(map(int, input("Enter the list elements separated by a space:").split()))

print(quick_sort(data_list))
