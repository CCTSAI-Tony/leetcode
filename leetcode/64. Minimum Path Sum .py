# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

#自己重寫, time complexity O(m*n)
#使用dp bottom up 來解題, 建立邊界值, dp 關係式: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        cost = [[0]*N for _ in range(M)] #creat a column
        cost[0][0] = grid[0][0]
        for j in range(1,N):
            cost[0][j] = grid[0][j] + cost[0][j-1] #建立邊界值
        for i in range(1,M):
            cost[i][0] = grid[i][0] + cost[i-1][0]
        for i in range(1,M):
            for j in range(1,N):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j] #從上 從左 取最小的那個 加本身
        return cost[M-1][N-1]


# 重寫第二次, time complexity O(mn), space complexity O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        '''
Dynamic Programming: O(MN) space

Start Point: 0, 0. Destination Point: M-1, N-1
Cost[i,j]: The cost to reach (i,j) from (0,0). We initialize
The solution will be cost(M-1,N-1)
Time & Space Complexity:O(MN)

        '''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        cost = [float('inf')]*N #先取最大值 已利最小值替換
        for i in range(M):
            cost[0] = grid[i][0] + cost[0] if i > 0 else grid[i][0] #建立邊界
            for j in range(1,N):
                cost[j] = min(cost[j-1], cost[j]) + grid[i][j] #解讀為 min(左邊來,從上來) 取最小額外加 grid[i][j]
        return cost[-1]

'''
Dynamic Programming: Using O(N) space

Space complexity can be reduced to O(N) since we only require the previous row to compute the current row.
Note that we initialize the cost array to inf. Note how we initialize cost[0] at every row iteration.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

cost = ['inf','inf,'inf']> [1,4,5]>[2,7,6]>[6,8,7]


'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        for i in range(M):
            grid[i][0] = grid[i][0] + grid[i-1][0] if i > 0 else grid[i][0] #建立縱軸邊界
            for j in range(1,N):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] if i > 0 else grid[i][j-1]+grid[i][j] #else 這邊建立橫軸邊間
        return grid[-1][-1]

'''
這個最好！
Dynamic Programming: Using O(1) space 直接修改map的值

Space complexity can be reduced to O(1) as grid can be reused as cost matrix
Notice how we iterate the two loops and the special condition we use for i=0










'''
# top down
class Solution(object):
    def helper(self, x, y, grid, cost):
        M, N = len(grid), len(grid[0])
        if x == M or y == N:
            return float('inf') #超過邊界處理
        elif cost[x][y] != -1:
            return cost[x][y]
        else:
            right, down = self.helper(x,y+1,grid,cost), self.helper(x+1,y,grid,cost) #solution of subproblems
            cost[x][y] = min(right, down) + grid[x][y]
        return cost[x][y]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        cost = [[-1]*N for _ in range(M)] #建立cost的矩正 初始都為-1
        cost[M-1][N-1] = grid[M-1][N-1] #給最右下值
        return self.helper(0, 0, grid, cost)
'''
Dynamic Programming using Memoization

Start Point: 0, 0. Destination Point: M-1, N-1
Cost[i,j]: The cost to reach destination from (i,j). Matrix is initialized to inf.
The solution will be cost(0,0)
Initialize the cost matrix with boundary condition. cost[M-1,N-1]=grid[M-1,N-1]
Be careful with what you return for out of bound grid points. Make sure you return infinity so that they are ignored within the min equation
Time and Space Complexity: O(MN)

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]


'''

'''
It acts as an unbounded upper value for comparison. This is useful for finding lowest values for something. for example, calculating path route costs when traversing trees.

e.g. Finding the "cheapest" path in a list of options:

>>> lowest_path_cost = float('inf')
>>> # pretend that these were calculated using some worthwhile algorithm
>>> path_costs = [1, 100, 2000000000000, 50]
>>> for path in path_costs:
...   if path < lowest_path_cost:
...     lowest_path_cost = path
...
>>> lowest_path_cost
1

if you didn't have float('Inf') available to you,
what value would you use for the initial lowest_path_cost? Would 9999999 be enough -- float('Inf') removes this guesswork.





'''
