def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

conversion_functions = {
    ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
    ('celsius', 'kelvin'): celsius_to_kelvin,
    ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
    ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
    ('kelvin', 'celsius'): kelvin_to_celsius,
    ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit,
}

def convert_temperature(value, from_unit, to_unit):
    return conversion_functions.get((from_unit, to_unit))(value)

value = float(input("Enter the temperature value: "))
from_unit = input("Enter the unit of the temperature you are converting from (celsius, fahrenheit, kelvin): ").strip().lower()
to_unit = input("Enter the unit of the temperature you want to convert to (celsius, fahrenheit, kelvin): ").strip().lower()

converted_value = convert_temperature(value, from_unit, to_unit)
print(f"{value} {from_unit} is {converted_value} {to_unit}>")

