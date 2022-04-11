'''
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

 

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

Constraints:

1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi <= 20
fromi != toi
1 <= amounti <= 100
'''

'''
Just to share a backtracking + greedy solution. The Python implementation was accepted.

First, compute net profit for every person.

For transactions:
[0, 1, 10]
[2, 0, 5]

Person, netProfit
0,         -5
1,         10
2,         -5
Then, preserve unsettled people only whose net profit != 0.

Now backtrack to maintain the unsettled range [startIdx :]. Person X is settled means that X's net profit becomes 0 after one transaction with another unsettled person Y. 
Obviously, the amount of this transaction must be equal to X's net profit in their absolute values for X to be settled.

Note that there may be some settled people within the unsettled range [startIdx :]. 
For instance, if someone within this unsettled range happened to be precisely closed out by someone else in the settled range.

The greedy condition is precise closing-out (two people's net profit sum = 0). 
Since precise closing-out reduces number of unsettled people by 2 rather than 1, it is in fact the optimal condition.

If greedy condition cannot be found, try non-greedy solutions.

'''


# 刷題用這個, time complexity O(n*2^n), space complexity O(2^n)
# 思路: greedy + backtracking, 詳細解法請看上面
class Solution(object):
    def minTransfers(self, transactions):
        # Compute net profit for every person.
        personNetProfit = dict()
        for lender, borrower, amount in transactions:
            personNetProfit[lender] = personNetProfit.get(lender, 0) - amount
            personNetProfit[borrower] = personNetProfit.get(borrower, 0) + amount
        # Preserve unsettled people only.
        netProfit = []
        for amount in personNetProfit.values():
            if amount != 0:
                netProfit.append(amount)
        return self.traverse(netProfit, 0, 0)
    
    def traverse(self, netProfit, startIdx, numTrans):
        # Skip settled people.
        while startIdx < len(netProfit) and netProfit[startIdx] == 0:
            startIdx += 1
        if startIdx + 1 >= len(netProfit):
            return numTrans
        else:
            for i in range(startIdx + 1, len(netProfit)):
                # Greedy condition.
                if netProfit[startIdx] + netProfit[i] == 0:
                    netProfit[i] += netProfit[startIdx]
                    minNumTrans = self.traverse(netProfit, startIdx + 1, numTrans + 1)
                    netProfit[i] -= netProfit[startIdx]  # back tracking
                    return minNumTrans
            minNumTrans = float("inf")
            for i in range(startIdx + 1, len(netProfit)):
                # Non-greedy condition for possible closing out in the future.
                if netProfit[startIdx] * netProfit[i] < 0:  # 一正一負
                    netProfit[i] += netProfit[startIdx]
                    minNumTrans = min(minNumTrans, self.traverse(netProfit, startIdx + 1, numTrans + 1))
                    netProfit[i] -= netProfit[startIdx]
            return minNumTrans


# 重寫第二次, time complexity O(n*2^n), space complexity O(2^n)
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        personNetProfit = defaultdict(int)
        for lender, borrower, amount in transactions:
            personNetProfit[lender] -= amount
            personNetProfit[borrower] += amount
        netProfit = []
        for amount in personNetProfit.values():
            if amount != 0:
                netProfit.append(amount)
        return self.traverse(netProfit, 0, 0)
    
    def traverse(self, netProfit, start_idx, numTrans):
        while start_idx < len(netProfit) and netProfit[start_idx] == 0:
            start_idx += 1
        if start_idx + 1 >= len(netProfit):
            return numTrans
        else:
            for i in range(start_idx + 1, len(netProfit)):
                if netProfit[start_idx] + netProfit[i] == 0:
                    netProfit[i] += netProfit[start_idx]
                    minNumTrans = self.traverse(netProfit, start_idx + 1, numTrans + 1)
                    netProfit[i] -= netProfit[start_idx]
                    return minNumTrans
            minNumTrans = float("inf")
            for i in range(start_idx + 1, len(netProfit)):
                if netProfit[start_idx] * netProfit[i] < 0:
                    netProfit[i] += netProfit[start_idx]
                    minNumTrans = min(minNumTrans, self.traverse(netProfit, start_idx + 1, numTrans + 1))
                    netProfit[i] -= netProfit[start_idx]
            return minNumTrans





