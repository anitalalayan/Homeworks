class Person:
    __slots__ = ('name', 'age', 'email')
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


    # def display(self):
    #     print(f"Personal details: {self.name}, {self.age}, {self.email} ")

    def __str__(self):
        return f"Personal details: {dict(name = self.name, age = self.age, email = self.email) }"



person1 = Person("John", 30, "<johndoe@gmail.com>")
print(person1)
print(person1.__dict__)
print(person1.__slots__)

# person1.lastname = "Doe"
print(person1)
