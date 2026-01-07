#Find the first Employee Earning at Least X
"""
You are given a sorted list of employee salaries (ascending order)
Write a function that returns the index of the first employee whose salary is greater than or equal to a target salary
If no such employee exists, return -1

Example Input:
salaries= [32000, 40000, 48000, 55000, 60000, 72000]
target = 50000

Expected Output:
3
"""

def first_salary_at_least(salaries, target):

    left = 0
    right = len(salaries) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if target <= salaries[mid]:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer

salaries = [32000, 40000, 48000, 55000, 60000, 72000]

print(first_salary_at_least(salaries, 50000))
