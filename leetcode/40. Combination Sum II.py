# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# 刷題用這個, time complexity O(2^n), space complexity O(n)
# 思路: backtracking, 經典!!
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(-1, candidates, target, res, [])
        return res
        
    def dfs(self, i, candidates, target, res, path):
        if i >= len(candidates) or target < 0:
            return
        if target == 0:
            res.append(path[:])
            return
        j = i + 1
        while j < len(candidates):
            num = candidates[j]
            if j > i + 1 and candidates[j] == candidates[j-1]:
                j += 1
                continue
            path += [num]
            self.dfs(j, candidates, target - num, res, path)
            path.pop()
            j += 1



# time complexity O(2^n), backtracking 刷題用這個
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()  #先排序很重要, 以利之後dfs剪枝
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue  #避免當層出現重複元素並往下展開
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res) #i+1 當前元素只能用一次



#重寫第二次, time complexity O(2^n), space complexity O(2^n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates. sort()
        self.res = []
        self.dfs(0, candidates, target, [], 0)
        return self.res
        
    def dfs(self, idx, candidates, target, path, curSum):
        if curSum >= target:
            if curSum == target:
                self.res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(i + 1, candidates, target, path + [candidates[i]], curSum + candidates[i])



重寫第三次, time complexity O(2^n), space complexity O(2^n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        self.res = []
        candidates.sort()
        self.dfs(0, candidates, [], 0, target)
        return self.res
    
    
    def dfs(self, idx, candidates, path, curSum, target):
        if curSum >= target:
            if curSum == target:
                self.res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(i + 1, candidates, path + [candidates[i]], curSum + candidates[i], target)







'''
DP法 buttom up  time complexity O(n^2), 很棒的技巧, 但很難想
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  #先排序很重要
        table = [set() for i in range(target +1 )] #range(target +1 ), zero based index issue
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1): #這邊range(target - i, 0, -1), range倒序到0 因為元素都是正的, 最小為1
                table[i + j] |= {elt + (i,) for elt in table[j]} #at beginning, there is nothing, |=, 新的加入, 有重複的不加入, 這是屬於set的專屬操作

            table[i].add((i,))  #別忘了自己的table也要新增元素

        return list(map(list, table[target])) #return table[target]每個項目 並用list 表現, 記得 map函數 外面要包一層list(), 不然無法顯現 <map at 0x108284780>
        #也可以 return [list(i) for i in table[target]]



r    s    r|=s
--------------
T    T    T
T    F    T
F    T    T
F    F    F

a = {1,2,3}
a |= {2,4}
a
{1, 2, 3, 4}





        a = (3,)
        a+=(4,)
        print(a)
        (3, 4)
         
         table = [None] + [set() for i in range(3)]
            print(table)
            [None, set(), set(), set()]
         



         利用set 可以避免重複 例如 [1,1,1,1,1,1] target:2
         ans: [(1,1)]
    
        
'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8,  sort[1,1,2,5,6,7,10]
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

for i in range(10,5,-1): 
    print (i)

10
9
8
7
6




'''
