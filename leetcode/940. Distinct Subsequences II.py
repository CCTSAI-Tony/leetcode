'''
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用dp, None: 1, a: 1*2, ab: 2*2 => return - 1, => ab: 2*2 - 1 = 3: a, b, ab, if aa: 2 * 2 - dp[None] - 1 = 2 => a, aa
class Solution(object):
    def distinctSubseqII(self, S):
        dp = [1] # 這是關鍵
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last: # 減掉重複的
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % (10**9 + 7)


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(dp[-1] * 2)
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i
        return (dp[-1] - 1) % (10 ** 9 + 7)


