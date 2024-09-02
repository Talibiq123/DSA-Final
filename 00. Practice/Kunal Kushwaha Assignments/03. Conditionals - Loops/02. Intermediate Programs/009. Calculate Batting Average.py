total_runs = int(input("Enter the total runs scored: "))

times_out = int(input("Enter the number of times the player has been out: "))

if times_out == 0:
    print("The player has never been out, so the batting average cannot be calculated.")
else:
    batting_average = total_runs / times_out

    print(f"The batting average is: {batting_average:.2f}")
