#Create a program to find the number of unique elements in a list

 if len(lst) <= 1:
        return lst
    
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num] += 1

    unique_count = 0

    for value in counting_list:
        if value >= 1:
            unique_count += 1

    return unique_count

lst = list(map(int, input("Enter the list elements separated by a space: ").split()))
print(count_unique_elements(lst))
