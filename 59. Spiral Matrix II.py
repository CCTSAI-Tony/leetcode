class Solution:
    def generateMatrix(self, n):
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)] #生出 n x n matrix 
        left, right, top, down, num = 0, n-1, 0, n-1, 1
        while left <= right and top <= down:
            for i in range(left, right+1):
                res[top][i] = num 
                num += 1
            top += 1 #過一螺旋 top往下內縮一格w
            for i in range(top, down+1):
                res[i][right] = num
                num += 1
            right -= 1 #過一螺旋 right往左內縮一格
            for i in range(right, left-1, -1): #r記得倒退
                res[down][i] = num
                num += 1
            down -= 1 #過一螺旋 down往上內縮一格
            for i in range(down, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1 #過一螺旋 left往右內縮一格
        return res

        '''
        b = Solution()
        b.generateMatrix(5)

         [[1, 2,  3,  4,  5],
         [16, 17, 18, 19, 6],
         [15, 24, 25, 20, 7],
         [14, 23, 22, 21, 8],
         [13, 12, 11, 10, 9]]




        '''