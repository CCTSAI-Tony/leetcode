'''
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], 
website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
'''


'''
1) The idea is to use min heap to sort the websites visited by each user in ascending order.
2) then use a dict with users as keys and visited website as values
3) traverse through each of these lists of websites and create a sequence of 3 for all possible combinations
4) find the count for each of the sequence
'''

#參考別人, 刷題用這個
#Time Complexity: O(n*k^3), n: len(user), k: max_len(visited_webs of same user)
#思路: 首先zip username, timestamp, website, 然後對其依time stamp 做排序, 建一個dict => user: visited webs
#若前一步奏沒有排序, 則個別user visited webs 順序會亂, 
#再建一個dict 紀錄所有3_sequence 的組合: count, 使用iteration combinations 來對個別user visited_web 做挑選, 
#記得用set消除同個user 的重複組合sequence, 同個user 相同的3_sequence, count 只能算1 => 超級重要!!
#注意: combonation 的每一個組合都是升序排列的, 因為之前按照時間排序過了, 利用這個特性就可以當作sequence 的 key
#最後利用sorted 回報 sequence.items() 裡面count 最多且lexico 最小的key, 因為sort 是升序, 紀錄count的時候是-=1
from itertools import combinations
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        sequence = defaultdict(int)
        user_web = defaultdict(list)
        zip_items = list(zip(username, timestamp, website))
        zip_items.sort(key=lambda x: x[1]) #先對時間排序
        for user, time, web in zip_items:
            user_web[user].append(web)
        for user in user_web.keys():
            if len(user_web[user]) < 3:
                continue
            for comb in set(combinations(user_web[user], 3)): #time complexity: k^3
                sequence[comb] -= 1
        return sorted(sequence.items(), key=lambda x: (x[1], x[0]))[0][0]
        


# from itertools import combinations 
# a = [1,2,3,4]
# list(combinations(a, 3)) 
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

#重寫第二次, time complexity O(n*k^3), space complexity O(n*k^3)
from itertools import combinations
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        sequences = defaultdict(int)
        webs = defaultdict(list)
        for username, website, timestamp in sorted(zip(username, website, timestamp), key=lambda x: x[2]):
            webs[username].append(website)
        for user in webs:
            if len(webs[user]) < 3:
                continue
            for comb in set(combinations(webs[user], 3)):
                sequences[comb] -= 1
        return min(sequences.items(), key=lambda x: (x[1], x[0]))[0]



#自己想的, 暴力解 time complexity O(2^n), n: len(max(user's visited web))
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        sequence = defaultdict(int)
        user_web = defaultdict(list)
        zip_items = list(zip(username, timestamp, website))
        zip_items.sort(key=lambda x: x[1])
        for user, time, web in zip_items:
            user_web[user].append(web)
        for user in user_web.keys():
            if len(user_web[user]) < 3:
                continue
            self.dfs(user_web[user], 0, sequence, [], set())
        return sorted(sequence.items(), key= lambda x: (x[1], x[0]))[0][0].split("/")
        
            
    def dfs(self, webs, i, sequence, path, visited):
        if len(path) == 3:
            three = '/'.join(path)
            if three not in visited:
                sequence['/'.join(path)] -= 1
                visited.add('/'.join(path))
                return
        if i >= len(webs):
            return
        self.dfs(webs, i+1, sequence, path+[webs[i]], visited)
        self.dfs(webs, i+1, sequence, path, visited)



























