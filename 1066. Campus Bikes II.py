'''
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 

Example 1:



Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
Example 2:



Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
 

Note:

0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 10
'''


# I passed a boolean list into my dfs method, where "0" means the bike is available for other users, and "1" means occupied.

#自己重寫 Python DFS with  memorization, "Time Complexy: O(A(m取n)), n is number of workers, m is number of bikes".
#思路: 利用第幾個工人 與當下bikes 的 array 狀態選擇配對 當作dp的特徵值, 可以發現有重複子問題=> 使用top down memo dp
#dp 關係式: temp = min(temp, self.helper(workers[p], bikes[i])+ self.dfs(p+1, array[:i]+[1]+array[i+1:], workers, bikes, memo))
#技巧: 使用tuple(array) 當作dict的key


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        memo = {}
        array = [0]*len(bikes)
        return self.dfs(0, array, workers, bikes, memo)
    
    def dfs(self, p, array, workers, bikes, memo):
        if (p, tuple(array)) in memo:
            return memo[(p, tuple(array))]
        if p == len(workers):
            return 0
        temp = float("inf")
        for i in range(len(array)):
            if array[i] == 0:
                temp = min(temp, self.helper(workers[p], bikes[i])+ self.dfs(p+1, array[:i]+[1]+array[i+1:], workers, bikes, memo))
        memo[(p, tuple(array))] = temp
        return temp
            
    def helper(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1] - b[1])


#lru cache 版本
from functools import lru_cache
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.bikes = bikes
        self.workers = workers
        array = [0]*len(bikes)
        return self.dfs(0, tuple(array))
    @lru_cache(None)    
    def dfs(self, p, array):
        if p == len(self.workers):
            return 0
        temp = float("inf")
        for i in range(len(array)):
            if array[i] == 0:
                temp = min(temp, self.helper(self.workers[p], self.bikes[i])+ self.dfs(p+1, array[:i]+(1,)+array[i+1:]))
        return temp
            
    def helper(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1] - b[1])














