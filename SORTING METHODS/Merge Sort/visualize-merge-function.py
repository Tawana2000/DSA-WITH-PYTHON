# The merge() function takes two sorted lists and merges them into one sorted list.

def merge(left, right):
    output = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1

        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

print(merge([4, 5], [2, 3, 7, 9])) 
