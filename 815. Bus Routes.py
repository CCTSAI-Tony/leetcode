'''
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], 
this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, 
what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
'''

#刷題用這個, time complexity O(len(bus_stops))
#思路: 利用bus_stop當作node, route當作edge => 建立undirected graph
#要注意的地方 => 建立 route_seen 來過濾重複的route, 但不需要建立bus_seen 來過濾重複的bus_stop, 因為過濾重複的route自然就過濾重複的bus_stop
#同一個route 有可能有重複的bus_stop => defaultdict(set) 來過濾同一個公車站重複的route
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        path = defaultdict(set)
        for i, v in enumerate(routes):
            for bus_stop in v:
                path[bus_stop].add(i) #同一個route 有可能有重複的bus_stop => 造成重複add route
        route_seen = set()
        queue = deque([S])
        taken = 0
        while queue:
            for _ in range(len(queue)):
                bus_stop = queue.popleft()
                if bus_stop == T:
                    return taken
                for route in path[bus_stop]:
                    if route not in route_seen:
                        route_seen.add(route)
                        for next_bus in routes[route]:
                            if next_bus != bus_stop: #過濾掉本身的bus_stop
                                queue.append(next_bus)
            taken += 1
        return -1



#自己想的 time complexity O(n^2*m^2) => n: len(routes), m: max(len(routes[i]))
#思路: 以bus 當作node, 若bus1, bus2 都有停特定bus_Stop, 則bus1 與 bus2 連結起來 => undirected graph
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = defaultdict(list)
        for i, v in enumerate(routes):
            for n in v:
                for j, w in enumerate(routes):
                    if i != j and n in w:
                        graph[i].append(j)
        
        queue = deque()
        seen = set()
        for i, v in enumerate(routes):
            if S in v:
                queue.append((i))
                seen.add(i)
        bus_count = 1
        while queue:
            for _ in range(len(queue)):
                bus = queue.popleft()
                if T in routes[bus]:
                    return bus_count
                for transfer in graph[bus]:
                    if transfer not in seen:
                        queue.append(transfer)
                        seen.add(transfer)
            bus_count += 1
        return -1