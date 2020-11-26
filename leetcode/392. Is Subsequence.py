'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''


# Time complexity O(T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range (0, len(s)):    
            try:
                index = t.index(s[i])
            except ValueError: 
                return False

            t = t[index+1:]

        return True


# a = "earkuhalguewk"
# a.index("k") 回報第一個符合的index
# 3

# a = ""
# a.index("k")
# ValueError   

# What this code does is it looks for the index of a letter and if it can't find it, returns False. 
# The t = t[index+1:] part will start the search from the place where the last character was found added by one so it doesn't keep the last found character.


# dp法 自己想的
# Time complexity O(T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        dp = [False for _ in range(len(s))]       
        index = 0
        for i in range(len(t)):
            if index < len(s) and t[i] == s[index]:
                dp[index] = True
                index += 1      
        return dp[-1]





# binary search!
# Time complexity: O(T + SlogT)

import collections
import bisect
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for i in range(0, len(t)):
            d[t[i]].append(i)
        start = 0
        for c in s:
            idx = bisect.bisect_left(d[c], start)
            if len(d[c]) == 0 or idx >= len(d[c]):
                return False
            start = d[c][idx] + 1
        return True
















