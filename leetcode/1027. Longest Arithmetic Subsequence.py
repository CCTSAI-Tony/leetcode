'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, 
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: A = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: A = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: A = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= A.length <= 1000
0 <= A[i] <= 500
'''

#刷題用這個, dp bottum up, time complexity O(n^2), space complexity O(n^2)
#思路: dp[(i, d)]: 代表以step: d 到 A[i] 總共有幾個數字, dp[(i, d)] = dp[(j, d)] + 1, if (j, d) not in dp, dp[(i, d)] = 2
#注意: [15, 20, 0, 5, 15, 20, 25] 裡面有兩個20, dp[(1, 5)] = 2, dp[(5,5)] = 4 => dp[(6, 5)] = 4 + 1, 
#就算離A[i] 距離d的數字有可能重複, 但愈後面相同的數字, dp[(j, d)] 只會大不會小, 所以dp[(i, d)] 不會因重複數字受影響而變小
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(A[1:], start=1): #enumerate start=1 index 起始數值
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2 #兩個數 構成一個d
        return max(dp.values())


#自己重寫, time complexity O(n^2), space complexity O(n^2), 2996ms
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                num1 = A[j]
                num2 = A[i]
                d = num2 - num1
                if (j, d) in dp:
                    dp[(i, d)] = dp[(j, d)] + 1
                else:
                    dp[(i, d)] = 2
        return max(dp.values())

a = [1,4,7]
b = [1,2,3,4,5,6,7]
all(i in b for i in a)
True










