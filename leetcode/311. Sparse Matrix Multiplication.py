'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 

Constraints:

1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100
'''

# Given A and B are sparse matrices, we could use lookup tables to speed up. At the beginining I thought two lookup tables would be necessary. 
# After discussing with @yavinci, I think one lookup table for B would be enough. Surprisingly, 
# it seems like detecting non-zero elements for both A and B on the fly without additional data structures provided the fastest performance on current test set.

# However, I think such fastest performance could due to an imperfect test set we have for OJ right now: there are only 12 test cases. 
# And, for an element B[k, j], it would be detected for non-zero elements several times if we detecting both A and B on the fly, 
# depending on how many i's make elements A[i, k] non-zero. With this point, the additional data structures, like lookup tables, 
# should save our time by focusing on only non-zero elements. If it is not, I am worried the set of OJ test cases probably is not good enough.

# Anyway, I am posting my respective solutions below. Comments are welcome. Thanks @yavinci again for discussing with me.

# Python solution with only one table for B (~196ms):

#刷題用這個, time complexity O(mnl)
#思路: 利用hash table 紀錄B 的 non-zero item, 這樣就能優化iteration, 跳過0的element
#重要觀念: (m, n) x (n, l) => (m, l)
#C[i][j] = sum(A[i][k] * B[k][j] for k in range(len(A[0]))
class Solution(object):
    def multiply(self, A, B):
        if A is None or B is None: 
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.") # (m, n) x (n, l) => (m, l)
        C = [[0 for _ in range(l)] for _ in range(m)] #最後得到的matrix
        tableB = {}
        for k, row in enumerate(B): #record non-zero elements
            tableB[k] = {} #dic 中 dic
            for j, eleB in enumerate(row):
                if eleB: 
                    tableB[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row): #這裡的k 在 A 是 col
                if eleA:
                    for j, eleB in tableB[k].items(): #這裡的k 在 B 是 row
                        C[i][j] += eleA * eleB
        return C


#刷題用這個
#自己重寫, time complexity O(m*n*l), space complexity O(m*l)
from collections import defaultdict
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if n != len(B):
            return None
        C = [[0]*l for _ in range(m)]
        table_B = defaultdict(dict)
        for k in range(len(B)):
            for j in range(len(B[0])):
                if B[k][j]:
                    table_B[k][j] = B[k][j]
                    
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in table_B[k]: #已省略zero elements
                        C[i][j] += A[i][k] * B[k][j]
        return C


# 重寫第二次, time complexity O(mnl), space complexity O(ml)
from collections import defaultdict
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, l = len(mat1), len(mat1[0]), len(mat2[0])
        mat3 = [[0] * l for _ in range(m)]
        mat2_sparce = defaultdict(list)
        for i in range(n):
            for j in range(l):
                if mat2[i][j]:
                    mat2_sparce[i].append(j)
        for i in range(m):
            for j in range(n):
                if mat1[i][j]:
                    for k in mat2_sparce[j]:
                        mat3[i][k] += mat1[i][j] * mat2[j][k]
        return mat3



#naive sparce matrix multiplication, time complexity O(m*n*l), space complexity O(m*l) 沒省略zero elements
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if n != len(B):
            return None
        C = [[0]*l for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in range(l):
                        if B[k][j]:
                            C[i][j] += A[i][k] * B[k][j]
        return C








