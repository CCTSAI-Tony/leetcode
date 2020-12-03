'''
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''

#自己想的, time complexity O((mn)^2), space complexity O(mn)
#思路: backtracking, 此題比較不一樣, 因為每個path的起點都有可能引導至不同的答案, 因此若一條path 經過該cell, 該cell 依然可以當作新的起點, 只是該path 要做去重的動作
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    gold = self.dfs(i, j, grid, set())
                    max_gold = max(max_gold, gold)
        return max_gold
    
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        visited.add((i, j))
        direc = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        nxt_gold = 0
        for d in direc:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in visited:
                nxt_gold = max(nxt_gold, self.dfs(x, y, grid, visited))
        visited.remove((i, j))
        return grid[i][j] + nxt_gold