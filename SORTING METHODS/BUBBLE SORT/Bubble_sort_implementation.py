"""
In bubble sort we compare each element with its next (adjucent) element and swap them accordingly
Suppose if we have a list [27,15,6,1,2,8] and want to sort them in ascending order using bubble sort method
Iteration 1:
      - compare 27 with 15 and swap cause 27 > 15. So the new list will be = [15,27,6,1,2]
      - compare 27 with 6 and swap cause 27 > 6. So the new list will be = [15,6,27,1,2]
      - Compare 27 with 1 and then with 2, the final list after first iteration will be = [15,6,1,2,27]
      - Now that the largest element is placed where it should be (last position), we will go for the second iteration to place the second largest element at its position
Iteration 2:
      Now that we have the list as [15,6,1,2,27]
      - Compare 15 with 6 and swap
      - Continue this process until 15 is placed in its position, the new list will be = [6,1,2,15,27]

We will continue this process until the list is sorted and final result will be = [1,2,6,15,27]

"""

def bubble_sort(lst):

    for i in range(len(lst)):
        for j in range(len(lst) - 1):    # len(lst) - 1 , because this will be the second largest number, there will not be any other number after the largest number to compare with.
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

data_list = [15,27,6,1,2]
print(f"Unsorted list: {data_list}")

sorted_lsit = bubble_sort(data_list)
print(f"Sorted list: {sorted_lsit}") 


# In this example, we compare all consecutive elements during each loop iteration, Hence we can further optimize this bubble sort. 
