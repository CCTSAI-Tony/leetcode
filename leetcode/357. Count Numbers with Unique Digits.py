'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

# For the first (most left) digit, we have 9 options (no zero); for the second digit we used one but we can use 0 now, so 9 options; 
# and we have 1 less option for each following digits. Number can not be longer than 10 digits.


# Dynamic Programming 刷題用這個

# Next you can improve backtracking by dynamic programming. Assume you want to know all unique digit numbers from 100 to 999. 
# First place can take 9 (1 to 9). Second place can take 9 (0 to 9 but not what we took in first place). Last place can take only 8.
# https://goo.gl/photos/oLz3dmPimXBgWWsDA
# Example: n=4

# n = 1 temp = 9
# n = 2 temp = 9 * 9
# n=3 temp = 9 * 9 * 8
# n=4 temp = 9 * 9 * 8 * 7

# 參考別人自己重寫, dp, time complexity O(n), 刷題用這個
# 思路: 0 也算一個unique digit , 因此 1 digit 有1+ 9個, 2 digit 因為第一個digit不能是leading zero, 所以只能有9個選項, 第二個digit可以選0, 所以還是9個選項
# 之後每多一個digit, 選項就會-1, ex: 四個digits: 9*9*8*7
# dp[i]: i digits 的 所有組合, 最後sum所有的digits 組合就是答案
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if i <= 2:
                dp[i] = dp[i-1] * 9
            else:
                dp[i] = dp[i-1] * (9-i+2)
        return sum(dp)


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1  #初始值 = 1 (n = 0 時)
        temp = 1
        factor = 9
        for i in range(n):
            temp = temp * factor
            res += temp
            factor = factor - 1 if i != 0 else factor #i=0, digit = 1, factor = factor
        return res






class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product
            
        return ans


#digits = 2, ans = 1 + 9 + 9*9 = 91 (digit = 0 也算一個)



#python, backtracking 以n = 2 來想 滿好理解的
class Solution(object):    
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.counter = 0  #class 全域變數
        self.n = n
        ran = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 0:
            return 1
        if n == 1:
            return len(ran)
        self.helper(n, ran, [])
        return self.counter + 10

    def helper(self, n, r, c):
        if len(c) > 1 and c[0] != 0:  #c[0] != 0 prevent starting with 0, len(c) > 1 重要(2個digits 開始)! 因為digits = 0,1 都已被計算
            self.counter += 1
        if n == 0:
            return
        for j in range(len(r)):
            self.helper(n-1, r[:j]+r[j+1:], c+[r[j]])  #r[:j]+r[j+1:] 排除j, c+[r[j]] 記得r[j] 要list化





























