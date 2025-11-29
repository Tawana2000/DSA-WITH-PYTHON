#Sort employees by salary using Bubble Sort
# You are given a list of employees, where each employee is represented as a tuple: (name, salary)
# Write a Bubble Sort program to sort the employees by salary in descending order (highest-paid first).
#Also count how many swaps the algorithm makes while sorting


def bubble_sort_employee(employees):

    n = len(employees)
    swaps = 0

    for i in range(n - 1):

        swapped = False
        # Small optimization: store salary lookups locally
        for j in range(n - 1 - i):

            # Compare salaries for DESCENDING (higher salary first)
            if employees[j][1] < employees[j + 1][1]:
                employees[j], employees[j + 1] = employees[j + 1], employees[j]
                swapped = True
                swaps += 1

        # If no swaps, list is sorted → stop early
        if not swapped:
            break

    return employees, swaps
