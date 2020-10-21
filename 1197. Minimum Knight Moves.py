'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
'''

# Python greedy + bfs solution, 12ms beats 100%

# I'd like to share my solution here in case someone is interested.

# The basic idea is to make sure the total number of moves required always decrease if we move along the long edge.
# I found the boundary 4 by drawing a graph, then solve the remaining number of steps by BFS.

#刷題用這個, time complexity O((|x| + |y|) // 4) => O(300//4) => O(1)
#思路: 先把四象限轉化成第1象限, greedy 沿著離目標的長邊前進 ex: 例如 x >= y, 往x的方向走2 往 y的方向走1
#前進的途中, 若x, y有一個先變0, 則下次那個方向的前進向量變成反方向, 這樣能保證離目標的距離是最短的, 因為控制該向量離目標距離 <= |1|
#why while x > 4 or y > 4 => 因為在這段區間裡, 利用長邊走2的greedy 可能造成suboptimal solution
#重要: 剩下的步數由bfs來完成, bfs 的八個向量, 若該向量x, y方向都遠離目標, 則跳過該向量
from collections import deque
class Solution(object):
    def minKnightMoves(self, x, y):
        # greedy
        x, y = abs(x), abs(y) #離目標的x, y 距離
        res = 0
        while x > 4 or y > 4: #沿著最大邊走
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1 # if y >= 1 => 避免 y 變成負的, 這樣能保持離目標的最短距離 greedy
            else:
                x -= 1 if x >= 1 else -1
                y -= 2 
            res += 1
        # bfs        
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
        queue = deque([(0, 0)])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x and j == y:
                    return res + steps
                for di, dj in moves:
                    if (x - i) * di > 0 or (y - j) * dj > 0: # x, y 方向 至少有一個方向往目標前進
                        queue.append((i + di, j + dj))
            steps += 1

# Image if we use grid of 3 instead of 4. At greedy step, target (1, 2) we may go from (3,4) to (2,2), then that is not optimal. We should go from (3,4) to (1,2) in optimal. 
# I think it's a bit tricky to prove the correctness. But, in general, I think the boarder of grid of 4 could tolerate our greedy approach only.

#自己重寫, time complexity O(1)
from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                y -= 2
                x -= 1 if x >= 1 else -1
            res += 1
        steps = 0
        queue = deque([(0, 0)])
        direc = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x and j == y:
                    return res + steps
                for d in direc:
                    if (x - i) * d[0] >= 0 or (y - j) * d[1] >= 0:
                        queue.append((i+d[0], j+d[1]))
            steps += 1


# x = 0
# x += 1 if x > 0 else 100
# x
# 100




#naive bfs
from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0)])
        dic = [(1,2),(-1,2),(2,1),(-2,1),(2,-1),(-2,-1),(1,-2),(-1,-2)]
        k = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) == (x, y):
                    return k
                for d in dic:
                    ni, nj = i + d[0], j + d[1]
                    if (ni, nj) not in visited:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
            k += 1