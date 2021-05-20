'''
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). 
You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. 
The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
'''

#思路: bfs topological sort 來檢查是否有環 + 尋找最長路徑, time complexity O(v + e), space complexity O(v + e)
from collections import defaultdict, deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        degree = [0] * n
        graph = defaultdict(list)
        f = defaultdict(lambda: defaultdict(int))
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            degree[b] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)
        p = []
        while queue:
            t = queue.popleft()
            p.append(t)
            for j in graph[t]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
        if len(p) < n:
            return -1
        res = 0
        for i in p:
            c = ord(colors[i]) - ord("a")
            f[i][c] = max(f[i][c], 1) # 只算本身一個node, 自身顏色算一個
            for j in range(26): # 枚舉26種顏色
                for k in graph[i]: # 因為沒有環, 可以在下層不同路徑下, 更新下層node最大color value => f[k][j]
                    t = 0
                    if ord(colors[k]) - ord('a') == j:
                        t = 1
                    f[k][j] = max(f[k][j], f[i][j] + t) # 更新到k節點, 路徑該顏色的node最多有幾個
                res = max(res, f[i][j]) #更新max => 到i節點有該顏色的color value
        return res
