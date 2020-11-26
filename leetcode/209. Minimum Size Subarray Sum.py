'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

#O(n)
class Solution:
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1 #一開始設比len(nums)大1
        for right, n in enumerate(nums):
            total += n #當while loop 走完, 就會向右一格, total +n 若大於s 再進入while loop 得到數字數 並修改left值
            while total >= s:
                result = min(result, right - left + 1) #取最小值, 目前right - 目前left + 1 目前實際數字數
                total -= nums[left] #往右移一格 
                left += 1 #往右移一格
        return result if result <= len(nums) else 0


# O(n log n)  模板1
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n #[1,2,3,4,5] > [1,3,6,10,15]
        left = 0
        for right, n in enumerate(nums): #此時nums已修改
            if n >= s:
                left = self.find_left(left, right, nums, s, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0
    
    def find_left(self, left, right, nums, target, n):
        while left <= right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid -1 
        return left

# enumerate(iterable, start=0)

# l1 = ["eat","sleep","repeat"] 
  
# # printing the tuples in object directly 
# for ele in enumerate(l1): 
#     print ele 
# print 
# # changing index and printing separately 
# for count,ele in enumerate(l1,100): 
#     print count,ele 

# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')

# 100 eat
# 101 sleep
# 102 repeat


#模板2
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n #[1,2,3,4,5] > [1,3,6,10,15]
        left = 0
        for right, n in enumerate(nums): #此時nums已修改
            if n >= s:
                left = self.find_left(left, right, nums, s, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0
    
    def find_left(self, left, right, nums, target, n):
        while left + 1 < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid 
            else:
                right = mid 
        
        mid = (left + right) // 2
        if n - nums[mid] >= target:
            return right
        return left









