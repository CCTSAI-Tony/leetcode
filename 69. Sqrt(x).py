# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.


#time complexity O(1), space complexity O(1)
#思路: e**(0.5 * log(x)) 會很接近實際sqr值但會比sqr值小, ex: 1.9998 vs 2
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x))) # int(x**0.5)
        right = left + 1
        return left if right * right > x else right





#刷題用這個 time complexity O(logn), space complexity O(1)
#思路: 模板2 binary search, 要注意的就是初始l, r的值
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l + 1 < r:
            mid = l + (r-l) // 2
            if mid*mid > x:
                r = mid
            else:
                l = mid
        if r*r > x:
            return l
        return r

'''
# Binary search  

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.





'''