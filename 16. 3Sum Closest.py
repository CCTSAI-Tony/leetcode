# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum #找到就直接公布答案
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result



#  自己重寫 time complexity O(n^2), 刷題用這個
#  思路: 先nums.sort(), 找定fixNum, nums[i], 再對剩下的nums[i+1:] 進行2 pointers處理
#  依temp = nums[i] + nums[left] + nums[right] 對target的值比較來進行微調, 若大於target 右往左一格, 小於target 左往右一格
#  每動一次就查看temp離target的絕對值是否比較小, 若是則res = temp
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]: #避免重複fixNum
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp < target:
                    left += 1
                elif temp > target:
                    right -= 1
                else:
                    return temp
                if abs(target - temp) < abs(target - res):
                    res = temp
        return res
        
#重寫第二次 time complexity O(n^2)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet_num = float("inf")
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[i-1]:  #優化
                continue
            fix_num = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = fix_num + nums[l] + nums[r]
                if abs(threeSum - target) < closet_num:
                    res = threeSum
                    closet_num = abs(threeSum - target)
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    return threeSum
        return res







