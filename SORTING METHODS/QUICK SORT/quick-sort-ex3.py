# You are given a list of 2D points (x, y)
"""
Sort the points using Quick Sort based on:
- Distance from the origin (0, 0), smaller distance first
- If distance are equal -> Smaller x first
- if x si also equal -> smaller y first


Input

points = [
    (3, 4),
    (1, 1),
    (0, 2),
    (2, 2),
    (1, 2),
    (0, 0)
]


Expected Output

[
    (0, 0),
    (1, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 4)
]
"""


def distance(p):
    return p[0] ** 2 + p[1] ** 2


def quick_sort(points):

    if len(points) <= 1:
        return points
    
    else:
        pivot = points.pop()
        pivot_distance = distance(pivot)

    left_elements = []
    right_elements = []

    for pairs in points:
        point_distance = distance(pairs)

        if point_distance < pivot_distance:
            left_elements.append(pairs)

        elif point_distance == pivot_distance and point_distance[0] < pivot_distance[0]:
            left_elements.append(pairs)

        elif (
            point_distance == pivot_distance 
            and point_distance[0] == pivot_distance[0]
            and point_distance[1] < pivot_distance[1]
        ):
            left_elements.append(pairs)

        else:
            right_elements.append(pairs)

    
    return quick_sort(left_elements) + [pivot] + quick_sort(right_elements)


points = [(3,4), (1,1), (0,2), (2,2), (1,2), (0,0)]

sorted_points = quick_sort(points)

print(sorted_points)
