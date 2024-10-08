class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def celsius(self):
        return self.__temperature

    @celsius.setter
    def celsius(self, value):
        self.__temperature = value

    @property
    def fahrenheit(self):
        return (self.__temperature * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__temperature = value


temp1 = Temperature(27)
temp1.fahrenheit = 45
print(temp1.fahrenheit)
