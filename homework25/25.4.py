class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            raise TypeErroe("Name must be a string and price must be a number")
        item = {'name': name, 'price': price}
        self.__items.append(item)

    def remove_item(self, name):
        for item in self.__items:
            if item['name'] == name:
                self.__items.remove(item)
                return
        print("Item not found")

    def display_total(self):
        total = len(self.__items)
        print(f"The total number of items is: {total}")




cart = ShoppingCart()
cart.add_item('Blush', 35)
cart.add_item('Lipstick', 26.53)
cart.add_item('Brow Gel', 15)

cart.display_total()

cart.remove_item('Blush')
cart.display_total()




