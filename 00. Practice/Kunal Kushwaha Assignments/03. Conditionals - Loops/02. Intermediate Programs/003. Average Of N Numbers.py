n = int(input("Enter the number of elements: "))

total_sum = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total_sum += num

average = total_sum / n

print(f"The average of the entered numbers is: {average}")
