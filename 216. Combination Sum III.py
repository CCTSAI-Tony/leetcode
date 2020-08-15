'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 
can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
#backtracking
class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(range(1,10), k, n, 0, [], res) #這邊使用range 生成器,功能跟list 一樣, 但儲存效率提高
        return res
    
    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking, return 回去換下一個,直到迭代完成
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in range(index, len(nums)): #len(nums) = 9
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)#use index(i+1) to control the next round range 

# a = (range(1,10))
# len(a)
# 9
# a[3]
# 4
# [a[i] for i in range(0,9)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [i for i in a]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [1,2,3,4,5,6,7,8,9]
        self.dfs(nums, k, n, 0, [], res)
        return res
    
    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)






