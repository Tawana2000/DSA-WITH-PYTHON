#Your task is to sort the array in descending order using the selection sort algorithm and also count the number of swaps performed.
"""
1.Implement selection sort to sort in descending order.
2.Keep a counter for number of swaps.
3.Print the sorted array and total swaps.
"""

class Selection_Sort:

  def sort_array(self, array):

    for i in range(len(array)):
      min_max = i
      for j in range(i + 1, len(array)):
        if array[j] > array[min_max]:
          min_max = j
      array[i], array[min_max] = array[min_max], array[i]
  return array

SS = Selection_Sort()
print(SS.sort_array([5, 2, 9, 1, 5, 6]))
