def linear_search_product(product_list, target_product):
    indices = []
    
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Banana", "Grapes"]
target_product = "Banana"

result = linear_search_product(products, target_product)

if result:
    print(f"The target product '{target_product}' is found at indices: {result}")
else:
    print(f"The target product '{target_product}' is not found in the list.")
