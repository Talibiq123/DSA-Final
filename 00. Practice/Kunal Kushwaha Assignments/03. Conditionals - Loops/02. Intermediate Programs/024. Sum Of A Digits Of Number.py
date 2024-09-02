def sum_of_digits(number):
    number = abs(number)
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum


num = int(input("Enter a number to calculate the sum of its digits: "))

result = sum_of_digits(num)

print(f"The sum of the digits of {num} is: {result}")
