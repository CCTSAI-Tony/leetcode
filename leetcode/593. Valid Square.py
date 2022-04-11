'''
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
 

Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104
'''

'''
The idea is to calculate all the distance between each two points, and sort them. 
In this way, we get 4 edges and 2 diagonals of the square in order. 
If the 4 edges equal to each other, that means it should be equilateral parallelogram. 
Finally, we check whether the 2 diagonals equal to each other so as to check if it's a square.
'''
# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 計算每個edge, square 包含四個相等邊長加兩個相等長度對角線
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p3 == p4:
            return False
        def cal_dis(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        l0, l1, l2= cal_dis(p1, p2), cal_dis(p1, p3), cal_dis(p1, p4)
        l3, l4, l5= cal_dis(p2, p3), cal_dis(p2, p4), cal_dis(p3, p4)
        edges = sorted([l0, l1, l2, l3, l4, l5])
        if edges[0] == edges[1] == edges[2] == edges[3] and edges[4] == edges[5]:
            return True
        return False



