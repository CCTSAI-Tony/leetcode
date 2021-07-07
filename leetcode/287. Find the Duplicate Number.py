'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

# Use a binary search variant

# The array is not sorted - but the indices of the array are sorted - #Insight 破題! [1,3,4,2,2] => [0,1,2,3,4]
# Find the mid index. Call it M.
# Traverse the main array and count all numbers <= M (注意是<=). Say the count is K.
# Say N = 200. Num elements = 201. M = 100. Low=1. High = 200.
# Say K = 101. Then we know original list of 201 elements has 101 elements <= 100. There must be a duplicate from 1 to 100. 
# So we should check in left half of index space - remember we are searching index space not element space. high = mid.
# Say K = 100. Then we know original list of 201 elements has 100 elements <= 100. It has 101 elements > 100 or from 101 to 200. 
# So we should search right half of the index space: remember we are searching index space not element space low =mid+1.


# 思路: 基本思路就是不斷縮小數值區間找出重複的值, 注意不是縮小元素區間
# ex: 1,2,3,4,5, num <= 5 有五個, 若之間出現重複元素, ex: 1,2,2,3,4,5 num <= 5 有6個, 從這判斷就知道重複元素會是在哪個區間
# time complexity O(nlogn), n = len(nums)
# 模板2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return  None
        low = 1
        high = len(nums) - 1
        while low + 1 < high:
            mid = low + (high - low)//2
            count = self.count(nums, mid)
            if count > mid:
                high = mid
            elif count <= mid:
                low = mid
        if self.count(nums, low) > low:
            return low
        else:
            return high
                
    def count(self, nums, target):
        count = 0
        for num in nums:
            if num <= target:
                count += 1
        return count

#自己重寫, time complexity O(nlogn), space complexity O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        low, high = 1, n
        while low + 1 < high:
            mid = low + (high - low) // 2
            if self.count(nums, mid) > mid:
                high = mid
            else:
                low = mid
        if self.count(nums, low) > low:
            return low
        return high
                
    def count(self, nums, target):
        count = 0
        for num in nums:
            if num <= target:
                count += 1
        return count




#不懂請看上面詳解, 基本思路就是不斷縮小數值區間找出重複的值, 注意不是縮小元素區間
#左閉右開
# time complexity O(nlogn), n = len(nums)
class Solution(object):
    def findDuplicate(self, nums):
        if len(nums) == 0:
            return 0
        low = 1
        high = len(nums)
        while low < high:
            mid = (low + high)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count = count + 1
            if count > mid:
                high = mid
            else:
                low = mid+1
        return low #也可以high 最終low meets high








