'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]
 

Constraints:

1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
# There is no repeated edges and no self-loops in the graph. 題目條件
# The Graph is connected and all nodes can be visited starting from the given node. 題目條件
# 刷題用這個 recursion 優先
# DFS recursively, time complexity O(V+E)
# 思路: 利用dict來存對應的copy node, 利用dfs精神 來遍歷串連neighbor, 遇到之前未遍歷過的建立新node, 遇到已遍歷過的建立連結即可
# 畫個conected graph 就清楚了, 每個點只有copy 一次, 此題是undirected graph
class Solution:
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val)  #新建node = nodeCopy 也可以寫成 Node(node.val,[])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy
    
    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:  #幫忙建copy
                neighborCopy = Node(neighbor.val)
                dic[neighbor] = neighborCopy #建立鄰居copy
                dic[node].neighbors.append(neighborCopy)  #建立鄰居 of nodeCopy
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])  #這句重要, 加入已經建立的neighborCopy,
               # ex: 相連接的兩個節點互為鄰居, 其一幫對方建立copy, 對方則不需要為自己建copy, 直接拿來用就好, 若幫對方重新建立node, 則對方與你的連結也就消失了, 而且會無限循環
               # dfs 精神, 已拜訪過的就無需再深入拜訪, 因此這裡就無需dfs下去, 只需建立連結就行
# BFS
class Solution:
    def cloneGraph1(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val) #新建node = nodeCopy 也可以寫成 Node(node.val,[])
        dic = {node: nodeCopy} #key:value
        queue = collections.deque([node]) #新建dequeu = [node] 
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors: #node.neighbors = []
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy #build up a neighbor kay:value pair
                    dic[node].neighbors.append(neighborCopy) #nodeCopy.neighbors list append
                    queue.append(neighbor) #遍歷圖的每個node
                else:
                    dic[node].neighbors.append(dic[neighbor]) #dic[node] = 當下nodeCopy, dic[neighbor]=neighborCopy(already created)
        return nodeCopy

# DFS iteratively
class Solution:
    def cloneGraph2(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy





































