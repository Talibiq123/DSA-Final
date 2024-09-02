original_price = float(input("Enter the original price of the product: "))

discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = (discount_percentage / 100) * original_price

final_price = original_price - discount_amount

print(f"Discount amount: {discount_amount}")
print(f"Final price after discount: {final_price}")
