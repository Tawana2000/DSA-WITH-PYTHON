# You are organizing a running competition. The finish times (in seconds) of 8 participants are stored in a list:
# [52, 47, 59, 45, 50, 49, 55, 48]
# Write a python function that: 1.Sorts the times in ascending order (fastest to slowest), 2.Prints the top3 fastest runners, 3.Prints the slowest runner's time 
# Use selection sort method

class Selection_Sort:

    def running_comp(self, lst):
        self.lst = lst

        for i in range(len(lst)):
            min_max = i

            for j in range(i + 1, len(lst)):
                if lst[j] > lst[min_max]:
                    min_max = j

            lst[i], lst[min_max] = lst[min_max], lst[i]

        return lst
    
lst = [52, 47, 59, 45, 50, 49, 55, 48]
SS = Selection_Sort()
print(SS.running_comp(lst))
