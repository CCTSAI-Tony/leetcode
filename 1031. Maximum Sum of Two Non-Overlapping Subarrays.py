'''
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, 
which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
'''

# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/581060/Python-prefix-sum-with-diagram-explanation
# Explanation: Suppose we already have array of prefix sum, and we are at index i-th of prefix_sum. There are two possible ways to find maximum result:
# (1) maxL + the last sum of A's subarray of length == M. maxL:= maximum sum of A's subarray of length == L, 
# before the ending at i, and the last subarray with length == M. (In the diagram, possible result (1))

# (2) maxM + the last sum of A's subarray of length == L. maxM:= maximum sum of A's subarray of length == M, 
# before the ending at i, and the last subarray with length == L. (In the diagram, possible result (2))

# Complexity: Time O(N), N is len(A). Space O(1)

#思路: no overlaping 就是不重疊, 但是可以相接, time complexity O(n), space complexity O(1)
#有兩種狀況, L 在前, M 在後 or M 在前 L 在後, 利用i指針遍歷 不斷更新 在前面的 maxL or maxM, 後面的m or l 則是隨著指針往前m or 往前l 不斷與前面對應的 max組成 non-overlaping 值
#遍歷的途中, 這兩種狀況與舊的res哪種比較大 就更新 res
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)): #建立prefix sum array
            A[i] += A[i - 1]
        res, maxL, maxM = A[L + M - 1], A[L - 1], A[M - 1] #初始條件
        for i in range(L + M, len(A)): #range(L + M) 避開初始條件的最後一格 L + M - 1
            maxL = max(maxL, A[i - M] - A[i - M - L]) #L在前面, A[i - M] => L的最後一個element
            maxM = max(maxM, A[i - L] - A[i - L - M]) #M在前面
            res = max(res, maxL + A[i] - A[i - M], maxM + A[i] - A[i - L])
        return res


#自己重寫, time complexity O(n)
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i-1]
        max_l = A[L-1]
        max_m = A[M-1]
        res = A[L+M-1]
        for i in range(L+M, len(A)):
            max_l = max(max_l, A[i-M] - A[i-M-L])
            max_m = max(max_m, A[i-L] - A[i-L-M])
            res = max(res, max_l + A[i] - A[i-M], max_m + A[i] - A[i-L])
        return res



