'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''

# This solution should have been as simple as return math.log(n,3) % 1 == 0 ( %1 == 0 is to check the result of log is integer).

# However you will surprisingly find that the result of math.log(243, 3) is 4.999999999999999 instead of 5.0. 
# This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. 
# See Floating Point Arithmetic: Issues and Limitations for more information.

# So we need round() to approximate the result of log to nearest integer, and make sure the difference between the real value and rounded value is small.


import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: 
        	return False
        x = math.log(n,3)
        return abs(round(x) - x) < 0.0000000000001 

round(2.4)
2