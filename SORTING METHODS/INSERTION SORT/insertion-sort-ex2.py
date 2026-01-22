# Sort and Trace
"""
Given this list: [8, 4, 9, 2, 6]
Your task:
Write a Python class to:
1. Perform Insertion Sort.
2. Print the array after each insertion step.
3. At the end, print the total number of shifts (how many times elements were moved right)
"""

class Insertion_Sort:

    def sort_trace(self, arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
            print(f"Step {i} (Key = {key}): {arr}")

        print(f"Total Shifts: {i + 1}")
        return arr
            
IS = Insertion_Sort()
IS.sort_trace([8, 4, 9, 2, 6])
