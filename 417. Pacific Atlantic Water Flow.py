'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''


#自己想的 TLE TIME COMPLEXITY O(MN*MN)
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):
                if self.dfsp(i,j,matrix,[]) and self.dfsa(i,j,matrix,[]):
                    res.append((i,j))
        return res
    
    def dfsp(self, i, j, matrix, visited):
        if i == 0 or j == 0:
            return True
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in direc:
            if 0 <= i + d[0] < len(matrix) and 0 <= j + d[1] < len(matrix[0]) and (i + d[0], j + d[1]) not in visited:
                if matrix[i][j] >= matrix[i + d[0]][j + d[1]]:
                    if self.dfsp(i + d[0], j + d[1], matrix, visited + [(i, j)]):
                        return True
    
    def dfsa(self, i, j, matrix, visited):
        if i == len(matrix)-1 or j == len(matrix[0])-1:
            return True
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in direc:
            if 0 <= i + d[0] < len(matrix) and 0 <= j + d[1] < len(matrix[0]) and (i + d[0], j + d[1]) not in visited:
                if matrix[i][j] >= matrix[i + d[0]][j + d[1]]:
                    if self.dfsa(i + d[0], j + d[1], matrix, visited + [(i, j)]):
                        return True



# The DFS solution is straightforward. Starting from each point, and dfs its neighbor if the neighbor is equal or bigger than itself. 
# And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. 
# Finally go through all nodes again and see if it can be both reached by two oceans. The trick is if a node is already visited, 
# no need to visited again. Otherwise it will reach the recursion limits.

# This question is very similar to https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ And here are some common tips for this kind of question

# init a directions var like self.directions = [(1,0),(-1,0),(0,1),(0,-1)] so that when you want to explore from a node, you can just do
# for direction in self.directions:
#             x, y = i + direction[0], j + direction[1]
# this is a what I normally do for a dfs helper method for exploring a matrix

def dfs(self, i, j, matrix, visited, m, n):
  if visited: 
    # return or return a value
  for dir in self.directions:
    x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j] (or a condition you want to skip this round):
           continue
        # do something like
        visited[i][j] = True
        # explore the next level like
        self.dfs(x, y, matrix, visited, m, n)
Hope it helps
 
#  刷題用這個!
#  you are doing DFS from the present cell to the neighbours from which it can receive the water.
#  time complexity O(mn), space complexity O(mn)
#  思路: 利用pacific and atlantic 接觸位置當作擴散點, 往內陸探勘, 只擴散比自己大與相等的, 擴散到的元素 登記在分別的visited list裡, 以避免重複遍歷
#  最後比較兩個visited list, 若座標在兩個visited list都有出現, 代表這個座標的水可以流入這兩個海洋
#  此題的核心是利用不同擴散點來建立從海岸到內陸的遞增序列, 兩個海洋不同方向的遞增序列交會處就是我們要的點
#  可以想像成不同出海口往上游遍歷, 遇到鄰居visited = True的 代表該點已有路徑到出海口, 所以不需重複遍歷
class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]: 
            return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]  #不能in place modify matrix[i][j] 表示visited, 所以才要額外建visited table
        
        a_visited = [[False] * n for _ in range(m)]
        result = []
        
        for i in range(m):  #左右
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n):  #上下
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point 
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)




#自己重寫
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False]*n for _ in range(m)]
        a_visited = [[False]*n for _ in range(m)]
        res = []
        
        for i in range(m):
            self.dfs(i,0,matrix,p_visited,m,n)
            self.dfs(i,n-1,matrix,a_visited,m,n)
        for j in range(n):
            self.dfs(0,j,matrix,p_visited,m,n)
            self.dfs(m-1,j,matrix,a_visited,m,n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append((i,j))
        return res
    
    
    
    def dfs(self,i,j,matrix,visited,m,n):
        visited[i][j] = True
        for d in self.directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and matrix[i][j] <= matrix[x][y]:
                self.dfs(x,y,matrix,visited,m,n)



 


# bfs 參考別人, 自己重寫
# Python solution using bfs and sets.
# time complexity O(mn), space complexity O(mn)
# 思路: 同樣思路使用bfs, 與dfs不一樣的是這些reachable place離出海口都是最近的路徑, 使用bfs一定會用到stack概念
from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = set([(0,j) for j in range(n)] + [(i,0) for i in range(m)])  #list comprehension
        atlantic = set([(m-1,j) for j in range(n)] + [(i,n-1) for i in range(m)])
        return list(self.bfs(pacific, matrix) & self.bfs(atlantic, matrix))
        
    
    def bfs(self, reach_ocean, matrix):
        queue = deque(reach_ocean) #初始出海口
        m, n = len(matrix), len(matrix[0])
        direcs = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                (x, y) = queue.popleft()
                for d in direcs:
                    new_x, new_y = x + d[0], y + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] \
                    >= matrix[x][y] and (new_x, new_y) not in reach_ocean:
                        queue.append((new_x, new_y))
                        reach_ocean.add((new_x, new_y))
        return reach_ocean

set 交集!!
{1,2,300} & {2,300,6}
{2, 300}



















