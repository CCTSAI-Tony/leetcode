'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), 
where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''

# Dijkstra=> 適用non-negative edge
# Time: O((V+E)logV) p662, 520ms
# Space: O(V+E)
# (max times while loops executes) log (max number of elements in the priority queue)
# = (Edge) * log ( Nodes)
#  思路: single source shortest path, 不懂看課本 p659
#  若出現edge有重量 通常使用 collections.defaultdict(dict) 來紀錄 weight[u][v] = w, 代表 u----->v weight: w
#  這邊使用heapq 來pop出 目前source 可以花最短的時間到達的頂點, 並利用dist 來紀錄已被加進去的頂點, 來以防重複加入
import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w #time function
        heap = [(0, K)]  # (time, node)
        dist = {}
        while heap:  #挑選最小的
            time, u = heapq.heappop(heap) #min q
            if u not in dist:  #把確定source 到該點時間的頂點加進來, 並防止重複加入
                dist[u] = time #紀錄sorce 到該頂點的時間
                for v in weight[u]: #與之相連的頂點
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))  #增加 與之相連的node 被relax 的 w, dist[u] 代表source 到 該頂點前一點的時間
        return max(dist.values()) if len(dist) == N else -1  # len(dist) == N 確保完全頂點都有, max(dist.values()) 最短路徑 source 到最後一個頂點所花的時間

#自己重寫
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        weight = defaultdict(dict)
        for u, v , w in times:
            weight[u][v] = w
        
        heap = [(0, K)]
        dist = {}
        
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == N else -1

# Bellman-Ford => 可以用在有negative edge, 但不能有negative edge cycle
# Time: O(VE), 1132 ms
# Space: O(N)
# 思路: bellman-ford p.651, 因為此題weight 是 time 都是正數, 所以不用check 是否有negative circle
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]  #一開始 source到所有的vertex 都是無限大
        dist[K-1] = 0  #zero based index issue, 一開始, source distance 設 0, 並開始relax 其他edge
        for _ in range(N-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        return max(dist) if max(dist) < float("inf") else -1 # if max(dist) < float("inf") else -1, 確保所有vertex, source 都能到得了

# anyone can explain why the solution for Bellman-Ford should loop for N-1 times? thx!
# I think it is because the longest path can only be length N-1.
# Therefore, if we do it N-1 times, we actually carefully make sure every length of path is updated correctly.





#自己重寫
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf")] * N
        dist[K-1] = 0
        for _ in range(N-1):
            for u, v, time in times:
                if dist[v-1] > dist[u-1] + time:
                    dist[v-1] = dist[u-1] + time
        return max(dist) if max(dist) != float("inf") else -1


