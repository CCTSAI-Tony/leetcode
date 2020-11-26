# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

#time complexity O(m*n)
#思路: 首先pop最上一排, 接下來從上到下pop每行最後一個, 再來pop最下一行並reverse, 再來從下到上pop第一個元素, 以上為1循環
#注意避免pop from empty list, 若pop行, 要 if matrix 確保至少有empty row 給你pop, 若要pop每行裡面的元素, 要if matrix and matrix[0], 確保每行裡面有元素給你pop
class Solution(object):
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0) #取得第一排 
            if matrix and matrix[0]: #matrix[0] The intention is probably to ensure pop() is not applied when the matrix is empty  重要！ 雙重保險！
                for row in matrix:
                    ret.append(row.pop()) #依序取得最右邊一排
            if matrix:
                ret += matrix.pop()[::-1] #取得最下面一排從右到左
            if matrix and matrix[0]:
                for row in matrix[::-1]: #從下到上
                    ret.append(row.pop(0)) #依序取得最左邊一排  >若matrix還在 回到while頂 從頭執行 
        return ret

        '''
# matrix[0] 確保row 裡面有東西可以pop(), if matrix 確保裡面有row, ex: [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
a = [4]
a += []
a
[4]






        首先matrix.pop(0) 取得第一排
        
        A = [[5,6,7,8]]
        A.pop()[::-1]
        [8, 7, 6, 5]





        A = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
            [13,14,15,16]
            ]

            A.pop(0) >[1, 2, 3, 4]

            A
            [[5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]





        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
             

        a = [1,2,3]
        while a:
            if a[0]==1:
                a.append(4)
            if a[1]==2:
                a.append(5)
            if a[2]==3:
                a.append(6)
            print(a)
            break

        [1, 2, 3, 4, 5, 6]

        說明 code if stament 從上執行到下














            '''