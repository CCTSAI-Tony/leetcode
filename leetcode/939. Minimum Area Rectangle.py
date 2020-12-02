'''
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
'''

In order to form a rectangle, you need four points all positioned at 90 degrees to each other.

In this approach, we store all given points in a set.

Then iteratively go through all the points in two loops (x1, y1) and (x2, y2) while checking if (x1, y2) and (x2, y1) are also valid points. If so, we found a rectangle.

We calculate the area of this rectangle. If this area is smaller than the minimum area seen so far, make it the minimum area.

#刷題用這個, time complexity O(n^2)
#思路: 先找尋2個點, (x1, y1), (x2, y2), 若(x1, y2) and (x2, y1) 存在, 則找到符合的rectangles
#注意: if x1 > x2 and y1 > y2: 這句很重要, 不單單是過濾一樣的點, 還過濾重複的組合 (只考慮rectangle 的左下右上這兩點的組合)
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_area = sys.maxsize
        points_table = set((x, y) for x, y in points)
            
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2: 
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 -  x2) * abs(y1 - y2)
                        min_area = min(area, min_area)
                        
        return 0 if min_area == sys.maxsize else min_area


#自己重寫, time complexity O(n^2)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float("inf")
        points_table = set((x,y) for x, y in points)
        
        for (x1, y1) in points:
            for (x2, y2) in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x2-x1) * abs(y2-y1)
                        min_area = min(min_area, area)
        return min_area if min_area != float("inf") else 0


#重寫第二次, time complexity O(n^2), space complexity O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float("inf")
        points_set = set()
        for p in points:
            points_set.add(tuple(p))
        for p1 in points:
            for p2 in points:
                if p1[0] > p2[0] and p1[1] > p2[1]:
                    p3, p4 = (p1[0], p2[1]), (p2[0], p1[1])
                    if p3 in points_set and p4 in points_set:
                        min_area = min(min_area, (p1[0] - p2[0]) * (p1[1] - p2[1]))
        return min_area if min_area != float("inf") else 0








#這個會TLE, time complexity O(n^2*n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float("inf")
        points_table = set((x,y) for x, y in points)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i] #time complexity O(n)
                x2, y2 = points[j]
                if (x1, y2) in points_table and (x2, y1) in points_table:
                    area = abs(x2-x1) * abs(y2-y1)
                    if area:
                        min_area = min(min_area, area)
        return min_area if min_area != float("inf") else 0


