'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# good! 刷題用這個
# Python solution (Accepted), O(n) time, O(1) space
# 思路: 2 round solution, first round only to mutiply elements that came previously before yourself, 
# and second round, only to mutiply elements that came after you
class Solution:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(n):  
            output.append(p)  #先append p, 因為要不包含自己
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):  #排除最後一個
            output[i] = output[i] * p
            p = p * nums[i]
        return output


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        n = len(nums)
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * p
            p *= nums[i]
        return res

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        p = 1
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

# 重寫第四次, time complexity O(n), space complexity O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        res = []
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

'''
first time going through the array, it's beginning to the end. p keeps a running total of the product, 
and each element will equal the running total of the products of the elements that came before. then the 2nd time going through the array, 
you're doing the same process, but backwards, finishing off the result by multiplying the elements that came after.

example: [1,2,3,4]. let's say initially, your output is [1, 1, 1, 1] and p = 1.

Loop 1:
i = 0, your output becomes [1, , , ] and p = p * 1 (1)
i = 1, your output becomes [1, 1, , ] and p = p * 2 (2)
i = 2, your output becomes [1, 1, 2, ] and p = p * 3 (6)
i = 3, your output becomes [1, 1, 2, 6]

Loop 2 (p = 1 again)
i = 3, your output becomes [1, 1, 2, 6*1] and p = p * 4 (4)
i = 2, your output becomes [1, 1, 2*4, 6] and p = p * 3 (12)
i = 1, your output becomes [1, 1*12, 8, 6] and p = p * 2 (24)
final result: [24, 12, 8, 6]
'''











