# Quick sort implementation
#1.Check for base condition and determine the pivot
#2.Place the elements into the greater and lesser sublists
#3.Call the function recursively to merge the two sublists

def quick_sort(lst):

    length = len(lst)

    if length <= 1:
        return lst
    
    else:
        pivot = lst.pop()

    
    right = []
    left = []

    for elements in lst:
        if elements > pivot:
            right.append(elements)

        else:
            left.append(elements)

    return quick_sort(left) + [pivot] + quick_sort(right)

list1 = [30, 2, 17, 7, 23, 6, 12, 8]
print(f"Unsorted List: {list1}")

print(f"Sorted List: {quick_sort(list1)}")