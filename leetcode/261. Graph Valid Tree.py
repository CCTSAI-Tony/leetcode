'''
You have a graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
'''

# DFS

# Simple extension of cycle finding algorithm for directed graphs. You need to include the parent as well in the DFS call.
# Now if a nbr is in visited and the nbr is not the parent, then we have a cycle.
# Notice how we build an undirected graph: include both edges.
# O(V+E)

# 刷題用這個, time complexity O(V+E), space complexity O(V+E)
# 思路: check undirected graph 是否有環
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            u,v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        visited = set([])
        if not self.dfs(0, -1, graph, visited):
            return False
        if len(visited) != n:
            return False
        return True
    
    def dfs(self, node, parent, graph, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if not self.dfs(nbr, node, graph, visited):
                    return False
            elif nbr in visited and nbr != parent:
                return False
        return True

