'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

#為什麼用dp而不是greedy, 因為coins 並不是單一個倍數
#DP BOTTOM UP, 參考別人修改 用這個
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]





#DP BOTTOM UP
class Solution(object):
    def coinChange(self, coins, amount):

        if not amount : return 0
        
        dp = [float("inf") for i in range(amount+1)]
        
        for i in range(1, amount+1) :
            if i in coins :  #just use that coin
                dp[i] = 1
            else :
                new = [coin for coin in coins if coin < i] #find any denomination smaller than coin
                if not new :  
                    dp[i] = float("inf")
                for j in new :
                    dp[i] = min(dp[i], 1 + dp[i-j])
        if dp[-1] == float("inf") :
            return -1

        return dp[-1]


# This solution is not very unique to what else is posted, but I hope the comments will help somebody understand the solution 
# if they are new to dynamic programming. This is essentially an unbounded knapsack problem

# The key to this solution is using the minCoins array where each value is the minimum amount of coins needed to create the amount equal to its index. 
# The zero-th index is a zero amount and initiating the rest of the values to amount+1 helps because you can never use more coins than the required amount 
# because the smallest possible coin is 1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = len(coins)
        
        # Values in this array equal the number of coins needed to achieve the cost of the index
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        
        # Loop through every needed amount
        for i in range(amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    # minCoins[i]: number of coins needed to make amount i
                    # minCoins[i-coin]: number of coins needed to make the amount before adding 
                    #                   the current coin to it (+1 to add the current coin)
                    minCoins[i] = min(minCoins[i], minCoins[i-coin] + 1)
        
        # Check if any combination of coins was found to create the amount
        if minCoins[amount] == amount + 1:
            return -1
        
        # Return the optimal number of coins to create the amount
        return minCoins[amount]









