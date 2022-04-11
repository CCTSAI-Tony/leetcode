'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

#自己想的, time complexity O(n*n, k*log(n*n)), 刷題用這個, 最直白
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not (matrix or  matrix[0] ):
            return 0
        
        row , col = len(matrix), len(matrix[0])
        heap = []
        for i in range(row):
            for j in range(col):
                heap.append(matrix[i][j])
        heapq.heapify(heap)
        for _ in range(k):
            ans = heapq.heappop(heap)
        
        return ans



# 1. Binary search (based on the solution from @光速小子) gives me 72 ms.

# The time complexity is O(n * log(n) * log(N)), where N is the search space that ranges from the smallest element to the biggest element. 
# You can argue that int implies N = 2^32, so log(N) is constant. In a way, this is an O(n * log(n)) solution.

# The space complexity is constant.



#這個解法太酷了, 自己重寫, 不能用bisect_left, 因為target有可能存在重複元素, 用bisect_right 才能越過那些重複元素
#time complexity log(max(num)- min(num)) * n*logn, n: len(matrix),
#思路:利用matrix裡最大值與最小值, 計算 mid值 來對各row做bisect, 並sum出index總和是否 == k, 若小於 lo = mid, 一步一步找出kth smallest item
#why bisect.bisect_right, 因為zero index issue, 自己套一下題目例子就知道
#模板2, 注意這題不能 if sum(bisect.bisect_right(row, mid) for row in matrix) == k, 就return mid, 此時mid還不一定在matrix 裡面
import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low + 1 < high:
            mid = low + (high-low) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) >= k: #這邊一定要>= 來收斂target
                high = mid
            else:
                low = mid
        if sum(bisect.bisect_right(row, low) for row in matrix) >= k:
            return low
        return high

# why 一定要>=k, high = mid, 因為這樣才能收斂至target(實際存在於matrix的item), 一旦小於target就必定 sum < k, 
# 若只有 > k, high = mid, 有可能選到比target大但不存在於matrix的元素, ex: [1,2,5] k = 2, bisect_right(list, 4)=> k 也等於2, 
# 一切都是因為bisect_right, 所以要往小收斂


#重寫第二次, time complexity O(n * log(n)), space complexity O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return False
        l, r = matrix[0][0], matrix[-1][-1]
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.helper(mid, matrix) >= k: # >= => 重複的最左邊 
                r = mid
            else:
                l = mid
        if self.helper(l, matrix) >= k:
            return l
        return r
        
        
    def helper(self, val, matrix):
        count = 0
        for row in matrix:
            count += self.binary(val, row)
        return count
    
    def binary(self, val, row): #相當於 bisect right
        l, r = 0, len(row)-1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if row[mid] > val:
                r = mid
            else:
                l = mid
        if row[l] > val:
            return l
        if row[r] > val:
            return r
        return r + 1


# 重寫第三次, time complexity O(n * log(n)), space coplexity O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def helper(num):
            count = 0
            for row in matrix:
                count += binary_search(num, row)
            return count
        
        def binary_search(num, row):
            l, r = 0, len(row) - 1
            while l + 1 < r:
                mid = l + (r - l) // 2
                if row[mid] > num:
                    r = mid
                else:
                    l = mid
            if row[l] > num:
                return l
            elif row[r] > num:
                return r
            else:
                return r + 1
        l, r = matrix[0][0], matrix[-1][-1]
        while l + 1 < r:
            mid = l + (r - l) // 2
            if helper(mid) >= k:
                r = mid
            else:
                l = mid
        if helper(l) >= k:
            return l
        else:
            return r




#why use bisect_right, cause index issue, ex: [[1,2,3],[4,5,6],[7,8,9]], mid = 5, k=4
#sum(bisect.bisect_right(row, 4) for row in matrix) = 5>k=4

# #注意這邊使用while lo<hi: 左閉右開, 當low = high 代表已搜索到最後一個元素了, 若改成while lo<=hi: 陷入無限迴圈

# #也可以這樣 while lo<=hi: 但要改成 hi = mid-1, 同工異曲之妙
# import bisect
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         lo, hi = matrix[0][0], matrix[-1][-1]
#         while lo<=hi:
#             mid = (lo+hi)//2
#             if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
#                 lo = mid+1
#             else:
#                 hi = mid-1
#         return lo

# # b = [1,2,3,4,5]
# # sum(i for i in b)
# # 15



# import bisect
# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         lo, hi = matrix[0][0], matrix[-1][-1]
#         while lo<hi:
#             mid = (lo+hi)//2
#             if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
#                 lo = mid+1
#             else:
#                 hi = mid  #左閉右開
#         return lo


