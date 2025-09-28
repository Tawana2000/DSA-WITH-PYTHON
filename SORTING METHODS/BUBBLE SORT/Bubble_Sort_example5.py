# You are analyzing a football team's performance. The players scored the following number of goals this season: [12, 5, 20, 7, 15, 3, 9].
# Your task: 1.Use bubble sort to sort the list in ascending order, 2.While sorting, also count how many swaps were made in total, 3.Return both the sorted list and and the swap count

class Bubble_Sort:

    def bubble_sort(self, lst):
        self.lst = lst
        size = len(lst)

        for i in range(size):
            swapped = False
            for j in range(size - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    swapped = True
                    
            if not swapped:
                break
        return lst
    
BBS = Bubble_Sort()
print(BBS.bubble_sort([12, 5, 20, 7, 15, 3, 9]))
