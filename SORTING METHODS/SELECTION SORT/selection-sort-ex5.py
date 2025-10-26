# You are working in a company's HR analytics team, you have a list of employees with their names, departments, and monthly salaries (in USD):
"""
employees = [
    ["Alice", "Engineering", 7200],
    ["Bob", "HR", 4800],
    ["Charlie", "Engineering", 6800],
    ["Diana", "Finance", 7500],
    ["Evan", "HR", 5000],
    ["Fiona", "Finance", 6200]
]
"""
# Write a python program that:
"""
1. Sorts the employees by salary (descending), highest earners first.
2. If two employees have the same salary, sort them alphabetically by name.
3. After sorting, print: 
-> The top 3 highest earners (name + department + salary).
-> The average salary of all employees
"""

class Selection_Sort:

    def employee_salary(self, employees):

        for i in range(len(employees)):
            min_max = i

            for j in range(i + 1, len(employees)):
                if employees[j][2] > employees[min_max][2]:
                    min_max = j

                elif employees[j][2] == employees[min_max][2] and employees[j][0] < employees[min_max][0]:
                    min_max = j

            employees[i], employees[min_max] = employees[min_max], employees[i]
            
        print("Sorted Employees (by salary): ")
        for name, department, salary in employees:
            print(f"{name} | {department} | ${salary}")
        
        print("\nTop 3 Highest Earners: ")
        for name, department, salary in employees[:3]:
            print(f"{name} | {department} | {salary}")

        avg_salary = sum(emp[2] for emp in employees) / len(employees)
        print(f"\nAverage Salary: ${avg_salary:.2f}")
        return employees

employees = [
    ["Alice", "Engineering", 7200],
    ["Bob", "HR", 4800],
    ["Charlie", "Engineering", 6800],
    ["Diana", "Finance", 7500],
    ["Evan", "HR", 5000],
    ["Fiona", "Finance", 6200]
]

SS = Selection_Sort()
SS.employee_salary(employees)
