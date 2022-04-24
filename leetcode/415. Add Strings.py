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


# 重寫第二次, time complexity O(m+n), space complexity O(m+n)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        carry = 0
        i = j = 0
        while i < len(num1) and j < len(num2):
            n1 = ord(num1[i]) - ord("0")
            n2 = ord(num2[j]) - ord("0")
            cur = n1 + n2 + carry
            cur, carry = cur % 10, cur // 10
            res.append(cur)
            i += 1
            j += 1
        if j < len(num2):
            while j < len(num2):
                n2 = ord(num2[j]) - ord("0")
                cur = n2 + carry
                cur, carry = cur % 10, cur // 10
                res.append(cur)
                j += 1
        if carry:
            res.append(carry)
        return "".join(map(str, res[::-1]))

# 重寫第三次, time complexity O(m+n), space complexity O(m+n)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res = []
        carry = 0
        while num1 or num2:
            n1, n2 = 0, 0
            if num1:
                n1 = ord(num1.pop()) - ord("0")
            if num2:
                n2 = ord(num2.pop()) - ord("0")
            val, carry = (n1 + n2 + carry) % 10, (n1 + n2 + carry) // 10
            res.append(val)
        if carry:
            res.append(carry)
        return "".join(map(str, res[::-1]))

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






















