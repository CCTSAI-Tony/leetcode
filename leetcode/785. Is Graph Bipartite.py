'''
Given an undirected graph, return true if and only if it is bipartite. (二分圖)

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B 
such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  
Each node is an integer between 0 and graph.length - 1.  
There are no self edges or parallel edges(重邊): graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
'''

# https://www.geeksforgeeks.org/bipartite-graph/
# Note that it is possible to color a cycle graph with even cycle using two colors. 
# It is not possible to color a cycle graph with odd cycle using two colors.

# Algorithm to check if a graph is Bipartite:
# One approach is to check whether the graph is 2-colorable or not using backtracking algorithm m coloring problem.
# Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
# 1. Assign RED color to the source vertex (putting into set U).
# 2. Color all the neighbors with BLUE color (putting into set V).
# 3. Color all neighbor’s neighbor with RED color (putting into set U).
# 4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
# 5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, 
# then the graph cannot be colored with 2 vertices (or graph is not Bipartite)

test cases
[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]

[[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],
[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]



# 刷題用這個, 此題是undirected graph, time complexity O(n)
# 思路: 最主要是check這個圖是否可以只被2個顏色區分而不衝突, 任何一邊相連接的兩個點不能為同個顏色
# 利用dict 來記錄color
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not self.dfs(i, color, graph):
                    return False
        return True
        
    def dfs(self, pos, color, graph):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]  #好技巧 1- 0 = 1, 1-1 = 0, 幫鄰居上顏色
                    if not self.dfs(i, color, graph):
                        return False
            return True


# 重寫第二次, time complexity O(n)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(cur) -> bool:
            for nxt in graph[cur]:
                if nxt in color:
                    if color[cur] == color[nxt]:
                        return False
                else:
                    color[nxt] = 1 - color[cur]
                    if not dfs(nxt):
                        return False
            return True
                    
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True



# 自己想的dfs, time compleity O(n)
# 思路: 遇到單點也就是graph[i] = [], 這個點塗上兩種顏色的其中一種皆可
# 最主要是check這個圖是否可以只被2個顏色區分而不衝突, 任何一邊相連接的兩個點不能為同個顏色
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        color = [0] * len(graph)
        self.res = True
        for i in range(len(graph)):
            if not graph[i] or visited[i]:
                continue
            color[i] = 1
            self.dfs(i, graph, visited, color, color[i])
            if self.res == False:
                return False       
        return self.res
    
    def dfs(self, i, graph, visited, color, prev_color):
        if visited[i]:
            if color[i] == prev_color:
                 self.res = False
            return
        if not color[i]:
            color[i] = prev_color*-1 #看前鄰居什麼顏色自己變相反顏色
        visited[i] = True
        for neighbor in graph[i]:
            self.dfs(neighbor, graph, visited, color, color[i])











































