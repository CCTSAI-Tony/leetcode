'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

#自己想的, time complexity O(n)
#思路: 2 pointers, 一個指針iterate non-zero item 並把此item放到pos指針位置, pos += 1, pos指針從0開始使non-zero item從頭排到尾
#這樣就能保持non-zero item 的順序, 之後pos到array尾 都設為0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(len(nums)-1, pos-1, -1):
            nums[i] = 0

#自己重寫, 刷題用這個
#思路, pos指針遇到0就會停住, 若pos指針不是0就不需要交換, 不管有沒有交換pos +=1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[pos] == 0:
                    nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1



#2 pointer, time complexity O(n)
#思路, j指針遇到0就會停住
class Solution(object):
    def moveZeroes(self, nums):
        if nums and len(nums) > 1:
            j = 0 # records the position of "0"
            for i in range(len(nums)):
                if nums[i]:
                    if not nums[j]: # check if necessary to swap
                        nums[i], nums[j] = nums[j], nums[i]
                    j += 1


# in-place
class Solution(object):
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                
#Not the best solution. What about when all nums are non zeroes? In that case you are stil swaping the variable with itself

