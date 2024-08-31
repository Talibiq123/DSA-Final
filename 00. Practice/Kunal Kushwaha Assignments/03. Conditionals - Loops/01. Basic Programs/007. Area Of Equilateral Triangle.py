import math

def area_of_equilateral_triangle(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2


side_length = float(input("Enter the length of a side of the equilateral triangle: "))

area = area_of_equilateral_triangle(side_length)
print(f"The area of the equilateral triangle is {area:.2f}")
