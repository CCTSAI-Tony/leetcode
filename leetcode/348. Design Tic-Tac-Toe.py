'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
'''

# Let's only look at rows first:
# row[] represents the move count of a row
# If player1 move on a cell in row[1], then row[1]+=1
# If player2 move on a cell in row[1], then row[1]-=1
# If both player1 and player2 move on some cells in row[1], 
# then row[1] will never become "n" because it is guaranteed that all moves are valid and will only moves on empty cells.
# If row[1] becomes "n", if it is currently player1's move, then player1 wins, else player2 wins.
# For each move, only check rows of current move, no need to check all rows.

# Do the same for columns to check winning condition on column.

# For diagnal, if rowIdx-colIdx==0, that means the move is on top-left to right-bottom diagnal. 
# If rowIdx+colIdx==n-1, that means the move is on top-right to bottom-left diagnal.

# So total space is "rows array + columns array + two diagnals": O(n+n+1+1)==O(n)
# For each move, time checking current row, column, and two diagnals takes O(n+n+1+1)==O(n)

#思路: 此題考驗簡化, 若暴力解就是check n*n cells, 然而我們可以分開計算row, column, diagonal 的狀況
#player1 的move + 1, player2 的move -1, 當 row, column, diagonal, 的個別絕對值 = n時, 代表目前move的人贏了
#因為題目說任何move都是有效且踩在empty cell, 所以只要個別確認該move 在哪一行 哪一列 哪一diagonal 來更新該行狀態
#time complexity for move O(n) => row: O(n), col: O(n), diagonal: O(2)
class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row]+=1 if player==1 else -1 #技巧
        self.col[col]+=1 if player==1 else -1
        if row+col==self.n-1: #右上左下斜線
            self.diag1+=1 if player==1 else -1
        if row-col==0:
            self.diag2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return 1 if player==1 else 2
        return 0



#自己重寫, time complexity O(n)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.dia1 = 0
        self.dia2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1
        if row - col == 0:
            self.dia1 += 1 if player == 1 else -1
        if row + col == self.n - 1:
            self.dia2 += 1 if player == 1 else -1
        
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or\
        abs(self.dia1) == self.n or abs(self.dia2) == self.n:
            return 1 if player == 1 else 2
        return 0


#重寫第二次, time complexity O(n), space complexity O(1)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal1 = 0
        self.diagonal2 = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1
        if row + col == self.n - 1:
            self.diagonal1 += 1 if player == 1 else -1
        if row - col == 0:
            self.diagonal2 += 1 if player == 1 else -1
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal1) == self.n or abs(self.diagonal2) == self.n:
            return 1 if player == 1 else 2
        return 0







a = 5
a += 10 if 1 > 10 else -10
a
-5

a = [1,2,3]
a += [100] if 1> 10 else [-100]
a
[1, 2, 3, -100]























