'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

#自己重寫 time complexity O(m + n), space complexity O(1)
#思路: 此題與leetcode 74 不一樣的地方在於就算當層row最後一個數字大於target, 當層row的下一行中間元素也有機會等於target
#因此, 跟74一樣 若當層row最後一個數字小於target skip 該row, 直到當層row最後一個數字大於target, 
#開始比對當層row最後一個元素, 比target大 col 往左(因為row往上只會更大), 比target小 row 往上(因為col往左只會更小)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):  #也可以 while col >= 0 and row <= len(matrix) - 1: row只會往上, col 只會往左
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False


#重寫第二次, time complexity O(m+n), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False

#重寫第三次, time complexity O(m + n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False





#binary search 自己重寫 模板2
#Time complexity O(mlogn), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = 0
        while 0 <= row < len(matrix):
            if target > matrix[row][-1]:
                row += 1
            else:
                left, right = 0, len(matrix[0]) - 1
                while left + 1 < right:
                    mid = left + (right - left) // 2
                    if target >= matrix[row][mid]:
                        left = mid
                    else:
                        right = mid
                
                if matrix[row][left] == target or matrix[row][right] == target:
                    return True
                row += 1  #持續往下一行遍歷, 不像leetcode 74, 此題下一行還是有機會找到target的
        return False






# 240. Search a 2D Matrix II
# Time Complexity: O(m + n)
# Space Complexity: O(1)
# Time Spent on this question: 20 mins
# 这题放弃直接看的最高票答案，方法聪明到让我无fuck说。直接用target和矩阵中的每个row的最后一个值比对。因为每个row都是排序过的，
# 也就是说最后一个值一定是该row最大的值，所以只要target值比这个最大值还要大，target值一定不再这个row里面，那么我们就增加row，
# 去下一排的row里面找。如果target比row中的最大值要小，说明target会出现在这个row中，那么我们就缩减col，然后一个一个找就行了。无fuck说

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        
        row, col = 0, len(matrix[0]) - 1 #col 直接比對最後一個
        while col >= 0 and row <= len(matrix) - 1:  #row只會往上, col 只會往左
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False

# what's the purpose of checking len(matrix) < 1 or len(matrix[0]) < 1? Should if not matrix enough to check if matrix is None? What is it checking here?

# Because the input matrix represents a 2D array, if we only have matrix != None, we would miss the edge case when the value inside of matrix equals to None, 
# for example when matrix = [[]]

# def is_arr():
#     matrix = [[]]
#     return True if matrix else False

# print(is_arr())   #return True, but should be False in our case, so we need extra edge case to check for it
# in this case, even though matrix isn't None, however, the value inside is None technically. According to the question description, 
# such a case should return False instead of True.









# 模板2
# binary search, Time complexity O(mlogn), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        row, col = 0, len(matrix[0]) -1
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][0]:
                return False
            else:
                low, high = 0, len(matrix[0]) -1
                while low + 1 < high:
                    mid = low + (high - low)//2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        low = mid
                    else:
                        high = mid
                if matrix[row][low] == target:
                    return True
                elif matrix[row][high] == target:
                    return True
                else:
                    row += 1  #跟leetcode 74不一樣的地方, 持續往下搜索
        return False


