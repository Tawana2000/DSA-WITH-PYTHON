#Linear Search with Strings

def linear_search_string(arr, target):
    for i in range(len(arr)):
        if arr[i].lower() == target.lower():  # Case-insensitive comparison
            return i
    return -1
