def is_palindrome_number(num):
    str_num = str(num)

    return str_num == str_num[::-1]


number = 12321
if is_palindrome_number(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
