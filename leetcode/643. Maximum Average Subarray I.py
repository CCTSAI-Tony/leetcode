'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''

#time complexity O(n), space complexity O(1)
#思路: sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        window = 0
        for i in range(k - 1):
            window += nums[i]
        
        for i in range(k - 1, len(nums)):
            if i - k >= 0:
                window -= nums[i - k]
            window += nums[i]
            max_avg = max(max_avg, window / k)
        return max_avg