def calculate_future_value(principal_amount, annual_rate, compounding_frequency_per_year, investment_duration_years):
    rate_decimal = annual_rate / 100
    future_value = principal_amount * (1 + rate_decimal / compounding_frequency_per_year) ** (compounding_frequency_per_year * investment_duration_years)
    return future_value


principal_amount = float(input("Enter the principal amount (initial investment): "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
compounding_frequency_per_year = int(input("Enter the number of times interest is compounded per year: "))
investment_duration_years = float(input("Enter the number of years the money is invested for: "))

future_investment_value = calculate_future_value(principal_amount, annual_rate, compounding_frequency_per_year, investment_duration_years)

print(f"The future value of the investment is: {future_investment_value:.2f}")
