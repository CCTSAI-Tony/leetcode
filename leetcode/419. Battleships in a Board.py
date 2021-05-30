'''
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. 
You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. 
In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
'''
O(n^2) time and O(1) space without modifying the board
#  At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships. 重要條件
#  思路: 依順序 check matrix[i][j] == "x" 的上方與左邊是否同為"x", 若沒有則代表找到獨立的battle ships, 若有則代表該ship已包含在其一 battle ships裡面
#  別忘了在邊界, 則不需check上方與左邊, 此題關鍵在於matrix 遍歷的順序, 與要check的方向相互應, 
#  因為battle ships之間一定會隔開, 所以不用怕確認完上方與左方後, 右方或下方連接的船與其他battle ships連接
#  建議此題搭配leetcode 200題 number of islands 一起練習

class Solution(object):
    def countBattleships(self, board):
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count


#自己重寫
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        count = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    count += 1
        return count

#重寫第二次, time complexity O(mn), space complexity O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if (i == 0 or board[i-1][j] == ".") and (j==0 or board[i][j-1] == "."):
                        count += 1
        return count











