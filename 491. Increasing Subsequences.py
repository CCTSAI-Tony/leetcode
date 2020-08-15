'''
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, 
and the length of an increasing subsequence should be at least 2.

 

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
'''

#自己想的 backtracking 288ms 刷題用這個
#time complexity O(2^n)
#思路: 利用backtracking 來探訪 all possible solution
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set() #過濾重複
        self.dfs(0,nums,[],res)
        return res
    
    def dfs(self, index, nums, array, res):
        if index == len(nums): #到底層return
            if len(array) >= 2:
                res.add(tuple(array))
            return
        if len(array) >= 2: #超過等於2字 就紀錄
            res.add(tuple(array))
            
        if array and nums[index] >= array[-1]: #當前數字大於array[-1], increasing subsequence
            self.dfs(index+1, nums, array+[nums[index]], res)
        if not array:  #加入當前數字為第一個數字
            self.dfs(index+1, nums, array+[nums[index]], res)
            
        self.dfs(index+1, nums, array, res)  #不包含當前數字






