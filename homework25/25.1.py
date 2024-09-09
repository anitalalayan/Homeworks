class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id


    def get_name(self):
        return self.__name 

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")

    
employee_1 = Employee(3, 'Bill', 200)

print(f"Employee ID: {employee_1.get_employee_id()}")  
print(f"Name: {employee_1.get_name()}") 
print(f"Salary: {employee_1.get_salary()}")  

employee_1.set_name('Ani')
print(f"Name: {employee_1.get_name()}")

employee_1.set_salary(-2222)

print(f"Salary: {employee_1.get_salary()}") 
