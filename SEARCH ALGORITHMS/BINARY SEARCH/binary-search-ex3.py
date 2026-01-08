# Last Salary <= Target
"""
You are given a sorted list of salaries (ascending order)
Write a function that returns the index of the LAST salary that is less than or equal to the target
If no such salary exists, return -1

salaries = [32000, 40000, 48000, 55000, 60000, 720000]
target = 55000

Expected OutPut
3

The Task is:
- Use binary search 
- Time Complexity must be O(logn)
- Do not use loops inside loop
- Return the index, not the value
"""

def last_less_salary(salaries, target):

    left = 0
    right = len(salaries)  -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if target >= salaries[mid]:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    return answer

salaries = [32000, 40000, 48000, 55000, 60000, 720000]
