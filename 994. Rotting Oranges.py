'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

#自己想的, time complexity O(m*n), 52ms
#思路: 典型bfs 求最短時間, 距離等, 建立rotten 收集2 當作擴散源, 建立 origin_fresh 收集1 當作驗證是否有殘留的fresh orange
#每次擴散若有找到新鮮的orange 把它變成2 => 放進 rotten  => 進行下一輪 minutes += 1, 若沒有結束while loop 迴圈, check 是否有殘留fresh, 有則return -1
#若沒有殘留fresh, return minutes
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        origin_fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    origin_fresh.append((i, j))
        direcs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        minutes = 0
        while rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for d in direcs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            rotten.append((x,y))
            if rotten:  #還有新增加rotten orange, 新一輪擴散
                minutes += 1
                
        for i, j in origin_fresh:
            if grid[i][j] == 1:
                return -1
        return minutes


