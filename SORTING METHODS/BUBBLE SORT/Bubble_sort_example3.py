#Imagine you are keeping track of the scores of 7 players in a video game [42, 17, 8, 99, 23, 56, 74], use bubble sort to arrange the scores in ascending order

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
print(BBS.bubble_sort([42, 17, 8, 99, 23, 56, 74]))
