# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.

#time complexity O(n)
#思路: 加法之類的都要有carry進位, 使用list.pop() 來對右到左進行進位運算, 進位 // 2, 餘數 % 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry: #只要其中一方不為none
            if a:
                carry += int(a.pop()) #取最右邊的數
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2 #進位

        return result[::-1]

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"




a = '123'
list(a)
['1', '2', '3']

result = ''
result += str(3)
result

'3'

'''
