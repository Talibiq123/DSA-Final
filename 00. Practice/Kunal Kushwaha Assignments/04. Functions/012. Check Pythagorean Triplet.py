def is_pythagorean_triplet(a, b, c):
    x, y, z = sorted([a, b, c])

    return x ** 2 + y ** 2 == z ** 2


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if is_pythagorean_triplet(a, b, c):
    print(f"The triplet ({a}, {b}, {c}) is a Pythagorean triplet.")
else:
    print(f"The triplet ({a}, {b}, {c}) is not a Pythagorean triplet.")
