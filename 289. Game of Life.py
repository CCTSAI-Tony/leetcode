'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''


# the key point is to understand that the change to a cell is only decided by its nearby 8 cell in the original grid.

# we should not use the updated cell to compute to change decision for other cell,therefore, the brute force way 
# is to store the result in a new grid,then assign result back

# But usually it requires use O(1) space, so the problem becomes: How can we store the middle result without use extra space.

# the solution is to store the result in the origin grid as different number by some rule, so when we compute decision for other cell, 
# we can know the original value of those nearby cell which has already been updated based on the rule

# for example, we can do like this

# living cells nearby | change | new value

# <2                      1->0     2
# 2,3                     1->1     1
# >3                      1->0     2
# 3                       0->1     3
# so when we count living cells nearby, we need to count those value equals to 1 and 2

#思路: inplace modefied, 使用其他代號來暗示當前的狀況與之後的狀況, 之後再依這些暗號來給予該cell的next_state (0 or 1)
#小心邊界index issue
class Solution(object):
    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for a in range(max(0, i - 1), min(i + 2, m)): #check neighborhood, max(0, i - 1), min(i + 2, m) avoid crossing boundary
                    for b in range(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2: #exclude itself, and count 1,2 for its neighborhood
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1



