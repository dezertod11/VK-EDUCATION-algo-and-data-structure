def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    return merged_array

arr1 = [1,2,3,4,5,6,7,8]
arr2 = [1,5,6,7,8,10]
merged_array = merge_sorted_arrays(arr1,arr2)
print(merged_array)