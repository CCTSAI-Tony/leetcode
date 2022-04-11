'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

# 刷題用這個, backtracking, time complexity O(n^(t/m)), space complexity O((t/m)), t: target value, m: minimal value
# 思路: 利用dfs 來尋找所有的組合, 但利用backtracking 來控制space complexity, and start index 來剪枝重複的答案
# start index 的作用在於只能單方向找尋答案來避免重複組合
# 這題的前提是 Given an array of distinct integers candidates
# 改進後的 108ms, 刷題用這個
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, candidates, target, [], res)
        return res
        
    def dfs(self, start, candidates, remain, path, res):
        if remain == 0:
            res.append(path.copy())
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.dfs(i, candidates, remain - candidates[i], path, res)
            path.pop()




# 重寫第二次, time complexity O(n^(t/m)), space complexity O(n^(t/m))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, candidates, target, [], res)
        return res
        
    def dfs(self, start, candidates, remain, path, res):
        if remain == 0:
            res.append(path.copy())
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.dfs(i, candidates, remain - candidates[i], path, res)
            path.pop()


# 重寫第三次, time complexity O(n^(t/m)), space complexity O((t/m))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(start, path, cur_sum):
            if cur_sum == target:
                ans.append(path.copy())
                return
            elif cur_sum > target:
                 return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                new_sum = cur_sum + candidates[i]
                dfs(i, path, new_sum)
                path.pop()
        dfs(0, [], 0)
        return ans


# 這個不好, 因為space complexity 比較大, comb 是list
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.backtrack(candidates, target, [], 0)
        return self.results

    def backtrack(self, candidates, remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            self.results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            self.backtrack(candidates, remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()




# naive dfs
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.dfs(candidates, 0 ,target, [], res)
        return res
    
    
    def dfs(self, candidates, index ,target, path, res):
        if target < 0:
            return
        if target == 0:
            res.add(tuple(path))
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, i ,target - candidates[i], path + [candidates[i]], res)


#重寫第二次, time complexity O(n^(t/m)), space complexity O(n^(t/m))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.dfs(candidates, target, 0, [], 0, res)
        return res
    
    def dfs(self, candidates, target, idx, path, total, res):
        if total > target:
            return
        if total == target:
            path.sort()
            res.add(tuple(path))
            return
        for i in range(idx, len(candidates)):
            self.dfs(candidates, target, i, path + [candidates[i]], total + candidates[i], res)


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort() 
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):  #利用指針來避免重複的組合
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
        



#自己想的, time complexity O(n^(t/m)), space complexity O(n^(t/m)), t: target value, m: minimal value
#思路: backtracking, 利用path.sort() 來避免重複組合
#改進, 使用指針來避免重複組合 ex: (2,3,5) or (3,2,5) (5,2,3), 或者 (2,2,3), (2,3,2)=>順序不一樣, 但都是同一組合
#指針使得後面元素無法回去找前面元素, 使得答案順序只有一種
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.dfs(candidates, target, [], res)
        return res
    
    
    def dfs(self, candidates, target, path, res):
        if target < 0:
            return
        if target == 0:
            path.sort()
            res.add(tuple(path))
            return
        for num in candidates:
            self.dfs(candidates, target - num, path + [num], res)

        '''
        haha, for DFS (backtracking) (BFS as well) you can remember this template, actually more or less they are fixed. 
        So this kind of interview questions is quite easy to handle.

        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
        find all unique combinations in candidates where the candidate numbers sums to target.
        The same repeated number may be chosen from candidates unlimited number of times.

        因為 input nums 並沒有重複element 應此output也不會重複

        Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.

        Sorting is not necessary here. The only help with sorting is that you can stop searching earlier by breaking the for loop
        when nums[i] is larger than target. Overall, it won't decrease the scale of time complexity.

        a.combinationSum([2,3,6,7],7)

        [[2, 2, 3], [7]]

        '''

















