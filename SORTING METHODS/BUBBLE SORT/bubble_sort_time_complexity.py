"""
Time complexity of bubble sort
Let's say we have a list with a total of 8 elements, here is the breakdown of comparisons for each iteration:
- First iteration - 7 comparisons
- Second iteration - 6 comparisons
- Third iteration - 5 comparisons and so on

The total number of comparisons will be: 7 + 6 + 5 + 4 + 3 + 2 + 1
Hence, for n elements in a list, the total number of comparisons will be:
Comparisons (C) = (n - 1) + (n - 2) + ... + 2 + 1
= n(n - 1)/2   == n**2

🔴 The time complexity of comparison_based sorting algorithm is based on the number of comparisons.
Therefore the time complexity is:   TC = O(n**2)

- Worst Case Complexity: O(n**2)
- Average Case Complexity: O(n**2)
- Best Case Complexity: O(n) ---> When the list is already sorted and no swaps needed
"""
# Let's write a code for ascending order sorting for better understanding 

def bubble_sort_tc(lst):

    for i in range(len(lst) - 1):           # i look controls howmany passes are executed while j loop iterates through elements for swapping.
        swapped = True
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                swapped = True

        if not swapped:
            break

    return lst

lst = [7,6,5,4,3,2,1,12]
print(bubble_sort_tc(lst))


#The space complexity of Bubble sort is O(1), because it only requires a constant amount of additional space for its variables
