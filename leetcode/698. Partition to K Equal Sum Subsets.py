# Given an array of integers nums and a positive integer k, 
# find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 
# Example 1:

# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.



#自己重寫 time complexity O(k^n)
#backtracking!! 與leetcode 473一起服用 partition problem
#思路: 典型dfs backtracking, partition problem, 先設立4個桶子, 每個等於 sum(nums) // k
#每個數字有四個選擇, 若該數字進錯桶則backtrack到上一層, 恢復該桶數值, 換進下一個桶看看
#nums.sort(reverse=True) 則是優化, 讓backtrack的recursion tree 縮短, 此題是一定要這樣做, 不然會TLE
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)  #關鍵優化
        target = sum(nums) // k
        buckets = [target] * k
        n = len(nums)
        if self.dfs(0, k, nums, buckets, n, target):
            return True
        return False
    
    def dfs(self, i, k, nums, buckets, n, target):
        if i == n:
            return True
        for pos in range(k):
            if nums[i] > buckets[pos]:
                continue
            buckets[pos] -= nums[i]
            if self.dfs(i+1, k, nums, buckets, n, target):
                return True
            buckets[pos] += nums[i]
            if buckets[pos] == target:  # 重要: 剪枝優化 => 代表前面有放錯桶了, 導致現在全新的桶也不能容下目前的值
                break
        return False







# Python DFS
# Have k buckets initialized with 0. 
# Use DFS to try combination of all kinds of ∑nums[i]. Once it's exceed target=sum/k, the path failed.
# backtracking!! 與leetcode 473一起服用 partition problem
class Solution:
    def canPartitionKSubsets(nums, k):
        target, m = divmod(sum(nums), k)
        if m: 
            return False #無法平均分配
        dp, n = [0]*k, len(nums)
        nums.sort(reverse=True)  #優化, 大的先
        return nums[0] <= target and self.dfs(0, nums, dp, n, k, target)

    def dfs(self, i, nums, dp, n, k, target):
            if i == n:
                return len(set(dp)) == 1  #trick, 若每個bucket sum值 一樣, set後只有一個元素, 其實不需要這個, 直接return True就行, 到這階段代表每個bucket 值已經一樣
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and self.dfs(i+1, nums, dp, n, k, target):
                    return True
                dp[j] -= nums[i]
                if not dp[j]: #trick, 代表有元素就算放在空的bucket 都無法成功 k bucket same sum, 提早結束, 優化
                    break
            return False



