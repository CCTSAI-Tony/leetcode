class Solution:
    def isPalindrome(self, x):
    if x < 0:
        return False
    fow, rev = x, 0
    while fow:
        rev = rev * 10 + fow % 10
        fow //= 10
    return rev == x #true or flase

