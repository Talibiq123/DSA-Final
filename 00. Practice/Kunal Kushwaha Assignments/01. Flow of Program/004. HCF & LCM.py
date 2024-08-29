import math

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

hcf = math.gcd(num1, num2)

lcm = num1 * num2 // hcf

print(f"HCF is {hcf}.")
print(f"LCM is {lcm}.")
