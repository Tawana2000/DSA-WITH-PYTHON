# Modify the Bubble Sort algorithm to return the number of swaps it made while sorting the array.

class Bubble_Sort:

    def bubble_sort(self, lst):
        self.lst = lst
        size = len(lst)
        swapped = False
        count = 0
        
        for i in range(size):
            for j in range(size - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    swapped = True
                    count += 1

            if not swapped:
                break
        return lst, count
    
BBS = Bubble_Sort()
print(BBS.bubble_sort([4, 3, 1, 7, 3, 2]))
