"""
You are given an array of integers.
Your task is to perform insertion sort, but with a twist:

You must:

Sort the array in ascending order using Insertion Sort
Count the total number of comparisons made
Count the total number of shifts (moves)
Print the internal steps, including:
Which key is being inserted
Every shift operation
The array after each step
"""

class InsertionSortChallenge:

    def solve(self, arr):

        comparisons = 0
        shifts = 0

        print(f"Original Array: {arr}\n")

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            print(f"Step {i} (key = {key}):")

            # Optimized: single while condition
            while j >= 0:
                comparisons += 1  # checking arr[j] > key

                if arr[j] > key:
                    # shift the element right
                    arr[j + 1] = arr[j]
                    shifts += 1
                    print(f"  Shift: moved {arr[j]} → index {j+1}")
                    j -= 1
                else:
                    break
