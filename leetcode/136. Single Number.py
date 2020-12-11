'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

#這題是考xor 概念
#自己重寫 time complexity O(n), space complexity O(1)
#思路: 利用xor, k^k = 0 的特性 來找出單獨的值
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res

#自己重寫 reduce 
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0) 
#0 為 initial value 防止empty list, 但此題不需要, 因為題目有說non-empty list


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res








# [Python] Space O(1), XOR+Reduce, Very Simple One Liner (With Explanation)
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)

# Explanation
# I will try to explain this solution by walking through the initial solution that I wrote:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
		for n in nums:
			result ^= n
		return result

# The most crucial trick here is to recognize that if you XOR any same number together, you cancel it out (=0).
# For example:
# nums = [2,4,5,4,3,5,2]
# XORing everything together
# = 2 ^ 4 ^ 5 ^ 4 ^ 3 ^ 5 ^ 2
# = (2^2) ^ (4^4) ^ (5^5) ^ 3
# = 0 ^ 0 ^0 ^ 3
# = 3

# (If you are unfamiliar with the XOR operation, you can check out this stackoverflow post)

# Now, let's go back to the one liner:

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return reduce(lambda x, y: x^y, nums, 0)

# The reduce here just simplifies the previous for loop into one line, it's not doing anything different.
# The initializer 0 is put there to prevent the scenerio 
# where nums is an empty list (I didn't realize that the question statement explicitly mentioned that it would be non-empty).















