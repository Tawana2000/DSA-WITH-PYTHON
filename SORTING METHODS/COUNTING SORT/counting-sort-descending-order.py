# Write a counting sort program to sort a list in descending order

def counting_sort(lst):

    if not lst:
        return lst
        
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)
    
    for num in lst:
        counting_list[num] += 1

    sorted_output = []

    for index in range(len(counting_list) -1, -1, -1):
        sorted_output.extend([index] * counting_list[index])

    return sorted_output
