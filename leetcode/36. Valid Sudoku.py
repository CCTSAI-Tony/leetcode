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
