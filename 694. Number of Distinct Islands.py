'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated 
(and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
'''

#這裡指的be translated to equal the other 是指移動island 看是否可以完美重疊(不能轉與翻)

110 => ordrbbbb
011
000
111 => ordbrbbb 
010

#time complexiy: O(m*n)
#思路: 利用遍歷的方向都是由左往右, 由上往下, 因此相似island 的起點都是一樣的, 之後依照dfs遍歷順序往右往左往上往下添加方向值, 當該cell四個方向遍歷完畢添加back
#利用set 來過濾重複特徵的圖形, 最後rerurn len(set) => distinct islands
#添加back很重要, 來區分相似圖形, 簡單來說只有完全一樣的圖像 => dfs遍歷得到的特徵值才會完全一樣!
#為了區分相似的圖形, 遍歷的過程特定點back的時機也要一樣=>才是一樣的圖形, 不然是不一樣的, 注意此back 與一般的backtrack 有些許不一樣, 
#這裡的back是指所有該節點能走的路經都遍歷完畢回上一個node, 然而backtrack是指所有的路徑還沒全部遍歷完畢就知道無法往下走而回到上一個node 來查看其他可能路徑
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.steps = ''
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.helper(grid, i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        return len(distinctIslands)
    
    def helper(self, grid, i, j, direct):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.steps += direct
            grid[i][j] = 0 #改成0 以免重複遍歷
            self.helper(grid, i+1, j, 'd')  # down
            self.helper(grid, i-1, j, 'u')  # upper
            self.helper(grid, i, j+1, 'r')  # right
            self.helper(grid, i, j-1, 'l')  # left
            self.steps += 'b'  # back


#自己重寫 time complexity O(m*n)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.distinct = set()
        self.steps = ""
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, "o")
                    self.distinct.add(self.steps)
                    self.steps = ""
        return len(self.distinct)
    
    def dfs(self, i, j, grid, step):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.steps += step
            grid[i][j] = 0
            self.dfs(i+1, j, grid, "d")
            self.dfs(i-1, j, grid, "t")
            self.dfs(i, j+1, grid, "r")
            self.dfs(i, j-1, grid, "l")
            self.steps += "b"




