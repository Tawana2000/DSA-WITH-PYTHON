# Write a function to perform binary search

def binary_search(lst, target):

    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if target == lst[mid]:
            return mid
        
        elif target <= lst[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return None
