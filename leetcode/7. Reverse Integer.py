'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
#自己重寫 O(n)
#思路: list化 string, 再針對string前面是否有負號再決定反轉的位置, 再利用join來把list連起來, 最後用int() 整數化
#題目說 overflow 要是0, 包含負數小於 -2**32
class Solution:
    def reverse(self, x: int) -> int:
        temp = list(str(x))
        if temp[0] == "-":
            res = int("".join([temp[0]] + temp[1:][::-1]))
        else:
            res = int("".join(temp[::-1]))
        return res if res <= 2**31 -1 and res >= -2**31 else 0


#重寫第二次, time complexity O(32), space complexity O(32)
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = str(x)[1:][::-1]
            reverse = -int(num)
        else:
            num = str(x)[::-1]
            reverse = int(num)
        return reverse if reverse < 2 ** 31 and reverse >= -2 ** 31 else 0


class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])

        if -2**31 <= result <= (2**31)-1:
            return result
        else:
            return 0



            