# You are given a list of students exam scores, sort the scores in ascending order using Merge Sort
# Use recursion, scores = [72, 88, 64, 90, 55, 81]

def merge_sort(scores):

    if len(scores) <= 1:
        return scores
    
    mid = len(scores) // 2

    left_partition = merge_sort(scores[: mid])
    right_partition = merge_sort(scores[mid :])

    return merge(left_partition, right_partition)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

scores = [72, 88, 64, 90, 55, 81]
print(f"Unsorted Scores: {scores}")


print(f"Sorted Scores = {merge_sort(scores)}")
