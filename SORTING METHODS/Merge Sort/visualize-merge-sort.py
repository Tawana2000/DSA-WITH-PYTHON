# We might think that merge sort divides the whole list first. Then, it starts merging. But it doesn't work like that.
# Instead, we divide one side of the list first, merge it, and then divide and merge the other side. This process keeps going until the entire list is sorted.

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    left_partition = merge_sort(lst[: mid])
    righ_partition = merge_sort(lst[mid :])

    return merge(left_partition, righ_partition)

def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
    
    # Append the remaining element
    result.extend(left[i:])
    result.extend(right[j:])

    return result

given_lst = [6, 2, 45, 5, 7, 18, 3]
print(f'Unsorted: {given_lst}')

print(f'Sorted: {merge_sort(given_lst)}')