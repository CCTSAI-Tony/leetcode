'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

# The idea is the following:

# d is an array that contains booleans

# d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

# Example:

# s = "leetcode"

# words = ["leet", "code"]

# d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

# d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

# The result is the last index of d.

#TIME COMPLEXITY O(n^2*m), n = len(s), m = len(wordDict), dp[i] => 對應 s[:i]
#思路: 利用線性dp, 與string 分割來解題, bottom up, 小心不要超過index range
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)  #dp[i] = s[:i]
        dp[0] = True #初始條件 s[:0] =True
        for i in range(len(s)):  #i 最大 = len(s) -1 
            for j in range(i + 1, len(s)+1): #s[i:j] 左閉右開, 因此這裡要 len(s)+1
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]





# a = [1,2,3]
# a[2:3]
# [3]
#自己重寫, time complexity O(n^2*m)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]



#自己重寫 time complexity O(n^2*m) => m: len(wordDict) 每個字節in n最多有m個children, space complexity O(n^2)
#思路: memo top down dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.dfs(s, wordDict, memo)
    
    def dfs(self, s, wordDict, memo):
        if not s:
            return True
        if s in memo:
            return memo[s]
        for word in wordDict:
            if s[:len(word)] == word:
                memo[s] = self.dfs(s[len(word):], wordDict, memo) #index split O(n)
                if memo[s]:
                    break
        if s not in memo:
            memo[s] = False
        return memo[s]



