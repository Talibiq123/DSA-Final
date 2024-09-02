principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the annual interest rate (in %): "))

n = int(input("Enter the number of times interest is compounded per year: "))

time = float(input("Enter the time the money is invested for (in years): "))

rate = rate / 100

amount = principal * (1 + rate/n) ** (n*time)
compound_interest = amount - principal

print(f"The compound interest is: {compound_interest:.2f}")
print(f"The total amount after interest is: {amount:.2f}")
