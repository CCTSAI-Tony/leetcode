'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
# two pass + dictionary, time complexity O(n)
class Solution:
    def majorityElement1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums)//2:
                return num

# Sotring, time complexity O(nlogn)    
class Solution:
    def majorityElement4(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# Bit manipulation, time complexity O(32n), 跟137一起服用
# 思路: 利用32個bit, 加總每個num的bit, 若該bit > len(nums)//2, 代表majority element 有這個bit, 記得處理負數問題
class Solution:    
    def majorityElement5(self, nums):
        bit = [0]*32
        for num in nums:
            for j in range(32):
                bit[j] += num >> j & 1 #每個num 從最左邊bit 一路檢查到第32個bit, 利用 num >> j
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums)//2:
                # if the 32th bit is 1, 
                # it means it's a negative number 
                if i == 31:
                    res = -((1<<31)-res)  #處理負數
                else:
                    res |= 1 << i
        return res

#自己重寫, time complexity O(32n), 568ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0] * 32
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & 1 << i:
                    count += 1
            bits[i] = count
            
        for i, v in enumerate(bits):
            if v > len(nums) // 2:
                res |= (1 << i)
        
        return res if res < 2**31 else res-2**32

# Divide and Conquer, time complexity O(nlogn)
class Solution:
    def majorityElement6(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2]) #左半
        b = self.majorityElement(nums[len(nums)//2:]) #右半
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2] #永遠取過半的
'''
nums.count(a) > len(nums) // 2 can either be True (a.k.a. 1) or False (a.k.a. 0). a.k.a. also known as
If it is True, then we return [b, a][1], which is a. If it is False, then we return [b,a][0], which is b.
'''
