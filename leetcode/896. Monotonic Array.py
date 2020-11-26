'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

#自己想的, time complexity O(n), space complexity O(n) cause dfs
#思路: 針對一路小, 一路大 個別遍歷array看是否有不一致的狀況, 若有return False, 若無return True, 最終答案其中一邊是True 就return True
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return self.increasing(A) or self.decreasing(A)
    
    def increasing(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
    
    def decreasing(self, A):
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                return False
        return True

#自己想的, time complexity O(n), space complexity O(1) 
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                is_increasing = False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                is_decreasing = False
        if not is_increasing and not is_decreasing:
            return False
        return True








