'''
Given an array equations of strings that represent relationships between variables, 
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true
 

Note:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
'''

Bascially we are making a graph.
If a == b we will have two edges: a->b and b->a.
After we construct the graph, we check all the x != y
and make sure they are not able to visit each other.

Time: dfs is O(N). We do dfs number of inequalities times.
Space: O(N).

#time complexity O(N*(inequalities)), 刷題用這個
#思路: 先建立 graph, a == b, 建立 a->b, b->a, 若a!=b, 則等graph建立好後, 再從a出發dfs遍歷, 看是否會在同一個connected component 遇到b
#若是 return False, 不是return True
import collections
class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        graph = collections.defaultdict(list)
        notEquals = []
        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                notEquals.append((a, b))
            else:
                u, v = eq.split('==')    
                graph[u].append(v)
                graph[v].append(u)
         
        
        for u, v in notEquals:
            if self.canMeet(u, v, set(), graph):
                return False
        return True

    def canMeet(self, u, target, visited, graph):
        if u == target:
            return True 
        visited.add(u)
        for v in graph[u]:
            if v in visited:
                continue
            if self.canMeet(v, target, visited, graph):
                return True 
        return False

#自己重寫, 40ms
import collections
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = collections.defaultdict(list)
        not_equal = []
        for eql in equations:
            if eql[1:3] == "!=":
                a,b = eql.split("!=")
                not_equal.append((a,b))
            else:
                a,b = eql.split("==")
                graph[a].append(b)
                graph[b].append(a)
        for u, v in not_equal:
            if self.dfs(u, v, graph, set()):
                return False
        return True
    
    def dfs(self, u, target, graph, visited):
        if u == target:
            return True
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if self.dfs(v, target, graph, visited):
                    return True
        return False


# Union Find:

# for each equation,
# if it is an inquality,
# then add it to 'check' (a list that we use to check the validility of the input later)
# else:
# union the two expression
# After we find all connnected components, we can simply check if the lhs and rhs of each inequality in 'check' is in the same connected components.

# If they are, then they must be equal and therefore the inequality should not hold, so we return 'False'.


# time: O(N) where is the length of the input
# space: O(1) since we only store 26 characters in the parent dictionary.

#刷題用這個
#time complexity O(N), union find, why O(N): union 後, find(x) 會沿著path 尋找root, 並更新所有沿著path的node, 所以只要走完完整的path一遍, 就能全部更新完畢
#ex: a=b, b=c, c=d, d=e, e=f, f!= a
#思路: 把inequalities 放到check, 利用union 把equal a, b 綁定在同個component, 
#找完全部components後, 再對check裡面的a, b find, 若兩者同屬同一個component, 則return False
import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = {i:i for i in string.ascii_lowercase} #dict comprehension
        checks = []
        for eq in equations:
            if eq[1] == '!':
                checks.append(eq)
                continue
            self.union(eq[0], eq[3])
        
        for chk in checks:
            if self.find(chk[0]) == self.find(chk[3]):
                return False
        return True

    def find(self, x):  
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


# import string
# a = string.ascii_lowercase
# a
# 'abcdefghijklmnopqrstuvwxyz'

#自己重寫, time complexity O(N)
import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        check = []
        self.parents = {}
        for eq in equations:
            if eq[1:3] == "!=":
                (a, b) = eq.split("!=")
                check.append((a,b))
            else:
                (a, b) = eq.split("==")
                self.union(a, b)
        for (a, b) in check:
            if self.find(a) == self.find(b):
                return False
        return True
    
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parents[pa] = pb #這邊很容易出錯, 切記不是 self.parents[a] = b
            
    def find(self, a):
        if a not in self.parents:
            self.parents[a] = a
        elif self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]










