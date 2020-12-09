'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
 

Constraints:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
'''

#刷題用這個, time complexity O(n), space complexity O(1)
#思路: two pointers
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1



#自己想的, time complexity O(n), space complexity O(n)
#思路: prefixSum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            temp = nums[i] + prefixSum[-1]
            prefixSum.append(temp)
        total = prefixSum[-1]
        for i in range(len(prefixSum)):
            if i == 0 and total - prefixSum[i] == 0:
                return 0
            elif (i - 1) >= 0 and prefixSum[i-1] == total - prefixSum[i]:
                return i
        return -1