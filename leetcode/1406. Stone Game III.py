'''
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, 
and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, 
that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, 
and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. 
The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. 
The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, 
otherwise she will lose.
Example 4:

Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"
Example 5:

Input: values = [-1,-2,-3]
Output: "Tie"
 

Constraints:

1 <= values.length <= 50000
-1000 <= values[i] <= 1000
'''



# 經典minmax!, time complexity O(n), space complexity O(n)
# 思路: 每回合, 可以取連續1, 2 or 3 堆的石頭, 此題就是經典dp minmax, 每個選手的選擇都是最佳化
# 技巧: 使用top down dp 來解題
# Alice start first
# dp[i] means, if we ignore before A[i], 從尾端算上來
# what's the highest score that Alice can win over the Bob？
# There are three option for Alice to choose.
# Take A[i], win take - dp[i+1]
# Take A[i] + A[i+1], win take - dp[i+2]
# Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]
# dp[i] equals the best outcome of these three solutions.

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        
        def dfs(start):
            if start >= len(stoneValue):
                return 0
            
            if start in memo:
                return memo[start]
            
            memo[start] = float('-inf') 
            score = 0
            
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))
            
            return memo[start]
        
        score = dfs(0)  
        return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(start):
            if start >= len(stoneValue):
                return 0
            if start in memo:
                return memo[start]
            memo[start] = float("-inf")
            score = 0
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i+1))
            return memo[start]
        alice_score = dfs(0)
        if alice_score > 0:
            return "Alice"
        elif alice_score < 0:
            return "Bob"
        return "Tie"


# 重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(start):
            if start >= len(stoneValue):
                return 0
            if start in memo:
                return memo[start]
            score = 0
            memo[start] = float("-inf")
            for i in range(start, min(start + 3, len(stoneValue))):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i+1))
            return memo[start]
        diff_score = dfs(0)
        if diff_score == 0:
            return "Tie"
        elif diff_score > 0:
            return "Alice"
        else:
            return "Bob"


