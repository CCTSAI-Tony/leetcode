'''
Given an array of scores that are non-negative integers. 
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
Each time a player picks a number, that number will not be available for the next player. 
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''

# Solution 1: Recursion with memo, 32ms AC 98%.
# helper(i, j) return the margin of the score when it's current player's turn and the array left are nums[i]..nums[j] inclusively.
# Complexity, Time: O(n^2), Space: O(n)
# 思路: top down dp, 建立memo, state = (i,j) => 目前可以選擇的牌
# 自己turn的分數 - 對方turn的分數, 若 >= 0, 則代表我方獲勝
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}            
        return self.helper(0, len(nums)-1, nums, memo) >= 0

    def helper(self, i, j, nums, memo):
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            score = max(nums[j] - self.helper(i, j-1, nums, memo), nums[i] - self.helper(i+1, j, nums, memo)) 
            memo[(i, j)] = score
            
            return memo[(i, j)]




# Solution2: dynamic programming, dp[i][j] is the margin of the score when it's current player's turn and the array left are nums[i]..nums[j] inclusively.
# Complexity, Time: O(n^2), Space: O(n^2)
# dp[i][j] the person's effective score when pick, facing nums[i..j]
# 刷題用這個, time complexity O(n^2), space complexity O(n^2)
# 思路: dp[i][j] 當局的人可以獲得的最高有效分, 當nums array 只剩 nums[i:j+1], 此有效分是扣掉對方的turn得到的結果
# 技巧: 使用s 代表間隔 一步一步建立上去, 跟上面top down 只解決需要的子問題概念有些不同
 class Solution:
     def PredictTheWinner(self, nums: List[int]) -> bool:
         dp = [[0] * len(nums) for _ in range(len(nums))]
         for s in range(len(nums)): #s: 間距
             for i in range(len(nums)-s):
                 j = i + s
                 if i == j:
                     dp[i][i] = nums[i]
                 else:
                     dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j]) #自己turn - 對方的rurn
         return dp[0][-1] >= 0


#自己重寫 32ms
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for s in range(len(nums)):
            for i in range(len(nums)-s):
                j = i + s
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
                    
        return dp[0][-1] >= 0



# Solution 3: the dp updates the hill diagnal which depends only on previous hill diagal, so it could be turned to a 1-D DP.
# Complexity, Time: O(n^2), Space: O(n)
# 思路: 觀察上面的dp 可以發現dp updates 是依靠前面compute的diagonal, 所以嘗試2d > 1d, 畫個圖就清楚了 n*n
# 利用額外創造出的new_dp 來充當右邊新的diagonal, new_dp[j] 相當於 dp[j-s][j], 好招!
 class Solution:
     def PredictTheWinner(self, nums: List[int]) -> bool:
         n = len(nums)
         dp = nums[:] #copy => 此時的dp[i] 相當於 上面dp的 dp[i][j] => i == j
       
         for s in range(1, n):  #s: 間距
             newdp = [0] * n
             for j in range(s, n):
                 i = j - s
                 newdp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
                
             dp = newdp
         return dp[-1] >= 0



#自己重寫 44ms
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = nums[:]
        for s in range(1, len(nums)):
            new_dp = [0 for _ in range(len(nums))]
            for j in range(s, len(nums)):
                i = j - s
                new_dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
            
            dp = new_dp
        
        return dp[-1] >= 0



