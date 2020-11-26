'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

# Easy to understand one:
# dp[i][0] is the max account balance if there is no stock on hold
# dp[i][1] is the max account balance if there is a stock on hold

#搭配121,122 一起服用
#time complexity O(n)
#思路: dp[i][0] is the max account balance if there is no stock on hold, dp[i][1] is the max account balance if there is a stock on hold
#初始值, dp[0] = [0,0] 代表unhold stock balance 與 hold stock balance 都是0
#這題的想法就是分成手上無stock的max balance 與 有stock的max balance, 買在便宜賣在貴
#再計算當天hold stock max balace, why we use dp[i-2][0], cause dp[i-1][0] could have sell condition may violate cooldown restriction
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for _ in range(n+1)]
        dp[1][1] = 0 - prices[0] 
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])    #last day unhold balance or sell the stock on i-th day based on last day hold stock balance
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1]) # buy on i-th day based on two days ago unhold balance or yesterday hold balance, 
        return max(dp[-1]) #查看最後一天哪種狀況最多錢 其實也可 return dp[-1][0]



#自己重寫, time complexity O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0,0] for _ in range(len(prices)+ 1)]
        dp[1][1] = 0 - prices[0]
        for i in range(2, len(prices)+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
        return max(dp[-1])













# When we update dp[i][1], if we buy

#           / dp[i-2][0] ==> dp[i-1][0] == dp[i-2][0]
# dp[i-1][0]
#           \ dp[i-2][1] + prices[i-2] 賣掉股票
#              ==> have cool time at dp[i-1][0] may infect dp[i][1], thus have to use 
#              dp[i-2][0]
# Basing on the above analysis, we have to use dp[i-2][0].

# I am confused that the DP formula does not show the cool-down part.

# Because of the cooldown, dp[i][1] couldn't come from buying on i th day if i-1 th day was a sell, 
# so dp[i][1] = max(dp[i-1][0] - prices[i-1], dp[i-1][1]) if no cooldown rule