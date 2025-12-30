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

