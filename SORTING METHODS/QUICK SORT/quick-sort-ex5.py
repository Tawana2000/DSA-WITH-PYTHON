# Emergency Dispatch System (911/Hospital/Fire Dept)
"""
You are building a dispatch system that decides which emergency cases should be handled first.
Each emergency call is represented as: (call_id, severity, distance_km, wait_time_min)
- severity -> higher number = more dangerous
- distance_km -> distance to nearest responder
- wait_time_min -> how long the caller has been waiting

Sorting Rules (in THIS exact order)
sort the calls using Quick Sort by:
- Higher severity first
- If severity equal -> Longer wait time first
- If both equal -> Closer distance first
- If all equal -> Smaller call_id first
"""

def emergency_dispatch(calls):

    if len(calls) <= 1:
        return calls
    
    else:
        pivot = calls.pop()

    left_sorted_calls = []
    right_sorted_call = []

    for call in calls:

        if call[1] > pivot[1]:
            left_sorted_calls.append(call)

        elif call[1] == pivot[1] and call[3] > pivot[3]:
            left_sorted_calls.append(call)

        elif (
            call[1] == pivot[1]
            and call[3] == pivot[3]
            and call[2] < pivot[2]
        ):
            left_sorted_calls.append(call)

        elif (
            call[1] == pivot[1]
            and call[3] == pivot[3]
            and call[2] == pivot[2]
            and call[0] < pivot[0]
        ):
            left_sorted_calls.append(call)

        else:
            right_sorted_call.append(call)

    return emergency_dispatch(left_sorted_calls) + [pivot] + emergency_dispatch(right_sorted_call)


calls = [
    (201, 5, 2.4, 10),
    (202, 3, 1.1, 20),
    (203, 5, 5.0, 5),
    (204, 4, 2.0, 15),
    (205, 5, 2.4, 10),
    (206, 3, 0.5, 30),
]

sorted_calls = emergency_dispatch(calls)

print("[")
for call in sorted_calls:
    print(f"{call}")
print("]")
