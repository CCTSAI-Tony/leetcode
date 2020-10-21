'''
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
'''

# 題目說的 The given edges form an undirected tree. => 其實就是 acyclic undirected graph
# 自己想的, time complexity O(V+E), space complexity O(V+E)
# 思路: 先利用dfs 以隨便一個node找出離該node 最遠的node => 找到一端 end point, 再從該end point 找到另一端end point 並回報兩endpoints 之間的edge長度
# 技巧: 使用set 去重
from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges or not edges[0]:
            return 0
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        endpoint1 = self.dfs(0, graph, 0, set())[0]
        return self.dfs(endpoint1, graph, 0, set())[1]
        
        
    def dfs(self, node, graph, edge_len, visited):
        visited.add(node)
        max_len = edge_len
        furthestNode = node
        for neightbor in graph[node]:
            if neightbor in visited:
                continue
            nextNode, next_len = self.dfs(neightbor, graph, edge_len+1, visited)
            if next_len > max_len:
                max_len = next_len
                furthestNode = nextNode
        return (furthestNode, max_len)





