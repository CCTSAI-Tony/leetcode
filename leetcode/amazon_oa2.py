class EmployeeNode:
    def __init__(self, numofCalls):
        self.value = numofCalls
        self.children = []
        
a = EmployeeNode(20)
b = EmployeeNode(12)
c = EmployeeNode(18)
d = EmployeeNode(11)
e = EmployeeNode(2)
f = EmployeeNode(3)
g = EmployeeNode(15)
h = EmployeeNode(8)

a.children.append(b)
a.children.append(c)
b.children.append(d)
b.children.append(e)
b.children.append(f)
c.children.append(g)
c.children.append(h)

president = a

# time complexity O(n), space complexity O(h)
# 思路: 分治法
import heapq
def MaxTenureFinder(president):
    oldest = [float("-inf"), None]
    dfs(president, oldest)
    return oldest[1]
    
    
def dfs(node, oldest):
    if not node.children:
        return (node.value, 1)
    people = 1
    tenures = node.value
    for s in node.children:
        t, p = dfs(s, oldest)
        tenures += t
        people += p
    avg = tenures/people
    if avg > oldest[0]:
        oldest[0], oldest[1] = avg, node
    
    return (tenures, people)

a = MaxTenureFinder(president)
a.value => 18


#time complexity O(ElogE), space complexity O(V)
#思路: MST-KRUSKAL p631=> 先對weight cost 排序, 讓花費較小的edge 能提早union, 但若union發現是同一個component 則跳過 => non-safe edge
class Solution:
    def connect(self, num, connection):
        parents = dict()
        ranks = dict()
        connection.sort(key=lambda x: x[2])
        for a, b, w in connection:
            parents[a] = a
            parents[b] = b
            ranks[a] = 1
            ranks[b] = 1
        res = []
        for a, b, w in connection:
            if self.union(a, b, parents, ranks):
                res.append([a, b, w])
        return res
            
    def union(self, a, b, parents, ranks):
        root_a, root_b = self.find(a, parents), self.find(b, parents)
        if root_a == root_b:
            return False  #同一個component => non-safe edge
        else:
            if ranks[root_a] < ranks[root_b]:
                root_a, root_b = root_b, root_a
            parents[root_b] = root_a
            ranks[root_a] += ranks[root_b]  #union by rank
            return True
        
    def find(self, a, parents): # path compression
        if parents[a] != a:
            parents[a] = self.find(parents[a], parents)
        return parents[a]
    
if __name__ == "__main__":
    a = Solution()
    for args in (
        (
            5, [["A", "B", 1], ["B", "C", 4], ["B", "D", 6], ["D", "E", 5], ["C", "E", 1]],
        ),
    ):
        print(a.connect(*args))

[['A', 'B', 1], ['C', 'E', 1], ['B', 'C', 4], ['D', 'E', 5]]




#time complexity O(nlogn)
import heapq
class Solution:
    def labeling(self, string, k):
        heap = []
        for w in string:
            num = ord(w)
            heapq.heappush(heap, -num)
        res = []
        store = []
        temp = [None, 0]
        while heap:
            num = heapq.heappop(heap)
            w = chr(-num)
            if w != temp[0]:
                temp = [w, 1]
                res.append(w)
                while store:
                    w = store.pop()
                    num = ord(w)
                    heapq.heappush(heap, -num)
                    
            elif w == temp[0]:
                if temp[1] == k:
                    store.append(w)
                else:
                    temp[1] += 1
                    res.append(w)
        return "".join(res)

a = Solution()
a.labeling("aaaaaabbbbbb", 2)
'bbabbabbaa'

#time complexity O(n)
from collections import Counter
class Solution:
    def labeling(self, string, k):
        counts = Counter(string)
        h, l = ord("z"), ord("a")
        res = ""
        nxt = h
        i = h
        while i >= l:
            if counts[chr(i)] == 0:
                i -= 1
            elif counts[chr(i)] > k:
                res += chr(i) * k
                counts[chr(i)] -= k
                while (nxt >= i or counts[chr(nxt)] == 0) and nxt >= l:
                    nxt -= 1
                if nxt < l:
                    break
                res += chr(nxt)
                counts[chr(nxt)] -= 1
            else:
                res += chr(i) * counts[chr(i)]
                counts[chr(i)] = 0
                i -= 1
        return res








#這題較難, 多想想
#time complexity O(nlogn)
from heapq import heappush, heappop
def turnstile(n, times, direction):
    pq, ans = [], [-1] * n
    for t, d, i in zip(times, direction, range(n)):
        heappush(pq, (t, d, i))
    T, state = 0, None
    while pq:
        # get next person
        t, d, i = heappop(pq)
        # if not used in previous second, state is None
        if t - 1 > T: 
            state = None
        # update current time
        T = max(T, t)
        # if there are multiple people waiting
        # split them by direction and store
        cand = [[], []]
        cand[d].append((t, d, i))
        while pq and pq[0][0] <= T: #在T 時間內的arrive顧客都pop 並加入排隊序列
            tt, dd, ii = heappop(pq)
            cand[dd].append((tt, dd, ii))
        # judge direction
        if not cand[0]:
            D = 1
        elif not cand[1]:
            D = 0
        else:
            D = int(state in [None, 1]) #previous second is not used or exit => 優先為 1
        # deal with the group that goes first
        for tt, dd, ii in cand[D]:
            ans[ii], T, state = T, T + 1, D
        # push the group that goes after back to pq, cause latter cunstomer in pq may turn the turnstile before them
        for tt, dd, ii in cand[1 - D]:
            heappush(pq, (tt, dd, ii))
    return ans


LRU Cache Misses
#time complexity O(n), n = len(pages)
from collections import OrderedDict
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.miss = 0

    def add(self, value):
        if value in self.cache:
            self.cache.move_to_end(value, last=False) #最近的item移動到最左邊
            return
        else:
            self.miss += 1
            if len(self.cache) == self.capacity:
                self.cache.popitem() #pop掉最右邊的 => LeastRecently-Used item
            self.cache[value] =value
            self.cache.move_to_end(value, last=False)


def missses(pages, max_capacity):
    lru = LRU(max_capacity)
    for i in pages:
        lru.add(i)
    return lru.miss

print(missses([1,2,1,3,1,2], 2)) == 4



# Earliest Time to Complete Deliveries
#思路: Python Greedy, time complexity O(nlogn), space complexity O(1)
#offload時間長的, 盡量分配給開放時間早的building, 每個building 都只注意offloading 最長的item, 因此遍歷offloadtime時, time + offloadTime[i*4]
def earliestTime(numOfBuildings: int, buildingopenTime: List[int], offloadTime: List[int]) -> int:
    buildingopenTime.sort()
    offloadTime.sort(reverse=True) #大到小
    res = 0
    for i, time in enumerate(buildingopenTime):
        res = max(res, time + offloadTime[i*4])
    return res

# Time: O(nlogn)
# Space: O(1)

print(earliestTime(2, [8,10], [2,2,3,1,8,7,4,5])) #16
print(earliestTime(2, [8,40], [2,2,3,1,8,7,4,5])) #43

#time complexity O(n) 就是Throttling Gateway
def droppedRequests(num, requestTime):
    one_sec_left = ten_sec_left = min_left = 0
    one_sec_count = ten_sec_count = min_count = 0
    dropped_count = 0
    for i in range(num):
        if requestTime[i] > requestTime[one_sec_left]: #update current second initial state
            one_sec_left = i
            one_sec_count = 0
        while requestTime[i] - 10 >= requestTime[ten_sec_left]: #若超出十秒, 指針往右移, 並減少累積的count
            ten_sec_left += 1
            ten_sec_count -= 1
        while requestTime[i] - 60 >= requestTime[min_left]:
            min_left += 1
            min_count -= 1
        if one_sec_count >= 3 or ten_sec_count >= 20 or min_count >= 60:
            dropped_count += 1
        one_sec_count += 1
        ten_sec_count += 1
        min_count += 1
    return dropped_count


# Chemical Delivery System, time complexity O(f*nlogm), n: numOrders, m: len(the markings of each flask), f: flaskTypes, space complexity O(f*n)
from collections import defaultdict
class Solution:
    def foo(self, numOrders, requirements, flaskTypes, totalMarks, markings):
        # store the markings of each flask in a list (they are already sorted) to make binary search feasible
        markingsHt = defaultdict(list)
        for m in markings:
            markingsHt[m[0]].append(m[1])

        # compute the total waste for each flask
        minWaste, ret = float('inf'), -1
        for flask in markingsHt:
            waste = 0
            unfit = False
            for r in requirements:
                idx = self.binSearch(markingsHt[flask], r)
                if idx == len(markingsHt[flask]):
                    unfit = True
                    break
                waste += markingsHt[flask][idx] - r
                

            # solution is feasible and better than existing one (less waste), and if tie, only store for lower index flasktype
            if not unfit and  waste < minWaste:
                minWaste, ret = waste, flask

        return ret

    # binary search to find the "right larger than or equal to" element than target, will keep looking for exact match
    def binSearch(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

#Merge Two Sorted Lists
#自己重寫 time complexity O(m+n)
#思路: 使用dummy node 與 cur 指針 來連結 排序的node
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            
        cur.next = (l1 or l2)
        return dummy.next      

#Maximal Square
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == "0" else 1 for j in range(n)] for i in range(m)] #str => int
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
         
        length = max(max(row) for row in dp) # max(每行的最大值(array))
        return length**2

#time complexity O(n), space complexity O(n)
def UniqueDiviceName(num, devicenames):
    devices = {}
    res = []
    for device in devicenames:
        if device not in devices:
            devices[device] = 0
            res.append(device)
        else:
            devices[device] += 1
            unique_name = device+str(devices[device])
            res.append(unique_name)
    return res

devicenames = ["switch", "tv", "switch", "tv", "switch", "tv"]
UniqueDiviceName(6, devicenames)
['switch', 'tv', 'switch1', 'tv1', 'switch2', 'tv2']



Kindly see my Python code below. Time complexity is O(n + m) where n, m are lengths of s, t respectively and Space Complexity is O(1).

#time complexity O(len(s) + len(t)), space complexity O(1)
#String comparisons typically do a linear scan of the characters, the time complexity is O(N)
def findSmallestDivisor(s, t):
    s_len = len(s)
    t_len = len(t)
    if s_len % t_len:
        return -1
    quotient = s_len // t_len
    if t * quotient != s:
        return -1
    temp = ""
    for i in range(len(t)):
        temp += t[i]
        if t_len % len(temp):
            continue
        q = t_len // len(temp)
        if temp * q == t:
            return len(temp)


#time complexity O(nlogn), space complexity O(n), n = len(ability)
#思路: greedy + heap
import heapq
def multiProcessor(num, ability, processes):
    ability = [-num for num in ability]
    heapq.heapify(ability)
    time = 0
    while processes > 0:
        scheduled = heapq.heappop(ability)
        processes -= (scheduled * -1)
        scheduled = (scheduled * -1) // 2
        if scheduled > 0:
            heapq.heappush(ability, -scheduled)
        time += 1
    return time

multiProcessor(5, [3,1,7,2,4], 15)
4


#自己想的, time complexity O(n), space complexity O(1)
#思路: 遍歷最大值從 擺在index: 1 to (num-1)//2, 看是否最右端的值存在於interval中, 若是則retrun 該對應的array
#greedy, 左端increasing 越短越好 
def createWiningSequence(num, lowerEnd, upperEnd):
    interval = upperEnd - lowerEnd + 1
    if num > interval*2-1:
        return [-1]
    for i in range(1, (num-1)//2+1):
        if num - (i+1) > interval -1: #超過區間, 無法形成對應array
            continue
        else:
            res = []
            l = upperEnd - i
            for j in range(i):
                res.append(l)
                l += 1
            res.append(l)
            l -= 1
            for j in range(num-1-i):
                res.append(l)
                l -= 1
            return res

#time complexity O(n), space complexity O(n)
from collections import defaultdict
def SlowestKeyPress(num, keyTimes):
    record = defaultdict(int)
    prev = 0
    for i, v in keyTimes:
        period = v - prev
        record[i] = max(record[i], period)
    max_key = max(record.values())
    for key in record:
        if record[key] == max_key:
            return chr(ord("a") + key)



#time complexity O(nlogn), space complexity O(n)
import heapq
def countCutOffRank(cutOffRank, num, scores) -> int: # Actually, I didn't use 'num' parameter
    heap = []
    for score in scores:
        heapq.heappush(heap, -score) # For max heap, convert a score to negative
    
    result = 0
    while (heap and result < cutOffRank):
        score = heap[0] # Peek the maximum score
        if score == 0: #score = 0 can't level up
            break
        while (heap and heap[0] == score):
            heapq.heappop(heap)
            result += 1
    return result


# Test cases
print(countCutOffRank(3, 4, [100, 50, 50, 25])) # 3
print(countCutOffRank(4, 5, [2, 2, 3, 4, 5])) # 5
print(countCutOffRank(2, 5, [0,0,0,0,5])) # 1



#time complexity O(n), space complexity O(n)
from collections import defaultdict
def stockPairs(num, stocksProfit, target):
    dic = defaultdict(int)
    res = set()
    for stock in stocksProfit:
        temp = target - stock
        if temp in dic:
            if stock < temp:
                res.add((stock, temp))
            else:
                res.add((temp, stock))
        dic[stock] += 1
    return len(res)



# Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

# Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. 
# The song can only belong to only one genre.

# The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). 
# Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

# Example 1:

# Input:
# userSongs = {  
#    "David": ["song1", "song2", "song3", "song4", "song8"],
#    "Emma":  ["song5", "song6", "song7"]
# },
# songGenres = {  
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }

# Output: {  
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }

# Explanation:
# David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
# Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
# Example 2:

# Input:
# userSongs = {  
#    "David": ["song1", "song2"],
#    "Emma":  ["song3", "song4"]
# },
# songGenres = {}

# Output: {  
#    "David": [],
#    "Emma":  []
# }

#time complexity O(numUsers * numSongs)
from collections import Counter
def favorGenres(userSongs, songGenres):
    res = {}
    d = {s: g for g in songGenres for s in songGenres[g]} #好招學起來 for loop: inner for loop
    for name, songs in userSongs.items():
        c = Counter(d[s] for s in songs if s in d)
        mxcnt = max(c.values() or [0])
        res[name] = [g for g in c if c[g] == mxcnt]
    return res











1. construct sequence: Given num(size of the sequence), lowerEnd(lower end of integer range), upperEnd(upper end of integer range).
    Return a list of integers representing the winning sequence, otherwise return [-1].

    Winning sequence 是指 sequence符合一开始strictly increasing然后strictly decreasing，同时是最大的。例如 [9,10,9,8,7] 比 [8, 9, 10, 9, 8] 大，并且符合第一部分数字递增，第二部分数字递减。
    举个例子：num=3, lowerEnd=3, upperEnd=10; output [9,10,9,8,7]

2. LC221. Maximal Square类似

3. vo 會考lc212



# Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. 
# If the given string doesn't have k distinct characters, return 0.
# https://leetcode.com/problems/subarrays-with-k-different-integers

# Example 1:

# Input: s = "pqpqs", k = 2
# Output: 7
# Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
# Example 2:

# Input: s = "aabab", k = 3
# Output: 0
# Constraints:

# The input string consists of only lowercase English letters [a-z]
# 0 ≤ k ≤ 26

#time complexity O(n), space complexity O(n)
#思路: sliding window, 利用雙指針來紀錄 <= k distinct 的字串組合 ex: pqpqs k = 2: left=0, right=2 => 新增 p, qp, pqp, k=1:left = 2, right = 2 => 新增 p
#依照此方法, 算出k window and k-1 window result, 兩者相減就是exact k distict substrings的數量
import collections
def subStringsWithKDistinctCharacters(s, k):
    s = list(s)
    return atMost(s, k) - atMost(s, k-1)

def atMost(s, k):
    count = collections.defaultdict(int)
    left = 0
    ans = 0
    for right, x in enumerate(s):
        count[x] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        ans += right - left + 1
    return ans

right 0 left 0
ans 1
right 1 left 0
ans 3
right 2 left 0
ans 6
right 3 left 0
ans 10
right 4 left 3
ans 12
right 0 left 0
ans 1
right 1 left 1
ans 2
right 2 left 2
ans 3
right 3 left 3
ans 4
right 4 left 4
ans 5



# Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. 
# The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

# Don't include the first or final entry. You can only move either down or right at any point in time.

# Example 1:

# Input:
# [[5, 1],
#  [4, 5]]

# Output: 4
# Explanation:
# Possible paths:
# 5 → 1 → 5 => min value is 1
# 5 → 4 → 5 => min value is 4
# Return the max value among minimum values => max(4, 1) = 4.
# Example 2:

# Input:
# [[1, 2, 3]
#  [4, 5, 1]]

# Output: 4
# Explanation:
# Possible paths:
# 1-> 2 -> 3 -> 1
# 1-> 2 -> 5 -> 1
# 1-> 4 -> 5 -> 1
# So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
# Return the max of that, so 4.

#time complexity O(m*n), space complexity O(m*n)
def max_min_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif (i == 1 and j == 0) or (i == 0 and j == 1): #不包含 first entry
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = min(matrix[i][j], matrix[i][j - 1])
            elif j == 0:
                dp[i][j] = min(matrix[i][j], matrix[i - 1][j])
            else:
                dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1]))

    if n == 1: #id 不包含final entry
        return dp[0][-2]
    elif m == 1:
        return dp[-2][0]
    else:
        return max(dp[-2][-1], dp[-1][-2])


#自己重寫 manacher algorithm, time complexity O(n), 108ms
#思路: 參照別人代碼修改, 利用lps 對稱性質, 此算法可以讓新index在計算回文長度時參照對應center另一邊index的lps長度, 減少重複比對回文字串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        manacher_str = "#" + "#".join(s) + "#"
        n = len(manacher_str)
        lps = [0] * n
        c = 0
        r = 0
        for i in range(1, n):
            if r >= i:  #r > i 也可以, 沒差
                lps[i] = min(r-i, lps[c-(i-c)])  #lps[c-(i-c)] 鏡向對面相對應index的lps
            while i - lps[i] - 1 >= 0 and i+ lps[i] + 1 < n and manacher_str[i - lps[i] - 1] == manacher_str[i+ lps[i] + 1]:
                lps[i] += 1
            
            if i + lps[i] > r:
                c = i
                r = i + lps[i]
        max_len, max_center = max((v, i) for i, v in enumerate(lps))
        longest_palindrom = s[(max_center-max_len) //2 : (max_center+max_len) //2 ]  #唯一需要背的地方, 轉化成s原本的index, 不難懂看blog就清楚
        return longest_palindrom


#刷題用這個, time complexity O(N * logK) where N is the length of points.
#思路: 利用heapq, 數學公式 a與b的距離 = ((x1-x2)**2+(y1-y2)**2)**0.5, 使用max heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)  #trick, 乘一個負號 使得distance 比較大的堆積在前面, 這樣之後heappushpop 就會被擠出來
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]



#自己想的, time complexity O(n), backtracking, 40ms, 刷題用這個
#思路: 設"(" = 1, ")" = -1, pathSum 來紀錄目前括號的數量狀態, 途中若出現<0代表有")" 無法跟"(" 配對的情況->提早return, 最後全部配對完成 pathSum = 0, 才是valid的答案
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        self.dfs(n, '', 0, res)
        return res
    
    
    def dfs(self, n, path, pathSum, res):
        if pathSum < 0 or pathSum > n:  #代表有 ")" 但前面沒有"(" 與它配對 or "(" 過半
            return
        if len(path) == 2*n:
            if pathSum == 0: #剛好全部配對成功
                res.add(path)
            return
        self.dfs(n, path + "(", pathSum + 1, res)
        self.dfs(n, path + ")", pathSum - 1, res)


Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26

# The idea is to maintain a window and every time the window size is reached, we just add the substring to the dictionary
# Check for the condition that it has unique characters before adding them to the dictionary using sets
# time complexity O(kn), space complexity O(n)
def generate_substr(s, k):
    if not s or k == 0:
        return None
    
    result = {} #dic

    for i in range(len(s)-k+1):
        if len(set(s[i:i+k]))==k:
            result[s[i:i + k]] = 1
    return result.keys()

print(generate_substr('awaglknagawunagwkwagl',4))



# Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

# Conditions:

# You will pick exactly 2 numbers.
# You cannot pick the same element twice.
# If you have muliple pairs, select the pair with the largest number.
# Example 1:

# Input: nums = [1, 10, 25, 35, 60], target = 90
# Output: [2, 3]
# Explanation:
# nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
# Example 2:

# Input: nums = [20, 50, 40, 25, 30, 10], target = 90
# Output: [1, 5]
# Explanation:
# nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
# nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
# You should return the pair with the largest number.

#time complexity O(n), space complexity O(n)
def findPairWithGivenSum(nums, target):
    hashMap = {}
    target -= 30
    res = []
    for i, elem in enumerate(nums):
        if (target - elem) in hashMap:
            res.append((hashMap[(target - elem)], i))
        hashMap[elem] = i
    return max(res, key=lambda x: x[0]+x[1])
        
    

print(findPairWithGivenSum([1, 10, 25, 35, 60], 90))
print(findPairWithGivenSum([20, 50, 40, 25, 30, 10], 90))
    


#leetcode 239, 127, 572, 20, 829
#time complexity O(n), space complexity O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k-1):
            self.helper(nums, i, queue)
        res = []
        start = 0
        for i in range(k-1, len(nums)):
            self.helper(nums, i, queue)
            if queue[0] < start:
                queue.popleft()
            res.append(nums[queue[0]])
            start += 1
        return res
        
    def helper(self, nums, i, queue):
        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop()
        queue.append(i)



# 刷題用這個 Time Complexity: O(M^2*N), where M is the length of each word and N is the total number of words in the input word list.
# 自己重寫, 建立graph, , space complexity O(M^2*N)
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]  #關鍵, 建立不同切分的狀態: 對應有哪些字
                graph[s].append(word)
        
        return self.bfs(beginWord, endWord, graph)
    
    def bfs(self, beginWord, endWord, graph):
        queue, visited = deque(), set(beginWord) #一開始就加入beginword
        queue.append((beginWord, 1))
        while queue:
            for _ in range(len(queue)):
                word, step = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    for nextWord in graph[s]:  #在字典種查找
                        if nextWord not in visited:  #避免重複
                            visited.add(nextWord)  #登錄
                            queue.append((nextWord, step + 1))
        return 0


#time complexity O(s*t)
#思路: 利用dfs 分治法 來解題, 往左右child 找可能的子樹
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        return self.dfs(s, t)
    
    def dfs(self, s, t):
        if not s:
            return False
        if s.val == t.val and self.check(s, t):
            return True
        return self.dfs(s.left, t) or self.dfs(s.right, t)
    
    def check(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (not t and s) or (s.val != t.val):
            return False
    
        return self.check(s.left, t.left) and self.check(s.right, t.right)



#自己重寫, time complexity O(n), space complexity O(n), 刷題用這個, 指針應用搭配stack
#思路: 遇到closoing bracket, 若stack.pop() 不是對應的另一半, 就return False, 因為不能([)] 一定要 ([{}]), 大包小, 對應的一定要優先pop出來
#最後若stack 有殘餘沒配對成功的 要return False
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack= []
        for i in range(len(s)):
            if s[i] == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True


#刷題用這個, time complexity O(N^0.5)
#思路: N can be expressed as i consecutive numbers: k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer;
#思路: 數學推導, N = k * i + (i - 1 + 0) * i / 2 => N - (i - 1) * i / 2 = k * i => 若 N - (i - 1) * i / 2 可以被i整除, 代表可以找到正整數k
#因為k * i 一定是正的, 所以  N > (i - 1) * i / 2
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
            i, ans = 1, 0
            while N > i * (i - 1) / 2:
                if (N - i * (i - 1) / 2) % i == 0:
                    ans += 1
                i += 1
            return ans


#roblox 2020
#lifting weights, time complexity O(n*m), 
def liftWeights(weights, max_capacity):
    cache = set()
    max_weight = 0
    for weight in weights:
        new_cache = set()
        for ele in cache:
            temp = ele + weight
            if temp > max_capacity:
                continue
            new_cache.add(temp)
            max_weight = max(max_weight, temp)
        new_cache.add(weight)
        cache = cache.union(new_cache)
    return max(cache)

liftWeights([5,7,12,18], 20) => 19


#time complexity O(nlogn)
import heapq
def maxEvents(arrival, duration):
    # Write your code here
    heap = []
    for x, y in zip(arrival, duration):
        heapq.heappush(heap, (x+y, x))
    res = []
    while heap:
        e, s = heapq.heappop(heap)
        if not res or res[-1][0] <= s:
            res.append((e, s))
    return len(res)


#time complexity O(nlogn)
def efficientJanitor(weight):
    # Write your code here
    weight.sort(reverse=True)
    
    left, right = 0, len(weight)-1
    res = 0
    while left <= right:
        if left == right:
            res += 1
            break
        temp = weight[left]
        while left < right and temp + weight[right] <= 3.0:
            temp += weight[right]
            right -= 1
        left += 1
        res += 1
    return res



Create k group using n members

The key is dp[i][j] = dp[i-1][j-1] + dp[i][j-i];

    public static int nToKGroups(int n, int k) {
        if(n < k) {
            return 0;
        }
        int[][] dp = new int[k+1][n+1];
        for(int i = 1; i <= k; i++) {
            for(int j = i; j <= n; j++) {
                if(i==j) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-i];
                }
            }
        }
        return dp[k][n];
    }