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

class Selection_Sort:

    def hospital_management(self, patients):

        for i in range(len(patients)):
            low_high_urgency = i

            for j in range(i + 1, len(patients)):
                if patients[j][2] > patients[low_high_urgency][2]:
                    low_high_urgency = j
                elif patients[j][2] == patients[low_high_urgency][2] and patients[j][1] > patients[low_high_urgency][1]:
                    low_high_urgency = j
                elif patients[j][2] == patients[low_high_urgency][2] and patients[j][1] == patients[low_high_urgency][1] and patients[j][4] < patients[low_high_urgency][4]:
                    low_high_urgency = j
                elif patients[j][2] == patients[low_high_urgency][2] and patients[j][1] == patients[low_high_urgency][1] and patients[j][4] == patients[low_high_urgency][4] and patients[j][3] < patients[low_high_urgency][3]:
                    low_high_urgency = j

            patients[i], patients[low_high_urgency] = patients[low_high_urgency], patients[i]
        
        
        for name, age, urgency, department, arrival_time in patients:
            formatted_time = f"{arrival_time//100:02}:{arrival_time%100:02}"   
            print(f"Name: {name} | Age: {age} | Urgency: {urgency} | Department: {department} | Arrival: {formatted_time}")
        return patients
patients = [
    ["John", 72, 5, "Cardiology", 915],
    ["Emily", 45, 4, "Neurology", 945],
    ["Mark", 72, 5, "Orthopedics", 905],
    ["Sophia", 30, 5, "General", 915],
    ["David", 55, 4, "Cardiology", 930],
    ["Lily", 60, 4, "Cardiology", 925],
    ["Noah", 72, 5, "Cardiology", 915],
    ["Chris", 25, 3, "General", 870],
    ["Ava", 72, 5, "Cardiology", 900]
]

SS = Selection_Sort()
SS.hospital_management(patients)
