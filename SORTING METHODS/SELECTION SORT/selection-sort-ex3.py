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

class Selection_Sort:

    def store_products(self, products):

        for i in range(len(products)):
            min_max = i

            for j in range(i + 1, len(products)):
                if products[j][1] < products[min_max][1]:
                    min_max = j

            products[i], products[min_max] = products[min_max], products[i]

        print("Sorted products (cheapest to most expensive): ")
        for name, price in products:
            print(f"{name}: ${price}")

        print("\nCheapest product:", products[0][0], "-", products[0][1])
        print("\nMost expensive product:", products[-1][0], "-", products[-1][1])

        return products

products = [
    ["Keyboard", 49],
    ["Monitor", 120],
    ["Mouse", 25],
    ["Laptop", 899],
    ["Headphones", 59],
    ["USB Cable", 9]
]  

SS = Selection_Sort()
SS.store_products(products)
