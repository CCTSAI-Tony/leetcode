'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''

#自己重寫
#bit manipulation, time complexity O(1)
#思路: 先確認num 是否為power of 2 => 先確認是否只有一個1 bit, 再AND power of 4 pattern, 若 == num, 則代表num 是 4 的倍數 
#4的次方數 不會小於等於0
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num >= 1 and num & (num-1) == 0 and \
    num & 0b1010101010101010101010101010101 == num

# bit manipulation: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        test = 1
        while test < n:
            test = test << 2
        return test == n
# Consider the valid numbers within 32 bit, and turn them into binary form, they are:

# 1
# 100
# 10000
# 1000000
# 100000000
# 10000000000
# 1000000000000
# 100000000000000
# 10000000000000000
# 1000000000000000000
# 100000000000000000000
# 10000000000000000000000
# 1000000000000000000000000
# 100000000000000000000000000
# 10000000000000000000000000000
# 1000000000000000000000000000000
# Any other number not it the list should be considered as invalid.
# So if you XOR them altogether, you will get a mask value, which is:

# 1010101010101010101010101010101 (1431655765)
# Any number which is power of 4, it should be power of 2, I use num &(num-1) == 0 to make sure of that.
# Obviously 0 is not power of 4, I have to check it.
# and finally I need to check that if the number 'AND' the mask value is itself, to make sure it's in the list above.

# here comes the final code:

# return num != 0 and num &(num-1) == 0 and num & 1431655765== num

# ^  XOR Sets each bit to 1 if only one of two bits is 1

class Solution:
    def isPowerOfFour(self, num):
            return num != 0 and num &(num-1) == 0 and num & 1431655765 == num  # 好技巧 power of 2, num &(num-1) == 0




# recursion: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in (1, 4):
            return True
        if n % 4 or n < 1:
            return False
        return self.isPowerOfFour(n // 4)

# cycle: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 4 == 0:
            n = n / 4
        return n == 1


