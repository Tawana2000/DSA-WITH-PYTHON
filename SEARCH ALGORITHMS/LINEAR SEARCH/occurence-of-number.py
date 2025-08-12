# Create a program to find the occurrence of a given number in a list

def count_occurrence(lst, n):

    count = 0

    for element in lst:
        if element == n:
            count +=1

    return count
