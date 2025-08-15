# Create a program to perform operations on a list using various list methods.

"""
Perform these operations on the animals list:

- Add 'Raccoon' to the end of the animals list.
- Add all the elements from wild_animals to the end of the animals list.
- Remove the third element from the animals list using the pop() method.
- Remove the last element from the animals list using the pop() method.
- Insert 'Moose' at the third position in the animals list.
- Print the animals list.
"""

animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']
# perform list operations
animals.append('Raccoon')
animals.extend(wild_animals)
animals.pop(2)
