# Sort as simple list of integers in ascending order using Quick Sort:  nums = [8, 3, 1, 7, 0, 10, 2]

def quick_sort(nums):

    lenght = len(nums)

    if lenght <= 1:
        return nums
    
    else:
        pivot = nums.pop()

    left = []
    right = []

    for element in nums:

        if element < pivot:
            left.append(element)
        
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [8, 3, 1, 7, 0, 10, 2]
print(f"Original List: {nums}")

print(f"Sorted List: {quick_sort(nums)}")
