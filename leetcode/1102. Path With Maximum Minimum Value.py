'''
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9
'''

# Dijkstra
# Time: O(MN log MN), since for each element in matrix we have to do a heap push, => O(vlogv) Dijkstra 使用min-heap 初步估算
# which cost O(log # of element in the heap) times. The size of the heap can grow up to # of elemnts in the matrix.
# Space: O(MN). We need to keep track of the elements we have seen so far. Finally the size of seen will grow up to # of items in the matrix.

#刷題用這個
#思路: Dijkstra的變形, 核心觀念, 利用minheap 來pop出目前最好的選擇並relaxation該點附近的值,把這些點放入minheap裡, 
#持續從minheap挑出最好的選擇, 直到pop出的點是(n-1, m-1), 代表路徑已形成, 此時return -val 就是代表該路徑的最小值
#四方relaxation 為什麼要避開seen的, 第一是避免遍歷parent, 第二是避免連上已知minimum比自己還小的路徑末端, 第三是避免連上無法到達終點的路徑末端
#用這個方式可以保證連到(n-1, m-1) 的路徑 minimum一定是所有可能最大的
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(A), len(A[0])
        
        maxHeap = [(-A[0][0], 0, 0)] #(0,0) 當作source, 
        seen = [[0 for _ in range(C)] for _ in range(R)]
        seen[0][0] = 1
        while maxHeap:
            val, x, y = heapq.heappop(maxHeap) #優先pop出目前值最小 => 其實是minimum最大的路徑末端
            # seen[x][y] = 1 # got TLE
            if x == R - 1 and y == C - 1: 
                return -val
            for dx, dy in dire: #四方擴散=> 相似relaxation
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny]:
                    seen[nx][ny] = 1 # passed
                    heapq.heappush(maxHeap, (max(val, -A[nx][ny]), nx, ny)) #max(val, -A[nx][ny], 紀錄該路徑上最小值


#自己重寫, time complexity O(mnlog(mn))
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        seen[0][0] = 1
        max_heap = [(-A[0][0], 0, 0)]
        while max_heap:
            value, x, y = heapq.heappop(max_heap)
            if (x, y) == (len(A) -1, len(A[0]) -1):
                return -value
            for d in direc:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and not seen[nx][ny]:
                    seen[nx][ny] = 1
                    heapq.heappush(max_heap, (max(value, -A[nx][ny]), nx, ny))



# Union Find:
# Idea is similar to LC788 Swim in Rising Water or percolation.

# We want to find a path from (0,0) to (n-1, m-1) w/ max lower bound. So we just visit the cell in the order from largest to smallest, 
# and use UF to connect all the visited cells. Once we make (0,0) and (n-1, m-1) connected, we know we get a path with max lower bound, 
# which is just the value of the last visited cell.

# sort all the points in a descending order
# union the point with the explored points until start and end has the same parent
# Time: O(MN log MN)
# Space: O(MN)

#union-find time complexity O(MN log MN) => sort
#思路: 首先先對每個點依照matrix value 大到小排序, 之後依照排序遍歷, 遍歷到該點時向四方union, 注意只能union seen的, 因為代表該點比你大
#union 後, 大值點的parent 變成小值, 四方union 後, 查看(0,0) and (n-1, m-1) 是否在同一個component, 若是則return 目前該點的值, 
#因為按照順序是component裡最小的值

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        parent = [i for i in range(R * C)] #初始每個點都是自己的parent
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = [[0 for _ in range(C)] for _ in range(R)] #紀錄visited
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
        
        points = [(x, y) for x in range(R) for y in range(C)] #技巧!!
        points.sort(key = lambda x: A[x[0]][x[1]], reverse = True) # sort all the points by matrix value in a descending order
        
        for x, y in points: #依大到小遍歷
            seen[x][y] = 1
            for dx, dy in dire: #往四個方向union
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and seen[nx][ny]:
                    union(x * C + y, nx * C + ny) #技巧 2D 壓縮成1D
            if find(0) == find(R * C - 1): #查看是否(0,0) and (n-1, m-1) connected
                return A[x][y] #最小值
        
#自己重寫 time complexity O(mnlog mn) 1960ms
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])
        parents = [i for i in range(r*c)]
        visited = [[0 for _ in range(c)] for _ in range(r)]
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        
        points = [(x,y) for x in range(r) for y in range(c)]
        points.sort(key= lambda x: A[x[0]][x[1]], reverse=True)
        
        for x, y in points:
            visited[x][y] = 1
            for d in direc:
                nx, ny = x+d[0], y+d[1]
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny]:
                    self.union(x*c+y, nx*c+ny, parents)
            if self.find(0, parents) == self.find(r*c-1, parents):
                return A[x][y]
                
    
    def find(self, x, parents):
        if parents[x] != x:
            parents[x] =  self.find(parents[x], parents)
        return parents[x]

    
    def union(self, x, y, parents):
        rx, ry = self.find(x, parents), self.find(y, parents)
        if rx != ry:
            parents[ry] = rx


# find 不能寫成這樣, 會tle => 沒有path compression
def find(self, x, parents):
        if parents[x] != x:
            return self.find(parents[x], parents)
        return x









        





















