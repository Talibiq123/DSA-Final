n = int(input("Enter the number of numbers you want to sum: "))

total_sum = 0

for i in range(n):
    number = float(input(f"Enter number {i+1}: "))
    total_sum += number

print(f"The sum of the entered numbers is: {total_sum}")
