# You are given a list points on a 2D plane, represented as:
"""
(x, y)

Sort Rules:
1. Sort points by distance form the origin (0,0)v -> ascending
2. If two points have the same distance, sort by:
- x ascending
- then y ascending
3. Use Merge Sort only
4. Do NOT use sorted() or .sort()
"""


def distance(p):
    return p[0] ** 2 + p[1]**2


def merge_sort(points):

    if len(points) <= 1:
        return points
    
    mid = len(points) // 2

    left_sorted = merge_sort(points[:mid])
    right_sorted = merge_sort(points[mid:])

    return merge(left_sorted, right_sorted)

def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        dist_left = distance(left[i])
        dist_right = distance(right[j])

        if dist_left < dist_right:
            result.append(left[i])
            i += 1

        elif dist_left == dist_right and left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1

        elif (
            dist_left == dist_right
            and left[i][0] == right[j][0]
            and left[i][1] <= right[j][1]
        ):
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("Original Points: ")
print(points)

sorted_points = merge_sort(points)

print(f"\nSorted Points (by distance from origin):")
print(sorted_points)
