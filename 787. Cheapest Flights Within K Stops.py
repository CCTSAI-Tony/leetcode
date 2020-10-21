'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles. flight 都是unique

There will not be any self cycles means no [1,1,100] 這種東西.
'''
#注意 Dijkstra algorithm 只適用 all edge weights are non-negitive but 是否dag則沒關係(directed acyclic graph)


#  Priority Queue Solution

# A good case to practice Dijkstra.

# To implement Dijkstra, we need a priority queue to pop out the lowest weight node for next search. 
# In this case, the weight would be the accumulated flight cost. 
# So my node takes a form of (cost, src, k). cost is the accumulated cost, 
# src is the current node's location, k is stop times we left as we only have at most K stops. 
# I also convert edges to an adjacent list based graph g.

# Once k is used up (k == 0), we no longer push that node to our queue. Once a popped cost is our destination, we get our lowest valid cost.


# For Dijkstra, there is no need to maintain a best cost for each node since it's kind of greedy search. 
# It always chooses the lowest cost node for next search. 
# So the previous searched node always has a lower cost and has no chance to be updated. 
# The first time we pop our destination from our queue, we have found the lowest cost to our destination.



# Making the graph takes O(E)
# The size of priority queue is O(V), since we might put all the cities in it.
# So for every pop, it is O(LogV). Total is O(VLogV).
# For every edge we call an heappush, so that is ELogV
# O(E+ (V+E)LogV) -> O((V+E)LogV)
# V is the number of cities within range K stops, may have duplicate cities, which can be interpreted as each cities has k states(不同路徑)

# time complexity O((V+E)LogV)
# 思路: 利用heap 特性 heap.pop pop出 目前總花費最小的路徑, 再添加花費最小的新航線給該路徑, 但有限制一旦k == 0 但還未到目的地 則停止添加新路徑至pq, heap.pop出次要路徑繼續完成
# 這一題與傳統Dijkstra 思維有些落差, 只有用到min q的點子 比較像, 因為只要找到最終點, 其他點是不是最便宜不care, 所以使用greedy
import heapq
class Solution:
    def findCheapestPrice(n, flights, src, dst, K):
        pq, g = [(0,src,K+1)], collections.defaultdict(dict)  #注意為什麼是k+1, 因為把destination 也算進去了
        for s,d,c in flights: 
            g[s][d] = c  #好招 利用defaultdict(dict) 來達成g[s][d] = c, g[s] 是dict, [d] 是它其中一個key
        while pq:
            cost, s, k = heapq.heappop(pq)  #pop 出目前最小總花費的路徑
            if s == dst: 
                return cost
            if k:
                for d in g[s]:  #heappush 同一個出發點的航班, 這裡d代表在g[s] dict裡的 key們
                    heapq.heappush(pq, (cost+g[s][d], d, k-1))
        return -1





# Python heapq doesn't support update heap node's weight. 
# But if you implement your own heap structure and support that function, 
# you can maintain a n-size heap and time complexity is O((m + n)logn). m is number of edges and n is number of nodes. 
# 看課本p662 decrease key 代表 update vertex weight(減少key value, RELAX)
# And it can be improved to O(m + nlogn) with a Fibonacci heap where a delete min costs logn but an update cost costs constant time.



# You can do some research on Dijkstra’s algorithm. In general, it’s a greedy method to find the shortest path. 
# It consists of two operations, find the node with minimal cost (heappop), 
# and update node’s cost based on all the edges that incident on that node (heappush). 
# It’s greedy so all the nodes and edges will be visited once. So there are o(n) find min node and o(m) update node cost. 
# With a binary heap, both find min and update cost use o(logn). 
# With a Fibonacci heap, find min uses o(logn) and update cost uses o(1) amortized time. So total cost is o(m+nlogn).


# https://www.geeksforgeeks.org/binary-heap/

# Operations on Min Heap:
# 1) getMini(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).

# 2) extractMin(): Removes the minimum element from MinHeap. 
# Time Complexity of this Operation is O(Logn) as this operation needs to maintain the heap property (by calling heapify()) after removing root.

# 3) decreaseKey(): Decreases value of key. The time complexity of this operation is O(Logn). 
# If the decreases key value of a node is greater than the parent of the node, then we don’t need to do anything. Otherwise, 
# we need to traverse up to fix the violated heap property.


# BFS
# This is mostly straight forward BFS.
# When we are out of stops, or price is greater than min_price, we stop adding cities to the queue.
# Every time we encounter dst we compare the price and set it to the min.

# Making the graph takes O(E)
# BFS every node in adjacent list takes O(V+E), popleft V cities, append E edges
# V is the number of cities within range K stops. may have duplicate cities, which can be interpreted as each cities has K states

#刷題用這個, bfs, time complexity O(V+E), space complexity O(V+E)
#思路: 利用defaultdict 來串連同一個start起飛的航線, 再利用bfs queue 來逐一過濾與處理候選路徑花費
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        q = collections.deque()
        min_price = float('inf')

        for start, end, cost in flights: 
            graph[start].append((cost, end))
        q.append((src, 0, 0))
        while q:
            for _ in range(len(q)):
                city, stops, price = q.popleft()
                if city == dst:
                    min_price = min(min_price, price)
                    continue

                if stops < K+1 and price < min_price: #stops < K+1 包含終點
                    for price_to_end, end in graph[city]:
                        q.append((end, stops+1, price+price_to_end))

        return min_price if min_price != float('inf') else -1


# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200













