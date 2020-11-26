'''
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. 
You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
'''

Heap O(N^2 log N)
#刷題用這個, time complexity O(N^2*logN), space compolexity O(N^2)
#思路: 利用heap 搭配 四方遍歷 來優先pop出 ele 較低的cell, 並依pop出來的cell 時時更新目前的t => 降水高度時間
#優先pop出的cell進行四方遍歷, 若途中遇到ele很高的cell先push至heap, 再從heap pop出較低的cell開發新路徑, 若pop出的cell 大於目前的降水高度=> 更新降水高度
#記得建立set 去重已經push過的cell
#注意: 題目有說 每個cell => grid[i][j] is a permutation of [0, ..., N*N - 1]. 也就是就算grid[0][0] = t, grid[-1][-1] < t, 至少也要等到時間t 才能游到目的地
import heapq
class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        seen = {(0, 0)}
        hp = [(grid[0][0], 0, 0)]
        ans = 0
        while hp:
            ele, r, c = heapq.heappop(hp)
            ans = max(ans, ele)
            if r == c == N-1:
                return ans
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_r, n_c = r + di[0], c + di[1]
                if 0 <= n_r < N and 0 <= n_c < N and (n_r, n_c) not in seen:
                    seen.add((n_r, n_c))
                    heapq.heappush(hp, (grid[n_r][n_c], n_r, n_c))

#自己重寫
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0,0)])
        t = 0
        while heap:
            ele, r, c = heapq.heappop(heap)
            t = max(t, ele)
            if (r, c) == (N-1, N-1):
                return t
            direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in direc:
                n_r, n_c = r + d[0], c + d[1]
                if 0 <= n_r < N and 0 <= n_c < N and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    heapq.heappush(heap, (grid[n_r][n_c], n_r, n_c))

Binary Search + DFS O(N^2 log N)
#思路: 模板2 binary search + dfs, 利用binary search 來查找最短時間到達end point
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        left, right = grid[0][0], N**2-1
        while left + 1 < right:
            mid = left + (right-left) // 2
            if self.check(mid, N, grid):
                right = mid
            else:
                left = mid
        if self.check(left, N, grid):
            return left
        return right
        
    def check(self, ele, N, grid):
        stack = [(0, 0)]
        seen = set([(0, 0)])
        while stack:
            r, c = stack.pop()
            seen.add((r, c))
            if (r, c) == (N-1, N-1):
                return True
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
            for d in direc:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen and grid[nr][nc] <= ele:
                    stack.append((nr, nc))
        return False


Union-find O(N^2 log N) 156ms

#自己重寫
#思路: 利用union find 來找尋特定時間, 使得cell[0][0] 與 cell[N-1][N-1] 在同一個unit 底下
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.N = len(grid)
        self.parents = list(range(self.N**2)) #初始, 每個都是自己的parent
        self.rank = [1]*(self.N**2) #初始rank, 每個cell 都是1
        locations = {grid[i][j]:(i, j) for i in range(self.N) for j in range(self.N)} #建立ele: location, key:value pair
        for ele in range(self.N**2): #從最低點 一步一步union 起來
            r, c = locations[ele]
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
            for d in direc:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < self.N and 0 <= nc < self.N and grid[nr][nc] <= ele:  #union 起來的component 代表此component 的cell 都可以任意到達
                    self.union(nr*self.N+nc, r*self.N+c) #可以合併比你低的component
                    if self.find(0) == self.find(self.N**2-1): #與終點同一個component => 可以到達end point
                        return ele
        
    def find(self, x): #path compression
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, a, b): #union by rank
        root_a, root_b = self.find(a), self.find(b)
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parents[root_b] = root_a
        self.rank[root_a] += self.rank[root_b]







