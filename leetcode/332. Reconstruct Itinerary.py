 '''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

Python Recursive DFS, the key bit here is to prove that when we get struck, its indeed the last destination.
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B 解題思想! 強烈推薦
# 思路: 此題就是euler path, 遍歷圖的每個有向邊,且只能遍歷一次, 機票用完一次就沒了 => 此題有變種 => retoreNumbersOnCircle
# 題目有說from JFK 出發一定能遍歷全部的tickets, 代表全部有向邊都會run過一次, 且只有一次, 注意不是每個頂點出發都可以用光所有機票
# 此題重點是針對start 的airports 能到達的地方做排序, lexicographical order小的放後面, 這樣優先pop出來, 也就是route優先選擇lexicographical order當下一站
# 此題利用dfs來做深度排序, 同一個airport 在dfs遍歷有可能遍歷一次以上, 但每次遍歷到同一個 airport的時, 此airport選擇數都不一樣, 越接近底層選擇數越接近0, 也越早被寫進res
# 此題想法, 利用dfs 遍歷完該機場所有選擇路線後, 才 res append 該機場 -> 因為遍歷過程該機場還不是end node
# 不容易懂, 看圖就清楚了, 只要記得此題從JFK 出發一定能找到euler path
# 這種解法是bottom up的, 先找出last destination, => 請看下面補充知識
# time complexity O(nlogn), space complexity O(n)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjMap = self.makeAdjMap(tickets)
        res = []
        self.dfs(adjMap, "JFK", res)
        return res[::-1]
    
    def dfs(self, adjMap, airport, res):
        if airport in adjMap and len(adjMap[airport]) > 0:  # if airport in adjMap, 防止有機場沒辦法從那啟程, 沒辦法成為key     
            while len(adjMap[airport]) > 0:
                destination = adjMap[airport].pop()
                self.dfs(adjMap, destination, res)
        res.append(airport)
        
    def makeAdjMap(self, tickets):
        adjMap = {}
        for ticket in tickets:
            if ticket[0] not in adjMap:
                adjMap[ticket[0]] = [ticket[1]]
            else:
                adjMap[ticket[0]].append(ticket[1])
        for ticket in tickets:  #對到達地做排序, 字母排序小的放後面
            adjMap[ticket[0]].sort(reverse=True)
        return adjMap    

#刷題用這個
#重寫第二次, time complexity O(nlogn), space complexity O(n)
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for star, end in tickets:
            graph[star].append(end)
        for k in graph:
            graph[k].sort(reverse=True)
        self.res = []  
        self.dfs("JFK", graph)
        return self.res[::-1]
        
    def dfs(self, start, graph):
        while graph[start]:
            nxt = graph[start].pop() #pop掉, 代表此路徑被用過了
            self.dfs(nxt, graph)
        self.res.append(start)

#重寫第三次, time complexity O(nlogn), space complexity O(n), n = total tickets
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = list()
        flights = defaultdict(list)
        for ticket in tickets:
            s, e = ticket
            flights[s].append(e)
        for source in flights:
            flights[source].sort(reverse=True)
        
        self.dfs("JFK", flights, itinerary)
        return itinerary[::-1]
    
    def dfs(self, start, flights, itinerary):
        while flights[start]:
            nxt = flights[start].pop()
            self.dfs(nxt, flights, itinerary)
        itinerary.append(start)

# 補充知識 重要!!
# A directed graph has an Eulerian trail if and only if at most one vertex has (out-degree) − (in-degree) = 1, 
# at most one vertex has (in-degree) − (out-degree) = 1, every other vertex has equal in-degree and out-degree, 
# and all of its vertices with nonzero degree belong to a single connected component of the underlying undirected graph.
# 這就能解釋為什麼上面解法行得通!! start 與 end 各只有一個, 從start起飛不管怎麼飛stuck的地方都是一樣的, 就是end
# So, the algorithm is to find the end node first and delete the path to this node(backtrack), meanwhile using PriorityQueue to guarantee lexical order.
# Really amazing solution, I always don't know how to deal with Euler Path and know I begin to be some less confused.

#參照上面, 自己重寫, 刷題用這個 time complexity O(n)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airmap = {}
        res = []
        for ticket in tickets:
            if ticket[0] not in airmap:
                airmap[ticket[0]] = [ticket[1]]
            else:
                airmap[ticket[0]].append(ticket[1])
        for airport in airmap.keys():
            airmap[airport].sort(reverse=True)
        
        self.dfs("JFK", airmap, res)
        return res[::-1]
    
    def dfs(self, airport, airmap, res):
        if airport in airmap and len(airmap[airport]) > 0:
            while len(airmap[airport]) > 0:
                nextair = airmap[airport].pop()
                self.dfs(nextair, airmap, res)
        res.append(airport)

#再重寫一次
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for airports in graph.values():
            airports.sort(reverse=True)
        self.dfs("JFK", graph, res)
        return res[::-1]
    
    def dfs(self, airport, graph, res):
        if airport not in graph:
            res.append(airport)
            return
        while len(graph[airport]) > 0:
            next_air = graph[airport].pop()
            self.dfs(next_air, graph, res)
        res.append(airport)


#retoreNumbersOnCircle 變種題 => euler path 走完所有有向邊各一次 => 剛好走完一個環所有有向邊, 但頭尾vertex重複, 去掉其中一個, 從哪個vertex開始遍歷就是頭
from collections import defaultdict
class Solution:
    def restoreNumbersOnCircle(self, pairs: list) -> list:
        graph = defaultdict(list)
        res = []
        visited = set()
        for i in range(len(pairs)): #record key:vertec, value: edge
            graph[pairs[i][0]].append(i)
            graph[pairs[i][1]].append(i)
        first = pairs[0][0] #開頭
        self.dfs(first, graph, res, pairs, visited)
        return res[:-1]

    def dfs(self, node, graph, res, pairs, visited):
        for edge in graph[node]:
            if edge in visited:
                continue
            visited.add(edge)
            new_node = pairs[edge][0] if pairs[edge][0] != node else pairs[edge][1]
            self.dfs(new_node, graph, res, pairs, visited)
        res.append(node)

a = Solution()
a.restoreNumbersOnCircle([(3,4),(5,3),(2,4),(3,5),(3,2)])







https://www.quora.com/What-is-the-degree-of-vertex-in-a-directed-graph
https://leetcode.com/problems/reconstruct-itinerary/discuss/359942/Awesome-question-or-new-algo-to-learn-or-Eulerian-Path-or-Full-explanation-or-Code

# A connected graph has an Euler cycle if every vertex has even degree
# A Graph must have nodes with even degree and odd degree. 
# All the odd degree nodes are either start or end but all the even degree node will be only intermediate nodes.
# But in case when all the nodes has even degree, then it contains the Eulerian Tour, 
# as we we'll start from some node and will end to this same node, as we need to consume all the edges.
# directed graph node's degree is indegree + outdegree
# 重要!! eulerian path is not eulerian circle, but eulerian circle is one type of eulerian path

# Eulerian path
# In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
# Similarly, an Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex. 
# Important: 下面講的是 undirected graph!!
# If all nodes in graph has odd degree than its not possible to build Eulerian Path, 
# as for coming and going from/to a node we require even degree for some of the node.




#  另一種解法 dfs backtracking
#  思路: 請看下面, 這種解法比較直觀, 跟上面比起來, 這個方法是不斷check完整路徑長度是否等於self.valid_length, 若不是再回朔 check 其他分支
#  直到試到正確順序, 完整路徑長度才會等於self.valid_length, 記得每次挑下一個機場時都要sort, 
#  有趣的是, 每次試的完整路徑最後一站都是一樣的, 如同上面方法所說, 這個euler path, 只會有一組start and end
#  這種解法是top-down的
class Solution(object):
    def __init__(self):
        self.valid_length = 0
    
    def findItinerary(self, tickets):
        
        if tickets == None or len(tickets) == 0:
            return None
        
        # First make an adjacency map out of the tickets
        ticket_map = self.buildMap(tickets)
        #print(ticket_map)
        
        # Add the root and start the DFS
        route = ['JFK']
        self.dfs('JFK', route, ticket_map)
        
        return route


    def buildMap(self, tickets):
        # first lets put everything into a dict for easy lookup
        # format is start as key and [ends] as value
        ticket_map = {}
        for ticket in tickets:
            #print(ticket)
            start = ticket[0]
            dest = ticket[1]
            if not start in ticket_map:
                ticket_map[start] = [dest]
            else:
                ticket_map[start].append(dest)
                
        self.valid_length = len(tickets) + 1  #why + 1, ex: 四個邊五個節點
        return ticket_map
        
        
    def dfs(self, node, route, ticket_map):
        
        if node in ticket_map and len(ticket_map[node]) > 0:
            # Sort them so we'll pick the first lexographic path if there are several results
            children = sorted(ticket_map[node])  #新建一個sorted 的 list

            for child in children:
                route.append(child)                
                
                # first remove this path from the map
                ticket_map[node].remove(child)
                # Now go down to the next level
                result = self.dfs(child, route, ticket_map)
                
                # See if the DFS on that child produced a valid result, if so return it
                if len(result) == self.valid_length:
                    return result
                
                # The DFS did not produce the valid result, so undo the changes and try the next child
                else:
                    del route[-1]
                    ticket_map[node].append(child)
            
        return route  #base case, 隨著backtracking 不斷增減

a = {1:[1,2,3]}
a[1].remove(2)
a
{1: [1, 3]}


a = [1,2,3,4,5]
del a[-1]
a
[1, 2, 3, 4]



# The nice thing about DFS is it tries a path, and if that's wrong (i.e. path does not lead to solution), 
# DFS goes one step back and tries another path. It continues to do so until we've found the correct path (which leads to the solution). 
# You need to always bear this nice feature in mind when utilizing DFS to solve problems.

# In this problem, the path we are going to find is an itinerary which:

# uses all tickets to travel among airports
# preferably in ascending lexical order of airport code
# Keep in mind that requirement 1 must be satisfied before we consider 2. If we always choose the airport with the smallest lexical order, 
# this would lead to a perfectly lexical-ordered itinerary, but pay attention that when doing so, 
# there can be a "dead end" somewhere in the tickets such that we are not able visit all airports (or we can't use all our tickets), 
#     which is bad because it fails to satisfy requirement 1 of this problem. Thus we need to take a step back and try other possible airports, 
#     which might not give us a perfectly ordered solution, but will use all tickets and cover all airports.

# Thus it's natural to think about the "backtracking" feature of DFS. 
# We start by building a graph and then sorting vertices in the adjacency list so that when we traverse the graph later, 
# we can guarantee the lexical order of the itinerary can be as good as possible. When we have generated an itinerary, 
# we check if we have used all our airline tickets. If not, we revert the change and try another ticket. We keep trying until we have used all our tickets.




# One must use all the tickets once and only once. 題目要求
# Simply simple Python Solution - Using stack for dfs - with comments
# time complexity O(n), n: len(tickets)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}  #dict
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:  #src: source dst: destination
            if src in graph:
                graph[src].append(dst)  #增加目的地選擇
            else:
                graph[src] = [dst]  #build a key

        for src in graph.keys():
            graph[src].sort(reverse=True)  #for lexical order purpose
            # Sort children list in descending order so that we can pop last element 
            # instead of pop out first element which is costly operation
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting airport and keep adding the next child to traverse 
        # for the last airport at the top of the stack. If we reach to an airport from where 
        # we can't go further then add it to the result. This airport should be the last to go 
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this, backtrack to the top airport in the stack and continue to traaverse it's children @@
        ##重要, 因為題目有講至少有一組解, 但是最終站一定是一樣的, 就像dfs graph 我們一路找尋終點, 之後回到上一層遍歷未走完的其他分支
        #另外,遍歷其他分支, 每個分支一定有管道又回到上一層, 所以並不像終點是deadend, 看不懂請看最下面例子
        #就是無路可走的機場就如同遍歷完的節點,拿掉放進res,之後backtrack到上一層,上一層節點最終也無路可走

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:  
                # Check if elem in graph as there may be a case when there is no out edge from an airport 
                # In that case it won't be present as a key in graph
                stack.append(graph[elem].pop())  #pop出 lexical order 最前面的
            else:  #代表這個airport 從來都不是起飛點 或者 從他起飛的目的地都已完成
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't go anywhere from this
                # That's why we return the reverse of the result
        return res[::-1]





class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
        stack = []
        res = []
        stack.append("JFK")
        
        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0: 
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]




# class Solution:
#     def findItinerary(self, tickets):
#         graph = {}
#         for src, dst in tickets:
#             if src in graph:
#                 graph[src].append(dst)
#             else:
#                 graph[src] = [dst]

#         for src in graph.keys():
#             graph[src].sort(reverse=True)
#         stack = []
#         res = []
#         stack.append("JFK")
        
#         while len(stack) > 0:
#             elem = stack[-1]
#             print(stack)
#             if elem in graph and len(graph[elem]) > 0: 
#                 stack.append(graph[elem].pop())
#             else:
#                 res.append(stack.pop())
#                 print('res',res)
#         return res[::-1]

# a = Solution()
# a.findItinerary([["JFK","AFO"],["JFK","ATL"],["AFO","ATL"],["ATL","JFK"],["ATL","AFO"]])


# ['JFK']
# ['JFK', 'AFO']
# ['JFK', 'AFO', 'ATL']
# ['JFK', 'AFO', 'ATL', 'AFO']
# res ['AFO']
# ['JFK', 'AFO', 'ATL']
# ['JFK', 'AFO', 'ATL', 'JFK']
# ['JFK', 'AFO', 'ATL', 'JFK', 'ATL']
# res ['AFO', 'ATL']
# ['JFK', 'AFO', 'ATL', 'JFK']
# res ['AFO', 'ATL', 'JFK']
# ['JFK', 'AFO', 'ATL']
# res ['AFO', 'ATL', 'JFK', 'ATL']
# ['JFK', 'AFO']
# res ['AFO', 'ATL', 'JFK', 'ATL', 'AFO']
# ['JFK']
# res ['AFO', 'ATL', 'JFK', 'ATL', 'AFO', 'JFK']

# Out[518]:
# ['JFK', 'AFO', 'ATL', 'JFK', 'ATL', 'AFO']






def test(numbers):
    res = 0
    start = check(numbers)[0]
    left = check(numbers)[1]
    while left:
        for i in range(start, len(numbers)):
            if numbers[i] > left:
                numbers[i] -= left
            else:
                res += left
        res += left
        start = check(numbers)[0]
        left = check(numbers)[1]
    return res
    
def check(array):
    for i in range(len(array)):
        if array[i] != 0:
            return (i, array[i])
        return (-1, 0)

























