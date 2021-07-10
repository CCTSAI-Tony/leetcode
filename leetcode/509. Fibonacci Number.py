'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
'''

#自己想的
#思路: dp
class Solution:
    def fib(self, N: int) -> int:
        if not N:
            return 0
        dp = [0] * (N + 1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]



#重寫第二次, time complexity O(n), space complexity O(n)
from functools import lru_cache
class Solution:
    @lru_cache
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)



#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        return self.helper(N, memo)
    
    def helper(self, N, memo):
        if N in memo:
            return memo[N]
        memo[N] = self.helper(N-1, memo) + self.helper(N-2, memo)
        return memo[N]

#重寫第四次, time complexity O(n), space complexity O(n)
class Solution:
    memo = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n not in self.memo:
            fib_n = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = fib_n
        return self.memo[n]




#使用memo decorator
class Memorize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memorize  
def fib2(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib2(N-1) + fib2(N-2)


class Solution:
    def fib(self, N: int) -> int:
        return fib2(N)