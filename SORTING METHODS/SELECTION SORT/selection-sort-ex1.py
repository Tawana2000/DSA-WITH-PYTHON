# Write a program to sort the list items in descending order using selection sort

def selection_sort(lst):

    for i in range(len(lst)):
        max = i

        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max]:
                max = j

        lst[i], lst[max] = lst[max], lst[i]

    return lst

lst = list(map(int, input().split()))
print(selection_sort(lst))
