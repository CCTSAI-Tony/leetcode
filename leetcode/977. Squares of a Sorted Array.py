'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''
#time complexity O(nlogn)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return None
        res = []
        for num in A:
            res.append(num**2)
        res.sort()
        return res


#two pointers, O(n)
#思路: 這題用2 pointer 做, time complexity 會變成 O(n)
# 觀察數列, 兩端的絕對值都比越靠近中間的大, 利用此特點, 左右指針逐一往裡面遍歷, 較大者先放進res, 這裡使用deque appendleft, 因為答案輸出要increasing order
from collections import deque
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return None
        res = deque()
        left, right = 0, len(A)-1
        while left < right:
            if A[left]**2 >= A[right]**2:
                res.appendleft(A[left]**2)
                left += 1
            else:
                res.appendleft(A[right]**2)
                right -= 1
        res.appendleft(A[left]**2)
        return res


#重寫第二次, time complexity O(n), space complexity O(1)
from collections import deque
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        queue = deque()
        l, r = 0, len(A) - 1
        while l <= r:
            square1, square2 = A[l]**2, A[r]**2
            if square1 > square2:
                queue.appendleft(square1)
                l += 1
            else:
                queue.appendleft(square2)
                r -= 1
        return queue








# The question boils down to understanding that if we look at the magnitude of the elements 
# in the array, A, both ends "slide down" and converge towards the center of the array. 
# With that understanding, we can use two pointers, one at each end, to iteratively collect the larger square to a list. 
# However, collecting the larger square in a list with list's append, results in elements sorted in descending order. 
# To circumvent this, we need to append to the left of the list. 
# Using a collections.deque() allows us to append elements to the left of answer in O(1) time, maintaining the required increasing order.

#自己想的, time complexity O(nlogn), space complexity O(n)
import heapq
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        heap = []
        for num in A:
            heapq.heappush(heap, num**2)
        res = []
        for _ in range(len(heap)):
            res.append(heapq.heappop(heap))
        return res














