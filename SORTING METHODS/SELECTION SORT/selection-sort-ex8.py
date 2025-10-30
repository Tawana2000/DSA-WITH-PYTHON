# Advanced Hospital Management Problem
"""
Each patient record includes:
[name, age, urgency_level, department, arrival_time]
where:
- urgency_level: 1 (low) -> 5(critical)
- department: "Cardiology", Neurology", "Orthopedics", "General", etc.
- arrival_time: time in 24h format as integer, e.g. 930 for 9:30AM, 1515 for 3:15PM

Your Task
Using selection sort, sort the patients by the following rules (in priority order):
1. Urgency level -> Highest First 
2. If urgency is the same -> older patients first
3. If age is also the same -> earlier arrival time first (they came sooner)
4. If all above are equal -> alphabetical order of department name
Finally, print the sorted records neatly like:
Name: John | Age: 72 | Urgency: 5 | Department: Cardiology | Arrival: 09:15
"""
