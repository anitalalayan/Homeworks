class Person:
    def __init__(self, age):
        if not isinstance( age, int) or age < 1:
            raise ValueError("Age must be a positive integer")
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance( age, int) or age < 1:
            raise ValueError("Age must be a positive integer")
        self.__age = age



person = Person(25)
print(person.age)
person.age = 32
print(person.age)

person.age = 52
print(person.age)
