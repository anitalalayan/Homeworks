def display_product_details(**product_details):
    if not product_details:
        print("No product details provided.")
        return
    else: 
        print(product_details)


product = {
    'name': 'Laptop',
    'price': 999.99,
    'quantity': 10,
    'brand': 'Lenovo',
    'warranty': '2 years'
    }

display_product_details(**product)

