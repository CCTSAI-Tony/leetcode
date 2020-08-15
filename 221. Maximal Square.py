'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

# 221. Maximum Square
# > 类型：二维DP
# > Time Complexity O(N^2)
# > Space Complexity O(N^2)

#自己重寫 time complexity O(m*n), 232ms
#思路: 若cell為1 利用cell的上, 左, 左上的cells 看是否都為1, 若是則square邊長 + 1, 若不是則取這三個cell的最小值也就是0, 並加自身的1
#概念衍生為dp, dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == "0" else 1 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
         
        length = max(max(row) for row in dp) # max(每行的重大值-array)
        return length**2

#注意!! [max(row) for row in dp] vs max(row for row in dp)
#max(row for row in dp): 取最大的一行, 比較定義: 從左邊第一格數比到最右邊
#[max(row) for row in dp]: 每一行的最大值組成的數組




#思路: 若cell為1 利用cell的上, 左, 左上的cells 看是否都為1, 若是則square邊長 + 1, 若不是則取這三個cell的最小值也就是0, 並加自身的1
#概念衍生為dp, dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: 
        	return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)] #list comprehension 建構map, 把string matrix變成 int
        
        for i in range(1, m): #邊界值dp[0][n] and dp[m][0] = 原本matrix值
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        res = max(max(row) for row in dp) #max(dp[i][j]) 先取得每行最大值的集合, 再從此集合中取最大值
        return res ** 2

# https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm

a = [[1,2,3,4,5,6,7,8,9,10],
[11,22,33,44,55,66,77,88,99,110],
[1,222,333,444,555,666,777,888,999,1110]]

[max(row) for row in a]
[10, 110, 1110]

max([max(row) for row in a])
1110