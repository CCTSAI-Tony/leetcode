'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

#刷題用這個, time complexity O(m*n)
#思路: 遇到障礙cell, dp[i][j] = 0, 除非在邊界無法取得外 cell 可以從上or左取得信息, 這樣一來, 第一排or第一列也可以藉由擴散取得初始值
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return None
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))] #creat matrix 初始值都為0
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0 #定義起始位置！

        for i in range(len(obstacleGrid)): #row
            for j in range(len(obstacleGrid[0])): #column
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1>=0: #跳過邊界條件
                        dp[i][j] += dp[i-1][j]
                    if j-1>=0: #跳過邊界條件
                         dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

#重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]





#自己想的, time complexity O(m*n)
#思路: 有障礙的cell 設成-1, 之後計算dp[i][j]時跳過, 第一排與第一列, 障礙前都是1 障礙後都是0, 最後return 若dp[-1][-1] = -1 要回報0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1 
        for i in range(m):
            if dp[i][0] == -1:
                break
            dp[i][0] = 1
        for j in range(n):
            if dp[0][j] == -1:
                break
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] == -1:
                    continue
                up = dp[i-1][j] if dp[i-1][j] >= 0 else 0
                left = dp[i][j-1] if dp[i][j-1] >= 0 else 0
                dp[i][j] = up + left
        return dp[-1][-1] if dp[-1][-1] >= 0 else 0





        '''
        DP[0][0] = 0, if s[0][0] = 1
        DP[0][0] = 1, if s[0][0] = 0
        

        DP[i][j] = {0, if s[0][0] = 1;
                   or  DP[i-1][j] + DP[i][j-1], if s[i][j] = 0;
	
        }

        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

		The robot can only move either down or right at any point in time. 
		The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

		Now consider if some obstacles are added to the grids. How many unique paths would there be?

		Example 1:

		Input:
		[
		  [0,0,0],
		  [0,1,0],
		  [0,0,0]
		]
		Output: 2
		Explanation:
		There is one obstacle in the middle of the 3x3 grid above.
		There are two ways to reach the bottom-right corner:
		1. Right -> Right -> Down -> Down
		2. Down -> Down -> Right -> Right

        '''