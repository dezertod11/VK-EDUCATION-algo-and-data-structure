def reverseArray(arr, left, right):
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
        left  += 1
        right -= 1

def solution(arr, k):
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, n - k - 1)
    reverseArray(arr, n - k, n - 1)



# arr = [1,2,3,4,5,6,7,8]
# k = 4
# solution(arr, k)
# print(arr)