#Linear Search with Strings

def linear_search_string(arr, target):
    for i in range(len(arr)):
        if arr[i].lower() == target.lower():  # Case-insensitive comparison
            return i
    return -1

names = ["Alice", "Bob", "Charlie", "David"]
target = "charlie"

result = linear_search_string(names, target)
print("Found at index:", result if result != -1 else "Not found")
