'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

#自己想的, time complexity O(V+E), space complexity O(V+E), 92ms
#經典 dfs graph題 => 用bfs 也可以
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, graph, visited)
        return count
    
    def dfs(self, node, graph, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)


#重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, graph, visited)
        return count
    
    def dfs(self, i, graph, visited):
        if i in visited:
            return
        visited.add(i)
        for j in graph[i]:
            self.dfs(j, graph, visited)
        return


#重寫第三次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, graph, visited)
        return count
    
    def dfs(self, i, graph, visited):
        visited.add(i)
        for neighbor in graph[i]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)















