def is_palindrome_stack(s):
    stack = list(s)
    for char in s:
        if char != stack.pop():
            return False
    return True

def is_palindrome_pointer(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


s1 = "abcdefg"
ss = "sasha ahsas"
sos = "sosos"

print(is_palindrome_stack(s1),is_palindrome_stack(ss),is_palindrome_stack(sos))
print(is_palindrome_pointer(s1),is_palindrome_pointer(ss),is_palindrome_pointer(sos))