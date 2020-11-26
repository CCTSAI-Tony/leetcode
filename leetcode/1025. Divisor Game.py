'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000
'''

#time complexity O(n^2), space complexity O(n)
#思路: bottom up dp, 經典 => dp[i] 會參考下一輪對手會不會贏
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]): #下一輪對手不會贏
                        dp[i] = True
                        break
        return dp[N]




#code signal => pick game => [1,4,5,5,6] => [1,4,6] => who can't pick two same consecutive elments lose
class Solution:
    def pickGame(self, array: list) -> bool:
        memo = {}
        return self.dfs(array, memo)
    
    def dfs(self, array, memo):
        if tuple(array) in memo:
            return memo[tuple(array)]
        memo[tuple(array)] = False
        for i in range(1, len(array)):
            if array[i] == array[i-1]:
                new = tuple(array[:i-1] + array[i+1:])
                if not self.dfs(new, memo):
                    memo[tuple(array)] = True
        return memo[tuple(array)]















