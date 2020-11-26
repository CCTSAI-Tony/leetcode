'''
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
'''

import bisect
import sys


class Solution:
    
    # Overall complexity O(n^4)
    def maxSumSubmatrix(self, matrix, k):

        # Validation for corner case.
        if not matrix:
            return 0

        # Traditional kadane algorithm does not work https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        # here, as that algorithm always finds max sum
        # in a sub array and disregards intermediate sums
        # which needs to be considered for evaluating <=k criteria. 
        #
        # Below function stores prefix sum values
        # in a sorted list and performs binary 
        # search on this list to get the closest
        # element whose difference with current element
        # does not exceed k. 
        # Complexity for this algorithm is O(n^2)
        def max_sum_array_no_larger_than_k(l, k):  #想像k=5 l = [1,-1,2,4,5]  prefix_sums = [0]->[0,1]->[0,0,1]->[0,0,1,2]->[0,0,1,2,6]->[0,0,1,2,6,11]
            prefix_sums = [0]
            prefix_sum, max_sum = 0, -sys.maxsize  #這邊max_sum 為何還要重新定義成-sys.maxsize, 因為不想受到外部max_sum 已改變的影響
            for item in l:
                prefix_sum += item
                
                left = bisect.bisect_left(prefix_sums, prefix_sum - k)  
                if left < len(prefix_sums):
                    max_sum = max(max_sum, prefix_sum - prefix_sums[left])  #注意此時的prefix_sums[left] 還是原序列的元素

            # left = bisect.bisect_left(prefix_sums, prefix_sum - k) and if left < len(prefix_sums): 
            #這是用來確保目前從頭累加的prefix_sum 在prefix_sums裡有元素 前者減後者 <=k, ex k=5 l = [1,-1,2,100,5]

            # prefix_sum - prefix_sums[left] 可以理解為從某個col開始到某個col結束累加的值

            # prefix_sum - k 代表差值, 看在prefix_sums array 有沒有元素能被這差值相減得到的結果 <= 0, 若沒有則代表到目前累加的prefix_sum沒有機會不超過k

               # This has a worst case complexity of O(n) 
                bisect.insort(prefix_sums, prefix_sum)  #插入prefix_sum(從頭累加的)
            return max_sum

        row_len = len(matrix)
        col_len = len(matrix[0])
        max_sum = -sys.maxsize
        
        # Below loops basically fold 2-d array into 
        # a single dimensional array, so that above 
        # function can be applied to it.
        # Here we iterate through all possible 2-d
        # arrays possible for every column. 
        for from_col in range(col_len):  #不難想, 想像一個矩正,每一條col都是一個長方形
            col_values = [0 for _ in range(row_len)]  #col_values 每一個元素代表那一行, 每次從新的from_col 開始, col_values歸0
            for to_col in range(from_col, col_len):
                for row in range(row_len):
                    col_values[row] = col_values[row] + matrix[row][to_col]
                curr_sum = max_sum_array_no_larger_than_k(col_values, k)  #轉換成1D array 問題,max subarray sum no more than k.
                max_sum = max(curr_sum, max_sum)
        return max_sum


# One minor thing about the time complexity: I might be wrong 
# but I think the complexity of max_sum_array_no_larger_than_k should be O(n^2) since insort, being an O(n) function

# Python can handle arbitrarily large integers in computation. Any integer too big to fit in 64 bits 
# (or whatever the underlying hardware limit is) is handled in software. For that reason, Python 3 doesn't have a sys.maxint constant.

# The value sys.maxsize, on the other hand, reports the platform's pointer size, and that limits the size of Python's data structures such as strings and lists.

# import sys
# -sys.maxsize
# -9223372036854775807








import bisect
import sys


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix:
            return 0


        def max_sum_array_no_larger_than_k(l, k):
            prefix_sums = [0]
            prefix_sum, max_sum = 0, -sys.maxsize
            for item in l:
                prefix_sum += item
                
                left = bisect.bisect_left(prefix_sums, prefix_sum - k)
                if left < len(prefix_sums):
                    max_sum = max(max_sum, prefix_sum - prefix_sums[left])


                bisect.insort(prefix_sums, prefix_sum)
            return max_sum

        row_len = len(matrix)
        col_len = len(matrix[0])
        max_sum = -sys.maxsize


        for from_col in range(col_len):
            col_values = [0 for _ in range(row_len)]
            for to_col in range(from_col, col_len):
                for row in range(row_len):
                    col_values[row] = col_values[row] + matrix[row][to_col]
                curr_sum = max_sum_array_no_larger_than_k(col_values, k)
                max_sum = max(curr_sum, max_sum)
        return max_sum



# import bisect 
# li1 = [1, 3, 4, 4, 4, 6, 7] 
# li2 = [1, 3, 4, 4, 4, 6, 7]
# li3 = [1, 3, 4, 4, 4, 6, 7] 
# li4 = [1, 3, 4, 4, 4, 6, 7] 

# bisect.insort(li1, 5) 
# for i in range(0, 7): 
#     print(li1[i], end=" ") 

# 1 3 4 4 4 5 6 


# bisect.insort_left(li2, 5) 
# for i in range(0, 7): 
#     print(li2[i], end=" ") 

# 1 3 4 4 4 5 6 

# bisect.insort_right(li3, 5, 0, 4) 
# for i in range(0, 7): 
#     print(li3[i], end=" ") 

# 1 3 4 4 5 4 6 

# bisect.insort_right(li4, 5) 
# for i in range(0, 7): 
#     print(li2[i], end=" ") 

# 1 3 4 4 4 5 6 





































