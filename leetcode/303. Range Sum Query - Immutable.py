'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


# Python DP solution, O(n) for init and O(1) for query

# Use an extra element for summation so we don't need to check boundary condition in the query. 這在講self.sums = [0] * (len(nums) + 1), 
#若不這麼做 ex: sumRange(0, 5) 會out of list, slef.sums[5] - self.sums[0-1]
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i] #why - self.sums[i], cause need include nums[i]

# Given nums = [-2, 0, 3, -5, 2, -1]

# self.sums = [0,[-2],[-2],[1],[-4],[-2],[-3]


# TLE 自己想的
class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        

    def sumRange(self, i: int, j: int) -> int:
        self.sum = 0
        for i in range(i,j+1):
            self.sum+=self.array[i]
        return self.sum



