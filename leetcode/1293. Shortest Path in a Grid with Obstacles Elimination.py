'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

# 刷題用這個, time complexity O(mnk), space complexity O(mnk), m = rows, n = columns, k = allowed elimination usages
# 思路: bfs, 加入k_remain 來當作新的特徵, 同時代表同一個cell最多能重複經過k次
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, k)])
        direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set([(0, 0, k)])
        if k > (m-1+n-1):  # 優化
            return (m-1+n-1)
        while queue:
            for _ in range(len(queue)):
                i, j, steps, k_remain = queue.popleft()
                if (i, j) == (m-1, n-1):
                    return steps
                for d in direcs:
                    x, y = i + d[0], j + d[1]
                    new_k_remain = k_remain
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1:
                            new_k_remain -= 1
                            if new_k_remain < 0:
                                continue
                        if (x, y, new_k_remain) not in visited:
                            visited.add((x, y, new_k_remain))
                            queue.append((x, y, steps + 1, new_k_remain))
        return -1


