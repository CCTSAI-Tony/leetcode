'''
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, 
compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

 



After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

 

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
'''

python solution with heap


# The idea is that we maintain all the points of the current border in a min heap and always choose the point with the lowest length. 
# This is actually an optimized searching strategy over the trivial brute force method: 
# instead of dfs each point to find the lowest "border" of its connected component, 
# we can always start a search from the lowest border and update the points adjacent to it.

# Time Complexity is O(MN log(MN)), Space Complexity is O(MN)
# 思路: 利用heap 逐一拿出到目前為止borders中最低點, 並依此向四周搜尋比這低且之前沒被搜索過的地方來灌水填平成為新border, 
# 若比border高則無法灌水, 則直接成為新border, 被搜索完的地方都會成為新border之後並不會再被搜索or灌水, 只是灌水不灌水的差別
# 從最低點border開始搜尋可以保證其他border比它高或等高, 可以成功儲水至一樣高度
import heapq    
class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap) #從border的最低點開始搜尋, 因為若從不是最低點的地方開始, 水會從較低點的地方流出, 這個觀念很重要
            for (x, y) in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):  #上下左右
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:  #在邊界內且沒被探索過
                    result += max(0, height-heightMap[x][y])  #比邊界低的才能存水
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))  #若比邊界高則成為新邊界,不然舊邊界高度沿用
                    visited[x][y] = 1  #登記已搜索
        return result


# Thank you for your nice solution, in fact the idea is the same as the two pointer solution of Trapping Rain Water I, 
# the difference is that in a 1-D array, there are always two pointers to choose from and we only need to compare two pointers to know when to stop, 
# but in a 2-D array, we have more candidate pointers to choose from, so a heap can help us, 
# and a visited set can help us exclude visited points and check when to stop.












