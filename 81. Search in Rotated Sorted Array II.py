# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part 消除重複, nums may contain duplicates  ex: [1,3,1,1,1] 3
                l += 1                             #最終 l = mid
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]: #target若在這區間 縮小搜索 若不是則在另一半
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]: #注意運算子
                    l = mid + 1
                else:
                    r = mid - 1
        return False


# 模板2 刷題用這個 time complexity O(logn) if no duplicate, O(n) if all are duplicate
# 思路:  這邊使用 nums[mid] <= nums[right]: 要排除右邊重複元素造成的假區間, 使得這區間呈現真實排序的情況, 不會因為重複元素干擾正確判斷而跳過target
# 跟leetcode 33 最大差別就是多了一種情況, nums[mid] = nums[right] or nums[left], 造成假區間, 其他都一樣
# 去除右邊與mid 重複的元素, 不然卡在這中間的target 會永遠找不到, ex: [1,1, *3, 1] 3
# 利用已掃除重複元素創造的真實區間, 就算另一邊有假區間, 也可以正確選擇target在哪邊
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            while right > mid and nums[right] == nums[mid]:  #去除右邊與mid 重複的元素, 因為 if nums[mid] = nums[right]: 有可能陷入假區間陷阱 
                right -= 1
            if nums[mid] <= nums[right]:  #這邊記得要<= 因為右邊已消除重複的元素, 消除到最後有可能等於, 處理方式要跟 < 一樣, 若不放= 進入else會造成錯亂
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
                
            else:  #若上面<=情況不成立而是 nums[mid] > nums[right], 則 nums[mid] 到 nums[left] 這個區間就不會出現假區間,可以安心使用, ex: [3,3,3,0,3] or [3,3,3,0,1] 
                                                                # 反之若出現假區間, 則上面=情況先成立, 左邊假區間 指的是 nums[mid] = nums[left] 但中間有其他元素 ex:[1,3,1,1,1]
                                                                # 上面 < 成立 不是已消除假區間, 不然就是原本就沒假區間 [1,1,3,1] or [1,1,1,3]
                if nums[mid] >= target >= nums[left]:
                    right = mid
                else:
                    left = mid
        if nums[left] == target or nums[right] == target:
            return True
        return False

# 重要!! 假區間只會發生在頭尾其中一邊, 且要發生假區間, 頭尾必定要同一元素 => 證明出else 的情況 不會出現假區間
# 重複元素有可能 nums[mid] = nums[right], ex: [2,0,1,2,2,2,2]
# Follow up:
# Would this affect the run-time complexity? How and why?
# yes, if all are the same elements, time complexity will become O(n)


#自己重寫 time complexity O(lgn) if no duplicate, O(n) if all are duplicate
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            while mid < right and nums[mid] == nums[right]:
                right -= 1
            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
        if nums[left] == target or nums[right] == target:
            return True
        return False






# 模板2 刷題用這個 time complexity O(logn)
# 思路: 這邊使用  nums[mid] >= nums[left]: 要排除左邊重複元素造成的假區間, 使得這區間呈現真實排序的情況, 不會因為重複元素干擾正確判斷而跳過target
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            while left < mid and nums[left] == nums[mid]:
                left += 1
            if nums[mid] >= nums[left]:
                if nums[mid] >= target >= nums[left]:
                    right = mid
                else:
                    left = mid
                
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target or nums[right] == target:
            return True
        return False

'''
May I ask why you consider only nums[l] == nums[mid]?
Why don't we need this?
while r > mid and nums[r] == nums[mid]: # tricky part
r -= 1


Mid is a floor of (l+r)//2, so it can be equal to l. 
We want to make sure that the equal sign in condition nums[i] <= nums[mid] only happens when l = mid, 
so you have to remove the duplicates for the left. However for the right, it's not necessary, 
and it can make the calculation slower. For example find 2 in [0, 1, 2, 3, 3, 3, 3, 3, 3, 3], 
all the 3s can be skipped in a O(logN) manner if you don't do the r -=1, if you do, it will be O(N)







[0,0,0,0,0,0,1,2,2,5,6]   5
l          m         r
           l   m     r
'''









'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''