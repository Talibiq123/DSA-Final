def main():
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    operator = input("Enter operator from (+, -, *, /) : ")

    if operator == "=":
        print(f"The sum of {num1} is {num1 + num2}.")
    elif operator == "-":
        print(f"The Difference of {num1} and {num2} is {num1 - num2}.")
    elif operator == "*":
        print(f"The Multiplication  of {num1} and {num2} is {num1 * num2}.")
    elif operator == "/":
        try:
            result = num1 / num2
            print(f"The Division of {num1} by {num2} is {result}.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
