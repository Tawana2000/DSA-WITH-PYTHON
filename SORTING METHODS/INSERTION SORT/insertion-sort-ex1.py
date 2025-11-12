# Trace the algorithm
"""
You are given the following list:
arr = [9, 3, 7, 1, 5]
Using insertion sort, show how the list changes after each outer loop iteration (after each i)
Expected output:
Step 1 (key = 3): [3, 9, 7, 1, 5]
Step 2 (key = 7): [3, 7, 9, 1, 5]
"""

class Insertion_Sort:

    def trace_algorithm(self, arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
            print(f"Step {i} (Key = {key}): {arr}")
        
        return arr
    
IS = Insertion_Sort()
IS.trace_algorithm([9, 3, 7, 1, 5])
