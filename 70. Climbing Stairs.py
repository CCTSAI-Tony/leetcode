'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''
#自己想的 time complexity O(n)
#思路: 簡單dp, dp[0] = 1 初始值重要概念
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]* (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

#自己重寫 top down memo, time complexity O(n)
#思路: 建立memo, dfs recursion 回報memo[n], 若n不在dic 則利用subproblems 的關係式來建立 memo[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1,1:1}
        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n not in memo:
            memo[n] = self.dfs(n-1, memo) + self.dfs(n-2, memo)
        return memo[n]




# Top down - TLE 超過時間, 太多重複子路徑
class Solution:
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
 
# Bottom up, O(n) space
class Solution:
    def climbStairs2(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

# Bottom up, constant space
class Solution:
    def climbStairs3(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b
    
# Top down + memorization (list)
class Solution:
    def climbStairs4(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n-1, dic) #n-1 是因為zero based index的關係
    
    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
        return dic[n]
    
# Top down + memorization (dictionary) 酷斃了！
class Solution:  
    def __init__(self):
        self.dic = {1:1, 2:2}


    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]










