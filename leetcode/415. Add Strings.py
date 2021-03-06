'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
#time complexity O(n),
#思路:先list化, carry 進位思想要有
class Solution:
    def addStrings(self, num1, num2):
        nums1 = list(num1)
        nums2 = list(num2)
        res, carry = [], 0

        while nums1 or nums2:
            n1 = n2 = 0  #n1, n2 一定要給個預設值0 不然下面 n1 + n2 會報錯
            if nums1: 
                n1 = ord(nums1.pop()) - ord('0') #can't convert the inputs to integer directly
            if nums2: 
                n2 = ord(nums2.pop()) - ord('0')
            
            carry, remain = divmod(n1 + n2 + carry, 10)  #這邊重要 carry要帶進下一輪
            res.append(remain)
        
        if carry:  #最後記得加回最後進位的 carry
            res.append(carry)
        return ''.join(str(d) for d in res)[::-1] #記得先str化, 
        # 也可以 return "".join([str(d) for d in res])[::-1], join(str(d) for d in res) 代表裡面放generator, 另一種代表裡面放list object

# a = "-23444"
# list(a)
# ['-', '2', '3', '4', '4', '4']

# The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder.

# divmod(x, y)
# x and y : x is numerator and y is denominator
# x and y must be non complex

# Input : x = 9, y = 3
# Output :(3, 0)

# Input : x = 8, y = 3
# Output :(2, 2)
ord("0")
48

ord("1")
49

ord("2")
50

ord("-2")
TypeError: ord() expected a character, but string of length 2 found

 
" ".join(23)
TypeError: can only join an iterable

" ".join("23")
'2 3'

重要
a = [1,2,3,4,5]
"".join(str(d) for d in a)
'12345'
"".join([str(d) for d in a])
'12345'
join() 裡面要放interable object, 然而list comprehension 在join()裡面可以不用被[]包覆即可執行






















