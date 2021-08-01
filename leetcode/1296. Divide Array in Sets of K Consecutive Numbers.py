'''
Given an array of integers nums and a positive integer k, find whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109
 

Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/
'''

# 刷題用這個, time complexity O(mn), space complexity O(n)
# 思路: 使用counter, 再遍歷sorted count, 從小元素遍歷, 該元素個數代表要形成多少個以該元素開頭連續k個的subarray
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for n in sorted(count):
            if count[n] > 0:
                need = count[n]
                for i in range(n,n+k):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True

# 重寫第二次
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count = Counter(nums)
        for num in count:
            need = count[num]
            if need:
                for i in range(num, num+k):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True


