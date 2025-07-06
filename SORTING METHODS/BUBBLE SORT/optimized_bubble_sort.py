# Our bubble sort program carries out several unnecessary, redundant comparisons, we can avoid these redundant tasks and save time and resources by optimizing bubble sort

def bubble_sort(data):

    for i in range(len(data) - 1):    #Bubble sort places each element in its correct position, starting from the last postion and moving towards the start, when the correct element is placed at the second position, the correct element will be placed at the first position as well, therefore we can modify the outer loop to #len(data) - 1
        swapped = False        # To indicate that no swaps have taken place
        for j in range(len(data) - 1 - i):      #to avoid the inner loop making comparisons for the elements that already in their correct position placed by outer loop
            if data[j] > data[j + 1]:   #ascending order
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True    # If any elements is being swapped
        if not swapped:        # If swap remains false for the inner loop, it means no swap happened and the elements are already sorted and we can exit
            break
    return data

data_list = [4,6,99,45,0]
print(bubble_sort(data_list))
