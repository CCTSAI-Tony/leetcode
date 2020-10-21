'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true
 

Constraints:

0 <= s.length <= 104
0 <= t.length <= 104
s and t consist of lower-case letters, upper-case letters and/or digits.
'''


#刷題用這個, time complexity: O(n), space complexity: O(n)
#思路: s, t 若遇到不match的letter => 可以選擇replace, or insert => 最後return s == t or s == t[:-1] cause (len(s) + 1 = len(t))
#選擇insert or replace => 都指望在 return s == t, 但遍歷s 沒有發現mismatch => 則指望 return s == t[:-1]
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        l1, l2 = len(s), len(t)
        if l1 > l2: # force s no longer than t
            return self.isOneEditDistance(t, s)
        if l2 - l1 > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                if l1 == l2:
                    s = s[:i]+t[i]+s[i+1:]  # replacement
                else:
                    s = s[:i]+t[i]+s[i:]  # insertion
                break
        return s == t or s == t[:-1]



#自己想的, time complexity O(len(s)^2), space complexity O(len(s))
#思路: naive 暴力解
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        if len(s) == len(t):
            mis_match = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    mis_match += 1
            return mis_match == 1
        
        if not s or not t:
            return True
        
        if len(s) < len(t):
            s, t = t, s
        
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            if self.check(new_s, t):
                return True
        return False
        
    def check(self, a, b):
        if a == b:
            return True
        return False



