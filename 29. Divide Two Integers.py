# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


time complexity O(log (a/b))

class Solution:
    def divide(self, a, b):
        sig = (a < 0) == (b < 0) #positive = (dividend < 0) and (divisor < 0) 
        a, b, res = abs(a), abs(b), 0
        while a >= b:  #while dividend >= divisor:
            x = 0
            while a >= b << (x + 1): 
                x += 1  #when x = 0, b << (x + 1) ==2b a>=2b: x+=1, 因為之後 res += 1 << x 是以2的倍數成長
            res += 1 << x #when x = 0 1<<0 == 1, 也就是a >=b 但 a < 2b時, res += 1, 重要 !!
            a -= b << x  #記得a 要減去相對應得b
        return min(res if sig else -res, 2147483647)




        '''
        bitwise shift operators
        x << y  Returns x with the bits shifted to the left by y places
        This is the same as multiplying x by 2**y ex: 5<<3 40 5*8

        x >> y Returns x with the bits shifted to the right by y places. This is the same as dividing x by 2**y.
        5>>3 0  5/8 
        
        sig = (a < 0) == (b < 0)
        It will make sure both dividend and divisor are positive or negative. ie. the result -- dividend/divisor will be positive.

        2147483647 = 2**31-1

        For the purpose of this problem, assume that your function returns 2**31 − 1 when the division result overflows.


        '''

time complexity O(log (a/b))
# 思路: 利用bit shift 來記錄可以減去多少個divisor, 這個數目就上無條件捨去的商, 注意bit shift 往左移動一格*2, 所以要考慮  b< a < 2b 的情況
# 這題因為不能用到乘除法所以不能套用binary search 來判斷dividend 最多可以減掉多少個divisor
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)  #trick 不用除法判斷正負技巧
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            x = 0
            while dividend >= divisor << (x + 1):  #trick
                x += 1
            res += 1 << x
            dividend -= (divisor << x)
        return min(res, 2**31-1) if sig else -res


# 暴力解 TLE time complexity O(dividend/divisor)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        return min(res, 2**31-1) if sig else -res
            






