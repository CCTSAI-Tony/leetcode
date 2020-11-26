'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 9 or not num: #if num % 9 : num is not a nultiple of 9, if num is a nultiple of 9, num % 9 = 0
            return num % 9 

        else:
            return 9




# Reason this works:
# Every number whose digits sum to a multiple of 9 is divisible by 9.
# Otherwise, the iterative sum of digits leads to the remainder when divided by nine.

# We account for the case when the number is divisible by 9 or is 0.