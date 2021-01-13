'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]] to take course 1 you have to first take course 0
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''

# 刷題用這個
# 自己重寫 time complexity O(V + E), space complexity O(V+E)
# 思路: dfs directed graph, topological sort, 有趣的是建立graph, edge 方向相反, 不影響答案, 可以想像成不是dag的graph, 反方向也不是dag, vise versa
# dag不會有backedge, 有backedge 就會出現circle, 就不能完成全部課程
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [-1] * numCourses #-1 代表未遍歷, 0 代表遍歷中, 1 代表遍歷結束
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return False
        return True
    
    def dfs(self, i, graph, visited):
        if visited[i] == 1:
            return True
        if visited[i] == 0:
            return False
        visited[i] = 0
        for course in graph[i]:
            if not self.dfs(course, graph, visited):
                return False
        visited[i] = 1
        return True


#跟210一起服用
#DFS solution 不懂請看原文書 p607  箭頭所指方向f 可以看成先修課程, 重點是 dag不會有backedge, 有backedge 就會出現circle
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
                if visit[i] == -1:
                    return False
                if visit[i] == 1:
                    return True
                visit[i] = -1 #變灰色
                for j in graph[i]: #重點在這 
                    if not dfs(j):
                        return False
                visit[i] = 1
                return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


#自己想的, bfs topological sort, time complexity O(v+e), space complexity O(v+e)
#思路: acwing 解法, 利用indegree 來逐層加入indegree == 0 的點, 最後確認indegree裡面都是0 否則代表圖有環
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, graph = defaultdict(int), defaultdict(list)
        for edge in prerequisites:
            if edge[1] not in indegree:
                indegree[edge[1]] = 0
            indegree[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        queue = deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        return not any(indegree.values())






# if node v has not been visited, then mark it as 0. white color
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring(backedge). gray color, 
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors. black color, 不是 forwardedge 就是 cross edge


# prerequisites = [[1,0],[0,1]]
# for x, y in prerequisites:
#             print(x,y)

# 1 0
# 0 1

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
graph = [[1],[0]]
visit = [0,0]
  
visit = [-1,0]


visit = [-1,-1], visit[0] == -1, return False


Input: numCourses = 2, prerequisites = [[1,0]]

graph = [[],[0]]
visit = [0,0]

visit = [-1,0]

visit = [1,0]

visit = [1,-1] , visit[0] == 1, return True, 在這裡可以想成cross edge



