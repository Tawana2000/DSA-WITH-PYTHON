#You are given a list of integers, sort the list in descending order using Merge Sort, print each merge step

"""
Input:
arr = [5, 1, 8, 3, 2, 7]

Expected Output:
Merging [5] and [1] → [5, 1]
Merging [8] and [3] → [8, 3]
Merging [2] and [7] → [7, 2]
Merging [5, 1] and [8, 3] → [8, 5, 3, 1]
Merging [7, 2] and [8, 5, 3, 1] → [8, 7, 5, 3, 2, 1]

Final Sorted Array: [8, 7, 5, 3, 2, 1]
"""

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    sorted_left = merge_sort(arr[:mid])
    sorted_right = merge_sort(arr[mid:])

    return merge(sorted_left, sorted_right)

def merge(left, right):

    output = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] >= right[j]:
            output.append(left[i])
            i += 1

        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])
    print(f"Merging {left} and {right} -> {output}")

    return output

arr = [5, 1, 8, 3, 2, 7]
print(f"Final Sorted Array: {merge_sort(arr)}")
