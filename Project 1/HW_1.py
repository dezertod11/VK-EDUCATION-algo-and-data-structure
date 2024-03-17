def merge_sorted_arrays(arr):
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(arr):
        if arr[pointer2] == 0:
            arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
            pointer1 += 1

        pointer2 += 1
    return arr

def reverseArray(arr, left, right):
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
        left  += 1
        right -= 1

arr = [1,2,0,3,4,5,6,0]
merged_array = merge_sorted_arrays(arr)
reverseArray(arr, 0, len(arr) - 1)
print(merged_array)