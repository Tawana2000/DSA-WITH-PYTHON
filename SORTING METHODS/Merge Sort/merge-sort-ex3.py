# You are given a list of integers, sort the list using Merge Sort, and also count how many comparisons are made during the merge process.

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    left_sorted, left_comparisons = merge_sort(lst[:mid])
    right_sorted, right_comparisons = merge_sort(lst[mid:])

    merged, merge_comparisons = merge(left_sorted, right_sorted)

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons

    return merged, total_comparisons

def merge(left, right):

    result = []

    i = 0
    j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] < right[j]:
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

sorted_list, comparisons_count = merge_sort(lst)
print(f" Sorted List: {sorted_list}")
print(f"Total Comparisons: {comparisons_count}")
