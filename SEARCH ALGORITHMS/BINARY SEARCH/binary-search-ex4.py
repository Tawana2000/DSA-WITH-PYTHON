#Find the First Available Support Agent
"""
Scenario
A customer support system has a list of agents sorted by the time they become availble (in minutes from now).
Each agent is represented as:
(name, available_in_minute)
The list is sorted in ascending order by availability time.

Your task is to find the first agent who will be available within or before a given time limit.

Input:

agents = [
    ("Alice", 5),
    ("Bob", 10),
    ("Charlie", 15),
    ("David", 20),
    ("Eve", 30)
]

time_limit = 18


Expected Outpu:
2
"""
