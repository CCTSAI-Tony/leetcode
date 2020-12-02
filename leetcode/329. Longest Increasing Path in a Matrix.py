'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''



#自己重寫 time complexity O(m*n) space complexity O(m*n)
#思路: 此題是memo + dfs (top down dp), 因為有許多重複分支(子問題), 所以利用memo紀錄子問題結果 來降低複雜度
#利用dfs來找尋四周比自己大的元素 並從四條路中挑一個最大的值+1 就是最長increasing path, base case是四周都比自己小 return 1
#注意邊界狀況, 因為是top down dp, 所以不會像backtracking 有return None or retuen 單純回上一層再試其他選擇的狀況, dp 就是要一次評估所有子問題來挑選最好結果
#此題dfs不用visited, 因為 vertex.val > parent_vertex.val 才能往下走, 不會互為可通造成死迴圈
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp = self.dfs(i, j, matrix, dp, m, n)
                max_len = max(max_len, temp)
        return max_len
    
    def dfs(self, i, j, matrix, dp, m, n):
        value = matrix[i][j]
        if not dp[i][j]:
            dp[i][j] = 1 + max(
            self.dfs(i+1,j,matrix,dp,m,n) if i+1 < m and value < matrix[i+1][j] else 0,
            self.dfs(i-1,j,matrix,dp,m,n) if i-1 >= 0 and value < matrix[i-1][j] else 0,
            self.dfs(i,j+1,matrix,dp,m,n) if j+1 < n and value < matrix[i][j+1] else 0,
            self.dfs(i,j-1,matrix,dp,m,n) if j-1 >= 0 and value < matrix[i][j-1] else 0
            )
        return dp[i][j]


#重寫第二次, time complexity O(m*n), space complexity O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        cache = {}
        max_len = 0
        for i in range(m):
            for j in range(n):
                path_len = self.helper(i, j, matrix, cache, m, n)
                max_len = max(max_len, path_len)
        return max_len
    
    def helper(self, i, j, matrix, cache, m, n):
        if (i, j) in cache:
            return cache[(i, j)]
        val = matrix[i][j]
        length = 1 + max(
            self.helper(i+1, j, matrix, cache, m, n) if i+1 < m and val < matrix[i+1][j] else 0,
            self.helper(i-1, j, matrix, cache, m, n) if i-1 >= 0 and val < matrix[i-1][j] else 0,
            self.helper(i, j+1, matrix, cache, m, n) if j+1 < n and val < matrix[i][j+1] else 0,
            self.helper(i, j-1, matrix, cache, m, n) if j-1 >= 0 and val < matrix[i][j-1] else 0,
            )
        
        cache[(i, j)] = length
        return cache[(i, j)]


#重寫第三次, time complexity O(mn), space complexity O(mn)
from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        memo = defaultdict(lambda: 1)
        m, n = len(matrix), len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, matrix, memo, visited)
        return max(memo.values())
                
    def dfs(self, i, j, matrix, memo, visited):
        m, n = len(matrix), len(matrix[0])
        if (i, j) in memo:
            return memo[(i, j)]
        direc = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        visited.add((i, j))
        for d in direc:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and matrix[x][y] > matrix[i][j]:
                memo[(i, j)] = max(memo[(i, j)], self.dfs(x, y, matrix, memo, visited) + 1)
        visited.remove((i, j))
        return memo[(i, j)]


# We can find longest decreasing path instead, the result will be the same. Use dp to record previous results and choose the max dp value of smaller neighbors.

# memoization dp top-down 經典, dps + dp 特殊題型
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]: 
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(self.dfs(x, y, matrix, dp) for x in range(M) for y in range(N))

    def dfs(self, i, j, matrix, dp):
        M, N = len(matrix), len(matrix[0])
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(  #上下左右選最大的, if i, 是確保i-1 不會<0
                self.dfs(i - 1, j, matrix, dp) if i and val > matrix[i - 1][j] else 0,  #上
                self.dfs(i + 1, j, matrix, dp) if i < M - 1 and val > matrix[i + 1][j] else 0,  #下
                self.dfs(i, j - 1, matrix, dp) if j and val > matrix[i][j - 1] else 0,  #左
                self.dfs(i, j + 1, matrix, dp) if j < N - 1 and val > matrix[i][j + 1] else 0)  #右
        return dp[i][j]



# [(i,j) for i in range(3) for j in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#就如同
for i in range(3):
    for j in range(3):



# [(i,j) for j in range(3) for i in range(3)]
# [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]


# 超有趣的
# bfs topological sorting on a directed graph
class Solution:
    def longestIncreasingPath(self, matrix):
  # Step 1: build a directed acyclic graph
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for x, y in neighbors:
                  if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[i][j] < matrix[x][y]:  #local 最大值 indegree = 0
                      graph[(i,j)].append((x,y))
                      indegree[(x,y)]+=1

    # Step 2: Topological sorting with Kahn's algorithm
        queue = collections.deque([(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if (i,j) not in indegree])
        max_path_len = 0
        while queue:
            max_path_len += 1
            for _ in range(len(queue)):
                  node = queue.popleft()
                  for neigh in graph[node]:
                      indegree[neigh] -= 1
                      if not indegree[neigh]:
                          queue.append(neigh)
        return max_path_len










