# Write a quick sort program that sorts elements in ascending order. However, choose the middle element as the pivot

def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    
    else:
        pivot = lst.pop(len(lst) // 2)

    left = []
    right = []

    for elements in lst:
        if elements > pivot:
            right.append(elements)

        else:
            left.append(elements)

    return quick_sort(left) + [pivot] + quick_sort(right)

lst = list(map(int, input("Enter the list elements: ").split()))
print(quick_sort(lst))
