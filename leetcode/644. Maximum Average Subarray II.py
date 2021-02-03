# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is greater than or equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation:
# - When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum average is 12.75
# - When the length is 5, averages are [10.4, 10.8] and the maximum average is 10.8
# - When the length is 6, averages are [9.16667] and the maximum average is 9.16667
# The maximum average is when we choose a subarray of length 4 (i.e., the sub array [12, -5, -6, 50]) which has the max average 12.75, so we return 12.75
# Note that we do not consider the subarrays of length < 4.
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 104
# -104 <= nums[i] <= 104


# Binary Search Solution

# What is the range for the average value? Clearly, any average will lie between min(nums) and max(nums). So the intuition is to use binary search between this range.
# lo is initialized to min(nums). hi is initialized to max(nums). x = mid = (lo+hi)/2
# Now we want to solve the sub-problem: Does the array nums have a subarray of length greater than equal to k with average at least x? If yes, 
# then we can restrict our search to the range [x,hi]. Otherwise, we will search in the range [lo,x].
# Can we devise a linear time solution for the problem: Does the array nums have a subarray of length greater than equal to k with average at least x?
# nums[i]+...+nums[j] >= x * (j-i-1). This evaluates to: (nums[i]-x) + (nums[i+1]-x) + ...(nums[j]-x) >= 0
# The problem is transformed into the following problem: Do we have a sub-array of length greater than k in the transformed array with sum greater than zero?
# The above problem can be solved in linear time. Start by finding the sum of first k elements nums[i]-mid. If this sum is greater than zero, 
# then we can return True. Otherwise, say we have the cumulative sum until index j i.e. cum(j) where j >= k. 
# Now say we know the minimum cumulative sum until index i i.e. mcum(i) such that j-i >= k. Then if the cum(j) >= mcum(i) or cum(j) - mcum(i) >= 0, we can return True.


#刷題用這個, time complexity O(nlogm), m = max(nums) - min(nums), space complexity O(1)
#思路: 此題需要一些數學思路, 最大的子序列平均值發生在 max(nums), 最小發生在 min(nums) => 要立即產生binary search 想法
#此題特別技巧 while lo + precision < hi: 模板2變形
#判斷func => 確認有無子序列長度 >= k, sum >= mid(指定值) => 使用到presum list 技巧 => presum(j) - presum(i-1) => presum(i到j)
#可以對每個num 先減 mid => 判斷變成 if presum(j) - presum(i-1) >= 0, 延伸自 nums[i]+...+nums[j] >= x * (j-i-1)
#先確認前k的元素子序列是否滿足條件, 若沒有, 開始進行two pointer確認, 因為是從第k+1 個元素執行, 因此巧妙避開i與j 需要相隔k的元素的操作, 
#最重要的是, pre(i) 指針要記錄的是前序列發生過的最小值, 因為子序列長度可以 >= k
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lo, hi = min(nums), max(nums)
        precision = 1E-6
        while lo + precision < hi:
            mid = lo + (hi - lo) / 2.0
            if self.can_process(mid, nums, k):
                lo = mid
            else:
                hi = mid
        if self.can_process(hi, nums, k):
            return hi
        return lo

    def can_process(self, mid, nums, k):
        sum_so_far = 0
        for i in range(k):
            sum_so_far += nums[i] - mid
        if sum_so_far >= 0:
            return True
        prev, min_so_far = 0.0, 0.0
        for i in range(k, len(nums)): #確保sum(j) 與 sum(i) 相隔 >= k
            sum_so_far += nums[i] - mid
            prev += nums[i-k]-mid
            min_so_far = min(min_so_far, prev) #紀錄前面子序列出現過的最小值
            if sum_so_far >= min_so_far:
                return True
        return False




#重寫第二次,time complexity O(nlogm), space complexity O(1), m = max(nums) - min(nums)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo, hi = min(nums), max(nums)
        precision = 10 ** -6
        while lo + precision < hi:
            mid = lo + (hi - lo) / 2.0
            if self.check(nums, k, mid):
                lo = mid
            else:
                hi = mid
        if self.check(nums, k, hi):
            return hi
        return lo 
        
        
    def check(self, nums, k, x):
        sum_until_j = 0
        for i in range(k):
            sum_until_j += nums[i] - x
        if sum_until_j >= 0:
            return True
        min_prev, sum_until_i = 0, 0
        for i in range(k, len(nums)):
            sum_until_j += nums[i] - x
            sum_until_i += nums[i-k] - x
            min_prev = min(min_prev, sum_until_i)
            if sum_until_j - min_prev >= 0:
                return True
        return False

