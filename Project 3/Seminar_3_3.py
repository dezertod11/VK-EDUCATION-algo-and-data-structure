import math

def binary_searc_sqrt(target):
    l, r = 0, target
    while l < r - 1:
        middle = (l + r + 1) // 2
        if pow(middle,2) < target:
            l = middle
            continue
        if pow(middle,2) > target:
            r = middle
            continue
        return middle
    middle = (l + r) / 2
    if pow(middle,2) > target:
        return l
    return r

