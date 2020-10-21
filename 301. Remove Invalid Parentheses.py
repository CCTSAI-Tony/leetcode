'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

# The basic idea is recursive DFS with pruning function.

# Generate new strings by removing parenthesis, and calculate the total number of mismatched parentheses inside the string by function calc(s).

# If the mismatched parentheses increased, then discard the string.

#time complexity O(n^2), n: len(s) 經典dfs/bfs題
#思路: 利用dfs 來prune s, 藉由calc helper 的幫忙, 先計算目前s有幾個mismatch parenthesis, 再遍歷s看是否拿掉特定parenthesis 可以改善mismatch => neighbor 節點
#若可以則繼續dfs(recursion), 若不可以跳過, 直到mismatch = 0, append to ans, 記得用visited set 來過濾重複節點
#calc 計算mismatch => a counts left mismatch parenthesis, b counts right mismatch parenthesis
#left 無法與right 配對 => left mismatch parenthesis, right 在 left 前 => right mismatch parenthesis
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s) #mi: mismatch
            if mi == 0:
                return [s] #return list, 所以ans.extend(s)
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:] #ns: new string, 排除該bracket
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns)) #直到 mi==0, return [s]
            return ans    
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0) #get(c, 0) 是遇到letter 預設為0, a counts for mismatched left bracket
                b += (a < 0) #if a <0 b+=1, b counts for mismatched right bracket, 先'('再')' b無法加1, 但 ")(" b += 1
                a = max(a, 0) #a counts for mismatched left bracket, 每當a<0 a重置為0
            return a + b #total mismatch

        visited = set([s]) #利用set排除重複 "()())()" 個別去除 第4,第5 bracket 重複s
        return dfs(s)
d = [1]
d.extend([]) #這個extend用法滿少見的, ans = []
d
[1]

s= "()())()"
set([s])
{'()())()'}

d = [1]
d.extend([4])
d
[1, 4]

d = [1]
d.append([4])
d
[1, [4]]


{1:10,2:20}.get(1,0)
10
{1:10,2:20}.get(5,0)
0

a=b=0
a = -1
b+=a <0
b
1

a = -1
b+= a<0
b
2
break

a=b=0
a = -5
b+=a <0
b
1



# BFS
#time complexity O(n^2), n: len(s)
#思路: 利用bfs 來遍歷, 藉由calc helper 的幫忙, 先計算目前s有幾個mismatch parenthesis, 再遍歷s看是否拿掉特定parenthesis 可以改善mismatch => neighbor node
#若可以則把neighbor加入queue, 若不可以跳過, 直到mismatch = 0, append to ans, 記得用visited set 來過濾重複節點
#calc 計算mismatch => a counts left mismatch parenthesis, b counts right mismatch parenthesis
#left 無法與right 配對 => left mismatch parenthesis, right 在 left 前 => right mismatch parenthesis
import collections
class Solution(object):
    def removeInvalidParentheses(self, s):
        res = []
        visited = set([s])
        queue = collections.deque([s])
        while queue:
            cur = queue.popleft()
            num_mismatched = self.calc(cur)
            if num_mismatched == 0:
                res.append(cur)    
            else:   
                for i, c in enumerate(cur):
                    if c in '()': #same as if c in ('(', ')'):
                        new_s = cur[:i] + cur[i+1:]
                        if new_s not in visited and self.calc(new_s) < num_mismatched:
                            visited.add(new_s)
                            queue.append(new_s)
        return res
        
   def calc(self, s):
        a = b = 0
        for c in s:
            a += {'(': 1, ')': -1}.get(c, 0)
            b += (a < 0)  # b counts for mismatched right bracket
            a = max(a, 0) # a counts for mismatched left bracket
        return a+b

s= "()())()"
queue = collections.deque([s])
queue
deque(['()())()'])
queue.popleft()
'()())()'









