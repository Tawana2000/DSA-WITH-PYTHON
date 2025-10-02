# You are a teacher grading a math quiz. The students got these scores:
#[72, 88, 95, 43, 67, 81, 59, 100, 76]
#Your task: 1.Use bubble sort to sort the scores in ascending order, 2.While sorting, track both: a.the total number of comparisons, b.The total number of swaps
#3. Return the sorted list, comparisons, and swaps

class BubbleSort:

    def math_scores(self, scores):

        self.scores = scores
        size = len(scores)
        comparisons = 0
        swaps = 0

        for i in range(size):
            swapped = False
            for j in range(size - 1 - i):
                comparisons += 1
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
                    swapped = True
                    swaps += 1

            if not swapped:
                break

        return scores, comparisons, swaps
    
BBS = BubbleSort()
print(BBS.math_scores([72, 88, 95, 43, 67, 81, 59, 100, 76]))
