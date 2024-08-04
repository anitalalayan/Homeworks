def area_circle(radius):
    return 3.14159 * radius ** 2  

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

area_functions = {
    'circle': area_circle,
    'square': area_square,
    'rectangle': area_rectangle,
    'triangle': area_triangle
}

def calculate_area(shape, **kwargs):
    return area_functions.get(shape.lower())(**kwargs)

print(f"circle_area: {calculate_area('circle', radius=5)}")
print(f"square_area:{calculate_area('square', side=4)}")
print(f"rectangle_area: {calculate_area('rectangle', length=6, width=3)}")
print(f"triangle_area: {calculate_area('triangle', base=8, height=5)}")

