'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

#time complexity O(n!), space complexity O(n)
#思路: 排, 列, 2個對角線, 只能有一個queen, 利用backtrack 一排一排遍歷
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution(): #關鍵
            solution = []
            for row, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0): #從第一層row 開始排列
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n: #已是最底層
                        add_solution()
                    else:
                        backtrack(row + 1) #進入下一層, 若下一層無法, backtrack
                    remove_queen(row, col) #回復原狀
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output


#重寫第二次, time complexity O(n!), space complexity O(n)
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n, self.queens  = n, [], 
        self.col, self.diag_1, self.diag_2 = defaultdict(int), defaultdict(int), defaultdict(int)
        self.res = []
        self.backtracking(0)
        return self.res
        
    def couldPlace(self, i, j):
        return not (self.col[j] + self.diag_1[i + j] + self.diag_2[i - j])
    
    def placeQueen(self, i, j):
        self.queens.append((i, j))
        self.col[j] = 1
        self.diag_1[i + j] = 1
        self.diag_2[i - j] = 1
    
    def removeQueen(self, i, j):
        self.queens.remove((i, j))
        self.col[j] = 0
        self.diag_1[i + j] = 0
        self.diag_2[i - j] = 0
    
    def addAnswer(self):
        ans = []
        for r, c in self.queens:
            row = "." * c + "Q" + "." * (self.n - (c + 1))
            ans.append(row)
        self.res.append(ans)
    
    def backtracking(self, r):
        for c in range(self.n):
            if self.couldPlace(r, c):
                self.placeQueen(r, c)
                if r == self.n - 1:
                    self.addAnswer()
                else:
                    self.backtracking(r + 1)
                self.removeQueen(r, c)


