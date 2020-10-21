'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
# 刷題用這個, time complexity O(m*n), 這題也是undirected grapgh 的題型
# 思路: Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, 表示以遍歷
# then increase the counter by 1, 每個count 都代表一個connected component(undirected graph)
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)  #擴散
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#' #遍歷到的都修改成'#' 以表示visited, 這邊吃過虧, 寫成grid[i][j] == '#' => maximum recursion depth exceeded in comparison, 無限循環
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)





#Python Union Find solution, with both path compression and union by rank, time complexity O(m*n), space complexity O(m*n)
#思路: 經典union find 題
class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n) #build [-1,-1,-1........]
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': #注意這個'1' 是 str
                    self.parent[i*n + j] = i*n + j #make set, 自己成為parent
                    self.count += 1

    def find(self, i): #path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y): #union by rank
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else: #same rank
                self.parent[rooty] = rootx #force one to be the other's parent
                self.rank[rootx] += 1
            self.count -= 1 #cause merge


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: #two case [] for not grid, [[]] for not grid[0] ,bool([])->False, bool([0])->True, bool(0) = False, bool([[]]) = True
            return 0

        uf = UnionFind(grid) #class object

        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in directions:
                        nr, nc = i + d[0], j + d[1]
                        if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1': #上下左右有1
                            uf.union(i*n+j, nr*n+nc) #i*n+j 尋找自己的parent, nr*n+nc 尋找周圍的parentdfis rs
        return uf.count

    def is_valid(self, grid, r, c): #row,column don't go over border
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

'''
Input:
11110
11010
11000
00000
'''



#自己重寫
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1
        return count
    
    def dfs(self, i, j, grid):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "#" 
            self.dfs(i+1, j, grid)
            self.dfs(i-1, j, grid)
            self.dfs(i, j+1, grid)
            self.dfs(i, j-1, grid)






