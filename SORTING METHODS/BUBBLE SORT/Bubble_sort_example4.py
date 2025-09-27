# Imagine you are analyzing race times (in seconds) for 8 runners: [54.3, 49.1, 61.0, 58.7, 47.5, 52.8, 60.2, 55.9], your task to:
#1. Use bubble sort to sort the times in ascending order (fastest runner first), 2.Track how many comparisons are made in total (not swaps this time, but every time two elements are compared), 3.Return both the sorted list and the comparison count

class Bubble_Sort:

    def bubble_sort(self, lst):
        self.lst = lst
        size = len(lst)
        count = 0

        for i in range(size):
            swapped = False
            for j in range(size - 1 - i):
                count += 1
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    swapped = True

        return lst, count
    
BBS = Bubble_Sort()
print(BBS.bubble_sort([54.3, 49.1, 61.0, 58.7, 47.5, 52.8, 60.2, 55.9]))
