        '''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

        '''

class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]: # // 向下取整
                if nums[low] <= target <= nums[mid]: #初步確認target是否在這區間
                    high = mid - 1
                else:
                    low = mid + 1 #不是就到另一邊
            else:
                if nums[mid] <= target <= nums[high]: #初步確認target是否在這區間
                    low = mid + 1
                else:
                    high = mid - 1 #不是就到另一邊

        return -1




# 模板2, time complexity O(log n), 請搭配81
# 思路: https://github.com/yuzhoujr/leetcode/issues/8 看圖比較好理解
# no duplicate element
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low + 1 < high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:  # no duplicate element, 可以 if nums[low] < nums[mid]
                if nums[low] <= target <= nums[mid]: #記得 <= target 有可能等於其中這兩個
                    high = mid 
                else:
                    low = mid 
            else:
                if nums[mid] <= target <= nums[high]: 
                    low = mid 
                else:
                    high = mid 
        
        if target == nums[low]:
            return low
        if target == nums[high]:
            return high

        return -1


#重寫第二次, time complexity O(logn), space complexity O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l + 1 < r:
            mid = l + (r-l) // 2
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        return -1




#重寫第三次, time complexity O(logn), space complexity O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) //2
            if nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1










'''
You may assume no duplicate exists in the array.

binary search
// 向下取整

a.search([0,1,2,4,5,6,7,8],8) ans:7

low=0 high=7
mid = 3 nums[mid]=4
low=4 high=7
mid = 5 nums[mid]=6
low=6 high=7
mid = 6 nums[6] = 7
low = 7 high = 7
mid =7 nums[7]=8 ans!

a.search([6,7,8,1,2,3,4,5],8) ans:2

a.search([7,8,1,2,3,4,5,6],1) ans:1


'''

