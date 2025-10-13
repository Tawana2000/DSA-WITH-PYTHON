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
                
            print(f"  Step {j + 1}: {products}")
            
        if not swapped:
            break

    return products


products = [
    ("Laptop", 1200),
    ("Phone", 800),
    ("Tablet", 600),
    ("Monitor", 300),
    ("Mouse", 50)
]

print("\n Sorted Products:")
sorted_products = bubble_sort_products(products)
for name, price in sorted_products:
    print(f"{name} - ${price}")
