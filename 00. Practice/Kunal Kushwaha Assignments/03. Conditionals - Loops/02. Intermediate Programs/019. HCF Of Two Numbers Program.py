def calculate_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = calculate_hcf(num1, num2)

print(f"The HCF (GCD) of {num1} and {num2} is: {hcf}")
