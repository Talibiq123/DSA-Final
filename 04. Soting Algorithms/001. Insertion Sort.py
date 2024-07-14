# Program to sort an array using Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        
    return arr


arr = [5, 2, 4, 6, 1, 3]
sorted_arr = insertion_sort(arr)
print('Array after sorting: ', sorted_arr)
