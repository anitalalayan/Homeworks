#Write a program that simulates a car dealership system. The program should have classes for cars, customers, and salespeople. Cars should have attributes such as make, model, and price. Customers should have attributes such as name and contact information. Salespeople should have attributes such as name and commission rate. The program should allow salespeople to manage car inventory, customers to search for and purchase cars, and salespeople to view their sales history. Use interfaces to implement classes for different types of cars (e.g., electric, hybrid) and abstract classes for sales operations.
from abc import ABC, abstractmethod


class Cars(ABC):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
   
    @abstractmethod   
    def get_info(self):
        ...
        
        
class Electric(Cars):
    def get_info(self):
        return f" Electric car details: {self.make}, {self.model}, {self.price}"
    
    
class Hybrid(Cars):
    def get_info(self):
        return f" Hybrid car details: {self.make}, {self.model}, {self.price}"
    
        
    
class Customers:
    def __init__(self, name, contact_info):
        self.name = name 
        self.contact_info = contact_info
        
    def search_cars(self, car: 'Cars', salesperson: 'Salespeople'):
        for car in salesperson.car_inventory:
            if car == self.car:
                return car 
            return "car is not found "

        
    
    def purchase_car(self, car:'Cars', salesperson:'Salespeople'):
        if car in salesperson.car_inventory:
            salesperson.sell_car(self, car)
        else:
            print("Car is not available in inventory.")
        
        
class Salesoperations(ABC):
    
    @abstractmethod
    def sell_car(self, customer: 'Customer', car: 'Car'):
        pass

    @abstractmethod
    def view_sales_history(self):
        pass     
        
class Salespeople(Salesoperations):
    def __init__(self, name, commission_rate):
        self.name = name
        self.comission_rate = commission_rate
        self.car_inventory = []
        self.sales_history = []
        
    def add_to_inventory(self, car: 'Cars'):
        self.car_inventory.append(car)
        
    def sell_car(self,customer:'Customers', car: 'Cars'):
        if car in self.car_inventory:
            print(f"{car.get_info()} sold to {customer.name}")

            self.car_inventory.remove(car)
            self.sales_history.append((customer.name, car.get_info()))
        else:
            print("car not found")
        
    def view_sales_history(self):
        return[str(car) for car in self.sales_history]
        
        
    
car1 = Electric("Tesla", "Model S", 50000)
car2 = Hybrid("Toyota", "Prius", 15000)
  
salesperson1 = Salespeople("John", 0.05)

salesperson1.add_to_inventory(car1)
salesperson1.add_to_inventory(car2)

customer1 = Customers("Alice", "alice@example.com")

customer1.purchase_car(car1, salesperson1)

print(salesperson1.view_sales_history())
