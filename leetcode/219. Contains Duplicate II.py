'''
Given an array of integers and an integer k, find out whether there are two distinct indices 
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 2 sum 變種
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i #先建立 value:index pair, 若i - dic[v] <= k, dic[v] update i
        return False

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo and i - memo[num] <= k:
                return True
            else:
                memo[num] = i
        return False