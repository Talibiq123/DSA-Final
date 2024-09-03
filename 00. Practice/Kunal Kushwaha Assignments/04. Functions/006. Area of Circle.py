import math


def calculate_circumference(radius):
    return 2 * math.pi * radius


def calculate_area(radius):
    return math.pi * (radius ** 2)


input_radius = float(input("Enter the radius of the circle: "))

circumference = calculate_circumference(input_radius)
area = calculate_area(input_radius)

print(f"The circumference of the circle with radius {input_radius} is {circumference:.2f}.")
print(f"The area of the circle with radius {input_radius} is {area:.2f}.")
