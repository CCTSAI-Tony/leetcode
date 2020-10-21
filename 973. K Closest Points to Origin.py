'''
We have a list of points on the plane.平面  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.) 歐幾里德的

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''

# Easy to read Python min heap solution 

# We keep a min heap of size K.
# For each item, we insert an item to our heap.
# If inserting an item makes heap size larger than k, then we immediately pop an item after inserting ( heappushpop ).

# Runtime:
# Inserting an item to a heap of size k take O(logK) time.
# And we do this for each item points.
# So runtime is O(N * logK) where N is the length of points.

# Space: O(K) for our heap.

#刷題用這個, time complexity O(N * logK) where N is the length of points.
#思路: 利用heapq, 數學公式 a與b的距離 = ((x1-x2)**2+(y1-y2)**2)**0.5, 使用max heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)  #trick, 乘一個負號 使得distance 比較大的堆積在前面, 這樣之後heappushpop 就會被擠出來
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

#return [(x,y) for (dist,x, y) in heap] 在leetcode眼裏 == [[x,y],[x1,y2]...]

# I found it interesting that my solution ran much faster than "Divide And Conquer" solution under "Solution" tab which is supposed to run in O(N).
# Mine ran at 316ms while D&C solution ran at 536 ms.

# I am guessing that the D&C solution ran much slower than mine because it used recursions which would involved creating callstacks.

#這個方法最直覺
Sort the distance, O(nlogn); O(n)

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda p: p[0]**2 + p[1] ** 2)
        return points[:K]



#這個方法不難懂, 但太麻煩了 思路: 大問題切成小問題 
divide and conquer, avg O(n), worst (n^2); O(n), can be further reduced using in-place

class Solution(object):
    def kClosest(self, points, K):
        def findK(Points, K):
            if K == 0:
                return []
            if len(Points) <= K:
                return [p[1] for p in Points]

            pivot, left, right = Points[0], [], []
            for p in Points:
                if p[0] > pivot[0]:
                    right.append(p)
                elif p[0] < pivot[0]:
                    left.append(p)
            
            if len(left) >= K:
                return findK(left, K)
            else:
                return [l[1] for l in left] + [pivot[1]] + findK(right, K - 1 - len(left))
            
        Points = [[p[0]**2 + p[1]**2, p] for p in points]
        return findK(Points, K)
















