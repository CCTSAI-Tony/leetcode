'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. 
Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. 
For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
'''

An edge will connect two nodes into one connected component.

When we count an edge in, if two nodes have already been in the same connected component, the edge will result in a cycle. That is, the edge is redundant.

We can make use of Disjoint Sets (Union Find).
If we regard a node as an element, a connected component is actually a disjoint set.

For example,

Given edges [1, 2], [1, 3], [2, 3],
  1
 / \
2 - 3
Initially, there are 3 disjoint sets: 1, 2, 3.
Edge [1,2] connects 1 to 2, i.e., 1 and 2 are winthin the same connected component.
Edge [1,3] connects 1 to 3, i.e., 1 and 3 are winthin the same connected component.
Edge [2,3] connects 2 to 3, but 2 and 3 have been winthin the same connected component already, so [2, 3] is redundant.
Attention:The Union by Rank can optimize the time complexity from O(n) to O(logn) (even smaller).

#time complexity O(n), union find without Union by Rank and Path Compression
#思路: 此題若用一般dfs directed graph 找是否有backedge解法會行不通, 因為他要回報最大index 的 cycle caused edge 
#此題利用unifind 可以即時對input index 反應, 所以遇到cycle edge 的index 就是最大index of circle edge in input array (only one circle edge)
#若用傳統dfs方法, 要先build graph 這樣就無法表現原先array 的排序, 且無法一次找到可以remove 的 edge
class Solution(object):
    def findRedundantConnection(self, edges):
        parent = [0] * len(edges)
        for x, y in edges:
            if not self.union(x - 1, y - 1, parent): #x-1, y-1, zero based index issue
                return [x, y]
          
        raise ValueError("Illegal input.") #給自己測試test case 用的
    
    def union(self, x, y, parent):
        rootX = self.find(x, parent)
        rootY = self.find(y, parent)
        if rootX == rootY:
            return False
        parent[rootX] = rootY
        return True

    def find(self, x, parent): #use path compression
        if parent[x] == 0:
            return x
        parent[x] = self.find(parent[x], parent)
        return parent[x]
    
    
#自己重寫, 刷題用這個
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+ 1)]
        for (u, v) in edges:
            if not self.union(u, v, parent):
                return [u, v]
    
    def union(self, u, v, parent):
        pu, pv = self.find(u, parent), self.find(v, parent)
        if pu == pv:
            return False
        parent[pu] = pv
        return True
    
    def find(self, u, parent):
        if parent[u] == u:
            return u
        return self.find(parent[u], parent)






















