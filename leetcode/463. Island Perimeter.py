'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


'''
#  自己想的 time complexity O(m*n), space complexity O(1)
#  思路: matrix 遍歷每個cell, 若該cell == 1, 則check 上下左右是否也是1, 若是則每連接一個１, 周長就要減1
#  記得注意邊界狀況
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.perimeter = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.check(i, j, grid)
        return self.perimeter
      
    def check(self, i, j, grid):
        self.perimeter += 4
        if i - 1 >= 0 and grid[i-1][j] == 1:
            self.perimeter -= 1
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self.perimeter -= 1
        if j - 1 >= 0 and grid[i][j-1] == 1:
            self.perimeter -= 1
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self.perimeter -= 1


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s, m = len(grid), len(grid[0])
        ans = 0
        for x in range(s):
            for y in range(m):
                if grid[x][y] == 1:
                    ans += 4
                    if x < s - 1 and grid[x+1][y] == 1:  #同時減少與對方我方的一邊
                        ans -= 2
                    if y < m - 1 and grid[x][y+1] == 1:
                        ans -= 2
                        
        return ans

