# You are managing a small store, and you have a list of products with their prices (in USD):
"""
products = [
    ["Keyboard", 49],
    ["Monitor", 120],
    ["Mouse", 25],
    ["Laptop", 899],
    ["Headphones", 59],
    ["USB Cable", 9]
]
"""
# Write a python program that: 1.Sorts the products in ascending order by price using Selection Sort logic, 2.Prints the cheapest and most expensive product names, 3.Displays the entire sorted product list (name, price)

class ProductSorter:

    def store_products(self, products):
        products = sorted(products, key=lambda x: x[1])

        print("Sorted products (cheapest to most expensive):")
        for name, price in products:
            print(f"{name}: ${price}")

        cheapest = products[0]
        most_expensive = products[-1]

        print("\nCheapest product:", cheapest[0], "-", cheapest[1])
        print("Most expensive product:", most_expensive[0], "-", most_expensive[1])

        return products, cheapest, most_expensive


products = [
    ["Keyboard", 49],
    ["Monitor", 120],
    ["Mouse", 25],
    ["Laptop", 899],
    ["Headphones", 59],
    ["USB Cable", 9]
]

sorter = ProductSorter()
sorter.store_products(products)
