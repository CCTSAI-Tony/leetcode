'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, 
left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''

#參考別人, 刷題用這個, time complexity O((mn)^2), space complexity O(mn)
#思路: 利用房子1 當作bfs擴散點, 遍歷到每個0代表該房子能到達該空地, 並對該空地加上該房子到達此空地的最短距離, 最後再從這些空地中選出能到達每個房子的 最短distance
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reach = [[0] * n for _ in range(m)]
        distance = [[0] * n for _ in range(m)]
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    self.bfs(i, j, grid, reach, distance)
        min_path = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildings:
                    min_path = min(min_path, distance[i][j])
        return min_path if min_path != float("inf") else -1
                    
                    
    def bfs(self, i, j, grid, reach, distance):
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j, 0)])
        visited = set()
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y, d = queue.popleft()
            for direc in direcs:
                nx, ny = x + direc[0], y + direc[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    reach[nx][ny] += 1
                    distance[nx][ny] += d + 1
                    visited.add((nx, ny))
                    queue.append((nx, ny, d + 1))


#重寫第二次, time complexity O((mn)^2), space complexity O(mn)
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reaches = [[0] * n for _ in range(m)]
        distances = [[0] * n for _ in range(m)]
        buildings = 0
        min_distance = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    self.bfs(i, j, grid, reaches, distances, m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reaches[i][j] == buildings:
                    min_distance = min(min_distance, distances[i][j])
        return min_distance if min_distance != float(inf) else -1
                    
    def bfs(self, i, j, grid, reaches, distances, m, n):
        visited = set([(i, j)])
        queue = deque([(i, j)])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        d = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for direc in direcs:
                    nx, ny = x + direc[0], y + direc[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        reaches[nx][ny] += 1
                        distances[nx][ny] += d
                        queue.append((nx, ny))
            d += 1
