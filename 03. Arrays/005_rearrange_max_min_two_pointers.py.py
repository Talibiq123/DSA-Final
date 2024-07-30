# Rearrange an array in maximum minimum form using Two Pointer Technique
def rearrange_min_max(nums):
    n = len(nums)
    ans = [0] * n
    left = 0
    right = n-1
    for i in range(n):
        if i % 2 == 0:
            ans[i] = nums[right]
            right -= 1
        else: 
            ans[i] = nums[left]
            left += 1
    
    return ans
            

arr = [1, 2, 3, 4, 5, 6, 7]
result = rearrange_min_max(arr)
print(result)
