class SalaryDescriptor:
    def __init__(self, max_salary):
        self.max_salary = max_salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be positive.")
        if value > self.max_salary:
            raise ValueError(f"Salary cannot exceed {self.max_salary}.")
        instance.__value = value

    def __get__(self, instance, owner):
        return instance.__value

class Employee:
    salary = SalaryDescriptor(max_salary=100000)




employee = Employee()
employee.salary = 150000
print(employee.salary)

