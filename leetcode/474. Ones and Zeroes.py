'''
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
'''

# The knapsack solutions are inspired by this post. I take no credit for it.

# Knapsack O(length * m * n) time, O(length * m * n) space [Accepted]
# We allocate a list of size length x m x n to store all possibilities of subproblems with m1 and n1 up to m and n. 
# The idea is the same as the recursive solution: if a string can be included in a solution, we have two options: use it or skip it.

#TLE
class Solution: 
    def findMaxForm(self, strs, m, n):
        length = len(strs)
        dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(length+1)]
                    
        for i in range(1, length+1): #從1開始, dp[0][j][k] => 還未碰到任何string => return  0
            s = strs[i-1]
            m1 = s.count('0')
            n1 = s.count('1')
            
            for j in range(m+1):
                for k in range(n+1):
                    # this string can be used, so choose to use or skip
                    if j >= m1 and k >= n1:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-m1][k-n1]+1)
                    
                    # definitely cannot use this string
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        
        return dp[-1][-1][-1]

# Knapsack O(length * m * n) time, O(mn) space [Accepted]
# The difference between this version and the previous version is that we traverse the second and third loop backward from m to m1 and n to n1. 
# I also change how I calculate m1 and n1 because the count() method takes O(length(string)) time.

# 刷題用這個, 0,1背包問題,3828ms
# 思路: 建立dp based m and n, 遍歷strs, 計算string 裡面有幾個0 or 1, 反向遍歷 dp[j][k] = max(dp[j][k], dp[j-m1][k-m1] + 1) 裡面的dp皆是上一輪iteration的值, 充分代表i-1 
# 若m > m1, n > n1 => 可以選擇use it or skip it, 反向update dp
# dp[j][k] 代表在m = j, n = k 最多有幾個strings, 在目前遍歷到string[i] 的時候
# 為何反向只到m1, n1 因為低於它就不能use it
class Solution:
    def findMaxForm(self, strs, m, n):
        length = len(strs)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for s in strs:
            m1, n1 = 0, 0
            for ch in s:
                if ch == '0':
                    m1 += 1
                else:
                    n1 += 1
            
            for j in range(m, m1-1, -1):
                for k in range(n, n1-1, -1):
                    # can be used, so choose to use or skip
                    if j >= m1 and k >= n1: #這一行多餘
                        dp[j][k] = max(dp[j][k], dp[j-m1][k-n1]+1)
        return dp[-1][-1] 


#自己重寫, 0-1背包=>背包9講
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(len(strs)):
            m1, n1 = 0, 0
            for w in strs[i]:
                if w == "0":
                    m1 += 1
                elif w == "1":
                    n1 += 1
            for j in range(m, m1-1, -1):
                for k in range(n, n1-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-m1][k-n1] + 1)
        return dp[-1][-1]





# Recursion (Did not submit)
# The idea is like the coin change problem. Once we encounter strs[i], we calculate m1, the number of 0's, and n1, the number of 1's. 
# If m1 is less than m and n1 is less than n, it means we have two options with that string: to use it or to skip it. 
# If we use it, we reduce m by m1 and n by n1, add the counter by one, and go to the next string. If we skip it, we just go to the next string.

#TLE
class Solution:
    def findMaxForm(self, strs, m, n):        
        counter = self.findMax(strs, 0, m, n)
        return counter

    def findMax(self, strs, i, m, n):
        counter = 0
        if i < len(strs):                
            if m > 0 or n > 0:
                # use it or skip it
                m1 = strs[i].count('0')
                n1 = strs[i].count('1')
                use = 0
                
                # skip it
                skip = self.findMax(strs, i+1, m, n)
                
                # use it
                if m1 <= m and n1 <= n:
                    use = self.findMax(strs, i+1, m-m1, n-n1) + 1
                
                # update counter
                counter = max(use, skip)
                            
        return counter

# Memoization (Memory Limit Exceeded 63/63) 
# This is just like the recursive solution. I only add the self.memo dictionary to store pre-computed solutions.

#5776ms, dp top down
class Solution:
    def findMaxForm(self, strs, m, n):
        self.memo = {}  
        return self.findMax(strs, 0, m, n)

    def findMax(self, strs, i, m, n):
        if i < len(strs):
            if (i, m, n) in self.memo:
                return self.memo[(i,m,n)]
            
            if m > 0 or n > 0:
                # use it or skip it
                m1 = strs[i].count('0')
                n1 = strs[i].count('1')
                use = 0
                
                # skip it
                skip = self.findMax(strs, i+1, m, n)
                
                # use it
                if m1 <= m and n1 <= n:
                    use = self.findMax(strs, i+1, m-m1, n-n1) + 1
                
                # update counter
                counter = max(use, skip)
                self.memo[(i,m,n)] = counter
                
                return self.memo[(i,m,n)]
        return 0









