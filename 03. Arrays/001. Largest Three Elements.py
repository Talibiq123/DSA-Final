def find_three_largest(arr):
    if len(arr) < 3:
        return "Array should have at least three distinct elements"

    first, second, third = float('-inf'), float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != first and num != second:
            third = num

    if third == float('-inf'):
        return "Array does not have three distinct elements"

    return first, second, third

arr = [10, 4, 3, 50, 23, 90]
print(find_three_largest(arr))
