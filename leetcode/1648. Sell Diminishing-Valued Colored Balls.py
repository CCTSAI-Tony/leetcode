'''
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. 
Each colored ball's value is the number of balls of that color you currently have in your inventory. 
For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. 
After the transaction, there are only 5 yellow balls left, 
so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. 
You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
 

Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
'''

Algo
First, it should be clear that we want to sell from the most abundant balls as much as possible as it is valued more than less abundant balls. In the spirit of this, we propose the below algo

sort inventory in reverse order and append 0 at the end (for termination);
scan through the inventory, and add the difference between adjacent categories to answer.
Assume inventory = [2,8,4,10,6]. Then, we traverse inventory following 10->8->6->4->2->0. The evolution of inventory becomes

10 | 8 | 6 | 4 | 2
 8 | 8 | 6 | 4 | 2
 6 | 6 | 6 | 4 | 2
 4 | 4 | 4 | 4 | 2
 2 | 2 | 2 | 2 | 2 
 0 | 0 | 0 | 0 | 0 

Of course, if in any step, we have enough order, return the answer.

ans += k*(inventory[i] - q + 1 + inventory[i]) * q//2 + r*(inventory[i] - q) 
say if k = 3, inventory[i] = 4, inventory[i+1] = 2, orders = 5
basically the question becomes: [4,4,4,2], orders = 5, what is the max value?

the answer would be we pick the first three balls (k = 3) one round (q=1), ans = 4 + 4 + 4
then it comes to [3,3,3, 2] orders = 5 - 3 = 2, what is the max value:
we could get the max value by picking the first two colored ball with the number of 1: 3 + 3 (r =2), equivillant to:

r*(inventory[i] - q) -> 2 * (4-1)


# 刷題用這個 greedy
# 思路: 使用 arithmic sum  公式, k代表有多少相同上底數量的ball, 下底則是下一個球數量+1, 高: 上底數量 - 下一個數量(數量差ex: 10-7 => 3 => 10, 9, 8)
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]  # 這步很重要
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(inventory[i] + inventory[i] - q + 1) * q//2 + r*(inventory[i] - q) 
                    return ans % (10**9+7)
            k += 1 # 這步很重要累積k


# 重寫第二次
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory += [0]
        k = 1
        ans = 0
        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                if k * (inventory[i] - inventory[i+1]) < orders:
                    ans += k*(inventory[i]+ inventory[i+1] + 1)*(inventory[i] - inventory[i+1]) // 2
                    orders -= k * (inventory[i] - inventory[i+1])
                else:
                    q, r = divmod(orders, k)
                    ans += k*(inventory[i] + inventory[i] - q + 1)*q // 2 + r*(inventory[i] - q)
                    return ans % (10**9 + 7)
                
            k += 1


# naive algorithm, time complexity O(min(sum(inventory[i]), 109))
from collections import defaultdict
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        max_value = 0
        memo = defaultdict(int)
        res = 0
        for amount in inventory:
            max_value = max(max_value, amount)
            memo[amount] += 1
        while orders > 0:
            res += max_value
            memo[max_value] -= 1
            memo[max_value - 1] += 1
            if not memo[max_value]:
                max_value -= 1
            orders -= 1
        return res



