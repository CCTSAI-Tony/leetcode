# time complexity O(n^2)
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:  #當層看 ex:[1,2,2], 確保i = index時 該element 依然被計算, i > index時 且nums[i] == nums[i-1] 則跳過
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)

#刷題用這個
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:  #當層看 ex:[1,2,2], 確保i = index時 該element 依然被計算, i > index時 且nums[i] == nums[i-1] 則跳過
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()



''' 
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


'''