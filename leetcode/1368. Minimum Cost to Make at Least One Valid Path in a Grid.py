'''
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). 
A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. 
The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

 

Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. 
(0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 
change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
'''

'''
Instead of using Dijkstra, if there is no cost to visit neighbors, we add the neighbor to the front of the queue so that the front element always has the lowest cost.
'''


# 刷題用這個, time complexity O(nm), space complexity O(nm)
# 思路: 搭配Dijkstra 思想的 bfs, 最優解優先被找出來, 每個cell 都有四個方向的neighbor, 只有arrow 指向的cell, path cost = 0, 其餘都是1, cost =0 放回queue 前面
# 若不把cost = 0的選擇放在queue前面, 最後找到的路徑有可能不是最優解, 除非你使用priority queue(heap)
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                x, y, cost = queue.popleft()
                if (x, y) == (m-1, n-1):
                    return cost
                for i, direc in enumerate(directions):
                    nx, ny = x + direc[0], y + direc[1]
                    if 0 <= x < m and 0 <= y < n and (nx, ny) not in visited:
                        visited.add((x, y))
                        add_cost = 0 if grid[x][y] == (i + 1) else 1
                        nxt_cost = cost + add_cost
                        if add_cost == 0:
                            queue.appendleft((nx, ny, nxt_cost))
                        else:
                            queue.append((nx, ny, nxt_cost))
        return -1


# Dijkstra 解法, time complexity O(mnlog(mn)), space complexity O(mn)
# 技巧: 不僅使用visited 也使用seen 來排除 path cost比較大的選擇
from heapq import heappush, heappop
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        if M == 1 and N == 1:
            return 0
        
        pq = [(0, 0, 0)]
        seen = {}
        seen[(0, 0)] = 0
        
        visited = set()
        
        while pq:
            cost, i, j = heappop(pq)
            if (i, j) in visited:
                continue
                
            visited.add((i, j))
            if i == M - 1 and j == N - 1:
                return cost
            
            for new_x, new_y, d in [(i + 1, j, 3), (i - 1, j, 4), (i, j + 1, 1), (i, j - 1, 2)]:
                next_cost = cost if d == grid[i][j] else cost + 1
                
                if 0 <= new_x < M and 0 <= new_y < N and (new_x, new_y) and (new_x, new_y) not in visited and ((new_x, new_y) not in seen or seen[(new_x, new_y)] > next_cost):
                    heappush(pq, (next_cost, new_x, new_y))
                    seen[(new_x, new_y)] = next_cost
        
        return -1










