'''
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
'''


#刷題用這個, time complexity O(1), space complexity O(1)
class Solution(object):
    def check_win_positions(self, board, player):
        #Check the rows
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True                        

        #Check the columns
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True 
                                        
        #Check the diagonals
        if board[0][0] == board[1][1] == board[2][2]  == player or \
               board[0][2] == board[1][1] == board[2][0] == player:
            return True
                        
        return False
        
    def validTicTacToe(self, board):
        x_count, o_count = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    x_count += 1
                elif  board[i][j] == "O":
                    o_count += 1
                                        
        if o_count > x_count or x_count-o_count>1:
            return False
        
        if self.check_win_positions(board, 'O'):
            if self.check_win_positions(board, 'X'):
                return False
            return o_count == x_count
        
        if self.check_win_positions(board, 'X') and x_count!=o_count+1:
            return False

        return True







#自己想的, time complexity O(1), space complexity O(1)
#思路: matrix + dic, X 先下, 若O贏, X與O 下的次數要一樣
from collections import defaultdict
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        win_o, win_x = False, False
        row_x, row_o = defaultdict(int), defaultdict(int)
        col_x, col_o = defaultdict(int), defaultdict(int)
        dia1_x, dia1_o = defaultdict(int), defaultdict(int)
        dia2_x, dia2_o = defaultdict(int), defaultdict(int)
        count_x, count_o = 0, 0
        for i in range(3):
            for j in range(3):
                state = board[i][j]
                if state == "X":
                    count_x += 1
                    row_x[i] += 1
                    col_x[j] += 1
                    dia1_x[i-j] += 1
                    dia2_x[i+j] += 1
                elif state == "O":
                    count_o += 1
                    row_o[i] += 1
                    col_o[j] += 1
                    dia1_o[i-j] += 1
                    dia2_o[i+j] += 1
        win_x = True if 3 in list(row_x.values()) + list(col_x.values()) + list(dia1_x.values()) + list(dia2_x.values()) else False
        win_o = True if 3 in list(row_o.values()) + list(col_o.values()) + list(dia1_o.values()) + list(dia2_o.values()) else False
        if win_x and win_o:
            return False
        elif count_o > count_x:
            return False
        elif count_x - count_o > 1:
            return False
        elif win_x and count_x == count_o:
            return False
        elif win_o and count_x > count_o:
            return False
        return True


