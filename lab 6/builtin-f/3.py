def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

print(isPalindrome('heeh'))
print(isPalindrome('hello'))