'''
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
'''


# Solution 1: 3D DP
# Intuition
# Seem that most of games, especially stone games, are solved by dp?

# Explanation

# dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.

# Initial status dp[i][i][1] = 0 and dp[i][i][m] = infinity

# dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j] => stonesNumber[i][j] 代表 stones[i] 到 stones[j] 的所有石頭
# dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])

# The origine python2 solution is a bit too long on the memorization part.
# So I rewrote it in python3 with cache helper,
# so it will be clear for logic.

# Complexity
# Time O(N^3/K), Space O(KN^2), 利用lru_cache 來執行memo
# 題目: A move consists of merging exactly K consecutive piles into one pile => 只能連續合併
# 思路: 此題dp-有許多重複子問題 注意題目有說要連續合併k piles 才算一個move, 先建立stones 的 prefix sum => 因為要計算連續堆的石頭數
# dp關係式: dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.
# dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j] => stonesNumber[i][j] 代表 stones[i] 到 stones[j] 的所有石頭
# dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])
# base case: dp[i][i][1] = 0 and dp[i][i][m] = infinity
import functools
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + stones[i] #prefix[i] = stones[:i]
        res = self.dp(0, n - 1, 1, K)
        return res if res < inf else -1

    @functools.lru_cache(None)  #dp參數一定要hashable, 不然decorator 不能記住
    def dp(self, i, j, m, K):
        if (j - i + 1 - m) % (K - 1): #優化, 確認是否可以merge k item 來留下m piles, ex: k = 3 每一步都要消耗兩個piles, 所有piles - m piles == 要消失的piles => 注意有可能<0
            return float("inf")
        if i == j:
            return 0 if m == 1 else float("inf") #return 0 一樣過, 可能上面已經幫忙過濾全部不適合的條件, 或者test case不夠, 所以這裡還是增加一些條件補充, 
        if m == 1:
            return self.dp(i, j, K, K) + self.prefix[j + 1] - self.prefix[i] #看題目例子 stones = [3,5,1,2,6] => [3, 8, 6] => [17], K = 3 就懂了 total:25
        return min(self.dp(i, mid, 1, K) + self.dp(mid + 1, j, m - 1, K) for mid in range(i, j, K - 1)) # K - 1 => step, 優化用


#自己重寫, time complexity O(n^3), 刷題用這個
import functools
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i+1] = self.prefix[i] + stones[i]
        res = self.dp(0, n-1, 1, K)
        return res if res < float("inf") else -1
        
    @functools.lru_cache(None)
    def dp(self, i, j, m, K):
        if (j-i+1-m) % (K-1):
            return float("inf")
        if i == j:
            return 0 if m == 1 else float("inf") 
        if m == 1:
            return self.dp(i, j, K, K) + self.prefix[j+1] - self.prefix[i]
        return min(self.dp(i, mid, 1, K) + self.dp(mid+1, j, m-1, K) for mid in range(i, j))
        





















