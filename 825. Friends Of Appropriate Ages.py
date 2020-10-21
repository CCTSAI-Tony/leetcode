'''
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
'''

#刷題用這個
#binary search, time complexity O(nlogn)
#bisect.bisect() = bisect.bisect_right
#思路: 利用bisect.bisect_right 來找出合適的年齡區間
#<14歲不能交朋友, 只能交比自己小的, age[B] > 100 && age[A] < 100 => 沒意義 根本被包含在 age[B] > age[A]
#age[B] <= 0.5 * age[A] + 7 利用bisect_right 找出index1 => age[i] > 0.5 * age[A] + 7
#利用bisect_right 找出 > 自身age 的 index2, index2 - index1 - 1 就是本身可以交朋友的次數
import bisect
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages: 
            return 0
        cnt = 0
        N = len(ages)
        ages.sort()
        for i in range(N):
            a = ages[i]
            if a<=14: #含14歲以前不能交朋友 => 數學推導
                continue
            idx1 = bisect.bisect_right(ages, a)
            x = 0.5*a+7
            idx2 = bisect.bisect_right(ages, x)
            
            cnt += idx1-idx2 -1 #-1 不能跟自己交朋友
        return cnt

#自己重寫, time complexity O(nlogn)
import bisect
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        count = 0
        for i in range(n):
            if ages[i] <= 14:
                continue
            x = 0.5 * ages[i] + 7
            index1 = bisect.bisect_right(ages, x)
            index2 = bisect.bisect_right(ages, ages[i])
            count += index2 - index1 - 1
        return count

# Explanation
# Write a sub function request(a, b) to check if age a will friend requests age b.
# I just copy it from description:
# return !(condition1 || condition2 || condition3)

# Count nunmber of all ages to a map.
# Because we have at most 20000 ages but only in range [1, 120].

# For each age a and each age b != a, if request(a, b), we will make count[a] * count[b] requests.

# For each age a, if request(a, a), we will make count[a] * (count[a] - 1) requests. 

#time complexity O(n), 遍歷dict=> O(120) * O(120) => O(14400), 1 <= ages.length <= 20000.
#思路: 建立request func, 利用Counter 來紀錄相同年齡的count, if request(a, b) => counts += Counter[a] * Counter[b]
#若相同年齡則要扣掉自己, if request(a, a) => counts += Counter[a] * (Counter[a] - 1)
#因為age[B] <= 0.5 * age[A] + 7 & age[B] > age[A] => 含14歲以前不能交朋友
#age[B] > 100 && age[A] < 100 => 沒意義 根本被包含在 age[B] > age[A]
import collections
class Solution(object):
    def numFriendRequests(self, ages):
        c = collections.Counter(ages)
        return sum(self.request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)

    def request(self, a, b):
        return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)



#自己重寫, time complexity O(n)
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages_map = Counter(ages)
        count = 0
        for i in ages_map:
            for j in ages_map:
                if self.request(i, j):
                    if i != j:
                        count += ages_map[i] * ages_map[j]
                    else:
                        count += ages_map[i] * (ages_map[j] - 1)
        return count
        
    def request(self, a, b):
        return not (b <= a*0.5 + 7 or b > a or (b > 100 and a < 100))





#naive approach, time complexity O(n^2)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        for i in range(len(ages)):
            for j in range(i+1, len(ages)):
                if self.check(ages[i], ages[j]):
                    count += 1
                if self.check(ages[j], ages[i]):
                    count += 1
        return count
                
                
    def check(self, a, b):
        if b <= 0.5 * a + 7:
            return False
        if b > a:
            return False
        if b > 100 and a < 100:
            return False
        return True