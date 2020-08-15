'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''

We give each account an ID, based on the index of it within the list of accounts.

[
["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
["John", "johnnybravo@mail.com"], # Account 1
["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
["Mary", "mary@mail.com"] # Account 3
]
Next, build an emails_accounts_map that maps an email to a list of accounts, 
which can be used to track which email is linked to which account. This is essentially our graph.

# emails_accounts_map of email to account ID
{
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0], #因為id: 0 已經被上面遍歷過了, 所以可以跳過
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}
Next we do a DFS on each account in accounts list and look up emails_accounts_map to tell us which accounts are linked to that particular account via common emails. 
This will make sure we visit each account only once. This is a recursive process and we should collect all the emails that we encounter along the way.

Lastly, sort the collected emails and add it to final results, res along with the name.

- Yangshun

# 思路: 經典dfs graph題, 記得遍歷過的節點要標記以防再次遍歷, 只對未發現的節點往下遍歷 課本p607 看了就理解, 
# 課本是directed graph, 此題是undirected graph, 每個edge都是tree edge and back edge, 但dfs 遍歷精神都是一樣的
# 首先要建立每個email 對應到的account id(graph), 再利用帳號底下每個mail搭配account id(graph) 進行dfs遍歷
# 每完成一次完整的dfs相當於遍歷完一個subgraph的所有節點, 等於收集完這所有關聯 accounts 的 emails
# Time complexity O(NlogN), N is total lenth of mails, 因為sorted()
from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):  #enumerate 功用: 提供id
            for j in range(1, len(account)):  #why range 0, 因為range 0 是姓名
                email = account[j]
                emails_accounts_map[email].append(i)
        
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]: #以遍歷過的帳號就無需再次遍歷
                continue
            name, emails = account[0], set()  #為何用set, 因為要去除兩個帳號的重複common email
            self.dfs(i, accounts, emails, visited_accounts, emails_accounts_map)
            res.append([name] + sorted(emails)) #把收集的email set 與使用者綁定, sorted(set()) 是list
        return res

    # DFS code for traversing accounts.
    def dfs(self, i, accounts, emails, visited_accounts, emails_accounts_map): #這邊的emails當作一個收集set()
        if visited_accounts[i]:  #因為已加入set
            return
        visited_accounts[i] = True  #mark, 若不畫記會陷入無限循環, 
        for j in range(1, len(accounts[i])):  #針對該帳號底下的每個mail 來做dfs 看是否有其他帳號擁有該相同mail並收集該帳號mail, 本題最難的地方
            email = accounts[i][j]
            emails.add(email)
            for neighbor in emails_accounts_map[email]:  #遍歷擁有相同mail的帳號
                self.dfs(neighbor, accounts, emails, visited_accounts, emails_accounts_map)

#看以下例子, 利用帳號下面的mail 來觸發
{
  "johnsmith@mail.com": [0, 2], #combine 0, 2
  "john00@mail.com": [0, 3], #combine 3 to [0, 2]
  "johnnybravo@mail.com": [1, 2], #combine 1 to [0, 2, 3], 以上都發生在
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}




