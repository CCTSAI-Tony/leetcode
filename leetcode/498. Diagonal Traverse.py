'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
'''

Simple two step approach:
1- Group numbers according to diagonals. Sum of row+col in same diagonal is same.
2- Reverse numbers in odd diagonals before adding numbers to result list.

#刷題用這個, time complexity O(n^2), space complexity O(n^2)
#思路: 同一個diagonal 上的元素, row+col的值會一樣 => 當作key => 利用這樣的特性建立dict, 左到右, 上到下 一般遍歷 把這些元素放進同一個group
#之後對dic.keys() 做排序 最小的對角線從左上到右下, 依照key 把元素append to res, 觀察後會發現 key % 2 == 0, 在放進res前要reverse
import defaultdict
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        dd = collections.defaultdict(list)
        if not matrix: 
            return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in sorted(dd.keys()):
            if k%2==1: 
                dd[k].reverse()
            result += dd[k]
        return result


#自己重寫, time complexity O(n^2), space complexity O(n^2)
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return None
        dic = defaultdict(list)
        res = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                dic[i+j].append(matrix[i][j])
        
        for k in sorted(dic.keys()):
            if k % 2 == 0:
                dic[k].reverse()
            res += dic[k]
        return res








