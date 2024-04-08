import math
def area_circle(radius):
    return math.pi * radius ** 2
    
def volume_cylinder(diameter):
    r = diameter / 2
    circle = area_circle(r)
    volume = circle * 2
    return volume
