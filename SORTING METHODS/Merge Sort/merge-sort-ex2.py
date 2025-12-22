# You are given a list of employess, where each employee is represented as:
"""
(name, salary)

Input:
employees = [
    ("Alice", 5200),
    ("Bob", 4800),
    ("Charlie", 6000),
    ("David", 4500),
    ("Eve", 5200)
]

Expected Output:
[
    ("David", 4500),
    ("Bob", 4800),
    ("Alice", 5200),
    ("Eve", 5200),
    ("Charlie", 6000)
]
"""

# Use Merge sort, Compare using salary (index1), Ensure the sort is stable, Return the sortes list


def merge_sort(employees):

    if len(employees) <= 1:
        return employees
    
    mid = len(employees) // 2

    left_partition = merge_sort(employees[:mid])
    right_partition = merge_sort(employees[mid:])

    return merge(left_partition, right_partition)

def merge(left, right):

    result = []

    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(f"Sorted List: {merge_sort(employees)}")

employees = [
    ("Alice", 5200),
    ("Bob", 4800),
    ("Charlie", 6000),
    ("David", 4500),
    ("Eve", 5200)
]

print(f"Unsorted List: {employees}")
