'''
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  
For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: 
if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
'''

#自己想的, time complexity O(m*n), space complexity O(m*n)
#思路: 使用bfs, 建立map 來連結number cell 與 board 對應位置的值, 使用bfs, 初始cell = 1, 每一move可以有6種選擇 => new_cell, 
#當new_cell 對應的board值 != -1 時, new_cell 立即變成對應的board值, 建立visited 一但找到valid new_Cell 放入queue, 登記在visited, 已免重複遍歷
#直到new_Cell == m*n return move, 記得 valid new_cell <= m*n
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        square = {}
        m ,n = len(board), len(board[0])
        index = 1
        for i in range(m-1, -1, -1):
            if i % 2 == (m-1) % 2:
                for j in range(n):
                    square[index] = board[i][j]
                    index += 1
            else:
                for j in range(n-1, -1, -1):
                    square[index] = board[i][j]
                    index += 1
            
        queue = deque([1])
        visited = set([1])
        move = 0
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                if cell == m*n:
                    return move
                for i in range(1,7):
                    new_cell = cell + i
                    if new_cell <= m*n:
                        if square[new_cell] != -1:
                            new_cell = square[new_cell]
                        if new_cell not in visited:
                            visited.add(new_cell)
                            queue.append(new_cell)
            move += 1
        return -1



#重寫第二次, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        cells = {}
        idx = 1
        for i in range(m-1, -1, -1):
            if i % 2 == (m - 1) % 2:
                for j in range(n):
                    cells[idx] = board[i][j]
                    idx += 1
            else:
                for j in range(n-1, -1, -1):
                    cells[idx] = board[i][j]
                    idx += 1
        
        q = deque([1])
        visited = set([1])
        move = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == m * n:
                    return move
                for i in range(1, 7):
                    nxt = cur + i
                    if nxt <= m * n:
                        if cells[nxt] != -1:
                            nxt = cells[nxt]
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
            move += 1
        return -1

























