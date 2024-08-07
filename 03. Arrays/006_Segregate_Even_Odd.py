def segregate_even_odd(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


nums = [7, 2, 9, 4, 6, 1, 3, 8, 5]
ans = segregate_even_odd(nums)
print(ans)
