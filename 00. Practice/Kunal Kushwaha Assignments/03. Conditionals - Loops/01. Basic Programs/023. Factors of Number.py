def find_factors(n):
    factors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list


number = int(input("Enter an integer: "))
factors = find_factors(number)
print(f"The factors of {number} : {factors}")
