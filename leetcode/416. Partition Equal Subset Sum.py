'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

# One way is to treat problem as 0-1 knapsack that we need to pick some of the elements that sum up to target = sum(nums) / 2.
# Suppose dp[i][j] is a boolean that indicates whether we can pick some of the elements from nums[:i+1] to sum up to a specific value s. 
# Thus, if dp[i][j] is True, either dp[i-1][s] is already True(some elements from nums[:i] can already sum up to s), 
# or dp[i-1][s-nums[i]] is True(some elements from nums[:i] plus nums[i] equals to s).
# Therefore, we can have recurrence equation as

# dp[i][s] = dp[i-1][s] or (s >= nums[i] and dp[i-1][s-nums[i]])
# The base case dp[0][0] is True and we can always pick none of elements to sum up to 0.
# And we can use rolling dp arrays to reduce dp size from len(nums) * sum(nums)/2 to sum(nums)/2 since dp[i] depends on dp[i-1] alone. => space 優化
# The time complexity is O(len(nums) * sum(nums)) and Python 3 runs ~700ms.

# time complexity O(len(nums) * sum(nums)), dp bottom up, 省下空間度
# 思路: 只要能判斷有無subset sums up to sum(nums) / 2, 就能立刻判斷nums 可以平分subsets, 因為只要找到一半, 另一半就是剩下的集合
# 每一次iteration based on nums, 重建一次dp, 裡面的每一個item 由上一次的dp[i] 與上一次 (s >= x and dp[s-x]) 決定true or false
# dp[i][s] = dp[i-1][s] or (s >= nums[i] and dp[i-1][s-nums[i]]), 代表不加入nums[i] or 加入nums[i]
# ex: x = 3, dp[3] = false or (3 >= 3 and dp[3-3]) => True
class Solution:
    def canPartition(nums):
        target, n = sum(nums), len(nums)
        if target & 1: #代表奇數無法平分
            return False
        target >>= 1 #平分後的值
        dp = [True] + [False]*target  #zero based index, dp[0] = True
        for x in nums: #代表i iteration 加入x 的情況
            dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)] #s 代表sum up to 的target, 裡面的dp[s-x] 還是存在於上一次 未加入x 的 iteration生成的dp
            if dp[target]: 
                return True
        return False

# 刷題用這個, 比較直白
# 自己重寫, time complexity O(len(nums) * sum(nums)), 1348ms
# dp[i][j] is a boolean that indicates whether we can pick some of the elements from nums[:i] to sum up to a specific value j.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True  #we can always pick none of elements to sum up to 0
        
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j] or (j >= nums[i-1] and dp[i-1][j-nums[i-1]]) #不包含nums[i-1] or 包含nums[i-1]
            if dp[i][target]:
                return True
        return False






# Another solution is DFS + Memoization. We keep trying to reduce nums[j] from target value and see whether target value can be reduced to exactly 0. 
# And with memoization, time complexity can be limited within O(len(nums) * sum(nums)).
# Besides we can iterate from large to small values to prune our DFS (sort takes O(NlogN)). 
# Actually time will be much less since we can avoid checking most of {1,..., sum(nums)}. Python 3 runs ~ 50ms.

#back tracking + memo, time complexity O(len(nums) * sum(nums))
#思路: 似partion question, 利用dfs 看是否能sum up to target, 因為是平分, 所以只要確認能sum up to sum(nums) // 2 from nums => return True
#記得對nums.sort(reverse=True), 優化
class Solution:
    def canPartition(nums):
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: 
            return False
        nums.sort(reverse=True)
        return self.dfs(0, s >> 1, memo, n, nums)
    
    def dfs(self, i, x, memo, n, nums): #i: nums 的 index
        if x not in memo:
            memo[x] = False #預設
            if x > 0:
                for j in range(i, n): 
                    if self.dfs(j+1, x-nums[j], memo, n, nums):
                        memo[x] = True
                        break
        return memo[x]

#自己重寫, time complexity O(len(nums)*sum(nums), 44ms, 刷題用這個
#思路: 會遇到重複失敗子問題 => 使用memo prune 分支
#似partion question, 利用dfs 看是否能sum up to target, 因為是平分, 所以只要確認能sum up to sum(nums) // 2 from nums => return True
#nums.sort(reverse=True) => 優化用的, 可以不用
#memo[s] 代表是否可以在取得target - s 的元素集合中, 剩下的元素是否可以從中拼湊等於s
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)
        target = sum(nums) // 2
        nums.sort(reverse=True) 
        memo = {0:True}
        return self.dfs(0, target, memo, nums, n)
    
    def dfs(self, i, target, memo, nums, n):
        if target not in memo:
            memo[target] = False
            if target > 0:
                for j in range(i, n): #每個元素可能被選or不被選
                    if self.dfs(j+1, target - nums[j], memo, nums, n): #j+1, 避免重複選到一樣元素, 前面的元素都已遍歷過
                        memo[target] = True
                        break
        return memo[target]


#自己重寫
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m, n = len(nums), sum(nums)
        if n % 2:
            return False
        memo = {0: True}
        target = n // 2
        return self.dfs(0, target, m, nums, memo)
    
    def dfs(self, idx, target, m, nums, memo):
        if target in memo:
            return memo[target]
        memo[target] = False
        if target > 0:
            for i in range(idx, m):
                memo[target] = self.dfs(i+1, target-nums[i], m, nums, memo)
                if memo[target]:
                    break
        return memo[target]












