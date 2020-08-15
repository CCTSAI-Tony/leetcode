# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# time complexity O(n^2), 1316s, 刷題用這個
# 思路: 先nums.sort(), 選擇一個fixNum, nums[i] 並對nums[i+1:]數列進行 2 pointers 處理, 此題要注意的就是會有重複元素, 你要如何處理
# 一但組合找到, 還要對個別指針進行消除重複元素的動作
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort() #先排序
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue #往下一個迴圈繼續跑 避免重複選擇同一個fix_num
            l, r = i+1, len(nums)-1 # il..................r
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: #避免重複
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #避免重複
                        r -= 1
                    l += 1; r -= 1 #往下一個組合搜索
        return res

        #return  [list(t) for t in set(tuple(element) for element in res)] 利用set 避免重複

#自己重寫 time complexity O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            fix_num = nums[i]
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -fix_num:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -fix_num:
                    left += 1
                else:
                    right -= 1
        return res

#  自己想的 time complexity O(n^2) 1584s
#  思路: 利用fixNum, 在剩下的數組中搜尋2 elements sum to -fixNum => 把問題變成2 sum, 利用dict來紀錄之前的值
#  注意: ans_set 要add前 裡面的東西要先記得sorted, 不然會出現重複的答案只是順序不同
#  此方法跟上面最大不同是不用先對nums sort, 因為不是用雙指針
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        visited = [] #排除重複fixNum
        for i in range(len(nums)):
            dic = {}
            fixNum = nums[i]
            if fixNum in visited:
                continue
            visited.append(fixNum)
            new_nums = nums[:i] + nums[i+1:]
            for num in new_nums:
                if -fixNum-num in dic:
                    ans.add(tuple(sorted((fixNum, num, -fixNum-num ))))
                dic[num] = num
        return ans











