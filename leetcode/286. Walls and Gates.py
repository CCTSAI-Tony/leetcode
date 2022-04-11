'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  '''


#刷題用這個, time complexity O(m*n), space complexity O(m*n)
#思路: 典型bfs, 先找到所有gate位置, 再以這些位置進行bfs擴散, 這樣每個empty room 到達 gate 的距離都是最短的
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return None
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        k = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d in direc:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31-1:
                        rooms[x][y] = k
                        queue.append((x, y))
            k += 1




#重寫第二次, time complexity O(mn), space complexity O(mn)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return None
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        direcs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dis = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d in direcs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31 - 1:
                        rooms[x][y] = dis
                        queue.append((x, y))
            dis += 1


# 重寫第三次, time complexity O(mn), space complexity O(mn)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        dircs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            for _ in range(len(queue)):
                i, j, dist = queue.popleft()
                for d in dircs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31 - 1:
                        rooms[x][y] = dist + 1
                        queue.append((x, y, dist + 1))












