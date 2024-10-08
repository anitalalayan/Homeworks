class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int,float)) or width < 0:
            raise ValueError('width must be a positive integer or a float')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int,float)) or height < 0:
            raise ValueError('height must be a positive integer or a float')
        self.__height = height


    @property
    def area(self):
        return self.__width * self.__height



    @property
    def perimeter(self):
        perimeter = 2 * (self.__width + self.__height)
        return perimeter



rect = Rectangle(5, 5)

print(rect.area)

rect.width = 100
rect.height = 11
print(rect.area)

print(rect.perimeter)
