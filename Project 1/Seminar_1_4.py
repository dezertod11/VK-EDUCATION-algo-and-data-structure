def pppp(arr):
    pointer1 = 0
    pointer2 = 1

    while pointer2 < len(arr):
        if arr[pointer2] % 2 == 0:
            arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
            pointer1 += 1

        pointer2 += 1
    return arr


arr = [1,2,3,4,5,6,0,0]
pppp(arr)
# moved_null = move_even_to_front(arr)
# print(moved_null)