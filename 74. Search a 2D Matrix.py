# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

#刷題用這個
#自己重寫, 模板2, time complexity O(m + logn) m: len(matrix), n: len(row)
#思路: 因為每行row已經排序, 所以target若大於每行的最後一個就skip該行, 直到有一行最後一個元素比target大, 代表該行是唯一有可能存在target的地方
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            if row[-1] < target:
                continue
            left, right = 0, len(row)-1
            while left + 1 < right:
                mid = left + (right - left)//2
                if row[mid] >= target:
                    right = mid
                else:
                    left = mid
            if row[left] == target or row[right] == target:
                return True
            return False
        return False







#模板1 time complexity O(log m*n)
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1  #zero base index
        
        while low <= high:
            mid = (low + high) //2
            num = matrix[mid // cols][mid % cols] #先向下取整得到row 再餘數等於col, index = 4 自己帶入一下就知道為什麼這樣轉換

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false



'''

#自己重寫 模板2 time complexity O(m+logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, n-1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][n-1]:
                row += 1
            elif target < matrix[row][0]:
                return False
            else:
                low, high = 0, n-1
                while low + 1 < high:
                    mid = low + (high - low)//2
                    if target == matrix[row][mid]:
                        return True
                    elif target > matrix[row][mid]:
                        low = mid
                    else:
                        high = mid
                if target == matrix[row][low]:
                    return True
                if target == matrix[row][high]:
                    return True
                return False





















