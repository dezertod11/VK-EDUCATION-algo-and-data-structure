from queue import Queue

def is_subsequence_queue(a, b):
    q = Queue()
    for elem in a:
        q.put(elem)
    tpm = q.get()
    try:
        for elem in b:
            if tpm == elem:
                tpm = q.get_nowait()
    except:
        return True

    return False

def is_subsequence_pointer(a, b):
    l_a, r_a = 0, len(a) - 1
    l_b, r_b = 0, len(b) - 1
    while l_a <= r_a and l_b <= r_b:
        if a[l_a] == b[l_b]:
            l_a += 1
        l_b += 1
    return (l_a == r_a + 1)


a = list("aaa")
b = list("ababaas")

print(is_subsequence_queue(a,b))
print(is_subsequence_pointer(a,b))