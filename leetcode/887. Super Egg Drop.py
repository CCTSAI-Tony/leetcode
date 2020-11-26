'''
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000
'''

# Explanation
# Drop eggs is a very classical problem.
# Some people may come up with idea O(KN^2)
# where dp[K][N] = 1 + max(dp[K - 1][i - 1], dp[K][N - i]) for i in 1...N.
# However this idea is very brute force, for the reason that you check all possiblity.

# So I consider this problem in a different way:
# dp[M][K]means that, given K eggs and M moves,
# what is the maximum number of floor that we can check. 原來這題目是問這個, 重要!!

# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

# The dp equation is:
# dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
# which means we take 1 move to a floor,
# if egg breaks, then we can check dp[m - 1][k - 1] floors.  剩下m-1 moves, k-1顆蛋
# if egg doesn't breaks, then we can check dp[m - 1][k] floors.  剩下m-1 moves, k顆蛋

# dp[m][k] is the number of combinations and it increase exponentially to N


Complexity
For time, O(NK) decalre the space, O(KlogN) running, 
For space, O(NK).

# 刷題用這個
# 思路: O(KlogN) running, dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1, m 到logN 的時候, 差不多 dp[m][K] >= N, 所以O(KlogN)
class Solution:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]  #zero based index
        for m in range(1, N + 1):  #大樓多高, 我的步數就有多高
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1  # 這邊最難想
            if dp[m][K] >= N:  #一旦發現 此時moves 攜帶K個蛋 可以瀏覽整棟樓, return
                return m





https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn 有空看一下!




# Basic idea
# First of all, we can see to get the answer of larger floors and eggs, results of smaller cases are useful for analysis, which leads to dynamic programming.

# Next, how to define a state for each drop of getting the optimal floor? Here we have two variables:

# The number of eggs left to throw i, (0 <= i <= K)
# The number of floors left to test j, (1 <= j <= N)
# The answer (smallest times to get the optimal floor) can be the value of each dp state.

# Therefore, we define dp[i][j] as smallest number of drop to get the optimal floor with i eggs and j floors left.

# DP formula
# For the implementation of dp, we need two information:

# base case
# recursive relation
# Base case is rather intuitive to come up with. Think of cases with smallers eggs and floors:

# dp[1][j] = j, j = 1...N # one egg, check each floor from 1 to j
# dp[i][0] = 0, i = 1...K # no floor, no drop needed to get the optimal floor
# dp[i][1] = 1, i = 1...K # one floor, only check once
# To get recursive relation, let's consider a test case: 3 eggs and 100 floors.
# For the next drop, I can choose floor from 1 to 100, say I choose 25.
# There are 2 possible results for this drop:

# the egg brokes, I now have 2 eggs, and the floor to choose becomes 1~24.
# the egg remains safe, I still have 3 eggs, and the floor to choose becomes 26~100.
# Think of the worst case senerio and use the dp defination above, we can describe the situation of getting the optical floor with choosing floor 25 for the next drop as:
# dp[3][100] = 1 + max(dp[2][24], dp[3][75])

# Besides floor 25, in term of next drop, we can also choose floor from 1 to 100. Each drop would be similar to the case of 25 above. 
# The final result would be the minimum of all possible choices of next floors to drop:

# dp[3][100] = min(..., 1 + max(dp[2][23], dp[3][76]), 1 + max(dp[2][24], dp[3][75]), 1 + max(dp[2][25], dp[3][74]), ...) (take floor 24, 25, 26 as example)

# To generilize the above example, the dp formula would be:
# dp[i][j] = min(1 + max(dp[i-1][k-1], dp[i][j-k])), k = 1,2,...j

# The brute force solution
# With dp formula above, the brute force solution would be O(kn^2) as below:
# Optimization1: choosing k for each dp[i][j]
# The brute force solution gets TLE. To optimize, we should check for the unnecessary iteration in the for-loops. 
# More specifically, to get the k that best fits each drop, we don't need to go over all floors from 1 to j. 
# As for a fixed k, dp[i][k] goes up as k increases. This means dp[i-1][k-1] will increase and dp[i][j-k] will decrease as k goes from 1 to j. 
# The optimal value of k will be the middle point where the two meet. So to get the optimal k value for dp[i][j], we can do a binary search for k from 1 to j.
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
        
        for i in range(2, K+1):
            for j in range(2, N+1):
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[K][N]




# This will save the third for-loop of k from O(n) to O(logn). Total complexity is O(knlogn). Using binary seach, we can only do bottom up dp, as shown below:
# 模板2, 這個面試不錯
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:     
        d={}
        return self.dfs(K, N, d)


    def dfs(self, i, j, d):
        if i==1:
            return j
        if j==0:
            return 0
        if j==1:
            return 1
        if (i, j) in d:
            return d[i, j]
        lo, hi = 1, j
        while lo + 1 < hi:
            mid = (lo+hi)//2
            left, right = self.dfs(i-1, mid-1, d), self.dfs(i, j-mid, d)
            if left < right:
                lo = mid 
            else:
                hi = mid 
        
        if self.dfs(i-1, lo-1, d) >= self.dfs(i, j-lo, d):
            res = 1 + max(self.dfs(i-1, lo-1, d), self.dfs(i, j-lo, d))
            d[i, j]=res
            return res
        # elif dfs(i-1, hi-1) >= dfs(i, j-hi):
        else:
            res = 1 + max(self.dfs(i-1, hi-1, d), self.dfs(i, j-hi, d))
            d[i, j]=res
            return res



#這個面試不錯, 模板1
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dfs(i, j):
            if i==1:
                return j
            if j==0:
                return 0
            if j==1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 1, j
            while lo <= hi:  #找中間點
                mid = (lo+hi)//2
                left, right = dfs(i-1, mid-1), dfs(i, j-mid)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid - 1
            res = 1 + max(dfs(i-1, lo-1), dfs(i, j-lo))
            d[i, j]=res
            return res
        
        d={}
        return dfs(K, N)

# Optimization2: choosing k_1...k_N for each dp[i][1...N]
# To go one step further, till now, we are still finding the optimal floor k from 1 to j for each dp[i][j]. 
# But is this really the smallest range we can narrow? In fact, we can see that the optimal floor k for each dp[i][j] increases as j increases. 
# This means that once we get the optimal k for dp[i][j], we can save current k value and start the next round of for-loop directly, 
# instead of initiating k from 0 again. In this way, in the third for-loop, k will go from 1 to N only once as j in the second for-loop goes from 1 to N. 
# The total time complexity will be O(kn). The code is shown below:

# Why "The optimal value of k will be the middle point where the two meet."

# With increasing k, one value increases and the other decreases. To minimize the maximum of them, these two values should be as close as possible.

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
            
        for i in range(2, K+1):
            k = 1
            for j in range(2, N+1):
                while k < j+1 and dp[i][j-k] > dp[i-1][k-1]:
                    k += 1
                dp[i][j] = 1 + dp[i-1][k-1]
        return dp[K][N]



# Optimization3: space complexity
# Usually, we can save space complexity by one dimension if the recursive relation of dp is based the constant length of previous states. 
# Here, the current line dp[i] is getting updated based on the current line and previous line, 
# so we can only record those two lines and update them in the iteration process to save the space space complexity by one dimension. 
# Final time complexity O(kn), space complexity O(n). The code is shown below:

#這個不好懂, 有點dp 代表previous line, ndp 代表current line, current line取得 previous line data後, dp 再update 至current line
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """ 
        dp = range(N+1)  #代表初始只有一個雞蛋時, 若大樓n樓, 要幾個moves
        for i in range(2, K+1):
            k = 1
            ndp = [0, 1] + [float('inf')]*(N-1)
            for j in range(2, N+1):
                while k < j+1 and ndp[j-k] > dp[k-1]:
                    k += 1
                ndp[j] = 1 + dp[k-1]
            dp = ndp
        return dp[N]


# Summery
# Personally, I'd recommend thinking this problem through the following logic:

# Why dp? Under what circumstances should we use dp to solve a problem?
# What's the base case and recursive relation to describe a state in the problem?
# What's the dp formula based on the above analysis?
# Implement the brute force solution.
# Optimization: find the pattern of dp array, what iteration is unneccessary and can be saved?
# What's the time and space complexity? Any way to save the space complexity by one dimension?










