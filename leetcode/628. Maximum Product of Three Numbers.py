'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

# There are two possible ways to get the largest number:

# biggest number * 2nd biggest * 3rd biggest
# biggest number * smallest number * 2nd smallest number (if the two smallest numbers are negative)
# This formula will also work in the case there are all negative numbers, in which the smallest negative number will be the result (based on condition 1).

# We can simply sort the numbers and retrieve the biggest/smallest numbers at the two ends of the array.

#time complexity O(nlogn), 280ms
#思路: 先對nums排序, 因為負號的關係, 最大值可能為nums[0]*nums[1]*nums[-1], 也有可能 nums[-1]*nums[-2]*nums[-3], 這兩種可能在全部都是負數or全部都是正數or混雜下都適用
class Solution:
    def maximumProduct(self, nums):
      nums.sort()
      return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])

#自己重寫
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])