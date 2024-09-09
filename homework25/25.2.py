class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_price(self, price):
        if price < 10:
            raise ValueError("Price cannot be less than 10.")
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    

book = Book('1984', 'Orwell', 30)
print(book.get_title())
print(book.get_author())
print(book.get_price())

book.set_price(54)
print(book.get_price())

book.set_price(-45)
print(book.get_price())


