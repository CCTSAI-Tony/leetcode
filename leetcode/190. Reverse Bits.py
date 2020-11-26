'''
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, 
both input and output will be given as signed integer type and should not affect your implementation, 
as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?
'''

#bit manipulation, time complexity O(32) => O(1)
#思路: 利用每一輪,ans往右移 加上 n的最左邊bits, n往左移=>最左邊bit換成次左邊bit
class Solution(object):
    def reverseBits(self, n):
        ans = 0
        for i in range(32): #32 bits
            ans = (ans << 1) + (n & 1)
            n >>= 1 #往左shift
        return ans

#自己重寫, time complexity O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = ans + (n & 1)
            n >>= 1
            ans <<= 1
        ans >>= 1
        return ans
# 600 / 600 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# 98.59%
# Just generate the answer bit by bit, do not use things like "% 2" or "2 ** k" or "bin". 
# Bit manipulation is a lot faster. One small thing is the plus operator can be replaced by "bitwise or", aka "|". 
# However i found plus is more readable and fast in python.

'''
Let's work on an example. Say, n = 19, which is 00000000000000000000000000010011 in binary, so in the output we should get 11001000000000000000000000000000 in binary, 
which is 3355443200.
We initialize answer to 0, so in binary it's 32 zeroes. We loop over 32 times, since every integer is gonna have 32 possible 0/1.
1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, ans << 1 we shift all bits that we already have in our answer to the left, 
so after this shifting the bit on the right is 0, + by using + we set the last bit in the answer to the value that we got in n & 1.
2nd line in the loop we shift bits of our initial number n to the right, since we've already checked the last bit of n, so we just move on to the next bit.

So, in our example, I'm gonna show only first 5 right bits, since other bits are 0.
answer = 0, in binary: 00000000000000000000000000000000
answer << 1 is 00000000000000000000000000000000, n & 1 is 00000000000000000000000000000001 
after + operation answer is 00000000000000000000000000000001

answer = 1, in binary: 00000000000000000000000000000001
answer << 1 is 00000000000000000000000000000010, n & 1 is 00000000000000000000000000000001 注意n >>=1 往右shift 1個bits

after + operation answer is 00000000000000000000000000000011

answer = 3, in binary: 00000000000000000000000000000011
answer << 1 is 00000000000000000000000000000110, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000000110

answer = 6, in binary: 00000000000000000000000000000110
answer << 1 is 00000000000000000000000000001100, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000001100

answer = 12, in binary: 00000000000000000000000000001100
answer << 1 is 00000000000000000000000000011000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000011001

And after that in our example, we'll just shift ** 00000000000000000000000000011001 all the way to the left, which is gonna lead to 11001000000000000000000000000000.

Hope it helps :)
'''
