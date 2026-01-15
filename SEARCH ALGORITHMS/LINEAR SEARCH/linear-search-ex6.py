# Find the first employee earning more than a given salary
"""
Input:
employees = [
    ("Alice", 5200),
    ("Bob", 4800),
    ("Charlie", 6000),
    ("David", 4500)
]

Output
("Charlie", 6000)
"""

def highest_earner(employees):

    if not employees:
        return None
    
    highest = employees[0]

    for employee in employees:
        if employee[1] > highest[1]:
            highest = employee
    return highest

employees = [
    ("Alice", 5200),
    ("Bob", 4800),
    ("Charlie", 6000),
    ("David", 4500)
]

print(highest_earner(employees))
