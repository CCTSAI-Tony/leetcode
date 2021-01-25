'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0
 

Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

'''
# The solution is based on largest rectangle in histogram solution. Every row in the matrix is viewed as the ground with some buildings on it. 
# The building height is the count of consecutive 1s from that row to above rows. The rest is then the same as this solution for largest rectangle in histogram

#刷題用這個, time complexity O(mn), space complexity O(n), m:rows, n: cols
#思路: leetcode 84 進階版, 然而這題有一點dp的影子, height[i] 代表該col[i] 到目前row產生連續1 的長度 => 轉化成histogram的高度 => 轉化成 leetcode 84 題目
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans




#重寫第二次, time complexity O(mn), space complexity O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1) #技巧: 尾部多一個0
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0 #不能 height[i] += 1 if row[i] == "1" else 0 => 此邏輯變為 else += 0
            stack = [-1]
            for i in range(n + 1): #技巧: n + 1 使得最後強制進行while loop 來計算面積
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


























