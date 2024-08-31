def area_of_parallelogram(b, h):
    return b * h


base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = area_of_parallelogram(base, height)

print(f"The area of the parallelogram is {area:.2f}")
