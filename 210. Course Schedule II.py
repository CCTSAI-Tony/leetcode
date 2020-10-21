'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''



#參考別人修改 刷題用這個 96ms, time complexity O(VE), space complexity O(V)
#思路: dfs topological sort 可以同時return True or False 與修改res 來提早結束recursion 若遇到backedge, 而不是像下面單純return, 跑完全部recursion 才要return []
#好技巧, 學起來!
#order 最後的course, 愈早被加進path => 所以return path[::-1]
#最初每個vertex = -1, 開始遍歷 = 0, 遍歷完所有children, vertex = 1
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        visited = [-1] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(i, visited, graph, path):
                return []          
        return path[::-1]
    
    
    def dfs(self, i, visited, graph, path):
        if visited[i] == 0:
            return False
        if visited[i] == 1:
            return True
        visited[i] = 0
        for neighbor in graph[i]:
            if not self.dfs(neighbor, visited, graph, path):
                return False
        visited[i] = 1
        path.append(i)
        return True


#自己重寫, 刷題不用這個, dfs topological sort, time complexity O(VE) 196ms
#思路: 先建立directed graph, 最初每個vertex = -1, 開始遍歷 = 0, 利用2代表有back edge, return [], 遍歷完所有children, vertex = 1
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        visited = [-1] * numCourses
        path = []
        for i in range(numCourses):
            if visited[i] == -1:
                self.dfs(i, visited, graph, path)
                if 2 in visited:
                    return []
        return path[::-1]
    
    
    def dfs(self, i, visited, graph, path):
        visited[i] = 0
        for neighbor in graph[i]:
            if visited[neighbor] == -1:
                self.dfs(neighbor, visited, graph, path)
            elif visited[neighbor] == 0:
                visited[neighbor] = 2
                break
        if 2 not in visited:
            visited[i] = 1
            path.append(i)


# time complexity O(VE)
from collections import defaultdict
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses, key:[list]
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) #ex: 3:[1,2] ,edge 方向倒過來 所以最後self.res 不用reverse
        self.visited = [0 for x in range(numCourses)] # DAG detection 
        for x in range(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


#參考207
class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        res = []
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
                if visit[i] == -1:
                    return False
                if visit[i] == 1:
                    return True
                visit[i] = -1 
                for j in graph[i]: 
                    if not dfs(j):
                        return False
                visit[i] = 1
                res.append(i)
                return True

        for i in range(numCourses):
            if not dfs(i):
                return [] #If it is impossible to finish all courses, return an empty array
        return res





