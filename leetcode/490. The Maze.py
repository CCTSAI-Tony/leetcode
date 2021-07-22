'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''

# The Maze
# 定义:
# determine whether the ball could stop at the destination.

# 这里对于stop的判定条件是：球从一个方向朝着end卷过来，能否在end点的下一个位置碰到墙。举个不成立的例子

# 比如你从左边冲过来，到达了end，虽然end点的上下两头都有墙，但右边没有墙，这种就不符合定义。

# 思路
# 有了定义的条件，不难想象这是一道图的遍历。DFS和BFS都行。这里说一下BFS的思路。
# BFS前的基础设施
# 放入Queue的条件：当满足没有被访问过，且是一个新的起始点，我们放入Queue。新的起始点的定义是：从任意方向撞过来，并且触碰到墙后，触碰墙之前的最后一个节点。
# Visited数组设立一个和input matrix等长宽的二维boolean数组 
# 根据题目尿性的额外设施
# 方向数组，这个如果不写也行，只是要多写几个方向的判断。写的话，写成上下左右四个方向比较顺溜。
# BFS主代码
# 和一般的BFS没什么区别，先把最开始的起始点从Queue中pop出来，比对Termination Condition(是否和终结点坐标一致)。
# 不一致的话，就开始上下左右四个方向的滚动，每次滚动都滚到底，之后记住要回撤一部，因为while的终止条件使得最后球的坐标会在一面墙上。
# 然后对回撤完了的这个节点进行去重比较，没Visited过就放入queue中，成为之后上下左右滚动的起始点

# 代码
# Time: O(m * n): worst case visit the entire matrix
# Space: O(m * n): Visited Matrix

from collections import deque
class Solution(object):
    def hasPath(self, matrix, start, end):
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # up down left right
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        visited[start[0]][start[1]] = True

        q = deque([start])

        while q:
            tup = q.popleft()
            if tup[0] == end[0] and tup[1] == end[1]:
                return True

            for dir in dirs:
                # Roll the ball until it hits a wall
                row = tup[0] + dir[0]
                col = tup[1] + dir[1]

                while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 0: #一路滾到底
                    row += dir[0]
                    col += dir[1]

                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                (new_x, new_y) = (row - dir[0], col - dir[1])

                # Check if the new starting position has been visited
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return False


# 重寫第二次, time complexity O(mn), space complexity O(mn)
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        start, destination = tuple(start), tuple(destination)
        visited = set([start])
        queue = deque([start])
        direcs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == destination:
                    return True
                for d in direcs:
                    nx, ny = x + d[0], y + d[1]
                    while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                        nx, ny = nx + d[0], ny + d[1]
                    nx, ny = nx - d[0], ny - d[1]
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return False



#自己重寫dfs, time complexity O(m*n), space complexity O(m*n), 刷題用這個, 280ms
#思路: 跟bfs一樣
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set([(start[0], start[1])])
        i, j = start
        return self.dfs(i, j, maze, destination, visited)
        
    def dfs(self, i, j, maze, destination, visited):
        m, n = len(maze), len(maze[0])
        if (i, j) == (destination[0], destination[1]):
            return True
        visited.add((i, j))
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in direc:
            x, y = i + d[0], j + d[1]
            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                x, y = x+d[0], y+d[1]
            x, y = x-d[0], y-d[1]
            if (x, y) in visited:
                continue
            if self.dfs(x, y, maze, destination, visited):
                return True
        return False


























