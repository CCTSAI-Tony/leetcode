'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

#刷題用這個
#自己想的 time complexity O(n), space complexity O(1), #有待確認 str() and int() time complexity 是否近似 O(1)? 不過在此題是可以當作O(1)的, 因為長度不可能超過32
#思路: 這題的主要想法就是如何inplace modify, ex: 遇到一個數, 直接修改以那個數-1 當索引的值 就達成了inplace modify, 
#所以數列 index 0 代表positive 1, 直到最後一個index 代表 len(nums), 若遇到一個數超過len(nums) 則跳過, 因為已經能保證在1 ~ len(nums) 裡一定有missing positive
#因為裡面包含負數, 所以不能單純乘以-1 又能不破壞原本的值(假如前面的數指向該位置而改變屬性), 所以使用 str() 來改變type, 第一個沒被改動的index + 1 就是 first missing positive
#技巧 int("5") 等於 int(5) = 5, 使用這個技巧就能還原被改動的值type, 對沒被改動的也沒影響
#ex: [1,2,3,4,5] => 6, [1,2,-1,4,5] => 3

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = int(nums[i])
            if temp < 1 or temp > len(nums):
                continue
            nums[temp-1] = str(nums[temp-1]) #改變type
        for i in range(len(nums)):
            if nums[i] != str(nums[i]): #比對type
                return i+1
        return len(nums) + 1


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = int(nums[i])
            if temp <= 0 or temp > len(nums):
                continue
            nums[temp-1] = str(nums[temp-1])
        for i in range(len(nums)):
            if type(nums[i]) != str:
                return i+1
        return len(nums) + 1


#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if int(nums[i]) > 0 and int(nums[i]) <= n:
                nums[int(nums[i]) - 1] = str(nums[int(nums[i]) - 1])
        for i in range(len(nums)):
            if type(nums[i]) != str:
                return i + 1
        
        return n + 1


#重寫第四次, time complexity O(n), space complexity O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = int(nums[i])
            if temp >= 1 and temp <= len(nums):
                nums[temp - 1] = str(nums[temp - 1])
        for i in range(len(nums)):
            if type(nums[i]) == int:
                return i + 1
        return len(nums) + 1






# int(-5)
# -5
# int("-5")
# -5
# str("5")
# '5'
# str(5)
# '5'

# "5" == 5
# False

#其他人解法, 也不錯 利用nums[i]%n 還原被改動的值, 但對沒改動的值也沒影響
"""
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)): #跳過0
            if nums[i] // n == 0: #代表沒被改動 +n 過
                return i
        return n


# Optimized solution with O(1) Space

# Simply traverse the nums array and put any number within [1, N] in their right place. For example if 2 is in that input, then put 2 at index 1.
# Now traverse this "shuffled" array again. You expect 1 at 0th index. Otherwise it is missing. Then you expect 2 at 1st index and so on.
# Above idea can be a little tricky. What about cases like [1] and [1,1] - i.e. 1 is in its place or there are duplicates - we need to advance pointer regardless.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N, i = len(nums), 0
        while i < N:
            while 1<=nums[i]<=N:
                idx_expected = nums[i]-1
                if nums[i] == nums[idx_expected]:
                    break
                nums[i], nums[idx_expected] = nums[idx_expected], nums[i]
            i = i + 1
        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1


