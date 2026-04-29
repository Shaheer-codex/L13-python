import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference   

r = float(input("Enter the radius of the circle: "))
print("Circumference of the circle is", calculate_circumference(r))