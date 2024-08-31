def main():
    inr = float(input("Enter Amount in Indian Rupees: "))
    exchange_rate = 83.89
    usd = inr / exchange_rate
    print(f"{inr} rupees is approximately {usd:.2f} dollars.")


if __name__ == "__main__":
    main()
