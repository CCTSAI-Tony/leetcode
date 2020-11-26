'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
'''

#自己想的, 刷題用這個, time complexity O((2^n)*n), space complexity O((2^n)*n)
#As a result, for a graph with n nodes, at maximum, there could be 2^(n-1)-1 paths, For each path, there could be at most n-2 intermediate nodes => O(n) build a path
#思路: dfs backtracking, 記得該node 遍歷完後 要remove 該nodey在path與visited的紀錄, 給上一層乾淨的環境
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        res = []
        start, end = 0, len(graph) - 1
        self.dfs(start, end, [], visited, res, graph)
        return res
        
    def dfs(self, node, end, path, visited, res, graph):
        if node in visited:
            return
        if node == end:
            res.append(path+[end])
            return
        path.append(node)
        visited.add(node)
        for nxt in graph[node]:
            self.dfs(nxt, end, path, visited, res, graph)
        path.pop()
        visited.remove(node)
        return



















