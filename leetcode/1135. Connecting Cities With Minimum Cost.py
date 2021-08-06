'''
There are n cities labeled from 1 to n. 
You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi 
and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. 
If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.

 

Example 1:


Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:


Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
 

Constraints:

1 <= n <= 104
1 <= connections.length <= 104
connections[i].length == 3
1 <= xi, yi <= n
xi != yi
0 <= costi <= 105
'''
Prim -> add node -> bfs & minHeap

Kruskal -> add edge -> Sort by Cost & UnionFind


# 刷題用這個, time complexity O(nlogn)
# Prim, start from city 1
import heapq, collections
class Solution:      
    def minimumCostPrim(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a,b,cost in connections:
            graph[a].append((b,cost))
            graph[b].append((a,cost))
        visited = set()
        cost = 0
        minHeap = [(0,1)]
        while minHeap:
            minCost,city = heapq.heappop(minHeap)
            if city not in visited: # 這句很重要, 因為有很多相同城市, 但cost較大的路徑 => 要skip掉
                cost += minCost
                visited.add(city)  # 正式加到最小路徑
                for nxt,c in graph[city]:
                    if nxt not in visited:
                        heapq.heappush(minHeap,(c,nxt))
        return -1 if len(visited) < n else cost



class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.n = n
    def find(self,p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    def union(self,x,y):
        rx,ry = self.find(x),self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.n -= 1
            return True
        return False

class Solution:
    # Kruskal
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        cost = 0
        uf = UnionFind(N)
        for a,b,c in sorted(connections, key=lambda x:x[2]):
            if uf.union(a,b):
                cost += c
        return cost if uf.n == 1 else -1




