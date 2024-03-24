def linear_search(arr, value):
    for elem in arr:
        if elem == arr[i]:
            return i
    return -1

def bin_search_recur(arr, l, r, target):
    if l > r:
        return -1
    middle = (l + r) // 2
    if arr[middle] > target:
        bin_search_recur(arr,l , middle - 1, target)


def bin_search(data, target):
    left, right = 0, len(data) - 1
    if target < data[left] or target > data[right]:
        return -1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] < target:
            left = middle + 1
        if data[middle] > target:
            right = middle - 1
        if data[middle] == target:
            return middle
    return -1

def left_bin_search(data, target):
    l = 0
    r = len(data) - 1

    while l + 1 < r:
        m = (l + r) // 2
        if data[m] < target:
            return -1


def copy_time(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)
    N = 10 # precision, accuracy
    eps = pow(10, -N)

    while l + eps < r:
        mid = (l + r) / 2
        if (int(mid/x) + int(mid/y)) < n - 1:
            l = mid
        else:
            r = mid

    return round(r + min(x, y), N - 1)






