Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index #建立pair


#自己重寫 time complexity O(n)
#思路: 利用hash table 找出對應的pair
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numsIndex:
                return [numsIndex[target - nums[i]], i]
            numsIndex[nums[i]] = i
