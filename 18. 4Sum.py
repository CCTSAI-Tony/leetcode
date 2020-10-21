'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
                sum2 = nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2] = [(i,j)]
        
        result = set() #Unordered collections of unique elements set={} 避免重複
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l: #避免重複使用到同一個num
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            result.add(tuple(flist)) #把flist tuple化 
        return list(result)

        #nums = (1,2,4,4,5,6) 
        #d={3: [(0, 1)], 5: [(0, 2), (0, 3)], 6: [(0, 4), (1, 2), (1, 3)], 7: [(0, 5), (1, 4)], 8: [(1, 5), (2, 3)], 9: [(2, 4), (3, 4)], 10: [(2, 5), (3, 5)], 11: [(4, 5)]}
        #idea: find out all combination of two sum and target equals two among them, but filter equal element and use set to filter equal answer


#  自己重寫 time complexity O(n * m * p), n = len(dic), m = len(dic[sum1]), p = len(dic[sum2]), 128ms, 刷題用這個!!
#  利用dict, 增加space complexity 來降低time complexity
#  思路: 利用dict 來儲存所有兩個不同元素的組合,key = 兩個元素的和, 值 = 兩個元素indeces, 並從dict找出兩組key value的和 = target, key value可以重複 ex: 4+4 = 8
#  再分別遍歷這兩組key 裡面的組合, 確認是否有共用的元素, 若無則新增這一組 四個元素的組合
#  雖然這四個元素位置跟其他組不可能全部一樣, 但有可能值相同, 因此res 要使用set來過濾重複的答案
import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        dic = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum1 = nums[i] + nums[j]
                dic[sum1].append((i,j))
        
        for sum1 in dic:
            sum2 = target - sum1
            if sum2 in dic:  #key in dict is an O(1) operation.
                for tuple1 in dic[sum1]:
                    for tuple2 in dic[sum2]:
                        i, j = tuple1
                        k, l = tuple2
                        if i != k and i != l and j != k and j != l: #避免重複使用到同一個元素
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))) #記得add 至 set前, 要sorted, 不然不同順序set會認為是不同的組合
        return res



#  相比上面方法space complexity較低, 但大大增加time complexity
#  自己想的, 延續3sum time complexity O(n^3), 而且還有sort() 增加loading, 1152ms
#  思路: fix 2 nums, 剩下2 nums 再以左右指針遍歷, 相比上面方法一組fix_num1 & fix_num2 需找第三第四元素時, 遍歷太多不要的candidate
import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #避免重複fix_num1
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]: #避免重複fix_num2
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1             
        return res










