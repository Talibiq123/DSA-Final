nums = [1, 2, 4, 7, 7, 5]

second_largest = -1
largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] < largest and nums[i] > second_largest:
        second_largest = nums[i]

print("Second largest:", second_largest)
