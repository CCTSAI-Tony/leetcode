'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

#自己想的, time complexity O(mn), space complexity O(mn)
#思路: bfs
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        queue = deque([(0,0,1)])
        visited = set()
        direc = [(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]
        while queue:
            i, j, k = queue.popleft()
            if (i, j) == (m-1, n-1):
                return k
            for d in direc:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and not grid[x][y] and (x, y) not in visited:
                    queue.append((x, y, k+1))
                    visited.add((x, y))
        return -1




        