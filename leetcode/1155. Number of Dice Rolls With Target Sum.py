'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
'''

#自己想的 time complexity O(f^d), 536ms
#思路: 遇到要mod 很大值的題, 大多都是dp, 另外角度思考此題有許多重複的子問題 => 使用 dp
#使用lru_cache 當作 memo, base case 當d == 0, target == 0 return 1, target != 0 return 0
# dfs(self, d, f, target) = dfs(d-1, f, target - (i+1)) for i in range(f)
from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        return self.dfs(d, f, target) % mod
    
    @lru_cache(None)
    def dfs(self, d, f, target):
        if d == 0:
            return 1 if target == 0 else 0
        res = 0
        for i in range(f):
            res += self.dfs(d-1, f, target - (i+1))
        return res





























