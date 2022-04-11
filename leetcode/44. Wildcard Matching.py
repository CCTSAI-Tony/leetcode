'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

# What's the difference between this one and Regex Matching?

# The difference is that: the * in this problem can match any sequence independently, while the * in Regex Matching would only match duplicates, 
# if any, of the character prior to it.

# The demo test case isMatch("aa", "*") for this problem and isMatch("aa", "a*") 
# for Regex Matching problem could be the best effort to distinguish them for now. 
# isMatch("aab", "c*a*b") → false for this problem was a bit confusing to me in the beginning. 
# I think adding a test case such as isMatch("adcab", "*a*b") → true might be helpful.

https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
Python DP with illustration, time complexity O(len(s)*len(p))


# 刷題用這個
# time complexity O(len(s)*len(p))
# 思路: dp[i][j] 對 s[:i]p[:j], p[j-1] == "*"  可以當作s[i-1]=>dp[i-1][j] 也可以對應empty string => dp[i][j-1]
# dp[i][j] = dp[i-1][j-1] if s[i-1] == p[j-1] or p[j-1] == "?"
# 起始dp[0][0] = True, dp[0][j] = True, if p[:j] 都是"*"
# 可以簡化成 dp[i][j] = dp[i-1][j] or dp[i][j-1], ex: dp[i-1][j] => dp[i'][j] => dp[i'][j'] == dp[i-1][j-1]
class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':  #"*" 可以代表empty string
                break  #out of for loop
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}: #這邊也可以 (s[i-1], '?') or [s[i-1], '?']
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*': # * 可以當作當前比對leeter, 也可以比對多個字串, 也可以當作empty 
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]  #這裡是重點, 可以簡化成 dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]


#重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i][0] = True
            else:
                break
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
                elif p[i-1] in ["?", s[j-1]]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]


# 重寫第三次, time complexity O(mn), space complexity O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if not r:
                return not l
            if not l:
                return p[:r].count("*") == r
            memo[(l, r)] = False
            if p[r-1] == "*":
                memo[(l, r)] = dfs(l - 1, r) or dfs(l, r - 1) or dfs(l - 1, r - 1)
            elif p[r-1] == s[l-1] or p[r-1] == "?":
                memo[(l, r)] = dfs(l - 1, r - 1)
            return memo[(l, r)]
        return dfs(len(s), len(p))


# p[j-1] == '*', dp[i-1][j] 代表 s[:i-1] vs p[:j], 若dp[i-1][j]是True 代表 dp[i][j] 也是True, 因為"*"可以代表 any sequence of characters
# s[i-2] 後面的字 s[i-1] 可以被 "*" match, 所以dp[i][j] == s[:i] vs p[:j] 一樣是True

# p[j-1] == '*', dp[i][j-1] 代表 "*" 當作empty string

# p[j-1] == '*', dp[i-1][j-1] 代表 "*" 作為string 當前character

#另種想法
# Recurrence
# T[i][j] = T[i-1][j-1] if s[i] == p[j] or p[j] == '?'
# T[i][j] = T[i-1][j] || T[i][j-1] if p[j] == '*'
# T[i][j] = False

# time complexity O(len(s)*len(p))
# Another Top Down (Backwards) dfs memo, l, r => s[:l] , p[:r]
# 思路: 這題不是 backtracking 是 top down dp, 有興趣可以對照leetcode 10
# 與dp bottom up 相似, 唯一要注意就是memo, 與base case條件, memo[(i,j)] => 要預設False, 不然會key error
class Solution:
    def isMatch(self, s, p):
        memo = {} 
        return self.dfs(len(s), len(p), s, p, memo)
    def dfs(self, l, r, s, p, memo):
            if (l, r) in memo: 
                return memo[l, r]
            if not r: 
                return not l  
            if not l: 
                return p[:r].count('*') == r #剩下的pattern 都是"*", 因為可以對應empty string
            
            memo[l, r] = False
            if p[r-1] == '*':
                memo[l, r] = self.dfs(l-1, r, s, p, memo) or self.dfs(l, r-1, s, p, memo) or self.dfs(l-1, r-1, s, p, memo)    
            elif s[l-1] == p[r-1] or p[r-1] == '?':
                memo[l, r] = self.dfs(l-1, r-1, s, p, memo)
            return memo[l, r] 

 
#top down 重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(len(s), len(p), s, p, memo)
    
    def dfs(self, l, r, s, p, memo):
        if (l, r) in memo:
            return memo[(l, r)]
        if not r:
            return not l
        if not l:
            return p[:r].count("*") == r
        memo[(l, r)] = False
        if p[r - 1] == "*":
            memo[(l, r)] = self.dfs(l-1, r, s, p, memo) or self.dfs(l, r-1, s, p, memo) or self.dfs(l-1, r-1, s, p, memo)
        elif p[r - 1] in [s[l - 1], "?"]:
            memo[(l, r)] = self.dfs(l-1, r-1, s, p, memo)
        return memo[(l, r)]

# Top Down, dfs backtracking + memo
class Solution:
    def isMatch(self, s, p):
        memo = {} 
        return self.dfs(0, 0, s, p, memo)

    def dfs(self, i, j, s, p, memo):
            if (i, j) in memo: 
                return memo[(i, j)]
            if j == len(p): 
                return i == len(s) 
            if i == len(s): 
                return p[j:].count('*') == len(p) - j #剩下的pattern 都是"*", 因為可以對應empty string
            
            memo[(i, j)] = False #這要寫預設為False, 不然會key error
            if s[i] == p[j] or p[j] == '?':
                memo[(i, j)] = self.dfs(i+1, j+1, s, p, memo)
            elif p[j] == '*':    
                memo[(i, j)] = self.dfs(i, j+1, s, p, memo) or self.dfs(i+1, j, s, p, memo) #可以不用加 self.dfs(l-1, r-1, s, p, memo), why 保留前兩個足矣, 想一下就知道了
            return memo[(i, j)]    





#自己重寫! dp bottom up
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) +1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != "*":
                break
            dp[0][j] = True
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                    
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    
        return dp[-1][-1]
 
#自己重寫 top down dp
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(len(s), len(p),s,p,memo)
    
    def dfs(self, i, j, s, p, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if not j:
            return not i
        
        if not i:
            return p[:j].count("*") == j
        
        memo[(i,j)] = False
        
        if s[i-1] == p[j-1] or p[j-1] == "?":
            memo[(i,j)] = self.dfs(i-1, j-1, s, p, memo)
        
        if p[j-1] == "*":
            memo[(i,j)] = self.dfs(i-1, j, s, p, memo) or self.dfs(i, j-1, s, p, memo)
        
        return memo[(i,j)]
























































