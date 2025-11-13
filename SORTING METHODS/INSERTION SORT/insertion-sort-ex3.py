# Track Comparisons and Shift
"""
Given the array: arr = [12, 5, 7, 3, 11, 2]
The task is:
- Perform insertion sort
- After each step print:
-> The step number
-> The Key
-> The array state
- At the end, print:
-> Total number of comparisons
-> Total number of shifts
"""

class Insertion_Sort:

    def compare_shift(self, arr):

        comparisons = 0
        shifts = 0

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            # We count the comparison for entering the while-loop as well.
            while True:
                comparisons += 1  # for checking j >= 0
                if j >= 0 and arr[j] > key:
                    comparisons += 1  # for checking arr[j] > key
                    arr[j + 1] = arr[j]
                    shifts += 1
                    j -= 1
                else:
                    break

            arr[j + 1] = key

            print(f"Step {i} (Key = {key}): {arr}")

        print(f"Total Comparisons: {comparisons}")
        print(f"Total Shifts: {shifts}")

        return arr


IS = Insertion_Sort()
IS.compare_shift([12, 5, 7, 3, 11, 2])
