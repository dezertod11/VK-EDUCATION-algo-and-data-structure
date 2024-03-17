def merge_sorted_arrays(arr):
    pointer1 = 0
    pointer2 = 1

    while pointer2 < len(arr):
        if arr[pointer2] % 2 == 0:
            arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
            pointer1 += 1

        pointer2 += 1
    return arr

arr = [1,2,3,4,5,6,0,0]
merged_array = merge_sorted_arrays(arr)
print(merged_array)