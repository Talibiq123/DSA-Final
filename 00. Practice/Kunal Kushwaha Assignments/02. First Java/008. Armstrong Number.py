def armstrong_number(n):
    num_str = str(n)
    power = len(num_str)

    power_sum = sum(pow(int(digit), power) for digit in num_str)

    if power_sum == n:
        print(f"{n} is an Armstrong Number.")
    else:
        print(f"{n} is not an Armstrong Number.")


def main():
    num = int(input("Enter a Number: "))
    armstrong_number(num)


if __name__ == "__main__":
    main()
