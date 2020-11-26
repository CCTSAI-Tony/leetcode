'''
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  
More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  
The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
'''




#參考別人 time complexity O(n), dfs topological sort, 經典
#思路: dfs directed graph, topological sort, 若從該node出發有發現backedge 就不是safe
# 0: non-visited, 1: safe(visited), 2: not safe(visiting)
from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph:
            return None
        color = [0] * len(graph)
        res = []
        for i in range(len(graph)):
            if self.dfs(i, graph, color):
                res.append(i)
        return res
    
    def dfs(self, i, graph, color):
        if color[i] == 2:
            return False
        elif color[i] == 1:
            return True
        color[i] = 2
        for j in graph[i]:
            if not self.dfs(j, graph, color):
                return False
        color[i] = 1
        return True




#自己想的, TLE, time complexity O(n^2)
from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph:
            return None
        res = []
        for i in range(len(graph)):
            if self.dfs(i, set([]), graph):
                res.append(i)
        return res
    
    def dfs(self, i, seen, graph):
        if i in seen:
            return False
        seen.add(i)
        for j in graph[i]:
            new_seen = seen.copy()
            if not self.dfs(j, new_seen, graph):
                return False
        return True