'''
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
'''


# 刷題用這個, time complexity O(mn), space complexity O(mn)
# 思路: 建立2d dp, 每個cell 擴增為四個小cell 來紀錄橫,直, 斜線長度
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if len(mat) == 0:
            return 0
        
        dp = [[ [0, 0, 0, 0] for j in range(len(mat[0]))] for i in range(len(mat))]
        max_len = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    dp[row][col][0] = dp[row][col-1][0] + 1 if col > 0 else 1
                    dp[row][col][1] = dp[row-1][col][1] + 1 if row > 0 else 1
                    dp[row][col][2] = dp[row-1][col-1][2] + 1 if row > 0 and col > 0 else 1
                    dp[row][col][3] = dp[row-1][col+1][3] + 1 if row > 0 and col < len(mat[0])-1 else 1

                max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])
                
        return max_len

# 重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                    dp[i][j][3] = dp[i-1][j+1][3] +1 if i > 0 and j + 1 < n else 1
                    max_len = max(max_len, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return max_len





