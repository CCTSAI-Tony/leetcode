'''
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, 
so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 



 

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. 
Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.

'''

#刷題用這個, time complexity O(K*n^2)
#思路: 每一步都是1/8的機率, 若該步出界, 出借機率 += 該步機率, => return 1 - outboard possibility => on board possibility
#技巧, 使用bfs 搭配 memo 來儲存每步的機率
from collections import defaultdict
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # O(K*n^2) worst case, keep adding the probability of getting out of the board.
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        memo, out_board_p = {(r, c): 1}, 0
        # for each step we will create a new dict to record the onboard coordinates and their probabilities.
        for step in range(K):
            next_memo = defaultdict(int)
            for (i, j), prob in memo.items():
                for d in moves:
                    di, dj = i+d[0], j+d[1]
                    # if the next step is on the board, we record it for next step's calculation
                    if 0<=di<N and 0<=dj<N:
                        next_memo[(di,dj)] += prob * 0.125
                    # if the next step is not on the board, we sum it to our accumulate probability of out-board.
                    else:
                        out_board_p += prob * 0.125
            memo = next_memo
        # the on-board prob = 1 - the accumulate out board prob
        return 1-out_board_p




