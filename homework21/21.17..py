def Celsius_to_Fahrenheit(x):
    return x * 9/5 + 32

def Celsius_to_Kelvin(y):
    return y + 273.15

def Fahrenheit_to_Celsius(z):
    return 5/9 * (z - 32)

def Fahrenheit_to_Kelvin(i):
    return 5/9 * (i -32) + 273.15

def Kelvin_to_Celsius(j):
    return j - 273.15

def Kelvin_to_Fahrenheit(k):
    return 9/5 * (k - 273.15) + 32


temperatures = {
        ('Celsius', 'Fahrenheit'): Celsius_to_Fahrenheit,
        ('Celsius', 'Kelvin'): Celsius_to_Kelvin,
        ('Fahrenheit', 'Celsius'): Fahrenheit_to_Celsius,
        ('Fahrenheit','Kelvin'): Fahrenheit_to_Kelvin,
        ('Kelvin', ' Celsius'): Kelvin_to_Celsius,
        ('Kelvin', 'Fahrenheit'): Kelvin_to_Fahrenheit
        }



def convert_temperature(value, from_unit, to_unit):
    return temperatures.get((from_unit, to_unit))(value)


value = float(input("Enter the temperature value: "))
from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ")
to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ")



converted_value = convert_temperature(value, from_unit, to_unit)
print(f"{value} {from_unit} is {converted_value} {to_unit}")


