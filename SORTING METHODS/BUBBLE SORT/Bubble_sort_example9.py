#Sort employees by salary using Bubble Sort
# You are given a list of employees, where each employee is represented as a tuple: (name, salary)
# Write a Bubble Sort program to sort the employees by salary in descending order (highest-paid first).
#Also count how many swaps the algorithm makes while sorting


def bubble_sort_employee(employees):

    n = len(employees)


    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if employees[j][1] > employees[j + 1][1]:
                employees[j], employees[j + 1] = employees[j + 1], employees[j]
                swapped = True

        if not swapped:
            break

    return employees
