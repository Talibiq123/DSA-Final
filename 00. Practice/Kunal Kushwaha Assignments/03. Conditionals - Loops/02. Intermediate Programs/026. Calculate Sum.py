def calculate_sums(numbers_list):
    sum_of_negatives = 0
    sum_of_positive_evens = 0
    sum_of_positive_odds = 0

    for num in numbers_list:
        if num < 0:
            sum_of_negatives += num
        elif num > 0:
            if num % 2 == 0:
                sum_of_positive_evens += num
            else:
                sum_of_positive_odds += num

    return sum_of_negatives, sum_of_positive_evens, sum_of_positive_odds


user_numbers = []

print("Enter numbers (0 to terminate):")

while True:
    try:
        input_number = int(input())
        if input_number == 0:
            break
        user_numbers.append(input_number)
    except ValueError:
        print("Please enter a valid integer.")

negatives_sum, positive_evens_sum, positive_odds_sum = calculate_sums(user_numbers)

print(f"Sum of negative numbers: {negatives_sum}")
print(f"Sum of positive even numbers: {positive_evens_sum}")
print(f"Sum of positive odd numbers: {positive_odds_sum}")
