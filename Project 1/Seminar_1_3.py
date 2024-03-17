def merge_sorted_arrays(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1 # конец заполненной части массива arr1
    pointer2 = len(arr2) - 1             # конец массива arr2
    pointer3 = len(arr1) - 1             # конец массива arr1 вместе с нулями

    while pointer2 >= 0:
        if pointer1 >= 0 and arr2[pointer2] >= arr1[pointer1]:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        else:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        pointer3 -= 1

    return arr1

arr1 = [1,2,3,4,5,6,0,0]
arr2 = [1,5]
merged_array = merge_sorted_arrays(arr1,arr2)
print(merged_array)