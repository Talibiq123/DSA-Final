def find_largest_and_smallest(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    if (a <= b) and (a <= c):
        smallest = a
    elif (b <= a) and (b <= c):
        smallest = b
    else:
        smallest = c

    return largest, smallest


x = 10
y = 25
z = 15

largest_num, smallest_num = find_largest_and_smallest(x, y, z)
print(f"The largest number : {largest_num}")
print(f"The smallest number : {smallest_num}")
