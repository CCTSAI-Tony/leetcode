'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, 
late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. 
The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
 

Constraints:

1 <= n <= 105
'''

'''
Such a brilliant solution!!
The difficult part to think through is adding 'A' with ∑dp[i] *dp[n-1-i] i = 0,1,...,n-1,
For each dp[i], there are dp[i] *dp[n-1-i] combinations to get a result with length N. The result looks like dp[i] +'A'+ dp[n-1-i].

'''

'''
update:
i use the real value: #不包含A
i=0, possible =1 # 關鍵
i=1, possible =2 (P,L)
i=2, possible =4 (PP,PL,LP,LL)
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 利用觀察法來找出規律 ex: n=0, n=1, n=2, n=3..., 先得出不包含A dp 數組, 再討論加入A的情況
class Solution(object):
    def checkRecord(self, n):
        if n==1:
            return 3
        if n==0: 
            return 0
        mod=1000000007
        dp=[0 for i in range(n+1)]
        dp[0],dp[1],dp[2]=1,2,4
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3] )% mod
        res=dp[n] 
        for i in range(1,n+1):  # dp[i] +'A'+ dp[n-1-i], 討論 A 在不同天出現
            res+=dp[i-1]*dp[n -i]%mod
        res=res%mod
        return res

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 2, 4
        mod = 10 ** 9 + 7
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod
        res = dp[n] % mod
        for i in range(1, n+1):
            res += (dp[i-1] * dp[n-i]) % mod
        return res % mod
