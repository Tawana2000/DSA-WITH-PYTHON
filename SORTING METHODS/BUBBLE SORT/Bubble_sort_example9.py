#Sort employees by salary using Bubble Sort
# You are given a list of employees, where each employee is represented as a tuple: (name, salary)
# Write a Bubble Sort program to sort the employees by salary in descending order (highest-paid first).
#Also count how many swaps the algorithm makes while sorting


def bubble_sort_employee(employees):

    n = len(employees)
    swaps = 0

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if employees[j][1] > employees[j + 1][1]:
                employees[j], employees[j + 1] = employees[j + 1], employees[j]
                swapped = True
                swaps += 1

        if not swapped:
            break

    return employees, swaps

employees = [
    ("Alice", 5200),
    ("Bob", 4800),
    ("Charlie", 6000),
    ("David", 4500),
    ("Eve", 5200)
]

sorted_employees, swap_count = bubble_sort_employee(employees)

print("Sorted Employees by Salary (Descending): ")
for name, salary in sorted_employees:
    print(f"{name} - ${salary}")

print(f"\nTotal number of swaps: {swap_count}")
