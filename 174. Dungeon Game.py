'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room 
and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''
Dungeon 地牢

class Solution:
	def calculateMinimumHP(self, dungeon):
       '''
       :type dungeon: List[List[int]]
       :rtype: int
       '''
       R, C = len(dungeon), len(dungeon[0]) #row, column
       dp = [[0] * C for _ in range(R)] #build up map, list comprehension
       dp[-1][-1] = max(1 - dungeon[-1][-1], 1)# blood must >= 1
       for i in range(R - 2, -1, -1): #reverse, why R-2 because base 0 index and from R-1 row compute
           dp[i][C - 1] = max(dp[i + 1][C - 1] - dungeon[i][C - 1], 1) #建立邊界值 從下往上回朔
       for i in range(C - 2, -1, -1):
           dp[R - 1][i] = max(dp[R - 1][i + 1] - dungeon[R - 1][i], 1)#建立邊界值 從右往左回朔
       
       for i in range(R - 2, -1, -1):
           for j in range(C - 2, -1, -1):
               # if adding health is much larger than health required, set it to 1
               dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1) #選血少的, 看是從右還是從下回朔
       
       return dp[0][0]

'''
After observing the problem, we can find that there is one requirement. knight's health must >= 1. since the goal is to find the minimum health. 
A intuitive thought is to traverse from destination, from each cell compute the minimum health required to enter such cell. 
then back propagate to top will get us muimum health required
'''














