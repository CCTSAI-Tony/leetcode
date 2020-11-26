'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

# BFS 刷題用這個
# time complexity O(m*n)
import collections
class Solution:
	def solve(self, board):
	    queue = collections.deque([])
	    for r in range(len(board)):  #收集有效擴散點
	        for c in range(len(board[0])):
	            if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O": #邊界O
	                queue.append((r, c))
	    while queue:
	        r, c = queue.popleft()
	        if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
	            board[r][c] = "D" #防止再度加入
	            queue.append((r-1, c)) 
                queue.append((r+1, c)) #邊界O上下擴散
	            queue.append((r, c-1)) 
                queue.append((r, c+1)) #邊界O左右擴散
	        
	    for r in range(len(board)):
	        for c in range(len(board[0])):
	            if board[r][c] == "O":
	                board[r][c] = "X"
	            elif board[r][c] == "D":
	                board[r][c] = "O"


#自己重寫 bfs
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        m, n = len(board), len(board[0])
        stack = deque()
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][n-1] == "O":
                stack.append((i,n-1))
        for j in range(n):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[m-1][j] == "O":
                stack.append((m-1,j))
        while stack:
            x, y = stack.popleft()
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                board[x][y] = "D"
                stack.append((x+1, y))
                stack.append((x-1, y))
                stack.append((x, y+1))
                stack.append((x, y-1))
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"



#  刷題用這個 dfs
#  time complexity O(m*n)
#  思路: 利用邊界"O" 來連結內陸"O", 有連結到的改成"N", 沒連結到的"O", 之後對會變"x", 有連結的 "N" 變 "O"
#  另一角度利用內陸O dfs 擴散看是否能能找到邊界O 比較複雜, 還要考慮重複遍歷無限迴圈的問題
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(i,0,board)
            if board[i][n-1] == "O":
                self.dfs(i,n-1,board)
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(0,j,board)
            if board[m-1][j] == "O":
                self.dfs(m-1,j,board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != "N":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
    
    
    def dfs(self, i, j, board):
        m, n = len(board), len(board[0])
        if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
            board[i][j] = "N"
            self.dfs(i+1,j,board)
            self.dfs(i-1,j,board)
            self.dfs(i,j+1,board)
            self.dfs(i,j-1,board)

#此類問題擴散點儘量找已知最終型態的位置, 這樣才能把已知最終型態的結果擴散給與它相連的物件, 
#若相反, 已未知的地方當擴散點希望找到合適的目標並從合適的目標擴散回來在此題有點脫褲子放屁
#切記在此題 已未知找已知在擴散的路徑中不宜直接修改被擴散的物件, 因為被擴散的物件有可能因為防止重複遍歷的機制而無法向外聯繫導致"O" => "X", 如下圖

# [['O', 'O', 'O', 'O', 'X', 'X'],
#  ['O', 'O', 'O', 'O', 'O', 'O'],
#  ['O', 'X', 'O', 'X', 'O', 'O'],
#  ['O', 'X', 'S', '*', 'X', 'O'],
#  ['O', 'X', 'O', 'X', 'O', 'O'],
#  ['O', 'X', 'O', 'O', 'O', 'O']]

#這就是相反解法, 把未知的當擴散點, 利用dfs 向外搜索是否有找到合適目標, 注意這裡使用visited 已避免重複遍歷進入無限循環
#已找到合適目標來改變自身狀況, 此解法在這題會TLE, 因為不同擴散點之間有太多重複尋找路徑, 
#若用上面解法從已知來擴散並修改未知就能大大減少重工的問題
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if self.dfs(i,j,board, []):
                        board[i][j] = "O"
                    else:
                        board[i][j] = "X"
        
    
    
    def dfs(self, i, j, board, visited):
        if (i,j) in visited:
            return 
        visited.append((i,j))
        m, n = len(board), len(board[0])
        if i == 0 or i == m-1 or j == 0 or j == n-1 and board[i][j] == "O":
            return True
        direc = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in direc:
            if 0 <= i+d[0] < m and 0 <= j+d[1] < n and board[i+d[0]][j+d[1]] == "O":
                if self.dfs(i+d[0], j+d[1], board, visited):
                    return True











