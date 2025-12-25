# You are given a list of students, where each student is represented as: (name, grade)
"""
Sort Rules:
1. Primary Key: grade -> descending
2. Secondary Key: name -> ascending(A-Z)
3. Use Merge Sort
4. Do NOT use sorted() or .sort()


Input:
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 92),
    ("Eve", 78)
]


Output:
[
    ("Bob", 92),
    ("David", 92),
    ("Alice", 85),
    ("Charlie", 85),
    ("Eve", 78)
]
"""


def merge_sort(students):

    if len(students) <= 1:
        return students
    
    mid = len(students) // 2

    left_sorted = merge_sort(students[:mid])
    right_sorted = merge_sort(students[mid:])

    return merge(left_sorted, right_sorted)

def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1

        elif left[i][1] == right[j][1] and left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 92),
    ("Eve", 78)
]

sorted_students = merge_sort(students)

for name, grade in sorted_students:
    print(f"{name}, {grade}")
