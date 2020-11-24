'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''
#自己重寫, time complexity O(n), 此題只允許一次交易 => 總共買與賣個一次
#思路: greedy, 隨著指針紀錄最小價格, 並遍歷每天股價同時紀錄當天股價-最小股價的獲利, update 最大獲利, 同時遵守賣股票的日期一定出現在買股票日期的後面或當天
#可以允許當天買當天賣, 當然這樣獲利為0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float("inf")
        profit = float("-inf")
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)
        
        return profit  #profit 至少為0 當天買當天賣=>相當於什麼都不買

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, (price - min_price))
        return max_profit

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for num in prices:
            min_price = min(min_price, num)
            max_profit = max(max_profit, num-min_price)
        return max_profit






class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        min = prices[0]
        max_profit = float('-inf')
        for i in range(1, len(prices)):
            profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
            max_profit = max(max_profit, profit)
        return max(0, max_profit) #要注意避免負數 所以設個0, 因為可以什麼都不買

#idea: store max_profit, and change min