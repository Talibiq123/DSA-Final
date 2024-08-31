largest_number = None

while True:
    number = int(input("Enter an integer (0 to stop): "))

    if number == 0:
        break

    if largest_number is None or number > largest_number:
        largest_number = number

if largest_number is not None:
    print(f"The largest number entered is: {largest_number}")
else:
    print("No numbers were entered.")
