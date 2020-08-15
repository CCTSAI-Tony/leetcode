'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

#bit manipulation, time complexity O(n), space complexity O(1)
#思路: 利用xor 把0-n 給 xor一遍, 再xor 一遍nums, 出現在nums的num 會被抵銷, 只剩沒出現在裡面的數
class Solution:
    def missingNumber1(self, nums):
        res = 0
        for i in range(len(nums)+1): #why len(nums)+1,cause 0, 1, 2, ..., n distinct numbers
            res ^= i
        for num in nums:
            res ^= num
        return res



#自己重寫, 144ms
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for num in nums:
            res ^= num
        return res