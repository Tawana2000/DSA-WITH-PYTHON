# Write a function to perform Binary Search using recursion

def binary_search(lst, target, low, high):

    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == target:
            return mid
        
        elif lst[mid] > target:
            return binary_search(lst, target, low, mid - 1)
        
        else:
            return binary_search(lst, target, mid + 1, high)
        
    else:
        return None

lst = sorted([12, 4, 8, 3, 2, 9, 11, 23, 5])
target = int(input("Enter the target number: "))
result = binary_search(lst, target, 0, len(lst) - 1)

if result:
    print(f"Element {target} is found at index {result}")
else:
    print(f"{target} is not found in the list.")
