'''
(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) 
which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, 
including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. 
It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. 
Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example :


Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
Example 2:

Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
Output: 3
 

Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". 
In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000
topRight != bottomLeft
'''

'''
Similar to binary search, however, we need to cut the rectangle into 4 parts as shown in the figure below.
If the quarter area return as false, which means no ship in this area, we can safely return 0
if the quarter area returns as True, we should keep on dividing that area into four parts to further explore.
The base case will be the top and bottom points are the same, then we can get the exact result. 
If It True, we have one ship, if False, we have zero ship.
One subtle thing is in order to have no overlap for these four parts, we need to add a center point by 1 as shown in the figure.
'''


# 刷題用這個, time complexity O(nlogn), space complexity O(logn)
# 思路: 利用divide and conquer 來解題, 矩形能被切成四等份, 利用分治法對個別矩形再做進一步四等份, 直到個別四等份被解出來後, 合起來就是答案
# 技巧: 四等分中心點: center_x, center_y = (x0+x1)//2, (y0+y1)//2
# 切記: sea.hasShips 只是return bool, 因此要用int 來轉換成數字
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def d_c(bottom, top):
            if bottom.x>top.x or bottom.y>top.y:
                return 0
            if (top.x, top.y)  == (bottom.x, bottom.y): # 這行很重要, 矩形縮到只剩一個點    
                return int(sea.hasShips(top, bottom)) 
            else:
                if not sea.hasShips(top, bottom): # 這句重要, 修枝 optimization
                    return 0
                x0, y0 = bottom.x, bottom.y
                x1, y1 = top.x, top.y
                center_x, center_y = (x0+x1)//2, (y0+y1)//2
                f1 = d_c(bottom, Point(center_x, center_y))
                f2 = d_c(Point(center_x+1, center_y+1), top)
                f3 = d_c(Point(x0, center_y+1), Point(center_x, y1))
                f4 = d_c(Point(center_x+1, y0), Point(x1, center_y))
                return f1+f2+f3+f4
        return d_c(bottomLeft, topRight)    


# 重寫第二次, time complexity O(nlogn), space complexity O(logn)
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        return self.devide_and_conquer(sea, topRight, bottomLeft)
        
    def devide_and_conquer(self, sea, top, bottom):
        if top.x < bottom.x or top.y < bottom.y:
            return 0
        if (top.x, top.y) == (bottom.x, bottom.y):
            return int(sea.hasShips(top, bottom))
        if not sea.hasShips(top, bottom):
            return 0
        center_x, center_y = (top.x + bottom.x) // 2, (top.y + bottom.y) // 2
        f1 = self.devide_and_conquer(sea, Point(center_x, center_y), bottom)
        f2 = self.devide_and_conquer(sea, Point(center_x, top.y), Point(bottom.x, center_y + 1))
        f3 = self.devide_and_conquer(sea, top, Point(center_x + 1, center_y + 1))
        f4 = self.devide_and_conquer(sea, Point(top.x, center_y), Point(center_x + 1, bottom.y))
        return f1 + f2 + f3 + f4





