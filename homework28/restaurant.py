from abc import ABC, abstractmethod

class MenuItem:
    __slots__ = 'name', 'price', 'ingredients'

    def __init__(self, name:str, price:float, ingredients: list):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, Ingredients: [{', '.join(self.ingredients)}]"


class Appetizer(MenuItem):
    __slots__ = 'name', 'price', 'ingredients', 'serving_size'
    def __init__(self, name: str, price: float, ingredients: list, serving_size: str ):
        super().__init__(name, price, ingredients)
        self.serving_size = serving_size

    def __str__(self):
        return f"{super().__str__()}, Serving Size: {self.serving_size}"


class Entree(MenuItem):
    __slots__ = 'name', 'price', 'ingredients', 'dietary_info'
    def __init__(self, name: str, price:float, ingredients:list, dietary_info: str):
        super().__init__(name, price, ingredients)
        self.dietary_info = dietary_info

    def __str__(self):
        return f"{super().__str__()}, Dietary Info: {self.dietary_info}"


class Dessert(MenuItem):
    __slots__ = 'name', 'price', 'ingredients', 'dessert_type'
    def __init__(self, name: str, price: float, ingredients: list, dessert_type: str ):
        super().__init__(name, price, ingredients)
        self.dessert_type = dessert_type

    def __str__(self):
        return f"{super().__str__()}, Dessert type: {self.dessert_type}"


class Order(ABC):
    __slots__ = 'customer', 'menu_items', 'total_price'

    def __init__(self, customer: 'Customer'):
        self.customer = customer
        self.menu_items = []
        self.total_price = 0

    @abstractmethod
    def place_order(self, menu_item: MenuItem):
        ...

    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.menu_items)
        return self.total_price

    def __str__(self):
        item_details = [str(item) for item in self.menu_items]
        return (f"Order for {self.customer.name} (Contact: {self.customer.contact_info}): "
                f"[{', '.join(item_details)}], Total: ${self.calculate_total_price():.2f}")


class DineInOrder(Order):
    def __init__(self, customer: 'Customer'):
        super().__init__(customer)

    def place_order(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)
        self.customer.place_order(self)
        self.calculate_total_price()



class TakeawayOrder(Order):
    def __init__(self, customer: 'Customer'):
        super().__init__(customer)

    def place_order(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)
        self.customer.place_order(self)
        self.calculate_total_price()


class DeliveryOrder(Order):
    def __init__(self, customer: 'Customer'):
        super().__init__(customer)

    def place_order(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)
        self.customer.place_order(self)
        self.calculate_total_price()


class Customer:
    __slots__ = 'name', 'contact_info', 'order_history'
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def place_order(self, order: 'Order'):
        self.order_history.append(order)

    def get_order_history(self):
        return [str(order) for order in self.order_history]

    def display_review(self):
        rating = int(input("Enter your rating (1-10): "))
        comments = input("Enter your comments: ")
        review = Review(self.name, self.order_history[-1], rating, comments)
        review.display_review()


class Review:
    __slots__ = 'customer_name', 'order', 'rating', 'comments'

    def __init__(self, customer_name: str, order: Order, rating: float, comments: str):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments

    def display_review(self):
        print(f"Review by {self.customer_name}:  \nDetails: {self.order}")
        print(f"Rating: {self.rating}/10")
        print(f"Comment: {self.comments}")



customer1= Customer('Bill', '<billadams@gmail.com>')

appetizer = Appetizer('Rolls',10.5,['Vegetables','roll wrapper', 'shrimps'], '4 pieces')

dine_in_order = DineInOrder(customer1)
dine_in_order.place_order(appetizer)
print(customer1.get_order_history())

customer1.display_review()




