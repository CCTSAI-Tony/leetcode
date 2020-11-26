'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
'''

#自己寫的, time complexity O(n), space complexity O(n)
#思路: prefixsum, initial {0, -1}
from itertools import accumulate
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = list(accumulate(nums, lambda x, y: x+y))
        dic = {0:-1}
        max_len = 0
        for i, v in enumerate(prefixSum):
            if v-k in dic:
                max_len = max(max_len, i-dic[v-k])
            if v not in dic: #只登記最前面的
                dic[v] = i
        return max_len