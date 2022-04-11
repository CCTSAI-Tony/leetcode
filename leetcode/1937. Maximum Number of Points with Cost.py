'''
You are given an m x n integer matrix points (0-indexed). 
Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. 
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), 
picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
 

Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
 

Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105
'''

'''
The idea is to us dynamic programming, but we need to update each next row, 
using previous in linear time, we can not allow slower given problem constraints. Imagine, that we have row

A0, A1, A2, A3, A4, A5.

And we want to calcualte answers for the new row. For the first element we need to calculate:
max(A0, A1-1, A2-2, A3-3, A4-4, A5-5), for the second element
max(A0-1, A1, A2-1, A3-2, A4-3, A5-4),
max(A0-2, A1-1, A2, A3-1, A4-2, A5-3) and so on.

The trick is to find all this values using some preprocessing. 
Look at the value max(A0-2, A1-1, A2, A3-1, A4-2, A5-3), 
it can be written as max(max([A0+0, A1+1, A2+2] - 2), max([A2-2, A3-3, A4-4, A5-5]) + 2). 
And in fact all values can be written in similar way. What we need to do now is to calculate cumulative maximums ans we are done!

Complexity
Time complexity is O(mn), space complexity is O(n).
'''

# 刷題用這個, time complexity O(mn), space complexity O(n)
# 思路: 使用max accumulation (似prefix sum, 但不是, 只是取之前遇到的最大值) 來產生新row該指定col 作為舊row col的左邊 or 右邊的最大值
# 為什麼要取左邊 or 右邊, 因為 abs(c1 - c2)
from itertools import accumulate
class Solution:
    def maxPoints(self, P):
        m, n = len(P), len(P[0])
        dp = P[0]
        for i in range(1, m):
            c1 = list(accumulate([a+b for a,b in zip(dp, range(n))], max)) # new row col選在old row 右邊or相同
            c2 = list(accumulate([a-b for a,b in zip(dp[::-1], range(n-1,-1,-1))], max)) # new row col選在old row 左邊or相同
            dp2 = [max(c1[j] - j, c2[n-1-j] + j) for j in range(n)]
            dp = [x+y for x,y in zip(dp2, P[i])]
        return max(dp)


# 重寫第二次, time complexity O(mn), space complexity O(n)
from itertools import accumulate
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]
        for i in range(1, m):
            left = list(accumulate([a+b for a,b in zip(dp, range(n))], max))
            right = list(accumulate([a-b for a,b in zip(dp[::-1], range(n-1, -1, -1))], max))
            right.reverse()
            dp = [max(left[j] - j, right[j] + j) + points[i][j] for j in range(n)]
        return max(dp)




