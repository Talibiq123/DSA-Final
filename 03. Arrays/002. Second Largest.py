def second_largest(arr):
    if len(arr) < 2:
        return False

    largest, secondLargest = float("-inf"), float("-inf")
    for num  in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif largest > num > secondLargest:
            secondLargest = num
            
    if secondLargest == float("-inf"):
        return False
    else:        
        return secondLargest

arr = [12, 35, 1, 10, 34, 1]
ans = second_largest(arr)

if ans is False:
    print("Sorry! can't find. There is only one element in array.")
else:
    print(f"Second largest Element in the Array: {ans}")
