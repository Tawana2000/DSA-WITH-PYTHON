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
    

input_list = [3, 7, 4, 12, 9, 0, 6, 2, 14, 5]
print(f"Unsorted List: {input_list}")

sorted_list = counting_sort(input_list)
print(f"Sorted List: {sorted_list}")
