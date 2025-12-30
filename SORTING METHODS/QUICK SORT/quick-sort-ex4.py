# You are building a system that sorts ride requests before assgning drivers
"""
Each request is represented as: {user_id, distance_km, request_time}
distance_km -> how far the rider is from the drive
request_time -> smaller number = requested earlier

Sorting Rules:
Sort ride requests using Quick Sort by:
- Closer distance first
- If distance is equal -> earlier request first
- If both equal -> smaller user_id first
"""

def sort_rides(rides):

    if len(rides) <= 1:
        return rides
    
    else:
        pivot = rides.pop()

    sorted_left = []
    sorted_right = []

    for ride in rides:

        if ride[1] < pivot[1]:
            sorted_left.append(ride)
        
        elif ride[1] == pivot[1] and ride[2] < pivot[2]:
            sorted_left.append(ride)

        elif (
            ride[1] == pivot[1] 
            and ride[2] == pivot[2] 
            and ride[0] < pivot[0]
        ):
            sorted_left.append(ride)

        else:
            sorted_right.append(ride)

    return sort_rides(sorted_left) + [pivot] + sort_rides(sorted_right)


rides = [
    (102, 3.5, 12),
    (101, 1.2, 15),
    (104, 1.2, 10),
    (103, 5.0, 8),
    (105, 3.5, 11),
]

sorted_result = sort_rides(rides)

print("[")
for ride in rides:
    print(f"{ride},")
print("]")
