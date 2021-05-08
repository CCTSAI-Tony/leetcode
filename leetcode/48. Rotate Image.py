# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:

# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# Transpose the matrix and reverse each row.
# 思路: 這題要靠一下想像力, 轉置矩正, 再針對每行reverse, 就是順時90度
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j: #很重要, 少了這一行, 一切都沒變, 因為遇到i,j 調換一次 遇到 j, i 又調換回來
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:
            l.reverse() #不能l = l[::-1] 因為這樣只代表l 指向一個新的reverse l list而已, 並沒有修改原data


#重寫第二次, time complexity O(n^2), space complexity O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

#重寫第三次, time complexity O(n^2), space complexity O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()





# t = a = [1,2,3,4]
# a = a[::-1]
# a[0] = 100
# t
# [1, 2, 3, 4]
# a
# [100, 3, 2, 1]

 


#Most Direct - 52 ms
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]


~ 	NOT	Inverts all the bits
#singed integer => 0變1, 1變0
~0 => -1, ~1 => -2, ~2 => -3

'''
It walks over the "top-left quadrant" of the matrix and directly rotates each element 
with the three corresponding elements in the other three quadrants.
'''














#Most Pythonic - [::-1] and zip - 44 ms
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])



#List Comprehension - 60 ms

class Solution:
    def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]  #double list comprehensions


        '''
        You are given an n x n 2D matrix representing an image.

		Rotate the image by 90 degrees (clockwise).


        A=[
		[1,2,3],
		[4,5,6],
		[7,8,9]
		]

		A[::-1]=
		[7,8,9],
		[4,5,6],
		[1,2,3]
		]

		A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))] list comprehension!!

		741
		852
		963

		A 90 degrees (clockwise)
		[7,4,1],
		[8,5,2],
		[9,6,3]
		]

        len(A) =3 
        
        The tilde operator in Python
        i  ~i  
		0  -1
		1  -2
		2  -3
		3  -4 
		4  -5 
		5  -6
        
        [
		  [15,13, 2, 5],
		  [14, 3, 4, 1],
		  [12, 6, 8, 9],
		  [16, 7,10,11]
		]








		'''