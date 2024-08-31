def main():
    num1 = int(input("Enter 1st Number : "))
    num2 = int(input("Enter 2nd Number : "))
    if num1 == num2:
        print(f"Both Numbers {num1} and {num2} are equal.")
    elif num1 > num2:
        print(f"{num1} is Largest between {num1} and {num2}")
    else:
        print(f"{num2} is Largest between {num1} and {num2}")


if __name__ == "__main__":
    main()
