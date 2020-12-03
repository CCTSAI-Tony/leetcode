# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.


#刷題用這個, time complexity O(n), space complexity O(n)
#思路: sliding window
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            distinct[s[r]] += 1
            while len(distinct) > 2:
                distinct[s[l]] -= 1
                if distinct[s[l]] == 0:
                    del distinct[s[l]]
                l += 1
        
            max_len = max(max_len, r - l + 1)
        return max_len