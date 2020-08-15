'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
        if max(d.values()) > 1:
            return True
        else:
            return False

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))