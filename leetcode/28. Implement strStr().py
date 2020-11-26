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