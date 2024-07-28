# Rearrange array such that even positioned are greater than odd.
def rearrange_even_odd(nums):
    for i in range(0, len(nums)):
        if i % 2 == 0:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        else:
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                
    return nums

arr = [1, 2, 2, 1]
ans = rearrange_even_odd(arr)
print(ans)
