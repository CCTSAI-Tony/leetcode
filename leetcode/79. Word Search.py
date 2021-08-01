'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''
#自己重寫, time complexity O(mn*3^l), l: len of word, space complexity O(mn), 刷題用這個, backtracking
#思路: backtracking 經典題, 從matrix 找文字開頭當作起始搜尋點, 利用in place 修改來防止重複遍歷的問題, 若發現無法完成字串, 則一路backtrack到上層來試其他分支
#重點是回到上層途中要把in place 修改的地方 恢復回原本的樣貌
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word, 0):
                        return True
        return False
    
    
    def dfs(self, i, j, board, word, index):
        if index == len(word) - 1:
            return True
        m, n = len(board), len(board[0])
        direcs = [(1,0),(-1,0),(0,-1),(0,1)]
        temp = board[i][j]
        board[i][j] = "#"  #in-place modify 防止重複遍歷
        for d in direcs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[index+1]:
                if self.dfs(x, y, board, word, index+1):
                    return True
        board[i][j] = temp  #backtracking, 修復回來




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])): #for col in range(len(board[0])) 也可以寫成這樣
                if self.dfs(board, row, col, word):
                    return True
                    
        return False
    
    def dfs(self, board, row, col, word): # check whether can find word, start at (i,j) position  
        if len(word) == 0: # all the characters are checked 字串找到！
            return True
        if row < 0 or col <0 or row >= len(board) or col >= len(board[row]) or board[row][col] != word[0]: #這行代表提供到哪停止往下 
            return False
        
        temp = board[row][col] # first character is found, check the remaining part
        board[row][col] = "#" # avoid visit agian 

         # check whether can find "word" along one direction

        res = self.dfs(board, row-1, col, word[1:]) or self.dfs(board, row+1, col, word[1:]) \
        or self.dfs(board,row,col-1, word[1:] ) or self.dfs(board, row, col +1, word[1:])  #其中有True, return res = True
        
        board[row][col] = temp #若此層往下搜索都找不到 board[row][col] 把'#'改回來！
        
        return res

'''
(True or False) == True

True

(True or False) == False

False

def check():
    res = True or False
    return res

check()

True





Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


'''