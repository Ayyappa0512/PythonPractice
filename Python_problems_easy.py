# even or odd
import math


def even_odd(number):
    if(number == 1):
        return f"The given number {number} is Odd"
    elif(number%2 ==0):
        return f"The given number {number} is Even"
    else:
        return f"The given number {number} is Odd"
# print(even_odd(4))
# print(even_odd(1))
# print(even_odd(2))
# print(even_odd(7))

# Area of a Circle

def area_of_circle(radius):
    return math.pi*(radius**2)

print(f"Area of circle: {area_of_circle(5)}")