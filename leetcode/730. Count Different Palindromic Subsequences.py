'''
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

 

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.
 

Constraints:

1 <= s.length <= 1000
s[i] is either 'a', 'b', 'c', or 'd'.
'''

# 刷題用這個, time complexity O(n^2), space complexity O(n^2)
# In DFS(start, end), for instance, for the letter 'a', I compute the number of palindromes that start and end with 'a' in the following way:
# First of all, I compute when 'a' appears first (index i) and last (index j) in the segment I am considering. Then it breaks down into two cases:
# If i == j. There is only one 'a' in the segment. So the answer is 1.
# If i != j. The possible palindromes are 'a', 'aa', and 'a*a' where '*' stands for any palindromes contained in S[i+1:j]. 
# The answer would be DFS(i+1,j) + 2. Since I want to avoid repetitive computation, I write cache(i+1,j) + 2 instead.
# The worst case time complexity is O(n^2). The best case time complexity is O(n).

from functools import lru_cache
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1000000007
        
        @lru_cache(maxsize=None)
        def compute(start: int, end: int) -> int:
            if start >= end:
                return 0
            count = 0
            for ch in "abcd":
                left, right = s.find(ch, start, end), s.rfind(ch, start, end)
                if left == -1 or right == -1:
                    continue
                count += 1 if left == right else 2 + compute(left + 1, right)
                
            return count % MOD
        
        return compute(0, len(s))

