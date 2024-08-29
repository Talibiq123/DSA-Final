def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    hcf = gcd(a, b)
    lcm_value = lcm(a, b)

    print(f"GCD of {a} and {b} is {hcf}")
    print(f"LCM of {a} and {b} is {lcm_value}")


if __name__ == "__main__":
    main()
