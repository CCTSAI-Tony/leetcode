'''
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. 
Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to 
find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

# 完善一下楼主的措辞，更好理解
# A).关于无向无环图找最长链任选一节点找终点再由终点找另一端点的证明：
# 无向无环图所构成的最低高度树的根必为最长路径的中点或者两点，假设最长路径的端点为A,B
# Proof:
# 1.若以路径上其他点为根，则该点到某一端会更长；
# 2.若以不在路径AB上的点P为根，假设P到AB两个端点的路径与AB交点为O（注意只能有一个交点，否则会成环），则path(PO)+path(OA) or path(PO)+path(OB) 
# 必有一个大于最长路径取中点的高度max(PO+OA,PO+OB) > (AB)/2

# p
# .
# .
# A…….O....B
# B).关于无向图求最长路径的方法，任选一个节点Q，dfs/bfs到最远点W停止，则QW为Q为起点的最长路径，W必为图最长路径的一个端点，再以此端点W起步dfs/bfs找到另一个端点M，则WM为图的最长路径
# proof:假设Q为起点的最长路径QW若不为图最长路径的端点：假设Q通过l1路径与图最长路径AB交于q,
# 1.该路径不与图最长路径相交，不可能，因为若max(Aq,Bq)+qQ<QW,则可以构造新的最长路径max(Aq,Bq)+qQ+QW>Aq+Bq

# Q
# .
# .
# A…….q….B
# .
# W
# 2.该路径QW与AB相交于q点，若该路径Qq+qW>Qq+max(qA,qB),可推出qW>max(qA,qB),可构造新最长路径max(qA,qB)+qW>qA+qB

# 故该路径必为图最长路径的端点，证毕

# The idea is 'delete leaves layer by layer, until we reach the root'. 
# Find all the leaves and delete them, after removing, some nodes will become new leaves.Eventually there will be 1 level of leaves, that's the results we need.

#  python, Topological sort using BFS, 在這undirected grapgh 需要做一點變化
#  此題特別點 For an undirected graph with tree characteristics, 若有circle, 則找不出minimum height
#  思路: 此題關鍵點就是利用bfs topological sort的技巧套用在undorected grapgh, 變成找出最後一層indegree = 1 的 nodes
#  簡單思維就是undirected acyclic graph, 最低高度數的根必為最長路徑的中點 or 兩點(若最長路徑為偶數)
#  此題不用設visited, 因為條件不可逆, 曾經為indegree = 1 的nodes, 下一層的nodes 會把他們變成0
#  indegree = 1 代表目前是最外層, 向內indegree > 1
#  time complexity O(V+E)
import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:  #edge case 這很重要
            return [0]
        graph = collections.defaultdict(list) #key value default 是一個空list
        queue = collections.deque()
        indegree = [0]*n
        #undirected graph in adjacency list， and update the degree for each node,
        #remember it's undirected graph
        for pair in edges:
            graph[pair[0]].append(pair[1]) #針對每個節點計算degree 一個點的「度」：一個點的邊數量。
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] +=1
            indegree[pair[1]] +=1
        #the smallest degree is 1, which represent all these leaves
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        while queue:
            path = [] #若有下層node, path reset
            #standard BFS using deque
            for _ in range(len(queue)):  #利用底層與上層之相連node不斷往上削減indegree來找出上層root
                vertex = queue.popleft()
                path.append(vertex)  #紀錄當層indegree = 1 的 node, 最後queue都被pop完, 離開while loop, return 最後一層indegree = 1 的 node
                for neigh in graph[vertex]:
                    indegree[neigh] -=1
                    if indegree[neigh] == 1: 
                        queue.append(neigh)
        return path

# 這題若用傳統bfs 對每個node(視為擴散中心)執行bfs得出有幾層=> height, 在從中挑選最少的nodes 一定會tle

#自己重寫
from collections import deque, defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [0] * n
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
            
        while queue:
            path = []
            for _ in range(len(queue)):
                node = queue.popleft()
                path.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)
        return path










