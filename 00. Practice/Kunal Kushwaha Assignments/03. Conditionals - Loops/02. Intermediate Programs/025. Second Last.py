def count_even_days_in_august():
    days_in_august = 31
    even_days_count = sum(1 for day in range(1, days_in_august + 1) if day % 2 == 0)
    return even_days_count


even_days = count_even_days_in_august()

print(f"Kunal can go out on {even_days} even days in August.")
