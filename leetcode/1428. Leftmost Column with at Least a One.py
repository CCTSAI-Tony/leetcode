'''
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in non-decreasing order.

'''

# 刷題用這個, time complexity O(mlogn), space complexity O(1)
# 思路: 使用binary search
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row_d, col_d = binaryMatrix.dimensions()
        left_most = float("inf")
        for i in range(row_d):
            ans = self.binary_search(i, col_d, binaryMatrix)
            left_most = min(left_most, ans)
        return left_most if left_most != float("inf") else -1
            
        
    def binary_search(self, row_index, col_d, binaryMatrix):
        l, r = 0, col_d - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if binaryMatrix.get(row_index, mid) == 1:
                r = mid
            else:
                l = mid
        if binaryMatrix.get(row_index, l) == 1:
            return l
        elif binaryMatrix.get(row_index, r) == 1:
            return r
        else:
            return float("inf")



