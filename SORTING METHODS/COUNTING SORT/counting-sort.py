def counting_sort(lst):

    if len(lst) <= 1:
        return lst
    
    max_element = max(lst)     #Find the largest element
    counting_list = [0] * (max_element + 1)      #Create the counting list and set all the values to 0

    for num in lst:
        counting_list[num] += 1   #Fill the counting list with frequency of each number

    sorted_output = []
    for index, value in enumerate(counting_list):
        sorted_output.extend([index] * value)

    return sorted_output
