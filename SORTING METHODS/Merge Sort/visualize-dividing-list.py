# Visualize dividing the list recursively

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    print(f'lst: {lst}')
    mid = len(lst) // 2
    
    print(f'mid: {lst[mid]}')

    left = merge_sort(lst[:mid])
    print(f'Left Partition: {left}')

    right = merge_sort(lst[mid:])
    print(f'Right Partition: {right}')

    return "---"

lst = [5, 4, 7, 3, 2, 12]
merge_sort(lst)
