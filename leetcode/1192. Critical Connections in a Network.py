# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] 

# represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
 

# Constraints:

# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.


# Tarjan Algorithm (DFS) Python Solution with explanation

# In tarjan algorithm, we keep two arrays DFN and LOW in DFS procedure. 
# DFN array records the order of DFS for each node while LOW array records the lowest order of each node's neighbor except its direct parent. 
# Initially, LOW[i] equals to DFN[i].
# After DFS, we find edge(u,v) where DFN(u)<LOW(v) and get the final answers.

# https://www.cnblogs.com/nullzx/p/7968110.html 建議看
# time complexity: O(V + E), space complexity: O(V + E), 3372ms
# 思路: 此題 tarjan 不需求割點, 只求割邊, 因此不用考慮root 是否是割點的狀況
# tarjan 思路: 利用 dfs 遍歷 undirected graph, 設置dfn 與 low arrays, dfs遍歷途中 dfn[i] 紀錄該node遍歷的順序
# low[i] 則是代表該node不經過parent node 可以遇到nodes中最小的遍歷順序, 也包含自己
# 最後找割邊, 割邊的定義就是拿掉該邊, undirected graph 的connected components 會變多
# u, v 若low[v] > dfn[u] or low[u] > dfn[v] 則 u-v 就是割邊
from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
        res = []
        self.cur = 0
        self.dfs(0, None, graph, dfn, low)
        for v in connections:  #遍歷邊, 看能否找到割邊 cut edge
            if low[v[0]] > dfn[v[1]] or low[v[1]] > dfn[v[0]]:
                res.append(v)
        return res

    def dfs(self, node, parent, graph, dfn, low):
        if dfn[node] is None: #未遍歷
            dfn[node] = self.cur
            low[node] = self.cur
            self.cur += 1 #時間stamp ++
            for n in graph[node]:
                if dfn[n] is None:
                    self.dfs(n, node, graph, dfn, low)
                
            if parent is not None:
                l = min([low[i] for i in graph[node] if i!=parent]+[low[node]]) ## +[low[node]] 表示加入low[node] 一起比誰最小 [1] + [2] => [1,2]
            else:
                l = min(low[i] for i in graph[node]+[low[node]])
            low[node] = l



#自己重寫, time complexity O(V+E)
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        dfn = [None for _ in range(n)]
        low = [None for _ in range(n)]
        self.cur = 0
        res = []
        
        self.dfs(0, None, graph, dfn, low)
        
        for edge in connections:
            if low[edge[0]] > dfn[edge[1]] or low[edge[1]] > dfn[edge[0]]:
                res.append(edge)
        return res
        
    
    def dfs(self, node, parent, graph, dfn, low):
        if dfn[node] == None:
            dfn[node] = low[node] = self.cur
            self.cur += 1
            for i in graph[node]:
                self.dfs(i, node, graph, dfn, low)
            
            if parent != None:
                l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
            else:
                l = min([low[i] for i in graph[node]] + [low[node]])
            low[node] = l


# 重寫第二次, time complexity O(n), space complexity O(N)
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for pair in connections:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        cur = 0
        dfn = [None for _ in range(n)]
        low = [None for _ in range(n)]
        def dfs(node, parent):
            nonlocal cur
            nonlocal dfn
            nonlocal low
            if dfn[node] == None:
                dfn[node] = cur
                low[node] = cur
                cur += 1
                for nxt in graph[node]:
                    if dfn[nxt] == None:
                        dfs(nxt, node)
                if parent != None:
                    low[node] = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    low[node] = min([low[i] for i in graph[node]] + [low[node]])
        dfs(0, None)
        ans = []
        for pair in connections:
            if dfn[pair[0]] < low[pair[1]] or dfn[pair[1]] < low[pair[0]]:
                ans.append(pair)
        return ans




