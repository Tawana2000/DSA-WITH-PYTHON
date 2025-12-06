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

            # Insert key at the proper location
            arr[j + 1] = key

            print(f"  Result: {arr}\n")

        print(f"Total Comparisons: {comparisons}")
        print(f"Total Shifts: {shifts}")

        return arr


# Run the optimized version
sorter = InsertionSortChallenge()
sorter.solve([13, 2, 9, 7, 1, 6])


# More Optimized version
"""
This optimization includes:
- Minimal Python overhead
- Exact comparison & shift counting (as required by HackerRank, etc.)
- No list slicing, no extra objects, no function calls in hot loop
- Optional verbose mode for debugging

"""
"""
class InsertionSortChallenge:
    def solve(self, arr, *, verbose=False):
        n = len(arr)
        if n <= 1:
            if verbose:
                print(f"Original: {arr}")
                print("Total Comparisons: 0")
                print("Total Shifts: 0")
            return arr[:], 0, 0

        # Work on a copy to avoid mutating input
        a = arr[:]
        comparisons = 0
        shifts = 0

        if verbose:
            print(f"Original Array: {a}\n")

        # Main insertion sort loop - fully unrolled inner logic
        for i in range(1, n):
            key = a[i]
            j = i - 1

            if verbose:
                print(f"Step {i}: key = {key}")

            # Inner while loop: shift elements > key to the right
            while j >= 0:
                comparisons += 1
                if a[j] > key:               # actual comparison
                    a[j + 1] = a[j]          # shift
                    shifts += 1
                    if verbose:
                        print(f"  Shift: {a[j]} -> index {j+1}  |  Array: {a}")
                    j -= 1
                else:
                    break  # ← this is the key optimization (O(n) best case)

            # Place key in correct position
            a[j + 1] = key

            if verbose:
                print(f"  After insert: {a}\n")

        if verbose:
            print(f"Final Sorted Array: {a}\n")
            print(f"Total Comparisons: {comparisons}")
            print(f"Total Shifts     : {shifts}")

        return a, comparisons, shifts
"""
