'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

#自己想的, 課本解法, time complexity O(n^2), 3088ms => 若優化 1244ms, 刷題用這個
#思路: dp[i] => s[:i], 此題找longest palindromic sequence, 其實就是longest common sequence的變形, 把自己reverse 來比對就能找到最長 palindromic sequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return None
        if s == s[::-1]: #提早確認 優化
            return len(s)
        dp = [[0] * (len(s)+1) for _ in range(len(s)+1)]
        
        s_rev = s[::-1]
        
        for i in range(len(s)+1):
            dp[0][i] = dp[i][0] = 0
        
        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

#space complexity 優化 O(n*2) => O(n)
#dp 代表 i-1狀態, new_dp 代表 i狀態
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return None
        if s == s[::-1]:
            return len(s)
        dp = [0] * (len(s)+1)
        
        s_rev = s[::-1]
        
        for i in range(1, len(s)+1):
            new_dp = dp[:]
            for j in range(1, len(s)+1):
                if s[i-1] == s_rev[j-1]:
                    new_dp[j] = dp[j-1] + 1
                else:
                    new_dp[j] = max(dp[j], new_dp[j-1])
            dp = new_dp
        return dp[-1]


# I found that for python, the standard DP solutions (time O(n^2), space O(n^2)) might get TLE, while the O(n) space solutions can get accepted in ~1400ms.

# But if we simply check if s itself is a palindrome first, we could reduce a lot of unnecessary dp steps to speed it up.

# This standard dp solution (space O(n2) with the same trick got accepted in ~900 ms
# ex: babbab 用這個方法自己推導看看就清楚了
class Solution:
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1  #每個字都是自身palindrom
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]  #why 2, 因為是同字串兩個不同位置
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])  #是要左邊指針往右縮 還是右邊指針往左縮, i, j 向左, 向右指針
                    
        return dp[0][n-1]


# This space O(n) DP solution got accepted in 619 ms, beating 100%.
class Solution:
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in range(n)]
        dp[n-1] = 1

        for i in range(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:] #copy new dp
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]  #dp[j-1] 是i+1的狀況
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
                    
        return dp[n-1]






