def remove_same_char(s):
    s = list(s)
    if len(s) < 2:
        return s
    l = 1
    while l < len(s):
        if s[l - 1] == s[l]:
            s.pop(l)
            s.pop(l - 1)
            l = 1
            continue
        l += 1


    return s



