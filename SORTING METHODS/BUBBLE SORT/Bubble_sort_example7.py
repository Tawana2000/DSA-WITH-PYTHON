# You have a list of students and their scores
"""
students = [
    ["Alice", 72],
    ["Bob", 88],
    ["Charlie", 95],
    ["David", 43],
    ["Eva", 67],
    ["Frank", 81],
    ["Grace", 59],
    ["Helen", 100],
    ["Ian", 76]
]
"""
#The task is to:
#1.Use bubble sort to sort this list by score (the second element in each sublist) in ascending order.
#2. Keep track of both comparisons and swaps
#3. Return the sorted students list, the total comparisons, and the total swaps


class BubbleSort:

    def scores_list(self, students):
        self.students = students
        size = len(students)
        comparisons = 0
        swaps = 0

        for i in range(size):
            swapped = False
            for j in range(size - 1 - i):
                comparisons += 1
                if students[j][1] > students[j + 1][1]:
                    students[j], students[j + 1] = students[j + 1], students[j]
                    swapped = True
                    swaps += 1
                
            if not swapped:
                break

        return students, comparisons, swaps

BBS = BubbleSort()
print(BBS.scores_list(students))
