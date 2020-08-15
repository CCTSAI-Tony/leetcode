'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 
'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') 
represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), 
return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. 
For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
'''


Python DFS solution
#  發現b, recursive reveal adjacent squares, until that square is not a b(with none mine around it), 若不是b停止擴散
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        # run dfs to reveal the board
        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        if board[i][j] != 'E': #若是被發現過的還是未發現的地雷, 停止擴散
            return

        m, n = len(board), len(board[0])       
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)] #八方擴散

        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
                mine_count += 1

        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)  #若附近有地雷, 停止擴散 return
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)



#自己重寫 time complexity O(m*n)
#  思路: 使用dfs 來執行擴散, 若當下cell 附近沒有地雷, 則向八方擴散, 若遭擴散的cell不是"B", 則停止擴散下去
#  利用八個方向來尋找附近有幾顆地雷, 若0顆 則"B", 超過0顆 則 "count"
#  發現b, recursive reveal adjacent squares, until that square is not a b(with none mine around it), 若不是b停止擴散

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return None
        m, n = len(board), len(board) - 1
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        self.dfs(i, j, board)
        return board
        
    def dfs(self, i, j, board):
        if board[i][j] != "E":
            return
        m, n = len(board), len(board[0])
        directions = [(1,1), (1,-1), (1, 0), (-1, 0), (-1,1), (-1,-1), (0,1), (0,-1)]
        count = 0
        for d in directions:
            if 0 <= i + d[0] < m and 0 <= j + d[1] < n and board[i + d[0]][j + d[1]] == "M":
                count += 1
        if count == 0:
            board[i][j] = "B"
            for d in directions:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n :
                    self.dfs(i + d[0], j + d[1], board)
        else:
            board[i][j] = str(count)
            return



#  bfs 自己寫的 196ms, time complexity O(m*n)
#  思路: 記住不能像dfs 利用inplace mark 來避掉已visited 的cell, 因為無法向dfs一樣, 馬上改變該E cell 的mark
#  在把E cell 拿進queue以前就要mark 進 visited
#  同layer 的cell 可能加入還沒pop out 的對方 or 一樣的 E cell, 所以要建立visited 來避免重複加入E cell
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return None
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        queue = deque([(click[0], click[1])])
        direc = [(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1)]
        m, n = len(board), len(board[0])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                count = 0
                for d in direc:
                    new_x, new_y = x + d[0], y + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == "M":
                        count += 1
                if count > 0:
                    board[x][y] = str(count)
                    continue
                board[x][y] = "B"
                for d in direc:
                    new_x, new_y = x + d[0], y + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n and \
                    board[new_x][new_y] == "E" and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
        return board


