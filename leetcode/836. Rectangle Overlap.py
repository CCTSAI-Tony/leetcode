'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, 
and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
 

Constraints:

rect1.length == 4
rect2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1[0] <= rec1[2] and rec1[1] <= rec1[3]
rec2[0] <= rec2[2] and rec2[1] <= rec2[3]
'''

O(1)
Space: O(n)
Algorithm: compute the overlap area similar to LC 223 and return True only if both width and height are positive numbers, which indicates there is an overlap.
#刷題用這個, time complexity O(1), space complexity O(1)
#思路: 若有重疊, min(兩個矩型右邊or 上邊) - max(兩個矩型左邊or 下邊) 要 > 0
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
	        width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
	        height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
	        return True if width > 0 and height > 0 else False


#重寫第二次, time complexity O(1)
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return True if width > 0 and height > 0 else False



