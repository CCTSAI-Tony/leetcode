'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), 
amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, 
have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 先建立完整的hash table, 主key = time, sub key = name, value = city list, 之後再完整遍歷transactions 來找出invalid
from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        memo = defaultdict(dict)
        invalid = []        
        for item in transactions:
            name, time, amount, city = item.split(",")
            if time not in memo:
                memo[int(time)][name]=[city]
            else:
                if name not in memo[time]:
                    memo[int(time)][name]=[city]
                else:
                    memo[int(time)][name].append(city)
        for item in transactions:
            name, time, amount, city = item.split(",")
            if int(amount) > 1000:
                invalid.append(item)
                continue
            for j in range(max(0, int(time)-60), int(time)+61):
                if j not in memo:
                    continue
                if name not in memo[j]:
                    continue
                if len(memo[j][name]) > 1 or (memo[j][name][0] != city): #多重city 或不同city
                    invalid.append(item)
                    break              
        return invalid   





