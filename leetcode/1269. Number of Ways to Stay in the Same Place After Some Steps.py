'''
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 
1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
'''

#自己想的, memo dp, time O(m*n) space O(m*n), m:len(steps), n:len(arrLen)
#思路: 建立memo, key = (pos, steps), base case: if steps == 0 and pos == 0 => return 1 else 0, if pos 超過區間 => return 0, 
#有三個子問題 => 向左, 向右, 不動 => 會出現重複子問題 => 使用dp
#可以優化: 最大index遍歷距離 <= steps//2, 不然回不來
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        return self.dfs(0, steps, arrLen, memo) % (10**9 + 7)
    
    def dfs(self, pos, steps, arrLen, memo):
        if (pos, steps) in memo:
            return memo[(pos, steps)] 
        if steps == 0:
            if pos == 0:
                return 1
            return 0
        if pos < 0 or pos >= arrLen:
            return 0
        stay = self.dfs(pos, steps-1, arrLen, memo)
        left = self.dfs(pos-1, steps-1, arrLen, memo)
        right = self.dfs(pos+1, steps-1, arrLen, memo)
        memo[(pos, steps)] = stay + left + right
        return memo[(pos, steps)]

#優化版, time O(steps * min(steps//2, arrLen)), space O(steps * min(steps//2, arrLen))
#思路: 最大index遍歷距離 <= steps//2, 不然回不來
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        max_index = min(steps//2+1, arrLen)
        return self.dfs(0, steps, arrLen, memo, max_index) % (10**9 + 7)
    
    def dfs(self, pos, steps, arrLen, memo, max_index):
        if (pos, steps) in memo:
            return memo[(pos, steps)] 
        if steps == 0:
            if pos == 0:
                return 1
            return 0
        if pos < 0 or pos >= max_index:
            return 0
        stay = self.dfs(pos, steps-1, arrLen, memo, max_index)
        left = self.dfs(pos-1, steps-1, arrLen, memo, max_index)
        right = self.dfs(pos+1, steps-1, arrLen, memo, max_index)
        memo[(pos, steps)] = stay + left + right
        return memo[(pos, steps)]





