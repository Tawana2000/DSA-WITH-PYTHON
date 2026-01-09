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


def first_available_agent(agents, time_limit):

    left = 0
    right = len(agents) - 1
    answer = -1 

    while left <= right:
        mid = (left + right) // 2

        if agents[mid][1] <= time_limit:
            answer = mid
            right = mid - 1   # move left to find earlier agent
        else:
            left = mid + 1

    return answer
