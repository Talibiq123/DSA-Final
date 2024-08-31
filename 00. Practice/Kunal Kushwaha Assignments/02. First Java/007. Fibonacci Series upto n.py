def fibonacci_series(n):
    fib_series = [1, 1]

    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    print(", ".join(map(str, fib_series)))

def main():
    n = int(input("Enter the number of terms: "))
    fibonacci_series(n)

if __name__ == "__main__":
    main()
