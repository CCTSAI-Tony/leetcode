'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

 

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
 

Constraints:

1 <= n <= 107
'''


# 刷題用這個, time complexity O(n), space complexity O(logn)
# 思路: dfs backtracking
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1: 
            return []
        res = []
        def dfs(path, rest, target):  # 技巧, rest=2, skip 1 if target = 1
            if len(path)>0:
                res.append(path.copy()+[target])
            for i in range(rest, int(math.sqrt(target))+1): # i <= target//i, i.e., i <= sqrt(target)
                if target%i==0:
                    path.append(i)
                    dfs(path, i, target//i)
                    path.pop()
        path = []
        dfs(path, 2, n)
        return res
