total_sum = 0

while True:
    number = int(input("Enter an integer (0 to stop): "))

    if number == 0:
        break

    total_sum += number

print(f"The sum of all entered numbers is: {total_sum}")
