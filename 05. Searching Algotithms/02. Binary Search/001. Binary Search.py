def binary_search(nums, key):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high - low) // 2

        if key == nums[mid]:
            return mid
        elif key < nums[mid]:
            high = mid -1
        elif key > nums[mid]:
            low = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
ans = binary_search(arr, target)
if ans == -1:
    print("number is not found...")
else:
    print(ans)
