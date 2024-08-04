def area_circle(radius):
    pi = 3.141592653589793
    return pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height


area_calculators = {
    'circle': area_circle,
    'square': area_square,
    'rectangle': area_rectangle,
    'triangle': area_triangle
}

def calculate_area(shape, **kwargs):
    return area_calculators.get(shape.lower())(**kwargs)


print(calculate_area('circle', radius=5))        
print(calculate_area('square', side=4))         
print(calculate_area('rectangle', length=4, width=6))  
print(calculate_area('triangle', base=4, height=3))

