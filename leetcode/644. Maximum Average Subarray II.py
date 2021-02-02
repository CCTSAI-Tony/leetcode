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
# Now say we know the minimum cumulative sum until index i i.e. mcum(i) such that j-i >= k. Then if the cum(j) >= mcum(i), we can return True.


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lo, hi = min(nums), max(nums)
        precision = 1E-6
        while hi - lo > precision:
            mid = lo + (hi - lo) / 2.0
            if self.can_process(mid, nums, k):
                lo = mid
            else:
                hi = mid
        return lo

    def can_process(self, mid, nums, k):
        sum_so_far = 0
        for i in range(k):
            sum_so_far += nums[i] - mid
        if sum_so_far >= 0:
            return True
        prev, min_so_far = 0.0, 0.0
        for i in range(k, len(nums)):
            sum_so_far += nums[i] - mid
            prev += nums[i-k]-mid
            min_so_far = min(min_so_far, prev)
            if sum_so_far >= min_so_far:
                return True
        return False