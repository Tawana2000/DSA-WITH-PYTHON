# Write a function to perform linear search

def linear_search(lst, target):

    for index, element in enumerate(lst):
        if element == target:
            return index
        
    return None

lst = [1, 4, 5, 12, 3, 50, 21, 16, 23, 7]
target = int(input())

result = linear_search(lst, target)

if result:
    print(f"Index of the target value: {result}")
else:
    print("Target value not found in the list.")
