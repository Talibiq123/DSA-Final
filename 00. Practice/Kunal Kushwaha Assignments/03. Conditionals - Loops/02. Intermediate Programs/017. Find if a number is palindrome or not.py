def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


num = int(input("Enter a number to check if it's a palindrome: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
