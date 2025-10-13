#You have a list of products with their prices. Write a program using bubble sort to arrange the products in ascending order of their prices and show the list after each pass.

def bubble_sort_products(products):

    size = len(products)

    for i in range(size - 1):
        swapped = False
        print(f"\nPass {i + 1}:")

        for j in range(size - 1 - i):
            if products[j][1] > products[j + 1][1]:
                products[j], products[j + 1] = products[j + 1], products[j]
                swapped = True
                
            
        if not swapped:
            break

    return products
