import math


def area_of_rhombus_diagonals(d1, d2):
    return 0.5 * d1 * d2


def area_of_rhombus_side_and_angle(a, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return a * a * math.sin(angle_radians)


print("Choose the method to calculate the area of the rhombus:")
print("1. Using diagonals")
print("2. Using side length and included angle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    dia1 = float(input("Enter the length of the first diagonal: "))
    dia2 = float(input("Enter the length of the second diagonal: "))
    area = area_of_rhombus_diagonals(dia1, dia2)
    print(f"The area of the rhombus is {area:.2f}")

elif choice == 2:
    side = float(input("Enter the length of one side of the rhombus: "))
    angle = float(input("Enter the included angle between the two sides (in degrees): "))
    area = area_of_rhombus_side_and_angle(side, angle)
    print(f"The area of the rhombus is {area:.2f}")

else:
    print("Invalid choice. Please select either 1 or 2.")
