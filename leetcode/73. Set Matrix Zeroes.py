'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
#自己重寫, time complexity O(mn), space complexity O(1)
#思路: in place modify, 利用in place mark 來紀錄0的影響區間, 達成space complexity, O(1)
#此題要分兩塊看, 第一排與第一列要先看裡面是否有0, 若有0 之後再把該排or列元素 全部變成0
#內陸元素若是0, 則針對該元素的排 and 列 的第一個元素把它變成0, 之後其他元素對應到該排or列的首元素是0 自己也要變成0
#why 第一排 and 第一列要分開看, 原因在於(0,0)位置, 若第一列有0, 但(0,0)本身不是0, 其會被改成0, 進而造成第一排也都是0, 這樣是不對的
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m, n = len(matrix), len(matrix[0])
        
        firstRow_has_zero = False
        firstCol_has_zero = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol_has_zero = True
        
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow_has_zero = True
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRow_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if firstCol_has_zero:
            for i in range(m):
                matrix[i][0] = 0


#重寫第二次, time complexity O(mn), space complexity O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero, firstColZero = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0


#重寫第三次, time complexity O(mn), space complexity O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_0, first_col_has_0 = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_0 = True
                    if j == 0:
                        first_col_has_0 = True
                    if i != 0 and j != 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_has_0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_0:
            for i in range(m):
                matrix[i][0] = 0


#naive method, time complexity O(m*n), space complexity O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0


O(1) space solution in Python
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        
        row_zero = False  #指的是直的第一排
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        col_zero = False  #指的是橫的第一排
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True
                
        for i in range(1, m):  # 裡面 cell 若是 0 則 該 col and row 的第一個 cell mark成 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if col_zero: #橫的第一排 有0 則全部都是0
            for j in range(n):
                matrix[0][j] = 0
        if row_zero: #直的第一排 有0 則全部都是0
            for i in range(m):
                matrix[i][0] = 0




               

'''
Python O(1) space 

a = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

not all(a[0])

False

a = [
  [0,0,0],
  [1,0,1],
  [1,1,1]
]
if a[0]: print('ok')
else: print('bad')
>ok

a = [
  [],
  [1,0,1],
  [1,1,1]
]

if a[0]: print('ok')
else: print('bad')
>bad

a = [
  [1,1,1],
  [0,0,1],
  [1,1,1]
]

for row in a:
    if row[0]== 0:
        print('it has zero')
    else:
        print('it does not have zero')

it does not have zero
it has zero
it does not have zero



'''

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''