# Write a program to sort the employess using insertion sort, with the following rules:
"""
1. Higher salary comes first (descending)
2. If salaries are equal, more years of experience comes first
3. If both salary and experience are equal, sort alphabetically by name
"""

class InsertionSortEmployees:

    def sort(self, employees):

        comparisons = 0
        shifts = 0

        print(f"Original List:\n{employees}\n")

        # Standard insertion sort
        for i in range(1, len(employees)):
            key = employees[i]
            j = i - 1

            print(f"Step {i} (Key = {key}):")

            # While the left element should come AFTER key, shift it right
            while j >= 0:

                comparisons += 1  # We are comparing employees[j] and key

                left = employees[j]

                # Compare by salary (descending)
                if left[1] < key[1]:
                    condition = True
                # If salary equal → compare experience (descending)
                elif left[1] == key[1] and left[2] < key[2]:
                    condition = True
                # If both equal → compare name (ascending)
                elif left[1] == key[1] and left[2] == key[2] and left[0] > key[0]:
                    condition = True
                else:
                    condition = False

                if condition:
                    employees[j + 1] = employees[j]  # shift right
                    shifts += 1
                    print(f"  Shift: moved {employees[j]} → index {j+1}")
                    j -= 1
                else:
                    break

            employees[j + 1] = key

            print(f"  Result: {employees}\n")

        print(f"Total Comparisons: {comparisons}")
        print(f"Total Shifts: {shifts}")

        return employees

employees = [
    ("Alice", 5200, 3),
    ("Bob", 5200, 5),
    ("Charlie", 6000, 2),
    ("David", 4500, 7),
    ("Eve", 5200, 3)
]

sorter = InsertionSortEmployees()
sorter.sort(employees)
