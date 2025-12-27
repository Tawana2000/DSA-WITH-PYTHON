# You are given a list of products, where each product is represented as: (name, price, rating)
"""
Sort the products using Quick Sort with these priorities
- Lower price first
- If prices are equal -> higher rating first
- If both price and rating are equal -> Alphabetical name order
"""

def quick_sort(products):

    if len(products) <= 1:
        return products
    
    else:
        pivot_product = products.pop()

    left_elements = []
    right_elements = []

    for items in products:
        if items[1] < pivot_product[1]:
            left_elements.append(items)

        elif items[1] == pivot_product[1] and items[2] > pivot_product[2]:
            left_elements.append(items)

        elif items[1] == pivot_product[1] and items[2] == pivot_product[2] and items[0] < pivot_product[0]:
            left_elements.append(items)

        else:
            right_elements.append(items)

    return quick_sort(left_elements) + [pivot_product] + quick_sort(right_elements)


products = [
    ("Laptop", 1200, 4.5),
    ("Phone", 800, 4.7),
    ("Tablet", 800, 4.2),
    ("Monitor", 300, 4.6),
    ("Mouse", 25, 4.3),
    ("Keyboard", 25, 4.8),
]

sorted_products = quick_sort(products)

for name, price, rating in sorted_products:
    print(f"{name}, {price}, {rating}")
