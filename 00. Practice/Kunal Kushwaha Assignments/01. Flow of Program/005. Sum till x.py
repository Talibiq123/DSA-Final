total_sum = 0

while True:
    user_input = input("Enter a number (or 'x' to stop): ")

    if user_input.lower() == 'x':
        break

    try:
        number = float(user_input)  # Convert input to a number (float to handle decimals)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'x' to stop.")

print(f"Sum of all numbers: {total_sum}")
