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
#自己重寫, time complexity O(mn*3^l), l: len of word, space complexity O(l), 刷題用這個, backtracking
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



# 重寫第二次, time complexity O(mn*3^l), space complexity O(l)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, 1, word):
                        return True
        return False
    
    def dfs(self, i, j, board, idx, word):
        if idx == len(word):
            return True
        m, n = len(board), len(board[0])
        tmp = board[i][j]
        board[i][j] = "#"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[idx]:
                if self.dfs(x, y, board, idx + 1, word):
                    return True
        board[i][j] = tmp
        return False




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