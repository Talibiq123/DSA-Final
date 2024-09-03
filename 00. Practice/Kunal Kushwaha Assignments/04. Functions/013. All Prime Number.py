def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def primes_between(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_list = primes_between(start, end)

print(f"Prime numbers between {start} and {end}: {prime_list}")
