# def even_odd(in_num):
#     if in_num % 2 == 0:
#         return True
#     else:
#         return False


def main():
    num = int(input("Enter a Number : "))
    # ans = even_odd(num)
    # if ans:
    #     print(f"{num} is Even.")
    # else:
    #     print(f"{num} is Odd.")

    # or
    print(f"{num} is {'Even' if num % 2 == 0 else 'Odd'}.")


if __name__ == "__main__":
    main()
