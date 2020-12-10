'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''



# For the purpose of this problem, we will return 0 when needle is an empty string.
# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: kmp 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        nxt = self.built(needle)
        j = 0
        for i in range(m):
            while j > 0 and needle[j] != haystack[i]:
                j = nxt[j]
            if needle[j] == haystack[i]:
                j += 1
            if j == n:
                return i - n  + 1
        return -1
        
        
    def built(self, p):
        nxt = [0, 0]
        j = 0
        for i in range(1, len(p)):
            while j > 0 and p[i] != p[j]:
                j = nxt[j]
            if p[i] == p[j]:
                j += 1
            nxt.append(j)
        return nxt








#brute force, time complexity O(nm) n: len(haystack), n: len(needle)
class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0     #題目規定的
        for i in range(len(haystack) - len(needle)+1): # range 數到stop前一個
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

        '''
        Input: haystack = "hello", needle = "ll"
        Output: 2

        '''

#自己想的, naive solution, time complexity O(n*m), space complexity O(1)
#思路: n: len(haystack), m: len(needle)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)