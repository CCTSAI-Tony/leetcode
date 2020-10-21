'''
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
'''

#自己想的, time complexity O(n), 536ms
#思路: 裡面有可能出現 = sign, 允許重複元素, 利用stack 解題, 儲存之前的sign, 若stack[-1] 與 目前的sign相反, 代表找到一個pair, 若不是則cur_pair 歸0
#最後return 答案時, 若max_pair > 0 代表至少有三個元素完成一個pair => max_pair + 2, 若max_pair = 0 但stack 裡面有">" or "<" 則可能 2 < 5 < 8 or 9 > 5 > 1, length = 2
#其他return 1 ex: 100 or 5 = 5
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        max_pair = 0
        cur_pair = 0
        stack = []
        for i in range(1, len(A)):
            if A[i] > A[i-1] and stack and stack[-1] == ">":
                cur_pair += 1
                max_pair = max(max_pair, cur_pair)
                stack.append("<")
            elif A[i] < A[i-1] and stack and stack[-1] == "<":
                cur_pair += 1
                max_pair = max(max_pair, cur_pair)
                stack.append(">")
            else:
                cur_pair = 0
                if A[i] > A[i-1]:
                    stack.append("<")
                elif A[i] < A[i-1]:
                    stack.append(">")
                elif A[i] == A[i-1]:
                    stack.append("=")
        if max_pair > 0:
            return max_pair +2
        elif stack and (">" in stack or "<" in stack):
            return 2
        return 1


#其他人的答案, time complexity O(n)
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # Trivial case
        if len(A) == 1: return 1
        
        # dp[i] is the maximum turbulent subarray ending at the i-th element.
        # By default, our maximum subarray is a single element
        dp = [1]*len(A)
        
        # By default, if the previous element does not equal the current element
        # we have achieved a maximum subarray of len==2
        dp[1] = 2 if A[1] != A[0] else 1
        
        # Keep track of if the last element was greater than or less than previous
        # element
        last_was_gt = A[1] > A[0]
        
        
        for i in range(2, len(A)):
            # If element is equal to previous element reset dp[i]
            if A[i] == A[i-1]:
                dp[i] = 1
                continue
            
            # if last element was greater than the previous, we need
            # the current element to be less than the previous. Vice versa
            if last_was_gt:
                dp[i] = dp[i-1]+1 if A[i] < A[i-1] else 2
            else:
                dp[i] = dp[i-1]+1 if A[i] > A[i-1] else 2
            
            last_was_gt = A[i] > A[i-1]
        
        return max(dp)




