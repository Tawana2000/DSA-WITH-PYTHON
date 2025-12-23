# You are given a list of integers, sort the list using Merge Sort, and also count how many comparisons are made during the merge process.

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])

    return merge(left_partition, right_partition)

def merge(left, right):

    result = []

    i = 0
    j = 0
    comparisons = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            comparisons += 1
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons

lst = [10, 4, 7, 1, 9, 3]
print(f"Original List: {lst}")

print("Sorted List: ")
print(merge_sort(lst))
