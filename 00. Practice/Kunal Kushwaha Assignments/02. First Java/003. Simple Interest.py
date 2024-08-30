def main():
    principle = int(input("Enter Principle Amount : "))
    time = int(input("Enter Time Durataion : "))
    rate = int(input("Enter Interest Rate : "))

    simple_interest = (principle * time * rate) / 100
    print(f"Simple Interest is {simple_interest}.")

if __name__ == "__main__":
    main()

