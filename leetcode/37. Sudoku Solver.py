'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''


#自己重寫 time complexity O(9!^9), space complexity O(1) 經典好題多練, 遇到dfs backtracking 要考慮 return 是否要return True or False, 
#這種設計使得回到上一層有多的資訊可以參考, 例如是否要提前結束等..
#思路: dfs backtracking, 這題有趣的是要先建立rols, cols, blocks 的 dict, 來check是否在同樣的區間出現重複的值
#技巧: 此方法利用存儲"." 的位置 來當作dfs recursion的層數, 只有所有數字都填對 讓所有"." 都不見時, dfs才會到達最後一層, 不然會往上一層換其他選擇
#回上層記得恢復所有動過的global variables, remain 記得用deque 加回到最前面
from collections import defaultdict, deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        rows, cols, blocks, remain = defaultdict(set), defaultdict(set), defaultdict(set), deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3, j//3)].add(board[i][j])
                else:
                    remain.append((i, j))
        self.dfs(board, rows, cols, blocks, remain) #因為一定有解, 所以是true, 但我們已不在意, 只是希望它執行dfs而已
        
    def dfs(self, board, rows, cols, blocks, remain):
        if not remain:
            return True
        i, j = remain.popleft() #準備要填數字的cell,全部填完即成功
        for digit in range(1,10):
            d = str(digit)
            if d not in rows[i] and d not in cols[j] and d not in blocks[(i//3,j//3)]:   
                board[i][j] = d
                rows[i].add(d)
                cols[j].add(d)
                blocks[(i//3, j//3)].add(d)
                if self.dfs(board, rows, cols, blocks, remain):
                    return True
                board[i][j] = "."
                rows[i].remove(d)
                cols[j].remove(d)
                blocks[(i//3,j//3)].remove(d)
        remain.appendleft((i,j))
        return False


#重寫第三次, time complexity O(9!)^9 => ^9 => 9條row, space complexity O(1)
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        row, col, block = defaultdict(set), defaultdict(set), defaultdict(set)
        remain = []
        for i in range(m):
            for j in range(n):
                temp = board[i][j]
                if temp == ".":
                    remain.append((i, j))
                else:
                    row[i].add(temp)
                    col[j].add(temp)
                    block[(i//3, j//3)].add(temp)
        self.dfs(row, col, block, board, remain)
        
    def dfs(self, row, col, block, board, remain) -> bool:
        if not remain:
            return True
        i, j = remain.pop()
        for num in range(1, 10):
            d = str(num)
            if d not in row[i] and d not in col[j] and d not in block[(i//3, j//3)]:
                board[i][j] = d
                row[i].add(d)
                col[j].add(d)
                block[(i//3, j//3)].add(d)
                if not self.dfs(row, col, block, board, remain):
                    board[i][j] = "."
                    row[i].remove(d)
                    col[j].remove(d)
                    block[(i//3, j//3)].remove(d)
                else:
                    return True
        remain.append((i, j))
        return False

#重寫第四次, time complexity O(9!)^9, space complexity O(81)
from collections import defaultdict, deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
        remain = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3, j//3)].add(board[i][j])
                else:
                    remain.append((i, j))
        return self.dfs(board, rows, cols, blocks, remain)
        
    def dfs(self, board, rows, cols, blocks, remain):
        if not remain:
            return True
        i, j = remain.popleft()
        for k in range(1, 10):
            k = str(k)
            if k not in rows[i] and k not in cols[j] and k not in blocks[(i//3, j//3)]:
                rows[i].add(k)
                cols[j].add(k)
                blocks[(i//3, j//3)].add(k)
                board[i][j] = k
                if self.dfs(board, rows, cols, blocks, remain):
                    return True
                rows[i].remove(k)
                cols[j].remove(k)
                blocks[(i//3, j//3)].remove(k)
                board[i][j] = "."
        remain.appendleft((i, j))
        return False



# 重寫第五次, time complexity O(9!)^9, space complexity O(81)
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        row, col, block, remain = defaultdict(set), defaultdict(set), defaultdict(set), []
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    row[i].add(val)
                    col[j].add(val)
                    block[(i//3, j//3)].add(val)
                else:
                    remain.append((i, j))
        def dfs():
            if not remain:
                return True
            i, j = remain.pop()
            for val in range(1, 10):
                val = str(val)
                if val not in row[i] and val not in col[j] and val not in block[(i//3, j//3)]:
                    board[i][j] = val
                    row[i].add(val)
                    col[j].add(val)
                    block[(i//3, j//3)].add(val)
                    if dfs():
                        return True
                    board[i][j] = "."
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i//3, j//3)].remove(val)
            remain.append((i, j))
            return False
        dfs()










from collections import defaultdict, deque
class Solution:
    def solveSudoku(self, board):
        rows, cols, triples, visit = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])  #triples[(r // 3, c // 3)] 分成9宮格
                else:
                    visit.append((r, c))
        
        self.dfs(board, rows, cols, triples, visit) #因為一定有解, 所以是true, 但我們已不在意, 只是希望它執行dfs而已

    def dfs(self, board, rows, cols, triples, visit):
            if not visit: #沒有"."
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig  #修改global variable
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft() #拿掉一個 "."
                    if self.dfs(board, rows, cols, triples, visit):
                        return True
                    else: #恢復原狀
                        board[r][c] = "."
                        rows[r].discard(dig) #也可 rows[r].remove(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c))
            return False