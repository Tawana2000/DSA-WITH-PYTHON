# Write a counting sort program to sort a list in descending order

def counting_sort(lst):

    if not lst:
        return lst
        
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)
