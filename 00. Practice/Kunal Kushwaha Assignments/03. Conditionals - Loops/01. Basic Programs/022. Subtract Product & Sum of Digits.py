def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product


def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


number = int(input("Enter an integer: "))

product = product_of_digits(number)
total_sum = sum_of_digits(number)

result = product - total_sum

print(f"The result is: {result}")
