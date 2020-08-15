'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

class Solution:
    def maxProfit4(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        # k is big enougth to cover all ramps.
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0) #sum函數用法
        globalMax = [[0] * n for _ in range(k + 1)] #range(k+1) 表示0 transaction 至 k transaction
        for i in range(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            localMax = [0] * n
            for j in range(1, n): # i for whichtime transaction, j for whitch day
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    # We have made max profit with (i - 1) transactions in
                    # (j - 1) days.
                    # For the last transaction, we buy stock on day (j - 1)
                    # and sell it on day j.
                    globalMax[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transactions in
                    # (j - 1) days.
                    # For the last transaction, we buy stock on day j and
                    # sell it on the same day, so we have 0 profit, apparently
                    # we do not have to add it.
                    globalMax[i - 1][j - 1],  # + 0,
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1)  sale and sell it on day j.  localMax[j - 1] and localMax[j] 都是在一樣i的情況
                    localMax[j - 1] + profit) #所以cancel the day (j - 1)  sale and sell it on day j 就是交易次數還是一樣, 前一天的profit 不算一次交易次數
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]

'''
list(zip(prices[1:], prices[:-1])) = list((zip([2,6,5,0,3], [3,2,6,5,0]))) -> [(2, 3), (6, 2), (5, 6), (0, 5), (3, 0)]




'''
'''
I think the general idea has been thoroughly explained by other brilliant leetcoders. 
All of the solutions are beautiful and concise. However, most of the them don't look obvious to me,
so I wrote this and hope it looks more straight forward.
It's O(kn), apparently not optimal. 
I name the key variables as local profit and global profit to make things much understandable (well, at least , to me). 
Performance is not too bad though.
'''

# zip() in Python

# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

# name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
# roll_no = [ 4, 1, 3, 2 ] 
# marks = [ 40, 50, 60, 70 ] 
  
# # using zip() to map values 
# mapped = zip(name, roll_no, marks) 
  
# # converting values to print as set 
# mapped = set(mapped) 
  
# # printing resultant values  
# print ("The zipped result is : ",end="") 
# print (mapped) 

# The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
# ('Manjeet', 4, 40), ('Nikhil', 1, 50)}






#簡化版
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    
        if not prices:
            return 0
        
        if k >= len(prices) // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        
        
        profits = [0]*len(prices)
        for j in range(k):

            preprofit = 0
            for i in range(1,len(prices)):
            
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit+profit, profits[i]) #此時的profits[i] 是在交易次數j-1的情況, 交易次數越多 錢不會比交易次數少的 來得少
                profits[i] = max(profits[i-1], preprofit) #preprofit 有可能比profits[i-1] 想像profit 為負的r
    
        return profits[-1]













