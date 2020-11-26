'''
Given an array of integers nums and an integer threshold, 
we will choose a positive integer divisor and divide all the array by it and sum the result of the division. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
'''

# [Python] Binary search O(nlogm) (m=max(arr)), n = len(nums)

# 模板2, 自己重寫
# 思路: divide sum 最大值在於divisor == 1, 最小值在於divisor = max(nums), divisor大於 max(nums) 結果跟 max(nums) 一樣
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo + 1 < hi:
            mid = lo + (hi-lo) // 2
            if self.check(nums, threshold, mid):
                hi = mid
            else:
                lo = mid
        if self.check(nums, threshold, lo):
            return lo
        else:
            return hi
                
    def check(self, nums, threshold, divisor):
        sum = 0
        for num in nums:
            sum += ceil(num / divisor)  #向上取整
        return sum <= threshold



from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        L, R = 1, max(nums) + 1
        while L < R:
            m = (L + R) // 2
            if check(m):
                ans = m
                R = m
            else:
                L = m + 1
        return ans

    def check(self, nums, threshold, m):
        s = 0
        for x in nums:
            s += ceil(x/m)  
        return s <= threshold








