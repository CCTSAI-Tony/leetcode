'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

#刷題用這個, time complexity O(n^2)
#思路: 點在同一條線上, y = ax + b 必要符合, 可以不使用np
import numpy as np
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: #兩點必成一直線dss
            return len(points)
        res = 0
        count = collections.defaultdict(set) #用set是避免重複
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                slope, intercept = self.getSlopeAndIntercept(points[i], points[j])
                count[(slope, intercept)].add(i)
                count[(slope, intercept)].add(j)
                res = max(res, len(count[(slope, intercept)])) #動態更新最大值
        return res
    
    
    def getSlopeAndIntercept(self, p1, p2): #這裡的截距是y = ax + b 的 b    相同 a,b 就是在同一條線
        x1, y1 = p1
        x2, y2 = p2
        if x2 == x1: # vertical slope
            return float('inf'), x1
        slope = (y2 - y1) * np.longdouble(1) / (x2 - x1) #利用np.longdouble 提高精確度
        intercept = y2 - slope * x2
        return slope, intercept


# 重寫第二次, time complexity O(n^2), space complexity O(n)
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 1
        lines = defaultdict(set)
        for i in range(len(points)):
            for j in range(1, len(points)):
                slope, intercept = self.check_slope(points[i], points[j])
                lines[(slope, intercept)].add(i)
                lines[(slope, intercept)].add(j)
        return max(len(lines[key]) for key in lines)
        
    def check_slope(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if (x2 - x1) == 0:
            return float("inf"), x1
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return slope, intercept

# 重寫第三次, time complexity O(n^2), space complexity O(n)
# n 個點, 最多只有n-1條線
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        lines = defaultdict(set)
        for i in range(len(points)):
            for j in range(1, len(points)):
                self.check_lines(points[i], points[j], lines)
        return max([len(points) for line, points in lines.items()])
                
        
    def check_lines(self, p1, p2, lines):
        x1, y1 = p1
        x2, y2 = p2
        slope, intercept = 0, 0
        if x1 == x2:
            slope = float("inf")
            intercept = x1
        else:
            slope = (y2-y1)/(x2-x1)
            intercept = y2 - slope * x2
        lines[(slope, intercept)].add((x1, y1))
        lines[(slope, intercept)].add((x2, y2))




算點
count = collections.defaultdict(set)
count[(5,2)].add(3)
count
defaultdict(set, {(5, 2): {3}})
count[(5,2)].add(3)
count
defaultdict(set, {(5, 2): {3}})
'''
The gotcha in this problem is that Python has a problem with accuracy when dealing with division to calculate slope.
The workaround was to borrow longdouble(...) from numpy module.

Time complexity: O(N^2)
Space complexity: O(N^2)

截距

y = mx + b 
把x2,y2 代進去 y2 = slope*x2 +b, b = y2 - slope * x2


Extended Precision
Python’s floating-point numbers are usually 64-bit floating-point numbers, nearly equivalent to np.float64. 
In some unusual situations it may be useful to use floating-point numbers with more precision. 
Whether this is possible in numpy depends on the hardware and on the development environment: 
specifically, x86 machines provide hardware floating-point with 80-bit precision, and while most C compilers provide this as their long double type, 
MSVC (standard for Windows builds) makes long double identical to double (64 bits). NumPy makes the compiler’s long double available as np.longdouble 
(and np.clongdouble for the complex numbers). You can find out what your numpy provides with np.finfo(np.longdouble).

NumPy does not provide a dtype with more precision than C long doubles; in particular, the 128-bit IEEE quad precision data type (FORTRAN’s REAL*16) is not available.

For efficient memory alignment, np.longdouble is usually stored padded with zero bits, either to 96 or 128 bits. 
Which is more efficient depends on hardware and development environment; typically on 32-bit systems they are padded to 96 bits, 
while on 64-bit systems they are typically padded to 128 bits. np.longdouble is padded to the system default; 
np.float96 and np.float128 are provided for users who want specific padding. In spite of the names, np.float96 
and np.float128 provide only as much precision as np.longdouble, that is, 80 bits on most x86 machines and 64 bits in standard Windows builds.

Be warned that even if np.longdouble offers more precision than python float, it is easy to lose that extra precision, 
since python often forces values to pass through float. For example, the % formatting operator requires its arguments to be converted to standard python types, 
and it is therefore impossible to preserve extended precision even if many decimal places are requested. 
It can be useful to test your code with the value 1 + np.finfo(np.longdouble).eps.

a = 0.1
b = 0.2
a+b
0.30000000000000004

a = np.longdouble(0.1)
b = np.longdouble(0.2)
a+b
0.30000000000000001665











'''









