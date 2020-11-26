'''
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary 
in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
'''
# https://buptwc.com/2018/07/19/Leetcode-576-Out-of-Boundary-Paths/

'''
这道题乍一看很像一个标准的bfs，因为限定最多只能移动N次，我们只要bfs依次遍历发现出界就+1，当bfs的深度大于N的时候break。当然理论上是没有任何问题的，
确实能得出正确答案，但是这里N的取值范围达到了50，我们对任意一个点bfs有四个方向（可以走回头路），那么复杂度达到了4^N，显然会超时。当然我会在文章后面给出bfs的做法，
毕竟这是可以处理N比较小的情况的解法，让大家更熟悉bfs的套路。
我不知道你们有没有这种感觉，一般看到这个mod 1e9+7，这道题8成就是dp了，而且就是那种每个dp值你都得mod一下再去进行运算的那种。我觉得这算一个小技巧吧，看到mod 1e9+7就要想到dp。
显然，这里dp很好定义，我们定义dp[(i,j,N)]表示从i,j出发，最多走N步情况下满足题意的路径数量，那么我们所求也就是dp[(i,j,N)]。根据我们上面说的bfs的思路，递推式可得：
dp[(i,j,N)] = dp[(i+1,j,N-1)] + dp[(i-1,j,N-1)] + dp[(i,j+1,N-1)] + dp[(i,j-1,N-1)]
思路：

处理好边界情况：
当i,j仍然在网格内时，如果N=0，说明这条路走不出去,dp[(i,j,N)] = 0
当i,j仍然在网格内时，如果N>0，如递推式
当i,j在网格外时，说明已经走出去，dp[(i,j,N)] = 1
这里我为了方便代码书写就用的记忆化的形式，用一个cache来存储已经计算过的结果
'''

#自己重寫 time complexity: O(m*n*N), 刷題用這個
#思路: 典型 top down memo 題, 多一個參數N, 導致subproblem => dp[(i,j,N)] = dp[(i+1,j,N-1)] + dp[(i-1,j,N-1)] + dp[(i,j+1,N-1)] + dp[(i,j-1,N-1)]
#利用memo 來紀錄重複子問題, base condition=> 若i, j在格子外 return 1, 若在格子內但 N=0 return 0, else 往四方向擴散 N-1
#記得retrun 要mod 10**9 + 7
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0:
            return 0
        mod = 10**9 + 7
        memo = {}
        return self.dfs(m, n, i, j, N, memo) % mod
    
    
    def dfs(self, m, n, i, j, N, memo):
        if (i, j, N) in memo:
            return memo[(i, j, N)]
        elif 0 <= i < m and 0 <= j < n:
            if N == 0:
                return 0
            memo[(i, j, N)] = \
            self.dfs(m, n, i+1, j, N-1, memo) + \
            self.dfs(m, n, i-1, j, N-1, memo) + \
            self.dfs(m, n, i, j+1, N-1, memo) + \
            self.dfs(m, n, i, j-1, N-1, memo)
            return memo[(i, j, N)]
        else:
            return 1


# At time t, let's maintain cur[r][c] = the number of paths to (r, c) with t moves, and nxt[r][c] = the number of paths to (r, c) with t+1 moves.
# A ball at (r, c) at time t, can move in one of four directions. If it stays on the board, then it contributes to a path that takes t+1 moves. 
# If it falls off the board, then it contributes to the final answer.

#dp bottom up, time complexity O(m*n*N)
#思路: at step n, cur[i][j] 代表目前走到r,c with n 步的總共走法, nxt[x][y] 代表走到x,y with n+1 步的總共走法
#當i, j 的下一步走出格子外, 直接把目前到i,j 的走法加到ans, else 加到nxt[x][y]
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0:
            return 0
        mode = 10**9 + 7
        ans = 0
        nxt = [[0] * n for _ in range(m)]
        nxt[i][j] = 1
        for step in range(N): #可以走n步
            cur = nxt
            nxt = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for (x, y) in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                        if 0 <= x < m and 0 <= y < n:
                            nxt[x][y] += cur[i][j]
                        else:
                            ans += cur[i][j]
        return ans % mode


# 多了step 參數 => 狀態方程變為 (i, j, step)
import collections
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10**9 + 7
        cache = collections.defaultdict(int)
        return self.helper(i, j, m, n, N, cache) % mod


    def helper(self, i, j, m, n, N, cache):
        # 记忆化思想
        if (i,j,N) in cache:
            return cache[(i,j,N)]
        #i,j在网格内情况
        if 0<=i<m and 0<=j<n:
            if N == 0:
                cache[(i,j,N)] = 0
                return cache[(i,j,N)]

            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                cache[(i,j,N)] += self.helper(x,y,m,n,N-1,cache)
            return cache[(i,j,N)]
        # 网格外情况
        else:
            cache[(i,j,N)] = 1
            return cache[(i,j,N)]


# 下面是bfs代码，在这道题中tle
import collections
class Solution:
    def findPaths(m,n,N,i,j):
        mod = 10**9 + 7
        Q = collections.deque([(i,j,0)])
        res = 0
        while Q:
            x,y,step = Q.popleft()
            if step > N: 
                break
            if 0<=x<m and 0<=y<n:
                Q.append((x+1,y,step+1))
                Q.append((x-1,y,step+1))
                Q.append((x,y+1,step+1))
                Q.append((x,y-1,step+1))
            else:
                res += 1
        return res % mod








