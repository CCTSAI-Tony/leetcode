'''
Find the total area covered by two rectilinear rectangles in a 2D plane. (rectilinear 用直線圍著的)

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
'''


## Basic Ideas: 簡單數學原理
##     width: min(C,G)-max(A,E) 只看x值
##     height: min(D, H)-max(B,F) 只看y值
##
##     If width or height is not positive, they won't overlap
##
## Complexity: Time O(1), Space O(1)
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = abs(C-A)*abs(B-D)
        area2 = abs(E-G)*abs(F-H)
        w = min(C,G)-max(A,E)
        h = min(D, H)-max(B,F)
        if w<=0 or h<=0:
            return area1 + area2
        else:
            return area1 + area2 - w*h