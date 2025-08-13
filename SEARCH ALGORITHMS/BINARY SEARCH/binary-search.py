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

lst = [4, 5, 9, 12, 55, 79, 88, 99]
target = int(input("Enter the target element: "))
result = binary_search(lst, target)

if result:
    print(f"Element {target} is found at index {result}")
else:
    print(f"Element {target} wasn't found in the list {lst}")
