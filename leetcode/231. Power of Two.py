'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''
# bit manipulation, time complexity O(1), 32ms
# 思路: 2^x 不會出現負值, 只要負數return False, 若n是power of 2, 則其binary 只會出現1個1
class Solution:
    def isPowerOfTwo(self, n):
        return (n>0) and (n & (n-1)) == 0

# hi what does (n & (n-1)) mean?
# n & n - 1 removes the left most bit of n. If an integer is power of 2, there is a single bit in the binary representation of n. 
# e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0, also 16 > 0, 
# based on these facts there is only one bit in b10000, so 16 is power of 2.

#only works for n>0

# 自己想的, time complexity O(32) => O(1), 44ms
# 思路: 2^x 不會出現負值, 只要負數return False, 若n是power of 2, 則其binary 只會出現1個1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        count = 0
        for i in range(32):
            count += (n & 1)
            n >>= 1
        print(count)
        return count == 1


