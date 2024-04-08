import math
def area_circle(radius):
    return math.pi * radius ** 2
    
def volume_cylinder(diameter, height):
    r = diameter / 2
    base = area_circle(r)
    return base * height
