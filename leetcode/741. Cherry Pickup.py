'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
 

Example 1:


Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] is -1, 0, or 1.
grid[0][0] != -1
grid[n - 1][n - 1] != -1
'''

# time complexity O(n^3)
#思路: 利用f(i, j, k) 當作狀態函式, i + j = k 代表同一個步(也算同一個對角線) g[i][k-i] or g[j][k-j], 只是代表同一個對角線的其中兩格 or 有可能同一格
#注意這裡i 從 1開始, 所以要取得grid cell值的時候, 要減1, 因為 0 base index issue, 
# ex: f(1,2,3) = g[1][3-1] = g[1][2] => grid[0][1], f(1,2,3)是第二條斜線組合
#想法是與其來回走, 不如直接想成兩個路徑同時走, 若兩條路徑燈走到同一格, 只能取一次櫻桃, 不然可以取兩格的櫻桃
#若兩格其中一格不能走(代表不能來回), 則f(i, j, k) 就不用算, skip 此路徑方案
#from g[i][k-i] or g[j][k-j] => 1 <= i <= n, 1 <= k - i <= n, 推導出 k-n <= i <= k-1, 搭配 1 <= i <= n
#技巧: 一開始要把dp值設負無窮, 這樣invalid path才不會影響其他有效路徑
#技巧: 取斜線當作狀態方程時, dp 記得都是 1 base index, 但轉到實際grid 要轉為 0 based index
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float("-inf")] * (n*2+1) for _ in range(n+1)] for _ in range(n+1)]
        dp[1][1][2] = grid[0][0]
        for k in range(3, 2*n+1):
            for i in range(max(1, k-n), min(n, k-1) + 1):
                for j in range(max(1, k-n), min(n, k-1) + 1):
                    if grid[i-1][k-i-1] == -1 or grid[j-1][k-j-1] == -1:
                        continue
                    t = grid[i-1][k-i-1]
                    if i != j:
                        t += grid[j-1][k-j-1]
                    # 共有四種走法
                    for a in range(i-1, i+1): #前一次狀態方程式 i的可能值
                        for b in range(j-1, j+1): #前一次狀態方程式 j的可能值
                            dp[i][j][k] = max(dp[i][j][k], dp[a][b][k-1] + t)
                                 
        return max(0, dp[-1][-1][-1])





# 刷題用這個, 0 base index, 自己想的, time complexity O(n^3)
# 0 based index 解法, k值= 0 to 2n-2, dp 是3d matrix
# 0 <= i <= n-1, 0 <= k - i <= n-1 =>  k - n + 1 <= i <= k
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float("-inf")] * (n*2-1) for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]
        for k in range(1, 2*n-1):
            for i in range(max(0, k-n+1), min(n-1, k) + 1):
                for j in range(max(0, k-n+1), min(n-1, k) + 1):
                    if grid[i][k-i] == -1 or grid[j][k-j] == -1:
                        continue
                    t = grid[i][k-i]
                    if i != j:
                        t += grid[j][k-j]
                    for a in range(i-1, i+1): #前一次狀態方程式 i的可能值
                        for b in range(j-1, j+1): #前一次狀態方程式 j的可能值
                            dp[i][j][k] = max(dp[i][j][k], dp[a][b][k-1] + t)
                                            
        return max(0, dp[-1][-1][-1])





