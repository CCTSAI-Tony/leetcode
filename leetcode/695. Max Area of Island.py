'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

#刷題用這個, time complexity O(mn), space complexity O(1)
#思路: dfs 直接回傳值, and inplace modified 防止重複遍歷
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i, j, grid))
        return max_area
    
    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        grid[i][j] = -1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        area = 0
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                area += self.dfs(x, y, grid)
        return area + 1

#重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, self.dfs(i, j, grid, visited))
        return maxArea
                    
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        visited.add((i, j))
        direc = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        area = 1
        for d in direc:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                area += self.dfs(x, y, grid, visited)
        return area


#  自己想的 dfs, time complexity O(m*n) 212ms
#  思路: 典型dfs, 利用in-placed modify 來避免重複遍歷, 此題利用defaultdict(int)來紀錄島面積, 
#  記得傳参不能直接傳areas[(i,j)] 因為是int 不能修改 non mutable, 而是要連dict一起傳
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        areas = defaultdict(int)
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, areas, (i, j))
        return max(areas.values()) if areas else 0
    
    def dfs(self, i, j, grid, areas, start):
        m, n = len(grid), len(grid[0])
        areas[start] += 1
        grid[i][j] = -1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(x, y, grid, areas, start)



