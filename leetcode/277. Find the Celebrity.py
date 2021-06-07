'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. 
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. 
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). 
There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. 
The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
 

Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.
'''



# basic idea: find a potential celebrity, and verify his identity by definition, you can refer to the comments below for more details:

#time complexity O(n), 刷題用這個
#思路: celebrity 不會認識人, 沒被人認識的不是celebrity 利用以上條件來篩選不合格者, 
#用雙指針, left, right = 0, n-1 => knows(a,b) => 若True => a 不適任, 若False => b 不適任 => 刪到剩一個元素成為celebrity candidate
#針對這個candidate 做驗證, 若通過就是celebrity, 不通過 => 代表這裡面沒有celebrity
class Solution:
    def findCelebrity(self, n):
        # first, find the candidate for celebrity
        # left and right must meet at some point, this person is a potential celebrity
        left, right = 0, n - 1
        while left < right: 
            if knows(left, right):
                left += 1 #celebrity 不會認識人, 排除
            else:
                right -= 1 #celebrity 要被大家知道, 排除 => left 之後的都不認識 => left = right => celebrity candidate => 但並不代表left前面的都不認識
                           #但目前就只剩下這個candidate, 其他的都被淘汰的, 若candidate 不能通過驗證, 則這裡面沒有celebrity
        # left is a celebrity candidate 
        # next verify if the candidate is indeed a celebrity
        # case 1: at least one person doesn't know this candidate => not a celebrity 
        for i in range(n):
            if not knows(i, left) and i != left:
                return -1
        # case2: candidate knows at least one person => not a celebrity
        for i in range(n):
            if knows(left, i) and i != left:
                return -1

        return left

#自己重寫, time complexity O(n) space complexity O(1), 2320ms
class Solution:
    def findCelebrity(self, n: int) -> int:
        left, right = 0, n-1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for i in range(n):
            if knows(left, i) and left != i:
                return -1
        for i in range(n):
            if not knows(i, left):
                return -1
        return left

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        l, r = 0, n-1
        while l < r:
            if knows(l, r):
                l += 1
            else:
                r -= 1
        for i in range(n):
            if not knows(i, l) or (i != l and knows(l, i)):
                return -1
        return l



#別人O(n) 優化 => 1576ms
class Solution(object):
    def findCelebrity(self, n):
        candidate = 0
        
        # if celebrity > candidate, candidate must change to the celebrity, cause (knows(candidate, celebrity) == True)
        # if candidate == celebrity: candidate won't change, cause celebrity knows nobody.
        # after the loop, candidate is the only one can be the celebrity
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        # check people < candidate
        for i in range(candidate):
            if knows(candidate, i) or not(knows(i, candidate)):
                return -1
        
        # check if people > candidate are all knows the candidate
        for i in range(candidate+1, n):
            if not knows(i, candidate):
                return -1
            
        return candidate






#自己想的 time complexity O(n^2)
#思路: celebrity: in_degree = n-1, out_degree = 0
from collections import defaultdict
class Solution:
    def findCelebrity(self, n: int) -> int:
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if knows(i, j) and i != j:
                    out_degree[i] += 1
                    in_degree[j] += 1
        for i in range(n):
            if in_degree[i] == n-1 and out_degree[i] == 0:
                return i
        return -1





























