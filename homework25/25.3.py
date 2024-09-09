class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []


    def add_grades(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.__grades.append(grade)

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)


    def display_info(self):
        return {
            'name': self.__name,
            'roll_number': self.__roll_number,
            'grades': self.__grades,
            'average_grade': self.calculate_average()
        }


student = Student("Alice", 12345)

student.add_grades(85)
student.add_grades(92)
student.add_grades(78)

info = student.display_info()
print(info)

try:
    student.add_grades(105)
except ValueError as e:
    print(e)


info = student.display_info()
print(info)
