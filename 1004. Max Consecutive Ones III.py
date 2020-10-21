'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
'''

# time complexity O(n)
# 思路: 遇到1 就expand window, 遇到0 一樣expand window, 但count -= 1
# 每次update 長度都是在count >= 0 計算, 若count < 0, shrink window from start, 直到越過0 count += 1
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, end = 0, 0
        count = K #k counts to replace 0 with 1
        max_len = 0
        while end < len(A):
            if A[end] == 0:
                count -= 1
            while count < 0:
                 # shrink window
                if A[start] == 0:
                    count += 1
                start += 1
            max_len = max(max_len, end - start + 1) #更新長度
            end += 1
        return max_len


