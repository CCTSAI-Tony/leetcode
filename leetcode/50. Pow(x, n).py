'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

#刷題用這個, time complexity O(logn), space complexity O(logn)
#思路: divide and conquer and memo
class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def helper(x, n):
            if (x, n) in memo:
                return memo[(x, n)]
            if n == 0:
                return 1
            if n % 2:
                ans = x * helper(x, n//2) * helper(x, n//2)
            else:
                ans = helper(x, n//2) * helper(x, n//2)
            memo[(x, n)] = ans
            return ans
                
        if x == 0:
            return 0
        if n < 0:
            return 1 / helper(x, -n)
        else:
            return helper(x, n)


时间复杂度 = 一叉树里面每层的时间复杂度 * 层数 = 1 * log(b) = log(b)
空间复杂度 = O(h) 也就是一叉树的层数 = log(b)
# 思路: dfs 對大問題進行拆分, 不斷拆半, ex: b = 17, 17//2 = 8(2^8*2^8*2), 8//2 = 4, 4//2 = 2, 2//2 = 1, 1//2 = 0 (return 1)
# 0^0 == 1 , 2.1^0 == 1, (數學上定義)
# n is a 32-bit signed integer, within the range [−231, 231 − 1]
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:  #此題input 應該不會出現 0^-3 這種情況, or 0^0, 所以大膽給他return 0
            return 0
        if n < 0:
            return 1 / self.helper(x, -n)  #n < 0 , => 變分母
        else:
            return self.helper(x, n)
    
    def helper(self, x, n):
        if n == 0:  #base case
            return 1
        half = self.helper(x, n//2) #2^13 => 2^6 * 2^6 * 2
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x  #base case, n==1, half = x^0 == 1, return 1*1*x

#重寫第二次, time complexity O(logn), space complexity O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.dfs(x, -n)
        return self.dfs(x, n)
        
    def dfs(self, x, n):
        if n == 1:
            return x
        half = self.dfs(x, n // 2)
        if n % 2:
            return half * half * x
        else:
            return half * half






            '''
            Leetcode中被人讨厌最多的题目之一。
            但其实是个很好的Recursion入门题目。

            > Base Case:  b == 0
            > Function: F(a ^ b) = F(a ^ b // 2) *  F(a ^ b // 2)
            不论我们返回时候如何，我们执行第一步，先设立Base Case:
            if b == 0: return 1

            完了以后，我们要对大问题进行拆分，也就是不断的对b的值折半

            拆分：
            half = self.myPow(a, b // 2)

            当拆分到了最小的问题，满足base case b == 0 的时候，我们则进行返回，返回时候有三种可能

            Function的三种可能性：

            当b为偶数的时候，比如 2 ^ 100，拆分的时候就变成 (2 ^ 50) * (2 ^ 50)
            当b为基数的时候，比如 2 ^ 25，拆分的时候就变成 (2 ^12) * (2 ^ 12) * 2
            当b为负数的时候，返回 1.0 / self.myPow(a, -b)

            https://raw.githubusercontent.com/yuzhoujr/spazzatura/master/img_box/50.jpg
            '''







            '''