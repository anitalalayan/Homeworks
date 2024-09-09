class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, value):
        self.__product_id = value

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, name):
        self.__product_name = name

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def set_quantity_in_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity in stock cannot be negative.")
        self.__quantity_in_stock = quantity


    def add_stock(self, amount):
        if amount < 0:
            raise ValueError("Cannot add a negative number")
        self.__quantity_in_stock += amount

    def reduce_stock(self, amount):
        if amount < 0:
            raise ValueError("Cannot reduce the quantity by a negative number")
        if amount > self.__quantity_in_stock:
            raise ValueError("Invalid amount, exceeds the available quantity")
        self.__quantity_in_stock -= amount




product = Product(25, "Iphone15", 34)

product.add_stock(20)

print(f"Product in stock after addition: {product.get_quantity_in_stock()}")

product.reduce_stock(11)

print(f"Product in stock after reduction : {product.get_quantity_in_stock()}")

product.set_product_name("Smartphone")

print(f"Product name: {product.get_product_name()}")
