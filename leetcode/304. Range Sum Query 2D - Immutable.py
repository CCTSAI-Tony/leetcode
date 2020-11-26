'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''

# Python O( m * n ) init, O(1) query by integral image technique.

# Here we use the technique of integral image, which is introduced to speed up block computation.

# Also, this technique is practical and common in the field of matrix operation and image processing.

# Block sum formula on integral image.
# Block-sum of red rectangle
# = block-sum of D - block-sum of B - block-sum of C + block-sum of A
# = blocksum of bottom right - blocksum of top right - blocksum of bottom left + blocksum of top left
# SUM = D-B-C+A

# image

# Example of integral image ( focus on the purple block ).

# image

# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/511805/Python-O(m*n)-init-O(1)-query-by-integral-image.-90%2B-with-Explanation
#看上面連結圖比較好理解!

#刷題用這個, time complexity O(m*n) init, O(1) query by integral image technique
#思路: 先建立prefix sum, 每個位置都代表從左上原點拉到右下點的matrix sum
#再扣除掉左下點, 右上點的matrix sum, 加回左上點的matrix sum => 指定的matrix sum
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix:
            # Reject empty matrix
            return
        
        # get height and width of matrix (also known as image)
        h, w = len(matrix), len(matrix[0])
        
        # build integral image by recurrence relationship    
        self.integral_image = [ [ 0 for _ in range(w) ] for _ in range(h) ]


        for y in range(h): #每行從左到右加總

            summation = 0 #先針對每行加總, row = 0 的邊境狀況在此決定

            for x in range(w):

                summation += matrix[y][x]
                self.integral_image[y][x] = summation

                if y > 0:
                    self.integral_image[y][x] += self.integral_image[y-1][x] #承襲上一排加總
                    
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        bottom_right    = self.integral_image[row2][col2]
        bottom_left     = self.integral_image[row2][col1-1] if col1 >= 1 else 0 #else 0 means bottom_left = 0
        top_right       = self.integral_image[row1-1][col2] if row1 >= 1 else 0
        top_left        = self.integral_image[row1-1][col1-1] if col1 >= 1 and row1 >=1 else 0
        
        return bottom_right - bottom_left - top_right + top_left


#自己重寫, time complexity O(m*n) init, O(1) query by integral image technique
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.prefix[i][j] = row_sum
                if i > 0:
                    self.prefix[i][j] += self.prefix[i-1][j]
                    
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        downleft = self.prefix[row2][col1-1] if col1 > 0 else 0
        topright = self.prefix[row1-1][col2] if row1 > 0 else 0
        topleft = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.prefix[row2][col2] - downleft - topright + topleft





