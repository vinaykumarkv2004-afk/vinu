 #sample dictionary
products = {"Laptop": 500,"Mobile": 400,"Headphone": 100,"TV": 600}

print("Original dictionary:", products)

# 1) sort by price (ascending)
sorted_by_price = dict(sorted(products.items(), key=lambda item: item[1]))
print("Sorted by price:", sorted_by_price)

# 2) sort by product name (alphabetical order)
sorted_by_name = dict(sorted(products.items(), key=lambda item: item[0]))
print("Sorted by name:", sorted_by_name)