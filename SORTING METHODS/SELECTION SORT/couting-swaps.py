# Write a program to count the numbers of swaps made during the selection sort process

def count_swaps(lst):

    swaps = 0

    for i in range(len(lst)):
        min = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        if lst[i] != lst[min]:
            lst[i], lst[min] = lst[min], lst[i]

            swaps += 1

    return swaps

lst = list(map(int, input().split()))
print(count_swaps(lst))
