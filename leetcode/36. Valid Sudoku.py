'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.

'''

#刷題用這個, time complexity O(81), space complexity O(9)
#思路: 使用zip(*board) 來連結col
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_unit_valid(row):
                return False
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[m][k] for m in range(i, i + 3) for k in range(j, j + 3)]
                if not self.is_unit_valid(block):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        temp = [i for i in unit if i != "."]
        return len(set(temp)) == len(temp)


# 重寫第二次, time complexity O(1), space complexity O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_unique(row):
                return False
        for col in zip(*board):
            if not self.check_unique(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[k][l] for k in range(i, i + 3) for l in range(j, j + 3)]
                if not self.check_unique(block):
                    return False
        return True
    
    def check_unique(self, items):
        items = [item for item in items if item != "."]
        return len(items) == len(set(items))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and
        self.is_col_valid(board) and
        self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
    
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)

            '''
            def is_unit_valid
            set(unit) 留下不重複的 來判斷1-9不重複

            How to unzip?
            Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator.
            >>>a = [1,2,3]
            >>> b = [4,5,6]
            >>> c = [4,5,6,7,8]
            >>> zipped = zip(a,b)     # 打包为元组的列表
            [(1, 4), (2, 5), (3, 6)]
            >>> zip(a,c)              # 元素个数与最短的列表一致
            [(1, 4), (2, 5), (3, 6)]
            >>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
            [(1, 2, 3), (4, 5, 6)]

            a=[
              ["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ]

            print(list(zip(*a)))
            [('5', '6', '.', '8', '4', '7', '.', '.', '.'), 
            ('3', '.', '9', '.', '.', '.', '6', '.', '.'), 
            ('.', '.', '8', '.', '.', '.', '.', '.', '.'), 
            ('.', '1', '.', '.', '8', '.', '.', '4', '.'), 
            ('7', '9', '.', '6', '.', '2', '.', '1', '8'), 
            ('.', '5', '.', '.', '3', '.', '.', '9', '.'), 
            ('.', '.', '.', '.', '.', '.', '2', '.', '.'), 
            ('.', '.', '6', '.', '.', '.', '8', '.', '7'),
             ('.', '.', '.', '3', '1', '6', '.', '5', '9')]

             a[8][8] = '9'

            for i in (0, 3, 6):
              for j in (0, 3, 6):
                 print([a[x][y]for x in range(i, i + 3) for y in range(j, j + 3)])

            ['5', '3', '.', '6', '.', '.', '.', '9', '8']
            ['.', '7', '.', '1', '9', '5', '.', '.', '.']
            ['.', '.', '.', '.', '.', '.', '.', '6', '.']
            ['8', '.', '.', '4', '.', '.', '7', '.', '.']
            ['.', '6', '.', '8', '.', '3', '.', '2', '.']
            ['.', '.', '3', '.', '.', '1', '.', '.', '6']
            ['.', '6', '.', '.', '.', '.', '.', '.', '.']
            ['.', '.', '.', '4', '1', '9', '.', '8', '.']
            ['2', '8', '.', '.', '.', '5', '.', '7', '9']



            '''
