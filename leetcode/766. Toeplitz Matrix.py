'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
'''

#自己想的, time complexity O(m*n) space complexity O(max(m, n)), 但hash table 可能會超過memory limit
#思路: 同一個左上右下對角線的item => i-j 會一樣
from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return False
        Toeplitz = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i-j) in Toeplitz:
                    if matrix[i][j] != Toeplitz[i-j]:
                        return False
                else:
                    Toeplitz[i-j] = matrix[i][j]
        return True


Follow-Up 1 with Explanation and Diagrams => https://leetcode.com/problems/toeplitz-matrix/discuss/516366/Python-Follow-Up-1-with-Explanation-and-Diagrams

Summary
In order to handle the follow-up, we need to rely on the fact that the next element in a diagonal is on the next row in the next column.
We can keep a Deque/LinkedList tracking what value is expected in each row (expected_row).
Evaluate the matrix row by row removing the rightmost element in the deque and adding the current row's first element to the left of the deque.
You can then compare every cell in your expected_row to the current row. The indices will line up.
Initially, the expected row just contains the values from the first row in the matrix.

#自己重寫, 刷題用這個, time complexity O(m*n), space complexity O(row[0]) -> solve follow up 1
#思路: 使用deque 初始獲取第一條row, row1[-1] 並沒有下一個同對角線的item所以我們pop它, 反而pushleft row2[0] => 這樣使得row1[1:] 與matrix的下一行同個對角線的元素都在同一個col裡
#一個一個比較, 比較完一樣pop deque[-1] 加入下一行的row[0]... 直到比對完成
from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return False
        compared = deque(matrix[0])
        for i in range(1, len(matrix)):
            row = matrix[i]
            compared.pop()
            compared.appendleft(row[0])
            for j in range(1, len(row)):
                if compared[j] != row[j]:
                    return False
        return True

For the follow-up 2, we can only load a partial row at one time. We could split the whole matrix vertically into several sub-matrices, 
while each sub-matrix should have one column overlapped. We repeat the same method in follow-up 1 for each sub-matrix.

For example:

[1 2 3 4 5 6 7 8 9 0]              [1 2 3 4]              [4 5 6 7]              [7 8 9 0]
[0 1 2 3 4 5 6 7 8 9]              [0 1 2 3]              [3 4 5 6]              [6 7 8 9]
[1 0 1 2 3 4 5 6 7 8]     -->      [1 0 1 2]       +      [2 3 4 5]       +      [5 6 7 8]
[2 1 0 1 2 3 4 5 6 7]              [2 1 0 1]              [1 2 3 4]              [4 5 6 7]
[3 2 1 0 1 2 3 4 5 6]              [3 2 1 0]              [0 1 2 3]              [3 4 5 6]








