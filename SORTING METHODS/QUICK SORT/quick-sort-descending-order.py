# Write a program to sort the list itmes in descending order using quick sort

def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    
    else:
        pivot = lst.pop()

    left = []
    right = []

    for elements in lst:
        if elements > pivot:
            right.append(elements)

        else:
            left.append(elements)
    return quick_sort(right) + [pivot] + quick_sort(left)

data_list = list(map(int, input("Enter the list elements: ").split()))
print(quick_sort(data_list))
