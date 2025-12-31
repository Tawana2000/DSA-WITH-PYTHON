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
