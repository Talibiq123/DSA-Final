def calculate_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


def calculate_lcm(x, y):
    return abs(x * y) // calculate_hcf(x, y)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = calculate_lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is: {lcm}")
