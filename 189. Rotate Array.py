'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
# O(n) in time, O(1) in space
class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
# Classical 3-step array rotation: [1,2,3,4,5,6,7]>[4,3,2,1,7,6,5]>[5,6,7,1,2,3,4]
# reverse the first n - k elements

# reverse the rest of them

# reverse the entire array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            nums.pop(len(nums)-1)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums[:] = nums[len(nums)-1:] + nums[:len(nums)-1]rs


















