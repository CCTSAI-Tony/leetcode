# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 7 x 3 grid. How many possible unique paths are there?

 

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28
 

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.


#自己重寫, time complexity O(m*n), m,n 都是正數, 題目說的 40ms
#思路:  經典dp, 設邊界路徑為1, 內陸cell可到達路線 = 上方來的 + 左邊來的 (只允許往下與往右走)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


#重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

#重寫第三次, time complexity O(mn), space complexity O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += (dp[i-1][j] + dp[i][j-1])
        return dp[-1][-1]









class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 先開一個 m*n 的大表格，並讓邊界的預設值為 1（代表有一種走法）。
        dp = [[1] * m for _ in range(n)]
        for row in range(1, n): #range(1, m) = 邊界的預設值為 1, range從1開始 跳過0
            for col in range(1, m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[n-1][m-1] #finish點 n:raw m: column or dp[-1][-1]


        '''
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

			The robot can only move either down or right at any point in time. 
			The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

			How many possible unique paths are there?

			dp = [[1] * 4 for _ in range(5)]
            dp = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

            m x n matrix

            1 1 1 1 1 1 1 1 1 . . . . m columnn
            1 2 3 4 5     
            1 3 6
            1
            1
            1         x
            1       x o
            .
            .
            n row



            '''