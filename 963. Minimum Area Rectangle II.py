'''
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
'''

# Dot product of two sides in a rectangle should be zero because a . b = |a| |b| cos(90)
# If we can extend p3 by the same margin delta(p2 - p1), we can have the fourth point p4.
# x4 = x3 + (x2 - x1)
# y4 = y3 + (y2 - y1)
# If p4 in points, calculate area.

#刷題用這個, time complexity O(n^3) -> 破題 => 找出rectangle 的三點湊成一個直角
#思路: x1, x2, x3 最多可以形成兩個邊, 若這兩個邊內積 = 0, 代表找到直角, 利用這個關係, 可以推估第四點, 若第四點有在points, 可以計算面積
#1 > 2, 1 > 3, 再用1 > 2 之間的關係 => 推估 第四點
#find x1, x2, x3 combination => use remain iterate
#內積公式 => 兩個向量內積公式 => a = (x1, y1), b = (x2, y2) => a . b => x1*x2 + y1*y2, x向量*x向量 + y向量*y向量
#技巧: 把points 轉成 set, 之後搜尋只要O(1)
class Solution:
    def minAreaFreeRect(self, points):
        mn, st, n = float('inf'), {(x, y) for x, y in points}, len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in st:
                        mn = min(mn, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5) #畢氏定理
        return mn if mn < float("inf") else 0


#自己重寫, 刷題用這個 time complexity O(n^3), space complexity O(1)
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        st = {(x, y) for x, y in points}
        min_area = float("inf")
        for i in range(len(points)):
            x1, y1 = points[i] #list index => O(1)
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                for k in range(j+1, len(points)):
                    x3, y3 = points[k]
                    x4, y4 = (x3 + (x2-x1)), (y3 + (y2-y1))
                    if not (x2-x1)*(x3-x1) + (y2-y1)*(y3-y1) and (x4, y4) in st:
                        min_area = min(min_area, ((x2-x1)**2+(y2-y1)**2)**0.5 *((x3-x1)**2+(y3-y1)**2)**0.5)
        return min_area if min_area != float("inf") else 0


