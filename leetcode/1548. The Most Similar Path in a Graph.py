'''
We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai with city bi. 
Each city has a name consisting of exactly three upper-case English letters given in the string array names. 
Starting at any city x, you can reach any city y where y != x (i.e., the cities and the roads are forming an undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph of the same length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance. 
The path should be of the same length of targetPath and should be valid (i.e., there should be a direct road between ans[i] and ans[i + 1]). 
If there are multiple answers return any one of them.

The edit distance is defined as follows:


 

Example 1:


Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
Output: [0,2,4,2]
Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
[0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
[0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
[0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
Example 2:


Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
Output: [0,1,0,1,0,1,0,1]
Explanation: Any path in this graph has edit distance = 8 with targetPath.
Example 3:



Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
Output: [3,4,5,4,3,2,1]
Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
 

Constraints:

2 <= n <= 100
m == roads.length
n - 1 <= m <= (n * (n - 1) / 2)
0 <= ai, bi <= n - 1
ai != bi
The graph is guaranteed to be connected and each pair of nodes may have at most one direct road.
names.length == n
names[i].length == 3
names[i] consists of upper-case English letters.
There can be two cities with the same name.
1 <= targetPath.length <= 100
targetPath[i].length == 3
targetPath[i] consists of upper-case English letters.
 

Follow up: If each node can be visited only once in the path, What should you change in your solution?
'''


# Idea

# Let's first calculate the minimum edit distance without worrying about the path. We can use 2D DP to do that:

# dp[i][v] means the minimum edit distance for tp[:i+1] ending with city v.
# The trainsition function is:

# dp[i][v] = min(dp[i][v], dp[i-1][u] + edit_cost(v)) for all edges (u, v)
# , where edit_cost(v) at index i is names[v] != tp[i].

# And the minimum edit distance will be min(dp[-1][v] for v in range(n)).

# To construct the optimal path, we can maintain a 2D array (or dict) prev when populate dp. Suppose prev[i][v] is u. 
# Then (u, v) is the ending edge of the optimal path at dp[i][v].


# Complexity

# Time complexity: O(N^2 * len(tp))
# Space complexity: O(N * len(tp))


# 刷題用這個, time complexity O(N^2 * M), space complexity O(N* M), n: len city, m: len target path
# 思路: dp[i][v] means the minimum edit distance for tp[:i+1] ending with city v.
# 2d dp, dp[i][v] = min(dp[i][v], dp[i-1][u] + edit_cost(v)) for all edges (u, v), where edit_cost(v) at index i is names[v] != tp[i].
# 再建立2d prev dp 來重建path, dp[i][v] => prev[i][v]
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # init variables
        m = len(targetPath)
        dp = [[m] * n for _ in range(m)]
        prev = [[0] * n for _ in range(m)]
        
        # populate dp
        for v in range(n):
            dp[0][v] = (names[v] != targetPath[0])
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]: # 一開始 dp[i][v] = m
                        dp[i][v] = dp[i-1][u]
                        prev[i][v] = u
                dp[i][v] += (names[v] != targetPath[i])
                
        # re-construct path
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m - 1, 0, -1):  # why 0 not -1, 因為起始點沒prev
            u = prev[i][path[-1]]
            path.append(u)
            
        return path[::-1]


# 重寫第二次, time complexity O(N^2 * M), space complexity O(N* M), n: len city, m: len target path
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        m = len(targetPath)
        dp = [[m] * n for _ in range(m)]
        prev = [[0] * n for _ in range(m)]
        
        for v in range(n):
            dp[0][v] = names[v] != targetPath[0]
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]:
                        dp[i][v] = dp[i-1][u]
                        prev[i][v] = u
                dp[i][v] += names[v] != targetPath[i]
        ans = [0]
        min_dist = m
        for v in range(n):
            if dp[m-1][v] < min_dist:
                ans[0] = v
                min_dist = dp[m-1][v]
        for i in range(m-1, 0, -1):
            ans.append(prev[i][ans[-1]])
        return ans[::-1]





