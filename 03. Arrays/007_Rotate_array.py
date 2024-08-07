def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


def rotate_array(arr, d):
    n = len(arr)
    d = d % n

    reverse(arr, 0, n-1)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)

    return arr


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_array = rotate_array(nums, k)
print(rotated_array)
