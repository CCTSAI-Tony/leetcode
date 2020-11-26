'''
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point 
which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. 
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. 
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9
'''


The Idea behind this is to
Step 1 :
Get all the trees from a matrix in sorted order.
Step 2 :
Then for every tree let's know how many number of steps it takes from the previous node
(Initially for first tree we will start from (0,0))
If steps < 0 then we are unable to move further due to obstacle so return -1 else add these steps to the totalSteps.
Step 3 :
In order to get steps we use bfs


#自己重寫, time complexity O((mn)^2)
#思路: 除了0不能跨過, 就算還沒砍的樹一樣可以跨, 此題bfs的應用
#先建立所有樹的高度list, 對其高度做排序, 因為從最矮的開始砍, 所以是升序排列, 起始點(0,0) 利用bfs算出到達最矮樹的最小步數, 再從最矮的樹當作下一個起點利用bfs得出到達次矮的樹的最小步數...
#直到所有的樹都bfs遍歷過, 加總每個樹的步數就是total 最小的步數, 記得要避開obstacle, 若bfs無法到達下一個樹, 則return -1 => 無法砍完所有樹
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row, col = len(forest), len(forest[0])
        trees = [forest[x][y] for x in range(row) for y in range(col) if forest[x][y] > 0]
        trees.sort()
        total_steps = 0
        start_point = (0, 0)
        for tree in trees:
            steps, start_point = self.bfs(start_point, tree, forest)
            if steps < 0:
                return -1
            total_steps += steps
        return total_steps
    
    def bfs(self, s_point, target, forest):
        m, n = len(forest), len(forest[0])
        visited = [[False]*n for _ in range(m)]
        queue = deque([s_point])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if forest[i][j] == target:
                    return (steps, (i, j))
                for x, y in [(i+1, j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= x < m and 0 <= y < n and not visited[x][y] and forest[x][y] > 0:
                        visited[x][y] = True
                        queue.append((x,y))
            steps += 1
        return (-1, (None, None))




from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        noOfRows = len(forest)
        noOfColumns = len(forest[0])
        
        #step 1 
        trees = [ (forest[i][j], i, j) for i in range(noOfRows) for j in range(noOfColumns) if forest[i][j] > 1 ]
        trees = sorted(trees)
        
        #Implementation of step 3 BFS   
        x = 0
        y = 0 
        totalSteps = 0 
        
        #step 2 
        for tree in trees :
            steps = self.bfs(x,y,tree[1],tree[2], forest) #step 3 
            if steps < 0 :
                return -1 
            totalSteps += steps 
            x = tree[1] #改變起始位置
            y = tree[2]
            
        return totalSteps 


    def bfs(self,row,col,treeX,treeY, forest) :
        noOfRows, noOfColumns = len(forest), len(forest[0])
        visited = [ [False for j in range(noOfColumns)] for i in range(noOfRows)]
        queue = deque([])
        queue.append( (row,col) )
        steps = 0
        while queue :
            for _ in range(len(queue)):
                currX,currY = queue.popleft()
                if (currX == treeX) and (currY == treeY) :
                    return steps
                for r,c in [ (currX + 1,currY), (currX - 1,currY), (currX,currY + 1), (currX,currY - 1) ] :  
                    if (r >= 0) and (r < noOfRows) and (c >= 0) and (c < noOfColumns) and (not visited[r][c]) and (forest[r][c] > 0) :
                        visited[r][c] = True 
                        queue.append( ( r, c)  )
            steps += 1
        return -1 























