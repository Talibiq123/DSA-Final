def largest_three_elements(nums):
    n = len(nums)

    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num

    return first, second, third


arr = [10, 4, 3, 50, 23, 90]
ans = largest_three_elements(arr)
print(ans)
