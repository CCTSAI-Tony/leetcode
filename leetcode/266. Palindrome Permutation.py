'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

#自己想的, time complexity O(n)
#思路: check every letter frequency, if all occur even number of time => can form palindrom
#if appear > 1 letters occur odd number of time => can't form palindrom
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = Counter(s)
        odd = 0
        for v in dic.values():
            if v % 2:
                odd += 1
        return odd <= 1

# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_s = Counter(s)
        odd_count = 0
        for c in count_s:
            if count_s[c] % 2:
                odd_count += 1
        return True if odd_count < 2 else False