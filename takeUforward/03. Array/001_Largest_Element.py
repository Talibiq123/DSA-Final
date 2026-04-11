nums = [3, 2, 1, 5, 4]
max_val = nums[0]

for i in range(1, len(nums)):
    if nums[i] > max_val:
        max_val = nums[i]

print(f"Max value in the array is {max_val}")
