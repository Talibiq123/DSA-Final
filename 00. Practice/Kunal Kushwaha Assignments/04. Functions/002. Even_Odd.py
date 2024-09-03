def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


try:
    number = int(input("Enter a number: "))

    result = check_even_odd(number)
    print(f"The number {number} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
