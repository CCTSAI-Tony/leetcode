'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30, because N*N grid
grid[i][j] is either '/', '\', or ' '.
'''

# a = "\\"
# a[0]
# '\\'

# https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find
# Split a cell in to 4 parts like this.
# We give it a number top is 0, right is 1, bottom is 2 left is 3.

# Two adjacent parts in different cells are contiguous regions.
# In case '/', top and left are contiguous, botton and right are contiguous.
# In case '\\', top and right are contiguous, bottom and left are contiguous.
# In case ' ', all 4 parts are contiguous.

# Congratulation.
# Now you have another problem of counting the number of islands.

# DFS will be good enough to solve it.
# As I did in 947.Most Stones Removed with Same Row or Column
# I solve it with union find.

# Good luck and have fun.

# union find, Time Complexity: O(N^2)
# 思路: 每個cell 切成4個parts, top 0, right 1, bottom 2 left 3. (畫交叉線就清楚了)
# 利用union find, 若cell是"/" 代表 0,3 union, 1,2 union, 若cell 是"\" 代表 0,1 union, 2,3 union
# 最後check 總共有幾個disjoint complnents, 就是代表有幾個region
# 注意, 每到新cell時, 記得該cell 0 要與上面cell的 2 union, 該cell 3要與左邊cell 1 union
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.f = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i: #if i => i != 0, 不會index out range
                    self.union((i - 1, j, 2), (i, j, 0)) #上面的 cell 的down 與目前cell的top union
                if j:
                    self.union((i, j - 1, 1), (i, j, 3)) #左邊的 cell 的right 與目前cell的left union
                if grid[i][j] != "/":
                    self.union((i, j, 0), (i, j, 1))
                    self.union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    self.union((i, j, 3), (i, j, 0))
                    self.union((i, j, 1), (i, j, 2))
        return len(set(map(self.find, self.f))) #查看共有幾個不同的components
    

    def find(self, x):
        self.f.setdefault(x, x)
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
        return self.f[x]


    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)


#刷題用這個
#dfs 解法, 似counting the number of islands, time complexity O(n^2 * 4) => O(n^2) => O(N), N: vertex
#思路: 每個cell 切成4個parts, top 0, right 1, bottom 2 left 3. (畫交叉線就清楚了)
#利用dfs 遍歷每個part, 若該part 屬於 0, 1 and 該part所屬cell = "\\", dfs可以往上面cell的2 part與 右邊cell 的 3 part遍歷, 並mark matrix[k] = count, 代表同一個region
#最後回報self.cnt 總共有幾個disjoint region. self.cnt 就是dfs forest, 紀錄裡面有多少dfs tree (regions)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.matrix = [[[0, 0, 0, 0] for j in range(self.n)] for i in range(self.n)]
        self.cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(4):
                    if not self.matrix[i][j][k]: #代表有新的dfs tree, 新的region
                        self.cnt += 1 
                        self.dfs(i, j, k)
        return self.cnt

    def dfs(self, i, j, k):
        if 0 <= i < self.n > j >= 0 and not self.matrix[i][j][k]: #not self.matrix[i][j][k] 代表skip 遍歷過的
            if self.grid[i][j] == "\\":
                if k <= 1:
                    self.matrix[i][j][0] = self.matrix[i][j][1] = self.cnt
                    self.dfs(i - 1, j, 2)
                    self.dfs(i, j + 1, 3)
                else:
                    self.matrix[i][j][2] = self.matrix[i][j][3] = self.cnt
                    self.dfs(i + 1, j, 0)
                    self.dfs(i, j - 1, 1)
            elif self.grid[i][j] == "/":
                if 1 <= k <= 2:
                    self.matrix[i][j][1] = self.matrix[i][j][2] = self.cnt
                    self.dfs(i, j + 1, 3)
                    self.dfs(i + 1, j, 0)
                else:
                    self.matrix[i][j][0] = self.matrix[i][j][3] = self.cnt
                    self.dfs(i - 1, j, 2)
                    self.dfs(i, j - 1, 1)
            else:
                self.matrix[i][j][0] = self.matrix[i][j][1] = self.matrix[i][j][2] = self.matrix[i][j][3] = self.cnt
                self.dfs(i - 1, j, 2)
                self.dfs(i, j + 1, 3)
                self.dfs(i + 1, j, 0)
                self.dfs(i, j - 1, 1)


#自己重寫!
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.matrix = [[[0,0,0,0] for _ in range(self.n)] for _ in range(self.n)]
        self.cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(4):
                    if not self.matrix[i][j][k]:
                        self.cnt += 1
                        self.dfs(i, j, k)
        return self.cnt
    
    
    def dfs(self, i, j, k):
        if 0 <= i < self.n and 0 <= j < self.n and not self.matrix[i][j][k]:
            if self.grid[i][j] == "/":
                if 1 <= k <= 2:
                    self.matrix[i][j][1] = self.matrix[i][j][2] = self.cnt
                    self.dfs(i,j+1,3)
                    self.dfs(i+1,j,0)
                else:
                    self.matrix[i][j][0] = self.matrix[i][j][3] = self.cnt
                    self.dfs(i-1,j,2)
                    self.dfs(i,j-1,1)
            elif self.grid[i][j] == "\\":
                if k <= 1:
                    self.matrix[i][j][0] = self.matrix[i][j][1] = self.cnt
                    self.dfs(i-1,j,2)
                    self.dfs(i,j+1,3)
                else:
                    self.matrix[i][j][2] = self.matrix[i][j][3] = self.cnt
                    self.dfs(i+1,j,0)
                    self.dfs(i,j-1,1)
            else:
                self.matrix[i][j][0] = self.matrix[i][j][1] = self.matrix[i][j][2] = self.matrix[i][j][3] = self.cnt
                self.dfs(i+1,j,0)
                self.dfs(i,j-1,1)
                self.dfs(i-1,j,2)
                self.dfs(i,j+1,3)









