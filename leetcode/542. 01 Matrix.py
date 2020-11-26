'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

#自己想的 TLE TIME COMPLEXITY O(mn*mn)

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        distance = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    distance[i][j] = self.dfs(i,j,matrix,[], 0)
        return distance
    
    def dfs(self, i, j, matrix, visited, dis):
        if matrix[i][j] == 0:
            return dis
        if (i, j) in visited:
            return float("inf")
        
        min_dis = float("inf")
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]): 
                temp = self.dfs(x, y, matrix, visited+[(i,j)], dis + 1)
                min_dis = min(min_dis, temp)
        return min_dis





# 刷題用這個
# Approach -1-
# Naive BFS invoked multiple times (Slow)
# Idea

# Iterate over the matrix with a nested for-loop to find cells conatining 1
# Apply BFS algo on those cells -> pass those cells to a BFS helper to find distance to closest 0
# update the matrix cell with the distance

#bfs 972ms time complexity O(mn*mn)
# 思路: 遇到最短距離, 請用bfs, bfs精髓 用deque, popleft()
# 利用matrix 遍歷 1, 並以1當作bfs起點, 找出相鄰0的最短距離
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    d = self.bfs(i,j, matrix) # d = closest dist to a 0
                    matrix[i][j] = d # update M with d
        return matrix

    # BFS helper #
    def bfs(self, i, j, matrix):
        q = deque()
        q.append(((i,j), 0)) # d (dist to a zero) = 0 initially 
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            for i in range(len(q)): #此時len(q) 為同一層(同distance) cell, 這行是 bfs模板標配, 但這題可有可無, 因為append的時候就清楚標明 distance
                coor, d = q.popleft() #bfs
                x, y = coor
                # if a zero nei is found
                if matrix[x][y] == 0: #bfs 最短距離
                    return d
                visited.add(coor)
                # investiagte neighbours
                for dir in dirs:
                    newX, newY = x+dir[0], y+dir[1]
                    # within bounds:
                    if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]):
                        # not seen:
                        if (newX, newY) not in visited:
                            q.append(((newX, newY), d+1))
        return False

# main logic #
        '''
        steps:
            - itertate over matrix to find cells = 1
            - pass cells equaling 1 to a bfs to find the closest 0 to them
            - update matrix
        '''
#自己重寫
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return None
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    self.bfs(i,j,matrix)
        return matrix
    
    def bfs(self, i, j, matrix):
        matrix[i][j] = 100
        visited = set()
        queue = deque([(i,j)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        d = -1  #為了使初始為0
        while queue:
            d += 1   #初始 -1 + 1 = 0
            for _ in range(len(queue)):  #bfs模板標配, 代表一個level, 下一個levewl, 下下....
                x, y = queue.popleft()
                if matrix[x][y] == 0:
                    matrix[i][j] = d
                    return
                visited.add((x,y))
                for k in directions:
                    new_x, new_y = x + k[0], y + k[1]
                    if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and (new_x,new_y) not in visited:
                        queue.append((new_x, new_y))







# Optimized BFS invoked only once (Fast)
# Idea

# Instead of invoking BFS for each land cell to see how far we can get away from that source, we flip the problem.
# The flipped problem is to start from target (sea, 0) and to figure our the closest source (land, 1)
# This allows us to run a single BFS search that emerges from different places (all the targets aka all the zero cells) in the grid
# Add all the targets (all zero cells) into the queue. While you're at it, also mark those targets as visited (add to a visited set)
# Run a single BFS on the pre-processed queue and investigate neighbours.
# if neighbiour cell has not been visited --> then it must be land cell (since all the sea cells have been marked visited):
# append the neighbour cell into the queue and mutate the gird
# Code

# 思路: 相反解法, 一開始先收集所有0當作原始bfs起點, 這些0 bfs四個方向碰到的1會被mark visited, 且會給予0+1的距離, 之後0沒了
# 換成1 當作bfs起點, bfs四個方向碰到的1會被mark visited, 且會給予1+1的距離, 被修改的數字都是最短的, 因為bfs
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        visited = set() #以後visited都要用set, 若用list, 之後要查是否元素在這裡面花費較大
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]) and (newX, newY) not in visited:
                        matrix[newX][newY] = matrix[x][y] + 1 #依目前的擴散點四個方向內碰到, 所以依擴散點的數字+1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return matrix
    

Set in Python can be defined as the collection of items. In Python, these are basically used to include membership testing and eliminating duplicate entries. 
The data structure used in this is Hashing, a popular technique to perform insertion, deletion and traversal in O(1) on average. 
The operations on Hash Table are some what similar to Linked List. Sets in python are unordered list with duplicate elements removed.



