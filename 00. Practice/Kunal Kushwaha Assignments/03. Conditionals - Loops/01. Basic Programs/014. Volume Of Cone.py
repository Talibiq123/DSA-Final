import math

radius = float(input("Enter the radius of the base of the cone: "))
height = float(input("Enter the height of the cone: "))

volume = (1/3) * math.pi * radius**2 * height

print(f"The volume of the cone is: {volume}")