#from dataclasses import dataclass

#@dataclass(frozen=True)
class Fraction:
    def __init__(self, numerator:int, denominator:int):

        if denominator == 0:
            raise ZeroDivisionError

        def gcd(a, b):
            while b != 0:
                if a > b:
                    a -= b
                else:
                    b -= a
            return a

        divisor = gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __str__(self)->str:
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self)->str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def custom_validator(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Operand must be of type int or Fraction")
        if isinstance(other, int):
            other = Fraction(other, 1)
        return other


    def __add__(self, other)->'Fraction':
        other = self.custom_validator(other)
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other)->'Fraction':
        other = self.custom_validator(other)
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other)->'Fraction':
        other = self.custom_validator(other)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other)->'Fraction':
        other = self.custom_validator(other)
        if other.denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other)->bool:
        if self.custom_validator(other):
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            return False

    def __ne__(self, other)->bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        other = self.custom_validator(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other) -> bool:
        other = self.custom_validator(other)
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other) -> bool:
        other = self.custom_validator(other)
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other) -> bool:
        other = self.custom_validator(other)
        return self.__gt__(other) or self.__eq__(other)


    def __hash__(self)->int:
        return hash((self.numerator, self.denominator))

    def __float__(self)->float:
        return self.numerator / self.denominator

    def __int__(self)->int:
        return self.numerator // self.denominator

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def mixed_num(self)->str:
        whole = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        if remainder == 0:
            return str(whole)

        return f"{whole} {remainder}/{self.denominator}"

    def __iadd__(self, other):
        other = self.custom_validator(other)
        result = self + other  # __add__
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __isub__(self, other):
        other = self.custom_validator(other)
        result = self - other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self



if __name__ == "__main__":

    fraction1 =  Fraction(48, 64)
    fraction2 = Fraction(12, 23)

    print(fraction1)
    print(fraction2)
    print(fraction1 + fraction2)
    print(fraction1 - fraction2)
    print(fraction1 * fraction2)
    print(fraction1 / fraction2)
    mixed = fraction1.mixed_num()
    print(mixed)
    fraction1 += fraction2
    print(fraction1)

    print(fraction1 >= fraction2)
