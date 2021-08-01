'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
'''

# Thought process
# backtracking

# 4 subroutine calls
# backtrack(i, j+1) + backtrack(i, j-1) + backtrack(i+1, j) + backtrack(i-1, j)
# need to be aware of the current state (grid)
# base cases
# i < 0 or i == m or j < 0 or j == n or grid[i][j] == -1: return 0
# grid[i][j] == 2: return 1 if all other non-empty cells are visited (by checking the remaining count), otherwise return 0
# grid[i][j] == 0: mask current cell to be -1, return sum of 4 subroutine calls (remember to reset the state each subroutine calls)
# cannot use DP for cache because of the dynamic state? 作者也不清楚, 不過我覺得難度很大, 此題用backtracting 比較直覺

#time complexity O(3 ^ n), where n is the total number of cells without obstacles, Memory: O(n) for the DFS stack.
#思路: back tracking, 先計算初始有幾個empty square 為 non_empty_count 包含起點1 與終點 2
#找到起點1 的位置, 開始往四方dfs 遍歷, 若到達終點2 則看是否non_empty_count 只剩1(終點) 若是 rerturn True => 1 , 若不是 return False => 0
#每經過一個empty cell 就mark -1 防止重複遍歷, 若從該cell出發的四個路徑都遍歷完了, 則回到上層之前 要把該cell mark回 0, 這樣能讓上層其他路徑能經過該cell
#若遍歷的 cell out of bound or -1, return 0
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        non_obstacle_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    non_obstacle_count += 1 #包含起點與終點
                if grid[i][j] == 1:
                    start_i, start_j = i, j
    
        return self.backtrack(start_i, start_j, non_obstacle_count, grid)

    def backtrack(self, i, j, remain, grid):
        m, n = len(grid), len(grid[0])
        if i < 0 or i == m or j < 0 or j == n or grid[i][j] == -1:
            return 0
        if grid[i][j] == 2:
            return remain == 1 #只剩終點的square => True = 1
        res = 0
        grid[i][j] = -1 #mark -1, 防止重複遍歷
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            res += self.backtrack(x, y, remain-1, grid)
        grid[i][j] = 0 #backtracking 復歸原狀
        return res


#自己重寫 time complexity O(3 ^ n)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        safe_cell = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    safe_cell += 1
                if grid[i][j] == 1:
                    str_i, str_j = i, j
        return self.dfs(str_i, str_j, grid, safe_cell)
    
    def dfs(self, i, j, grid, safe_cell):
        m, n = len(grid), len(grid[0])
        res = 0
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
            return 0
        if grid[i][j] == 2:
            return safe_cell == 1
        grid[i][j] = -1
        for d1, d2 in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            x, y = i + d1, j + d2
            res += self.dfs(x, y, grid, safe_cell - 1)
        grid[i][j] = 0
        return res

# 重寫第二次, time complexity O(3 ^ n), space complexity O(h)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        remain = 0
        start_i, start_j = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    remain += 1
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                    
        return self.dfs(grid, remain, start_i, start_j, m, n)
    
    def dfs(self, grid, remain, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and grid[i][j] != -1:
            original = grid[i][j]
            if original == 2:
                return remain == 1
            grid[i][j] = -1
            res = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                res += self.dfs(grid, remain - 1, x, y, m, n)
            grid[i][j] = original
            return res
        else:
            return False





