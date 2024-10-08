class RangeDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}.")
        instance.__value = value

    def __get__(self, instance, owner):
        return instance.__value


class Product:
    price = RangeDescriptor(min_value=1, max_value=100)


product = Product()
product.price = 110
print(product.price)
