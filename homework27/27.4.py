class Descriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__score

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Score must be a number.")
        if not (0 <= value <= 100):
            raise ValueError("Score must be between 0 and 100.")

        instance.__score = value



class Student(Descriptor):

    score = Descriptor()
    def __init__(self, name):
        self.__name = name




student1 = Student('Helen')
student1.score = 52
print(student1.score)
