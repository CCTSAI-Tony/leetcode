'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

5 & 6 & 7 = 4
0 & 1 = 0
'''
'''
First let's think what does bitwise AND do to two numbers, for example ( 0b means base 2)

4 & 7 = 0b100 & 0b111 = 0b100
5 & 7 = 0b101 & 0b111 = 0b101
5 & 6 = 0b101 & 0b110 = 0b100
The operator & is keeping those bits which is set in both number.

For several numbers, the operator & is keeping those bits which is 1 in every number.

In other word, a bit is 0 in any number will result in 0 in the answer's corresponding bit.

Now consider a range

[m = 0bxyz0acd, n=0bxyz1rst]
here xyzpacdrst all are digits in base 2. (0,1)

We can find two numbers that are special in the range [m, n]
(1) m' = 0bxyz0111
(2) n' = 0bxyz1000
The bitwise AND of all the numbers in range [m, n] is just the bitwise AND of the two special number

rangeBitwiseAnd(m, n) = m' & n' = 0bxyz0000
This tells us, the bitwise AND of the range is keeping the common bits of m and n @@(from left to right) 
until the first bit that they are different, padding zeros for the rest.
'''
#bit manipulation, time complexity O(32) = > O(1)
#思路: 此題range m, n, 不需要在這range的數都bitwise AND 一遍, 只要從左bit到右bit 直到第一個bit m,n兩者是不同的
#代表在此range, 從這不同bit以下(包含此bit), 都不可能為1, 在這bit 以下, range的數代表的binary bit 有可能是1 or 0
# 2 special: m' = 0bxyz0111, n' = 0bxyz1000
class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n: #從左到右逐一比對bits, 注意m,n不斷變化
            m >>= 1 #把最右邊bit拿掉
            n >>= 1
            i += 1
        return n << i #padding zeros for the rest ,也可以 return m << i

# 8266 / 8266 test cases passed.
# Status: Accepted
# Runtime: 208 ms

'''
m:11001 :25 i=0
n:11110 :30

m:1100 i=1
n:1111

m:110 i=2
n:111

m: 11 i=3
n: 11

11(3) <<3  = 24

25&26&27&28&29&30 = 24




'''