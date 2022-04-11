'''
You are given an array points containing the coordinates of points on a 2D plane, 
sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 

Constraints:

2 <= points.length <= 105
points[i].length == 2
-108 <= xi, yi <= 108
0 <= k <= 2 * 108
xi < xj for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
'''

# Explanation
# Because xi < xj,
# yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

# So for each pair of (xj, yj),
# we have xj + yj, and we only need to find out the maximum yi - xi.
# To find out the maximum element in a sliding window,
# we can use priority queue or stack.


# Solution 1: Priority Queue
# Time O(NlogN)
# Space O(N)

# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 使用priority queue 來做題, 重要: put (x - y, x) into heap, 為什麼不是 (y - x, x), 因為想讓大的 y - x 被放在前面
# 若小的被放在前面, 大的有可能遺留在heap 中, 來不及被相同點比較 就移動下個點 然後就被下個點排除
# 又因為 yi - xi 越大越好, xi 越小的放前面越好
import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        res = -float('inf')
        for x, y in points:
            while q and x - q[0][1] > k:
                heapq.heappop(q)
            if q: 
                res = max(res, -q[0][0] + y + x)
            heapq.heappush(q, (x - y, x))  # why x - y, cause we want max (yi - xi) to be put in the front
        return res


# 重寫第二次, time complexity O(nlogn), space complexity O(n)
import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = float("-inf")
        heap = []
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                ans = max(ans, x + y - heap[0][0])
            heapq.heappush(heap, ((x - y), x))
        return ans




