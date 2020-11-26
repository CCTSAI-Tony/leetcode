'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. 
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

'''
#time complexity O(mnlog(mn)), space complexity O(mn)
#思路: Dijkstra Algorithm, dist + d < stopped[(newX, newY)] => I got it, it all depends on where you add the element into stopped.
#使用priority queue and hashtable 來實現 Dijkstra
import heapq
class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        visited = set() ## first line
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            if (x, y) in visited: #這裡是關鍵, 代表接下來distance較大者都skip
                continue ## second line
            else: 
                visited.add((x, y)) ## third line
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1


#重寫第二次, time complexity O(mnlog(mn)), space complexity O(mn)
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])]
        visited = set([(start[0]), start[1]])
        stopped = {(start[0], start[1]): 0}
        while queue:
            dist, x, y = heapq.heappop(queue)
            if (x, y) == (destination[0], destination[1]):
                return dist
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for i, j in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                d, nx, ny = 0, x, y
                while 0 <= nx + i < m and 0 <= ny + j < n and maze[nx+i][ny+j] != 1:
                    nx += i
                    ny += j
                    d += 1
                if (nx, ny) not in stopped or dist + d < stopped[(nx, ny)]:
                    stopped[(nx, ny)] = dist + d
                    heapq.heappush(queue, (dist + d, nx, ny))
        return -1























