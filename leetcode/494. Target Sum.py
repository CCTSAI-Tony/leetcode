# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, 
# you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:

# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
 

# Constraints:

# The length of the given array is positive and will not exceed 20. 重要!!
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

#思路: +0, -0 算不同答案, DP BUTTOM UP time complexity 依舊 O(2^n), 但有優化
#紀錄當下有可能產生幾種值, 並紀錄該值當下有幾種方式組成, 
#當index = 3 => dp = {1:1, 2:2, 3:3}, 當index = 4 nums[4] = 1 => new_dp的key = 舊dp裡的key +/- nums[4]產生新key, 並加上舊dp裡的key value =>
#新dp key = 2 => 舊dp 1 + 1 and 舊dp 3 - 1, 因此新dp[2] = 舊dp[1] + 舊dp[3], 最後答案return finalDP[S]
#跟dfs暴力解法相比, 此方法會合併舊dp +/- nums[i] = 相同的key 的路徑, 但還是改變不了worst case = O(2^n) 的事實
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)



#自己重寫, time complexity O(2^n), 224ms, 刷題用這個
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        dp = defaultdict(int)
        if nums[0] != 0:
            dp[nums[0]], dp[-nums[0]] = 1, 1
        else:
            dp[nums[0]] = 2
        for i in range(1, len(nums)):
            new_dp = defaultdict(int)
            for d in dp:
                new_dp[d + nums[i]] += dp[d]
                new_dp[d - nums[i]] += dp[d]
            dp = new_dp
        return dp[S]




# 分治法 + Memoization Solution, time complexity O(2^n)
# 思路: 建立memo 來紀錄(index, curr_sum) 以免重複遍歷
# 有可能出現重複子問題 => ex: +5 -5 => 子問題 or -5 +5 => 子問題
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0:
            if curr_sum == target:
                return 1
            else:
                return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum - nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]

#比較直覺, 刷題用這個
#自己重寫, time complexity O(2^n)
#思路: 有可能出現重複子問題 => ex: +5 -5 => 子問題 or -5 +5 => 子問題
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        index = len(nums) - 1
        cur_sum = 0
        memo = {}
        return self.dfs(index, nums, cur_sum, memo, S)
    
    
    def dfs(self, index, nums, cur_sum, memo, S):
        if (index, cur_sum) in memo:
            return memo[(index, cur_sum)]
        if index < 0:
            if cur_sum == S:
                return 1
            else:
                return 0
        positive = self.dfs(index-1, nums, cur_sum + nums[index], memo, S)
        negative = self.dfs(index-1, nums, cur_sum - nums[index], memo, S)
        memo[(index, cur_sum)] = positive + negative
        return memo[(index, cur_sum)]





#自己想的 dfs TLE, TIME COMPLEXITY O(2^n)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        self.res = 0
        self.dfs(0,nums,S, n, 0)
        return self.res
    
    def dfs(self, i, nums, S, n, path_sum):
        if i == n:
            if path_sum == S:
                self.res += 1
            return
        
        self.dfs(i+1, nums, S, n, path_sum + nums[i])
        self.dfs(i+1, nums, S, n, path_sum - nums[i])









