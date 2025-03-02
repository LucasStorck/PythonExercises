import math

radius = float(input("What is the radius of the circle?: "))

def calculator():
    return math.pi * radius ** 2
print(f"The area of circle is: {calculator()}" )
