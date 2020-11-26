'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. 
Given a list of positions to operate, count the number of islands after each addLand operation. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''

# UnionFind
# Use a land set to store all previous added lands.
# When a new land comes in, set union root to itself and add number of islands by 1.
# Check if any neighbor of this new land is already in our land set.
# If a neighbor is a previous added land, union these two. And minus the number of islands by 1, ONLY if we merged two unions.
# Attention: some neighbors may belong to the same union.
# After checking all its neighbors, add the number of islands to result list.
# Time: O(klog(mn))
# Space: O(mn)
# k is the length of positions
# input m and n are only useful, if we use list, instead of set =>  not resulted to index out of range


#參考別人, 刷題用這個, time complexity O(klog(mn)), space complexity O(mn)
#思路: 使用union find, 當新land 加入時, COUNT += 1, 並check四周有無land, 若有=>merge, 若兩者不屬於同一個島嶼 => count -= 1, 若屬於同一個則不做動作, 並把最後count 登入在res
class DSU:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.counts = 0
    
    def setParent(self, x):
        if x in self.parents:
            return
        self.parents[x] = x
        self.ranks[x] = 1
        self.counts += 1
        
    def findParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.findParent(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        par_x, par_y = self.findParent(x), self.findParent(y)
        if par_x != par_y:
            if self.ranks[par_x] < self.ranks[par_y]:
                par_x, par_y = par_y, par_x
            self.parents[par_y] = par_x
            self.ranks[par_x] += self.ranks[par_x] == self.ranks[par_y] #union 跟自己一樣的大的, rank + 1
            self.counts -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU()
        res = []
        for pos in positions:
            pos = tuple(pos)
            dsu.setParent(pos)
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = pos[0] + d[0], pos[1] + d[1]
                if (nx, ny) in dsu.parents:
                    dsu.union(pos, (nx, ny))
            res.append(dsu.counts)
        return res






















