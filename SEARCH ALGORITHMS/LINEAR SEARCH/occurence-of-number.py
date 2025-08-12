# Create a program to find the occurrence of a given number in a list

def count_occurrence(lst, n):

    count = 0

    for element in lst:
        if element == n:
            count +=1

    return count

lst = [2, 8, 13, 6, 6, 9, 7, 6, 6]
n = int(input("Enter the target number to find the number of occurrence: "))

print(count_occurrence(lst, n))
