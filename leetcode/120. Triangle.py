'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''
# O(n*n/2) space, top-down 
class Solution:
    def minimumTotal1(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in range(len(row))] for row in triangle] #建立table
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)): #row
            for j in range(len(triangle[i])): #column
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j] #最左邊路徑
                elif j == len(triangle[i])-1: #最右邊路徑
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j] #上排左右選最小
        return min(res[-1]) #最後一排選最小
'''
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
res = [[0 for i in range(len(row))] for row in triangle]
res
[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]

'''
# Modify the original triangle, top-down @@modify inplace
class Solution:
    def minimumTotal2(self, triangle):
        if not triangle:
            return 
        for i in range(1, len(triangle)): #row
            for j in range(len(triangle[i])): #col
                if j == 0:
                    triangle[i][j] += triangle[i-1][j] #最左邊路徑
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1] #最右邊路徑
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

# Modify the original triangle, bottom-up
class Solution:
    def minimumTotal3(self, triangle):
        if not triangle:
            return 
        for i in range(len(triangle)-2, -1, -1): #for i in range(4-2, -1, -1): > 2,1,0 扣除最後一排
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]) #從下往上加
        return triangle[0][0] 

# bottom-up, O(n) space
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = triangle[-1] #最後一排 [4,1,8,3]
        for i in range(len(triangle)-2, -1, -1): #2,1,0r
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j] # res[2] res[1] res[0]
        return res[0]











