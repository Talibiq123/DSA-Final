# Moving all zeroes to the end of the array
def moving_all_zeroes(nums):
    nonZeroIndex = 0
    
    for num in nums:
        if num != 0:
            nums[nonZeroIndex] = num
            nonZeroIndex += 1
    
    for i in range(nonZeroIndex, len(nums)):
        nums[i] = 0
    
    return nums

arr = [1, 2, 0, 4, 3, 0, 5, 0]
ans = moving_all_zeroes(arr)
print(ans)
