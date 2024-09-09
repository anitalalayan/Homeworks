class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:  
            self.__age = age
        else:
            print("Age cannot be negative.")


person = Person("Mark", 30)

person.greet()  
print(f"Age: {person.get_age()}")

person.set_age(31)
print(f"Updated Age: {person.get_age()}")

person.set_age(-5)
