def leap_year(year: int) -> None:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


user_input = int(input('Enter a leap year : '))
leap_year(user_input)
